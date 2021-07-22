"""
connectionGenerator Module

Created on Tue Dec  8 15:51:53 2020

@author: tfahry, Network Rail C&CA

This script takes a single structured unit diagram and generates a list of 
connections from it.

This module should not implement any XML logic - any XML operations should 
instead go in RSXParser's function definitions and only be called here.

"""

from NRFunctions import ResultType
#from transitiontime import calculateTurnaround
import RSXParser as rp
import xlwings as xw
from lxml import etree as et


def GenerateConnections(tree, DiagramObject, stationID, stationName, findall_mapping = False, secondsTolerance = 600):
    result = ResultType()
    made_so_far = set()
    
    if findall_mapping:
        location_mapping_file = et.parse(findall_mapping, parser = et.XMLParser(remove_blank_text=True)).getroot()
        location_mapping = {loc.attrib['longDesc']:loc.attrib['tiploc'] for loc in location_mapping_file}

    assert DiagramObject.standardised, f'Internal error: Unit diagram reader {DiagramObject.__class__} has not been standardised yet.'
    for i, udEntry in enumerate(DiagramObject.ud):
        
        if findall_mapping:
            if udEntry['location'] in location_mapping:
                stationID = location_mapping[udEntry['location']]
            elif udEntry['location'] in location_mapping.values():
                stationID = udEntry['location']
            else:
                continue
        
        if udEntry['location'] == stationName or findall_mapping:
            row = (stationID,
                   udEntry['arrHeadcode'],
                   udEntry['arrTime'],
                   udEntry['depHeadcode'],
                   udEntry['depTime'])

            result.tried.app({'row': row,
                              'excelRow': udEntry['excelRow'],
                              'entryArr': None,
                              'entryWait': None,
                              'conn': None})
            try:
                entryArr = rp.findUniqueEntry(tree,
                                              udEntry['arrHeadcode'],
                                              stationID,
                                              udEntry['arrTime'],
                                              -1,
                                              secondsTolerance)  # binding reference to tree

                entryWait = rp.findUniqueEntry(tree,
                                               udEntry['depHeadcode'],
                                               stationID,
                                               udEntry['depTime'],
                                               0,
                                               secondsTolerance)

                conn = rp.makecon(entryArr, operation=udEntry['activity'])

                if not rp.connectionExists(entryWait, conn) and not row in made_so_far:

                    made_so_far.add(row)

                    result.made.app({'row': row,
                                     'excelRow': udEntry['excelRow'],
                                     'entryArr': entryArr,
                                     'entryWait': entryWait,
                                     'conn': conn})
                else:
                    result.duplicate.app({'row': row,
                                          'excelRow': udEntry['excelRow'],
                                          'entryArr': entryArr,
                                          'entryWait': entryWait,
                                          'conn': conn})
            except ValueError as e:
                result.failed.app({'row': row,
                                   'excelRow': udEntry['excelRow'],
                                   'error': f'{e}'})
                print(f'{e}')

    return result


def AddConnections(result):
    for item in result.made.get:

        entryWait = item['entryWait']
        conn = item['conn']

        if not rp.connectionExists(entryWait, conn):
            entryWait.append(conn)


def highlightExcel(DiagramObject, result):
    assert DiagramObject.hasExcelRows, 'Unit diagram was not read from Excel'
    book = xw.Book(DiagramObject.pathToUD)
    assert len(
        book.sheets) == 1, 'Excel file has multiple sheets. Highlighting is only supported for files with 1 sheet.'
    sheet = book.sheets[0]
    #red, green, blue
    made_highlight_colors = {'wait': (89, 194, 83),
                             'arr': (107, 255, 99),
                             'activity': (151, 158, 221)}

    duplicate_highlight_colors = {'wait': (166, 166, 166),
                                  'arr': (217, 217, 217),
                                  'activity': (151, 158, 221)}

    failed_highlight_colors = {'wait': (255, 0,   0),
                               'arr': (255, 121, 121),
                               'activity': (151, 158, 221)}

    for entry in result.made.get:
        for i in entry['excelRow']['highlight_regions']:
            sheet.range(
                i['cellRange']).color = made_highlight_colors[i['content']]

        sheet.range(entry['excelRow']['annotation_cell']
                    ).value = f'searched for: {entry["row"]}'

    for entry in result.duplicate.get:
        for i in entry['excelRow']['highlight_regions']:
            sheet.range(
                i['cellRange']).color = duplicate_highlight_colors[i['content']]

        sheet.range(entry['excelRow']['annotation_cell']
                    ).value = f'searched for: {entry["row"]}'

    for entry in result.failed.get:
        for i in entry['excelRow']['highlight_regions']:
            sheet.range(
                i['cellRange']).color = failed_highlight_colors[i['content']]

        sheet.range(entry['excelRow']['annotation_cell']
                    ).value = f'searched for: {entry["row"]}, error:{entry["error"]}'
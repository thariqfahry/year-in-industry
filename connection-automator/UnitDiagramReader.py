"""
Unit diagram reader.

Created on Mon Feb  1 15:33:07 2021

@author: tfahry, Network Rail C&CA



the (new) standardized UD entry format - transform everything into this

{location       : e.g. Edinburgh
 arrTime        : e.g. '06:34:00'
 arrHeadcode    : e.g. 1K12
 depTime        : e.g. '06:51:00'
 depHeadcode    : e.g. 1K51
 activity       : e.g. 'split'  (can be 'split', 'join' or 'turnaround')
 excelRow       : [{"cellRange": "A1:B1", "content": 'arr'},
                   {"cellRange": "A2:B2", "content": 'wait'}
                   {"cellRange": "D1",    "content": 'activity'}]
} 
"""

from pandas import read_excel
from lxml import etree as et, objectify

from NRFunctions import timeStandardiser, convert_to_excel_address as c2e, get_first_element_of_list as n
from re import compile

'''
Base Reader class. All UDs should inherit from this class and define their own Parse() function that returns 
a list of entries that are formatted according to the udEntryFormat.
'''
class Reader:
    EmptyFill = 'UDNONE' #define what to fill empty cells with
    standardised = True  #default value
    hasExcelRows = False #default value
    
    udEntryFormat = {'location'     :   None,
                     'arrTime'      :   None,
                     'arrHeadcode'  :   None,
                     'depTime'      :   None,
                     'depHeadcode'  :   None,
                     'activity'     :   None,
                     'excelRow'     :   None}
        
    def __init__(self, pathToUD):
        self.pathToUD = pathToUD
        self.ud = self.Parse(self.pathToUD)
    
    def Parse(self, pathToUD):
        raise NotImplementedError('Parse() not implemented')
                
'''
Avanti Reader: user needs to drag and drop Word UD into Excel, trim off all rows up to "Diagram:" row 
and trim all columns up to station name
'''    
class Avanti(Reader):
    hasExcelRows = True
    activity_map = {'REVRSE':'turnaround',
                    'ATTACH':'join',
                    'DETACH':'split'}
        
    def Parse(self, pathToUD):
        udEntries = []
        z  = read_excel(pathToUD, dtype = str, header = None).fillna(self.EmptyFill)
        
        #create a list of rows
        z  = [j for i,j in z.iterrows()] 
        
        #specify the format <num><letter><num><num> that we will check headcodes against e.g. 1K11
        headcode_check = compile('[0-9][A-Za-z][0-9][0-9]') 
        
        station_column_no = 0
        arr_time_column_no = 1
        dep_time_column_no = 2
        headcode_column_no = 3
        activity_column_no = 4
        
        final_column_no = 6
        
        #first pass: transform sheet to udEntries
        for row_num, row in enumerate(z):
            #if the current row has a non-empty station name, and its headcode cell matches the format [0-9][A-Za-z][0-9][0-9]
            if z[row_num].iloc[station_column_no] \
            and headcode_check.match(z[row_num].iloc[headcode_column_no]):
                
                #...check 1 row above: if this test passes, there is no gap
                if headcode_check.match(z[row_num-1].iloc[headcode_column_no]):
                    if not z[row_num].iloc[headcode_column_no] == z[row_num-1].iloc[headcode_column_no]:
                        
                        udEntry = self.udEntryFormat.copy()
                        
                        udEntry['location']     = z[row_num].iloc[station_column_no]
                        udEntry['arrTime']      = z[row_num].iloc[arr_time_column_no]
                        udEntry['arrHeadcode']  = headcode_check.match(z[row_num-1].iloc[headcode_column_no]).group()
                        udEntry['depTime']      = z[row_num].iloc[dep_time_column_no]
                        udEntry['depHeadcode']  = headcode_check.match(z[row_num].iloc[headcode_column_no]).group()
                        if z[row_num-1].iloc[activity_column_no] in self.activity_map:
                            udEntry['activity'] = z[row_num-1].iloc[activity_column_no]
                        elif z[row_num].iloc[activity_column_no] in self.activity_map:
                            udEntry['activity'] = z[row_num].iloc[activity_column_no]
                        else:
                            udEntry['activity'] = self.EmptyFill
                        udEntry['excelRow']     = {'highlight_regions':[{"cellRange": f'{c2e(row_num-1,station_column_no)}:{c2e(row_num-1,final_column_no)}'   , 'content': 'wait'    },
                                                                        {"cellRange": f'{c2e(row_num  ,station_column_no)}:{c2e(row_num  ,final_column_no)}'   , 'content': 'arr'     },
                                                                        {"cellRange": f'{c2e(row_num ,activity_column_no)}:{c2e(row_num-1,activity_column_no)}', 'content': 'activity'}],
                                                   'annotation_cell'  : c2e(row_num, final_column_no+2)
                                                  }
                        
                        udEntries.append(udEntry)
                    
                #...or check 2 rows above, if this passes, the rows have a gap in between
                elif headcode_check.match(z[row_num-2].iloc[headcode_column_no]):
                    if not z[row_num].iloc[headcode_column_no] == z[row_num-2].iloc[headcode_column_no]:
                        
                        udEntry = self.udEntryFormat.copy()
                        
                        udEntry['location']     = z[row_num].iloc[station_column_no]
                        udEntry['arrTime']      = z[row_num-1].iloc[arr_time_column_no]
                        udEntry['arrHeadcode']  = headcode_check.match(z[row_num-2].iloc[headcode_column_no]).group()
                        udEntry['depTime']      = z[row_num].iloc[dep_time_column_no]
                        udEntry['depHeadcode']  = headcode_check.match(z[row_num].iloc[headcode_column_no]).group()
                        if z[row_num-2].iloc[activity_column_no] in self.activity_map:
                            udEntry['activity'] = z[row_num-2].iloc[activity_column_no]
                        elif z[row_num-1].iloc[activity_column_no] in self.activity_map:
                            udEntry['activity'] = z[row_num-1].iloc[activity_column_no]
                        elif z[row_num].iloc[activity_column_no] in self.activity_map:
                            udEntry['activity'] = z[row_num].iloc[activity_column_no]                        
                        else:
                            udEntry['activity'] = self.EmptyFill
                        udEntry['excelRow']     = {'highlight_regions':[{"cellRange": f'{c2e(row_num-2,station_column_no)}:{c2e(row_num-2,final_column_no)}'    , 'content': 'wait'    },
                                                                        {"cellRange": f'{c2e(row_num  ,station_column_no)}:{c2e(row_num  ,final_column_no)}'    , 'content': 'arr'     },
                                                                        {"cellRange": f'{c2e(row_num ,activity_column_no)}:{c2e(row_num-2 ,activity_column_no)}', 'content': 'activity'}],
                                                   'annotation_cell'  : c2e(row_num, final_column_no+2)
                                                   }
                        
                        udEntries.append(udEntry)
        
        #second pass: standardise times and map UD Activity to RailSys Activity
        for idx, entry in enumerate(udEntries):
             udEntries[idx]['arrTime'] = timeStandardiser(udEntries[idx]['arrTime'])
             udEntries[idx]['depTime'] = timeStandardiser(udEntries[idx]['depTime'])
             udEntries[idx]['activity'] = self.activity_map.get(udEntries[idx]['activity'], 'turnaround')
         
        return udEntries      


'''
ScotRail Reader: user needs to open XML or .xlsx UD in Excel, trim off all rows up to "Diagram:" row 
and trim all columns up to station name
'''    
class ScotRail(Reader):
    hasExcelRows = True
    activity_map = {'Revrse':'turnaround',
                    'Attach':'join',
                    'Detach':'split'}    
    
    def Parse(self, pathToUD):
        udEntries = []
        z  = read_excel(pathToUD, dtype = str, header = None).fillna(self.EmptyFill)
        
        #create a list of rows
        z  = [j for i,j in z.iterrows()] 
        
        #specify the format <num><letter><num><num> that we will check headcodes against e.g. 1K11
        headcode_check = compile('[0-9][A-Za-z][0-9][0-9]') 
        
        station_column_no = 0
        arr_time_column_no = 1
        dep_time_column_no = 2
        activity_column_no = 3
        headcode_column_no = 4
        final_column_no = 8
        
        #first pass: transform sheet to udEntries
        for row_num, row in enumerate(z):
            #if the current row has a non-empty station name, and its headcode cell matches the format [0-9][A-Za-z][0-9][0-9]
            if z[row_num].iloc[station_column_no]!= self.EmptyFill\
            and headcode_check.match(z[row_num].iloc[headcode_column_no]):
                
                #...check 1 row above: if this test passes, there is no gap
                if headcode_check.match(z[row_num-1].iloc[headcode_column_no]):
                    if not z[row_num].iloc[headcode_column_no] == z[row_num-1].iloc[headcode_column_no]:
                        
                        udEntry = self.udEntryFormat.copy()
                        
                        udEntry['location']     = z[row_num].iloc[station_column_no]
                        udEntry['arrTime']      = z[row_num].iloc[arr_time_column_no]
                        udEntry['arrHeadcode']  = headcode_check.match(z[row_num-1].iloc[headcode_column_no]).group()
                        udEntry['depTime']      = z[row_num].iloc[dep_time_column_no]
                        udEntry['depHeadcode']  = headcode_check.match(z[row_num].iloc[headcode_column_no]).group()
                        udEntry['activity']     = self.EmptyFill if z[row_num].iloc[activity_column_no] == self.EmptyFill else z[row_num].iloc[activity_column_no]
                        udEntry['excelRow']     = {'highlight_regions':[{"cellRange": f'{c2e(row_num-1,station_column_no)}:{c2e(row_num-1,final_column_no)}', 'content': 'wait'    },
                                                                        {"cellRange": f'{c2e(row_num  ,station_column_no)}:{c2e(row_num  ,final_column_no)}', 'content': 'arr'     },
                                                                        {"cellRange": f'{c2e(row_num ,activity_column_no)}'                                 , 'content': 'activity'}],
                                                   'annotation_cell'  : c2e(row_num, final_column_no+2)
                                                  }
                        
                        udEntries.append(udEntry)
                    
                #...or check 2 rows above, if this passes, the rows have a gap in between
                elif headcode_check.match(z[row_num-2].iloc[headcode_column_no]):
                    if not z[row_num].iloc[headcode_column_no] == z[row_num-2].iloc[headcode_column_no]:
                        
                        udEntry = self.udEntryFormat.copy()
                        
                        udEntry['location']     = z[row_num].iloc[station_column_no]
                        udEntry['arrTime']      = z[row_num-1].iloc[arr_time_column_no]
                        udEntry['arrHeadcode']  = headcode_check.match(z[row_num-2].iloc[headcode_column_no]).group()
                        udEntry['depTime']      = z[row_num].iloc[dep_time_column_no]
                        udEntry['depHeadcode']  = headcode_check.match(z[row_num].iloc[headcode_column_no]).group()
                        udEntry['activity']     = self.EmptyFill if z[row_num-1].iloc[activity_column_no] == self.EmptyFill else z[row_num-1].iloc[activity_column_no]
                        udEntry['excelRow']     = {'highlight_regions':[{"cellRange": f'{c2e(row_num-2,station_column_no)}:{c2e(row_num-2,final_column_no)}', 'content': 'wait'    },
                                                                        {"cellRange": f'{c2e(row_num  ,station_column_no)}:{c2e(row_num  ,final_column_no)}', 'content': 'arr'     },
                                                                        {"cellRange": f'{c2e(row_num-1 ,activity_column_no)}'                               , 'content': 'activity'}],
                                                   'annotation_cell'  : c2e(row_num, final_column_no+2)
                                                   }
                        
                        udEntries.append(udEntry)
        
        #second pass: standardise times and map UD Activity to RailSys Activity
        for idx, entry in enumerate(udEntries):
             udEntries[idx]['arrTime'] = timeStandardiser(udEntries[idx]['arrTime'])
             udEntries[idx]['depTime'] = timeStandardiser(udEntries[idx]['depTime'])
             
             udEntries[idx]['activity'] = self.activity_map.get(udEntries[idx]['activity'], 'turnaround')
         
        return udEntries        

'''
FTPE: read XML, and for each diagramExchange > unitDiagramList > unitDiagram > details element, iterate over all the
diagMovement and diagStatic elements (movements). When there is a headcode change between diagMovements, check for a diagStatic between
them. If present, extract the activity from that diagStatic. If absent, default to EmptyFill (which will later map to Turnaround).
'''
class FTPE(Reader):
    activity_map = {'REVRSE':'turnaround',
                    'ATTACH':'join',
                    'DETACH':'split'}
    
    def Parse(self, pathToUD):
        udEntries = []
        
        #Remove the XML namespace that FTPE diagrams have since that makes using XPath later impossible.
        parser = et.XMLParser(remove_blank_text=True)
        z= et.parse(pathToUD, parser)
        z=z.getroot()
        for elem in z.getiterator():
            if not hasattr(elem.tag, 'find'): continue  # (1)
            i = elem.tag.find('}')
            if i >= 0:
                elem.tag = elem.tag[i+1:]
        objectify.deannotate(z, cleanup_namespaces=True)
        
        #Because we only expect a single unitDiagramList, we write the left-hand side as (some_variable ,) to extract one and only one 
        #element from the search results returned by z.xpath(...). If there are less than or more than 1 element, a ValueError is raised.
        (unit_diagram_list, ) = z.xpath('./unitDiagramList') 
        
        #one unit_diagram_list = one train run
        for unit_diagram_element in unit_diagram_list:
            (details, ) = unit_diagram_element.xpath('details')
            
            #movement = either a diagStatic or diagMovement
            for idx, movement in enumerate(details):
                if movement.tag == 'diagMovement'\
                and movement.xpath(f'.//following-sibling::diagMovement[1]/journey[@origin="{n(movement.xpath("./journey/@dest"))}"]/activity[@trainid!="{n(movement.xpath("./journey/activity/@trainid"))}"]'):   
                    try:                               
                        udEntry = self.udEntryFormat.copy()
                        udEntry['location']     = n(movement.xpath("./journey/@dest"))
                        udEntry['arrTime']      = n(movement.xpath("./journey/@arr"))[0:8]
                        udEntry['arrHeadcode']  = n(movement.xpath("./journey/activity/@trainid"))[0:4]
                        udEntry['depTime']      = n(movement.xpath(".//following-sibling::diagMovement[1]/journey/@dep"))[0:8]
                        udEntry['depHeadcode']  = n(movement.xpath(".//following-sibling::diagMovement[1]/journey/activity/@trainid"))[0:4]
                        if movement.xpath(f'.//following-sibling::diagStatic[@loc="{n(movement.xpath("./journey/@dest"))}"][last()]'):
                            udEntry['activity'] = n(movement.xpath(f'.//following-sibling::diagStatic[@loc="{n(movement.xpath("./journey/@dest"))}"][last()]/activity/@id'))
                        else:
                            udEntry['activity'] = 'UDNONE'
                        udEntries.append(udEntry)
                    except:
                        pass
        
        for idx, entry in enumerate(udEntries):
             udEntries[idx]['arrTime'] = timeStandardiser(udEntries[idx]['arrTime'])
             udEntries[idx]['depTime'] = timeStandardiser(udEntries[idx]['depTime'])
             udEntries[idx]['activity'] = self.activity_map.get(udEntries[idx]['activity'], 'turnaround')
             
        return udEntries

if __name__ == '__main__':
    pass
    
    # s = ScotRail('u170.xlsx')
    
    # a = Avanti('utfw2.xlsx')
    
    # f = FTPE('uFTPE.xml')
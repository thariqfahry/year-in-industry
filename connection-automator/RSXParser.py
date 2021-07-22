"""
RSXParser Module

Created on Mon Nov 23 11:18:42 2020

@author: tfahry, Network Rail C&CA

This is an XML parser for manipulating RailSys RSX files.

This parser works directly on RSX files. It contains functions that let 'higher' 
parsers add, get, change and remove entries without them having to implement 
any XML logic.

"""
#%%
"""
Imports and function definitions.
"""

from lxml import etree as et
from datetime import datetime


#better length function. do not use with generators.
def len2(input): 
    return sum(1 for _ in input)

#returns first object of a list if the list contains one and only one item, otherwise raises exception.
def getIfExistsAndUnique(input):
    if len2(input)  ==1:
        return input[0]
    elif len2(input)==0:
        raise ValueError('not found in timetable')
    elif len2(input)>0:
        raise ValueError('non-unique')
    else:
        raise ValueError('unknown error')
#shorthand 
gu = getIfExistsAndUnique


def findUniqueEntry(tree,trainName,stationID,time,index,secondsTolerance = 600): #conArr entries are always the last stop (index = -1), and conWait the first (index = 0)
    timeSearchList = tree.xpath(f'.//train[starts-with(@name, "{trainName}")]//entry[@stationID="{stationID}"]')
    
    entries = []
    if timeSearchList !=[]:
        for entry in timeSearchList:
            if abs((datetime.strptime(entry.attrib['departure'],'%H:%M:%S') - datetime.strptime(time,'%H:%M:%S')).total_seconds())<secondsTolerance:
                entries.append(entry)

    #positive index checker
    entries2 = []    
    for entry in entries:
        timetableentries = entry.getparent()
        
        if index ==-1:
            if len2(timetableentries)-1 == list(timetableentries).index(entry):
                entries2.append(entry)
                
        elif index>=0:
            if index == list(timetableentries).index(entry):
                entries2.append(entry)
        else:
            raise TypeError(f'index {index} not understood @ {stationID} @ {trainName} @ {time}')
    
    try:
        return getIfExistsAndUnique(entries2)
    except ValueError as errormsg:
        raise ValueError(f'train {trainName} {"terminating" if index == -1 else "originating"} at {stationID} at {time} +/- {secondsTolerance/60:.1f} min was {errormsg}')
        

def connectionExists(entryWait, conn):
    are_existing_children_same = [entry.attrib['trainNumber'] == conn.attrib['trainNumber'] for entry in entryWait.getchildren()]
    return any(are_existing_children_same)


def makecon(entryArr,
            transitionTime='300',
            validityTime='86399',
            operation='turnaround',
            waitForArrTrain='true'):
    
    #Create an Element for our connection.
    connectionTemplate = et.Element('connection') 
    
    #Populate connection attributes.
    connectionTemplate.attrib['trainNumber']    = entryArr.getparent().getparent().attrib['number']
    if 'numbervar' in entryArr.getparent().getparent().attrib:
        connectionTemplate.attrib['numbervar'] = entryArr.getparent().getparent().attrib['numbervar']
        
    connectionTemplate.attrib['transitionTime'] = transitionTime
    connectionTemplate.attrib['validityTime']   = validityTime
    connectionTemplate.attrib['operation']      = operation    
    if 'pattern' in entryArr.getparent().getparent().attrib:
        connectionTemplate.attrib['trainPattern']   = entryArr.getparent().getparent().attrib['pattern']
        
    connectionTemplate.attrib['stationId']      = entryArr.attrib['stationID']
    connectionTemplate.attrib['trainDeparture'] = entryArr.attrib['departure']
    connectionTemplate.attrib['waitForArrTrain']= waitForArrTrain
    
    return connectionTemplate


def read(filename): #reads an XML and returns an ElementTree object
    parser = et.XMLParser(remove_blank_text=True)
    return et.parse(filename, parser)
    
def write(tree,filename):
    et.indent(tree,space='\t')
    tree.write(file = filename, pretty_print=True, xml_declaration=True, encoding="UTF-8", standalone="yes")
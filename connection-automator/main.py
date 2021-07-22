"""
Connection Macro Main module

Created on Tue Feb  9 10:21:22 2021

@author: tfahry, Network Rail C&CA
Requires Python 3.8 or newer. (Python 3.9 EXEs will not run on Windows 7.)

Top-level Connection Macro module containing the the GUI and main program loop.

To set up the environment if this is your first time running this code:
conda env create -f environment.yml
conda activate connectionmacro

1. To run:
python main.py

2. To compile to an .exe:
pyinstaller --clean --onefile --noconsole main.py -n ConnectionMacro.exe
Remember to update the VERSION code.

If, after compiling, the .exe does not run for whatever reason (e.g. failed to execute script main), compile it in console mode:
pyinstaller --clean --onefile --noconsole main.py -n ConnectionMacro.exe

And run ConnectionMacro.exe from a terminal to read the error description.

3. To update the GUI if you edit the ConnectionMacroUI.ui:
pyuic5 '.\qt\ConnectionMacroUI.ui' -o ConnectionMacroUI.py

4. To export an environment:
conda env export -n connectionmacro --from-history | Out-File environment.yml -Encoding utf8

Make sure the encoding is utf-8 (not UTF-8 with BOM) by opening in VS Code and checking.
"""

import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5 import QtCore

from ConnectionMacroUI import Ui_MainWindow

from connectionGenerator import GenerateConnections, AddConnections, highlightExcel
import UnitDiagramReader
from RSXParser import read, write
from NRFunctions import ResultType, hashfile

from copy import deepcopy

#remember to update version code in instructions too
VERSION = 'build JUL07'

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(f'Connection Macro {VERSION}')
        
        self.tableWidget.setColumnWidth(0, 45)
        self.tableWidget_2.setColumnWidth(0, 45)
        
        self.connectSignalsSlots()
        self.statusBar.showMessage('Ready')
        
        self.available_ud_readers = [cls.__name__ for cls in UnitDiagramReader.Reader.__subclasses__()]
        
        for reader in self.available_ud_readers:
            self.udselector.addItem(reader)
            #sys.frozen = True
        if getattr(sys, 'frozen', False):
            self.frozen = True
            self.debugbutton.setVisible(False)
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
    
    def cellChangedSlot(self, item):
        self.tableWidget.blockSignals(True)
        columnsOfSelectedCells = set([cell.column() for cell in self.tableWidget.selectedItems()])
        
        if item in self.tableWidget.selectedItems():
            if len(columnsOfSelectedCells) == 1:                #only allow changing multiple cells if they are all in the same column
                if columnsOfSelectedCells.pop() == 0:           #if it's the 0th column, we check and propagate the checkState to the highlightedCells.
                    checkState = item.checkState()
                    for highlightedCell in self.tableWidget.selectedItems():
                        highlightedCell.setCheckState(checkState)
                else:                                           #if it's any other column, check and propagate the text() value.
                    text = item.text()
                    for highlightedCell in self.tableWidget.selectedItems():
                        highlightedCell.setText(text)
                    
        self.tableWidget.blockSignals(False)
        
    def connectSignalsSlots(self):
        pass
    
    def debugbutton_clicked(self):
        pass
    
    def rsxbrowse_clicked(self):
        self.options = QFileDialog.Options()
        pathToRSX, _ = QFileDialog.getOpenFileName(self,"Load RSX", "","RailSys RSX file (*.rsx)", 
                                                        options=self.options)       
        if pathToRSX:
            self.lineEdit.setText(pathToRSX)
            
    def udbrowse_clicked(self):
        self.options = QFileDialog.Options()
        pathToUD, _ = QFileDialog.getOpenFileName(self,"Load unit digram", "","All Files (*)", 
                                                       options=self.options)
        if pathToUD:
            self.lineEdit_2.setText(pathToUD)
    
    def locationmappingbrowse_clicked(self):
        self.options = QFileDialog.Options()
        pathToLocationmapping, _ = QFileDialog.getOpenFileName(self,"Load location mapping", "","XML file (*.xml)", 
                                                        options=self.options)         
        if pathToLocationmapping:
            self.lineEdit_3.setText(pathToLocationmapping)
    
    #FIXME findUniqueEntry throws '24:02:01' error from dec19 unit diagram
    #TODO minimum and maximum times
    #TODO make failed conns exportable
    def generate_clicked(self): #try not to raise exceptions after setData
        #self.console.clear()
        self.saveButton.setDisabled(True)
        
        self._tree = read(self.lineEdit.text())
        tree = deepcopy(self._tree)
        self.diagram = getattr(UnitDiagramReader,self.udselector.currentText())(self.lineEdit_2.text())
        self.secondsTolerance = 600
        if self.thresholdbox.text():
            self.secondsTolerance = float(self.thresholdbox.text())*60
            
        if self.findallbox.checkState():
            self.tiploc = None
            self.stationname = None
            if not self.lineEdit_3.text():
                self.console.append('Find All requires a location mapping.')
                return
            self.locationmappingpath = self.lineEdit_3.text()
            self.console.append(f'Looking for all connections...')
            result = GenerateConnections(tree=tree, DiagramObject=self.diagram, stationID=self.tiploc, 
                                              stationName = self.stationname, findall_mapping = self.locationmappingpath, secondsTolerance=self.secondsTolerance)
        else:
            self.locationmappingpath = None
            self.tiploc = self.tiplocbox.text()
            self.stationname = self.stationnamebox.text()
            self.console.append(f'Looking for connections at {self.tiploc}...')
            result = GenerateConnections(tree=tree, DiagramObject=self.diagram, stationID=self.tiploc, 
                                              stationName = self.stationname, secondsTolerance= self.secondsTolerance)
        
        self.console.append(f'Found {result.made.count} connections out of {result.tried.count} in diagram. Rejected {result.duplicate.count} duplicates and failed {result.failed.count}.')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),   f'Made [{result.made.count}]')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), f'Duplicates in {self.lineEdit.text().split("/")[-1]} (will not add) [{result.duplicate.count}]')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), f'Falied [{result.failed.count}]')
        
        self.tableWidget.blockSignals(True)
        self.setData(self.tableWidget,result.made.get, self.diagram, checkboxes=(True))
        self.tableWidget.blockSignals(False)
        self.setData(self.tableWidget_2,result.duplicate.get, self.diagram)
        self.setFailed(self.tableWidget_3,result.failed.get, self.diagram)
        
        if self.highlightbox.checkState(): 
            if self.diagram.hasExcelRows:
                highlightExcel(self.diagram, result)
            else:
                self.console.append('Excel highlighting not supported for diagram type.')
        
        #only allow saving if the function successfully runs
        self.saveButton.setDisabled(False)

    def setData(self, widget, data, diagram, checkboxes = False):
        widget.clearContents()
        widget.setRowCount(len(data))
        for row, item in enumerate(data):            
            
            columnMap = {0:'', #checkbox placeholder
                         1:'transitionTime',
                         2:'operation',
                         3:'stationId',
                         5:'trainDeparture'}
            for key in list(columnMap.keys())[1:]:
                columnMap[key] = item['conn'].attrib[columnMap[key]]
            columnMap[4] = item['row'][1]
            columnMap[6] = item['row'][3]
            columnMap[7] = item['row'][4]
            if diagram.hasExcelRows:
                columnMap[8] = item['excelRow']['highlight_regions'][0]['cellRange']
            for key in columnMap.keys():
                newitem = QTableWidgetItem(columnMap[key])
                if key == 0 and checkboxes:
                    newitem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)
                    newitem.setCheckState(QtCore.Qt.Checked)                           
                if key not in [0,1,2]:
                    newitem.setFlags(newitem.flags() ^ QtCore.Qt.ItemIsEditable)
                widget.setItem(row, key, newitem)
             
    def setFailed(self, widget, data, diagram):
        widget.clearContents()
        widget.setRowCount(len(data))
        columnMap = {}
        for row, item in enumerate(data):
            columnMap[0] = item['error']            
            columnMap[1] = item['row'][0]
            columnMap[2] = item['row'][1]
            columnMap[3] = item['row'][2]
            columnMap[4] = item['row'][3]
            columnMap[5] = item['row'][4]
            if diagram.hasExcelRows:
                columnMap[6] = item['excelRow']['highlight_regions'][0]['cellRange']

            for key in columnMap.keys():
                newitem = QTableWidgetItem(columnMap[key])
                widget.setItem(row, key, newitem)
    
        
    def savebutton_clicked(self):
        self.options = QFileDialog.Options()
        pathToSave, _ = QFileDialog.getSaveFileName(self,"Save as","","RailSys RSX file (*.rsx)", 
                                                         options=self.options)
        
        if pathToSave:
            #make a copy of the tree object and regenerate the Result object since any previous run of the AddConnections function
            #would have modified the tree's elements 
            tree = deepcopy(self._tree)
            
            if self.locationmappingpath:
                result = GenerateConnections(tree=tree, DiagramObject=self.diagram, stationID=self.tiploc, 
                                              stationName = self.stationname, findall_mapping=self.locationmappingpath, secondsTolerance=self.secondsTolerance)
            else:
                result = GenerateConnections(tree=tree, DiagramObject=self.diagram, stationID=self.tiploc, 
                                             stationName = self.stationname, secondsTolerance=self.secondsTolerance)
                
            #Update result object with values from Transition Time and Activity columns in self.tablewidget.
            rows_to_be_removed = []
            for row_num in range(self.tableWidget.rowCount()):
                result.made._contents[row_num]['conn'].attrib['transitionTime'] = self.tableWidget.item(row_num,1).text()
                result.made._contents[row_num]['conn'].attrib['operation'] = self.tableWidget.item(row_num,2).text()
                
                if not self.tableWidget.item(row_num,0).checkState(): #if row is not checked
                    rows_to_be_removed.append(row_num)
                
            for row_to_be_removed in sorted(rows_to_be_removed, reverse = True): #reverse = we start from the bottom so that the list indexes aren't thrown off
                    del result.made._contents[row_to_be_removed]
            
            AddConnections(result)
            write(tree = tree, filename = pathToSave)

            self.console.append(f'\nAdded {result.made.count} connections into \n{pathToSave} and saved. (hash {hashfile(pathToSave)})')
            #longlands.rsx + scotrail u170.xlsx hash + all Edinburgh/EDINBUR connections = oregon-delta-wyoming-romeo-delaware-eleven

            
def excepthook(typ, value, tb):
    win.console.clear()
    if typ is PermissionError:
        win.console.append(f'Your Unit Diagram {value.filename.split("/")[-1]} is open. Please close it.')         
    else:
        win.console.append('******  Error  *********')
        win.console.append(value.__repr__())
        win.console.append('')
        #if not getattr(sys, 'frozen', False):
        for line in traceback.format_tb(tb):
            win.console.append(line)      
    #win.console.append(str(tb.tb_frame))
    
if __name__ =='__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

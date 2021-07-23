# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:02:12 2021

@author: tfahry

Top-level module of PEX formatter.
"""
VERSION = 'JUL23'

import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore

from pexformatterUI import Ui_MainWindow

from pexformatter import formatpex, write_csv

#make PyQt DPI-aware - without this, the UI scaling is off on certain computers
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(f'PEX formatter version {VERSION}')
    
    def pexfilebuttonclicked(self):
        self.options = QFileDialog.Options()
        pathToPEX, _ = QFileDialog.getOpenFileName(self,"Load .pex", "","All Files (*)", 
                                                       options=self.options)    
        if pathToPEX:
            self.pexfilebox.setText(pathToPEX)     
            self.formatsavebutton.setDisabled(False)

    def oplookupbuttonclicked(self):
        self.options = QFileDialog.Options()
        pathToOpLookup, _ = QFileDialog.getOpenFileName(self,"Load operator lookup file", "","CSV (*.csv)", 
                                                       options=self.options)    
        if pathToOpLookup:
            self.oplookupbox.setText(pathToOpLookup)
            
    def tiploclookupbuttonclicked(self):
        self.options = QFileDialog.Options()
        pathToTiplocLookup, _ = QFileDialog.getOpenFileName(self,"Load TIPLOC lookup file", "","CSV (*.csv)", 
                                                       options=self.options)    
        if pathToTiplocLookup:
            self.tiploclookupbox.setText(pathToTiplocLookup)                
    
    def outputfilebuttonclicked(self):
        self.options = QFileDialog.Options()
        pathToSave, _ = QFileDialog.getSaveFileName(self,"Set save file","","CSV (*.csv)", 
                                                         options=self.options)
        if pathToSave:
            self.outputfilebox.setText(pathToSave)
    
    def formatsavebuttonclicked(self):
        self.console.clear()
        df = formatpex(pex_file= self.pexfilebox.text(), 
                       toc_code_lookup_file=self.oplookupbox.text(), 
                       tiploc_lookup_file=self.tiploclookupbox.text())
        write_csv(df, self.outputfilebox.text())
        win.console.append(f'Successfully formatted {self.pexfilebox.text()} and wrote output containing {len(df)} rows to {self.outputfilebox.text()}.')
        
def excepthook(typ, value, tb):
    win.console.clear()
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
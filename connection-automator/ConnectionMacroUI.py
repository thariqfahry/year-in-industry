# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt\ConnectionMacroUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1201, 491)
        MainWindow.setMinimumSize(QtCore.QSize(1201, 491))
        MainWindow.setMaximumSize(QtCore.QSize(1201, 491))
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(400, 10, 791, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.gridLayout_3.addWidget(self.tableWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(7)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        self.gridLayout_4.addWidget(self.tableWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 130, 381, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 211, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.stationnamebox = QtWidgets.QLineEdit(self.frame)
        self.stationnamebox.setGeometry(QtCore.QRect(230, 10, 133, 20))
        self.stationnamebox.setObjectName("stationnamebox")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 40, 171, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.tiplocbox = QtWidgets.QLineEdit(self.frame)
        self.tiplocbox.setGeometry(QtCore.QRect(230, 40, 101, 20))
        self.tiplocbox.setObjectName("tiplocbox")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 150, 161, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_5.setObjectName("label_5")
        self.mintimebox = QtWidgets.QLineEdit(self.frame)
        self.mintimebox.setGeometry(QtCore.QRect(120, 70, 71, 20))
        self.mintimebox.setObjectName("mintimebox")
        self.maxtimebox = QtWidgets.QLineEdit(self.frame)
        self.maxtimebox.setGeometry(QtCore.QRect(200, 70, 71, 20))
        self.maxtimebox.setObjectName("maxtimebox")
        self.highlightbox = QtWidgets.QCheckBox(self.frame)
        self.highlightbox.setGeometry(QtCore.QRect(80, 140, 121, 21))
        self.highlightbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.highlightbox.setObjectName("highlightbox")
        self.findallbox = QtWidgets.QCheckBox(self.frame)
        self.findallbox.setGeometry(QtCore.QRect(10, 160, 191, 21))
        self.findallbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.findallbox.setObjectName("findallbox")
        self.thresholdbox = QtWidgets.QLineEdit(self.frame)
        self.thresholdbox.setGeometry(QtCore.QRect(270, 100, 41, 20))
        self.thresholdbox.setText("")
        self.thresholdbox.setObjectName("thresholdbox")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(19, 100, 241, 20))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(320, 100, 41, 20))
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 381, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 359, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.udselector = QtWidgets.QComboBox(self.layoutWidget)
        self.udselector.setObjectName("udselector")
        self.gridLayout.addWidget(self.udselector, 3, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 2)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QtCore.QRect(970, 440, 221, 23))
        self.saveButton.setObjectName("saveButton")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(10, 330, 381, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.console.setPalette(palette)
        self.console.setFrameShape(QtWidgets.QFrame.VLine)
        self.console.setObjectName("console")
        self.debugbutton = QtWidgets.QPushButton(self.centralwidget)
        self.debugbutton.setGeometry(QtCore.QRect(410, 440, 75, 23))
        self.debugbutton.setObjectName("debugbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(MainWindow.rsxbrowse_clicked)
        self.pushButton_2.clicked.connect(MainWindow.udbrowse_clicked)
        self.pushButton_3.clicked.connect(MainWindow.generate_clicked)
        self.saveButton.clicked.connect(MainWindow.savebutton_clicked)
        self.debugbutton.clicked.connect(MainWindow.debugbutton_clicked)
        self.tableWidget.itemChanged['QTableWidgetItem*'].connect(MainWindow.cellChangedSlot)
        self.pushButton_4.clicked.connect(MainWindow.locationmappingbrowse_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Add?"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Transition Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Activity"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Station"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ConArr"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ConArr Time"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ConWait"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ConWait Time"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Excel row #"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Made"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Transition Time"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Activity"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Station"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ConArr"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ConArr Time"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ConWait"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ConWait Time"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Excel row #"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Duplicates (will not add)"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Error code"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Station"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ConArr"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ConArr Time"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ConWait"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ConWait Time"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Excel row #"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Failed"))
        self.label_3.setText(_translate("MainWindow", "Find connections with UD station name"))
        self.stationnamebox.setText(_translate("MainWindow", "Edinburgh"))
        self.stationnamebox.setPlaceholderText(_translate("MainWindow", "e.g. \'Edinburgh\'"))
        self.label_4.setText(_translate("MainWindow", "that has TIPLOC code"))
        self.tiplocbox.setText(_translate("MainWindow", "EDINBUR"))
        self.tiplocbox.setPlaceholderText(_translate("MainWindow", "e.g. \'EDINBUR\'"))
        self.pushButton_3.setText(_translate("MainWindow", "Find connections"))
        self.label_5.setText(_translate("MainWindow", "between the times"))
        self.mintimebox.setPlaceholderText(_translate("MainWindow", "00:00:00"))
        self.maxtimebox.setPlaceholderText(_translate("MainWindow", "23:59:59"))
        self.highlightbox.setText(_translate("MainWindow", "Highlight Excel rows?"))
        self.findallbox.setText(_translate("MainWindow", "Find all?"))
        self.thresholdbox.setPlaceholderText(_translate("MainWindow", "10"))
        self.label_6.setText(_translate("MainWindow", "and accept a maximum RSX-UD time difference of"))
        self.label_8.setText(_translate("MainWindow", "minutes"))
        self.lineEdit_2.setText(_translate("MainWindow", "C:/Users/Tfarhy/OneDrive - Network Rail/2020.11.24_XML backend for adding connections/uAvanti.xlsx"))
        self.pushButton.setText(_translate("MainWindow", "Browse..."))
        self.lineEdit.setText(_translate("MainWindow", "C:/Users/Tfarhy/OneDrive - Network Rail/2020.11.24_XML backend for adding connections/donovan10.rsx"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse..."))
        self.label_2.setText(_translate("MainWindow", "Unit Diagram:"))
        self.label.setText(_translate("MainWindow", "RSX:"))
        self.label_7.setText(_translate("MainWindow", "Loc. mapping"))
        self.pushButton_4.setText(_translate("MainWindow", "Browse..."))
        self.saveButton.setText(_translate("MainWindow", "Add connections to RSX and save as..."))
        self.debugbutton.setText(_translate("MainWindow", "Debug"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))

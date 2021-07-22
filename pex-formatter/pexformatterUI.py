# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pexformatterUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 375)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 375))
        MainWindow.setMaximumSize(QtCore.QSize(400, 375))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 83))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.oplookupbox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.oplookupbox.setObjectName("oplookupbox")
        self.gridLayout.addWidget(self.oplookupbox, 1, 1, 1, 1)
        self.pexfilebox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pexfilebox.setObjectName("pexfilebox")
        self.gridLayout.addWidget(self.pexfilebox, 0, 1, 1, 1)
        self.oplookupbutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.oplookupbutton.setObjectName("oplookupbutton")
        self.gridLayout.addWidget(self.oplookupbutton, 1, 2, 1, 1)
        self.pexfilebutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pexfilebutton.setObjectName("pexfilebutton")
        self.gridLayout.addWidget(self.pexfilebutton, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.tiploclookupbox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tiploclookupbox.setObjectName("tiploclookupbox")
        self.gridLayout.addWidget(self.tiploclookupbox, 2, 1, 1, 1)
        self.tiploclookupbutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.tiploclookupbutton.setObjectName("tiploclookupbutton")
        self.gridLayout.addWidget(self.tiploclookupbutton, 2, 2, 1, 1)
        self.formatsavebutton = QtWidgets.QPushButton(self.centralwidget)
        self.formatsavebutton.setEnabled(False)
        self.formatsavebutton.setGeometry(QtCore.QRect(200, 340, 191, 23))
        self.formatsavebutton.setObjectName("formatsavebutton")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(10, 120, 381, 171))
        self.console.setObjectName("console")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 300, 381, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.outputfilebox = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.outputfilebox.setText("")
        self.outputfilebox.setPlaceholderText("")
        self.outputfilebox.setObjectName("outputfilebox")
        self.gridLayout_3.addWidget(self.outputfilebox, 0, 1, 1, 1)
        self.outputfilebutton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.outputfilebutton.setObjectName("outputfilebutton")
        self.gridLayout_3.addWidget(self.outputfilebutton, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pexfilebutton.clicked.connect(MainWindow.pexfilebuttonclicked)
        self.formatsavebutton.clicked.connect(MainWindow.formatsavebuttonclicked)
        self.oplookupbutton.clicked.connect(MainWindow.oplookupbuttonclicked)
        self.outputfilebutton.clicked.connect(MainWindow.outputfilebuttonclicked)
        self.tiploclookupbutton.clicked.connect(MainWindow.tiploclookupbuttonclicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PEX formatter version JUN30"))
        self.oplookupbox.setText(_translate("MainWindow", "lookup_tables/operator-lookup.csv"))
        self.pexfilebox.setPlaceholderText(_translate("MainWindow", "timetable.pex"))
        self.oplookupbutton.setText(_translate("MainWindow", "Browse..."))
        self.pexfilebutton.setText(_translate("MainWindow", "Browse..."))
        self.label.setText(_translate("MainWindow", "PEX file"))
        self.label_2.setText(_translate("MainWindow", "Operator lookup CSV"))
        self.label_3.setText(_translate("MainWindow", "TIPLOC lookup CSV"))
        self.tiploclookupbox.setText(_translate("MainWindow", "lookup_tables/tiploc-lookup.csv"))
        self.tiploclookupbutton.setText(_translate("MainWindow", "Browse..."))
        self.formatsavebutton.setText(_translate("MainWindow", "Format .pex and save to output file"))
        self.console.setPlaceholderText(_translate("MainWindow", "Select a .pex file."))
        self.label_5.setText(_translate("MainWindow", "Output file name"))
        self.outputfilebutton.setText(_translate("MainWindow", "Browse..."))


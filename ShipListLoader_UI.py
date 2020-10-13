# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShipListLoader_UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShiplistDataLoader(object):
    def setupUi(self, ShiplistDataLoader):
        ShiplistDataLoader.setObjectName("ShiplistDataLoader")
        ShiplistDataLoader.resize(537, 354)
        self.centralwidget = QtWidgets.QWidget(ShiplistDataLoader)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.CB_ListType = QtWidgets.QComboBox(self.groupBox)
        self.CB_ListType.setObjectName("CB_ListType")
        self.CB_ListType.addItem("")
        self.CB_ListType.addItem("")
        self.CB_ListType.addItem("") ##Add third empty box
        self.CB_ListType.addItem("") ##Add fourth empty box
        
        self.gridLayout_2.addWidget(self.CB_ListType, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.PB_ChooseList = QtWidgets.QPushButton(self.groupBox)
        self.PB_ChooseList.setObjectName("PB_ChooseList")
        self.gridLayout_2.addWidget(self.PB_ChooseList, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        ShiplistDataLoader.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ShiplistDataLoader)
        self.statusbar.setObjectName("statusbar")
        ShiplistDataLoader.setStatusBar(self.statusbar)

        self.retranslateUi(ShiplistDataLoader)
        QtCore.QMetaObject.connectSlotsByName(ShiplistDataLoader)

    def retranslateUi(self, ShiplistDataLoader):
        _translate = QtCore.QCoreApplication.translate
        ShiplistDataLoader.setWindowTitle(_translate("ShiplistDataLoader", "Shiplist Data Loader"))
        self.groupBox.setTitle(_translate("ShiplistDataLoader", "Load Ship List :"))
        self.label.setText(_translate("ShiplistDataLoader", "Choose one list option :"))
        
        self.CB_ListType.setItemText(0, _translate("ShiplistDataLoader", "Preliminary List"))
        self.CB_ListType.setItemText(1, _translate("ShiplistDataLoader", "Today Ship List"))
        self.CB_ListType.setItemText(2, _translate("ShiplistDataLoader", "Friday for Monday Ship List")) ##Add new choice 11/27/18
        self.CB_ListType.setItemText(3, _translate("ShiplistDataLoader", "Saturday for Monday Ship List")) ##Add new choice 11/28/18

        
        self.label_2.setText(_translate("ShiplistDataLoader", "Select your Ship List :"))
        self.PB_ChooseList.setText(_translate("ShiplistDataLoader", "Choose list here "))



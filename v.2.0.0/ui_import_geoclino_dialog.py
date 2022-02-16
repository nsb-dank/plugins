# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_import_geoclino_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImportGeoclinoDialog(object):
    def setupUi(self, ImportGeoclinoDialog):
        ImportGeoclinoDialog.setObjectName("ImportGeoclinoDialog")
        ImportGeoclinoDialog.resize(606, 236)
        self.btnBrowseFile = QtWidgets.QPushButton(ImportGeoclinoDialog)
        self.btnBrowseFile.setGeometry(QtCore.QRect(500, 60, 51, 20))
        self.btnBrowseFile.setObjectName("btnBrowseFile")
        self.lblFileName = QtWidgets.QLabel(ImportGeoclinoDialog)
        self.lblFileName.setEnabled(True)
        self.lblFileName.setGeometry(QtCore.QRect(20, 20, 471, 31))
        self.lblFileName.setObjectName("lblFileName")
        self.txtFileName = QtWidgets.QLineEdit(ImportGeoclinoDialog)
        self.txtFileName.setEnabled(True)
        self.txtFileName.setGeometry(QtCore.QRect(30, 60, 461, 21))
        self.txtFileName.setStyleSheet("background-color: #fff79a")
        self.txtFileName.setReadOnly(True)
        self.txtFileName.setObjectName("txtFileName")
        self.btnImport = QtWidgets.QPushButton(ImportGeoclinoDialog)
        self.btnImport.setGeometry(QtCore.QRect(340, 180, 111, 28))
        self.btnImport.setObjectName("btnImport")
        self.btnCancel = QtWidgets.QPushButton(ImportGeoclinoDialog)
        self.btnCancel.setGeometry(QtCore.QRect(472, 180, 111, 28))
        self.btnCancel.setObjectName("btnCancel")
        self.cboDestinationLayer = QtWidgets.QComboBox(ImportGeoclinoDialog)
        self.cboDestinationLayer.setEnabled(True)
        self.cboDestinationLayer.setGeometry(QtCore.QRect(30, 130, 281, 21))
        self.cboDestinationLayer.setObjectName("cboDestinationLayer")
        self.lblDestinationLayer = QtWidgets.QLabel(ImportGeoclinoDialog)
        self.lblDestinationLayer.setGeometry(QtCore.QRect(20, 100, 151, 16))
        self.lblDestinationLayer.setObjectName("lblDestinationLayer")
        self.lblFileName.setBuddy(self.txtFileName)

        self.retranslateUi(ImportGeoclinoDialog)
        QtCore.QMetaObject.connectSlotsByName(ImportGeoclinoDialog)
        ImportGeoclinoDialog.setTabOrder(self.txtFileName, self.btnBrowseFile)
        ImportGeoclinoDialog.setTabOrder(self.btnBrowseFile, self.cboDestinationLayer)
        ImportGeoclinoDialog.setTabOrder(self.cboDestinationLayer, self.btnImport)
        ImportGeoclinoDialog.setTabOrder(self.btnImport, self.btnCancel)

    def retranslateUi(self, ImportGeoclinoDialog):
        _translate = QtCore.QCoreApplication.translate
        ImportGeoclinoDialog.setWindowTitle(_translate("ImportGeoclinoDialog", "Import GeoClino Data"))
        self.btnBrowseFile.setText(_translate("ImportGeoclinoDialog", "..."))
        self.lblFileName.setText(_translate("ImportGeoclinoDialog", "GeoClino data file(XML file)"))
        self.btnImport.setText(_translate("ImportGeoclinoDialog", "Import Exec"))
        self.btnCancel.setText(_translate("ImportGeoclinoDialog", "Cancel"))
        self.lblDestinationLayer.setText(_translate("ImportGeoclinoDialog", "Target Layer"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_create_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateProjectDialog(object):
    def setupUi(self, CreateProjectDialog):
        CreateProjectDialog.setObjectName("CreateProjectDialog")
        CreateProjectDialog.resize(600, 230)
        self.txtProjectRootPath = QtWidgets.QLineEdit(CreateProjectDialog)
        self.txtProjectRootPath.setGeometry(QtCore.QRect(161, 18, 391, 21))
        self.txtProjectRootPath.setStyleSheet("background-color: #fff79a")
        self.txtProjectRootPath.setClearButtonEnabled(False)
        self.txtProjectRootPath.setObjectName("txtProjectRootPath")
        self.btnSelectFolder = QtWidgets.QPushButton(CreateProjectDialog)
        self.btnSelectFolder.setGeometry(QtCore.QRect(560, 15, 31, 28))
        self.btnSelectFolder.setObjectName("btnSelectFolder")
        self.lblProjectFolder = QtWidgets.QLabel(CreateProjectDialog)
        self.lblProjectFolder.setGeometry(QtCore.QRect(11, 20, 151, 16))
        self.lblProjectFolder.setObjectName("lblProjectFolder")
        self.lblTileLayer = QtWidgets.QLabel(CreateProjectDialog)
        self.lblTileLayer.setGeometry(QtCore.QRect(11, 123, 151, 16))
        self.lblTileLayer.setObjectName("lblTileLayer")
        self.btnSave = QtWidgets.QPushButton(CreateProjectDialog)
        self.btnSave.setGeometry(QtCore.QRect(386, 188, 93, 28))
        self.btnSave.setObjectName("btnSave")
        self.btnCancel = QtWidgets.QPushButton(CreateProjectDialog)
        self.btnCancel.setGeometry(QtCore.QRect(496, 188, 93, 28))
        self.btnCancel.setObjectName("btnCancel")
        self.lblProjectTitle = QtWidgets.QLabel(CreateProjectDialog)
        self.lblProjectTitle.setGeometry(QtCore.QRect(11, 93, 151, 16))
        self.lblProjectTitle.setObjectName("lblProjectTitle")
        self.txtProjectTitle = QtWidgets.QLineEdit(CreateProjectDialog)
        self.txtProjectTitle.setGeometry(QtCore.QRect(161, 91, 391, 21))
        self.txtProjectTitle.setStyleSheet("background-color: #fff79a")
        self.txtProjectTitle.setObjectName("txtProjectTitle")
        self.lblProjectFile = QtWidgets.QLabel(CreateProjectDialog)
        self.lblProjectFile.setGeometry(QtCore.QRect(11, 63, 151, 16))
        self.lblProjectFile.setObjectName("lblProjectFile")
        self.txtProjectName = QtWidgets.QLineEdit(CreateProjectDialog)
        self.txtProjectName.setGeometry(QtCore.QRect(161, 61, 151, 21))
        self.txtProjectName.setStyleSheet("background-color: #fff79a")
        self.txtProjectName.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.txtProjectName.setObjectName("txtProjectName")
        self.cboTileLayer = QtWidgets.QComboBox(CreateProjectDialog)
        self.cboTileLayer.setGeometry(QtCore.QRect(160, 123, 231, 21))
        self.cboTileLayer.setModelColumn(0)
        self.cboTileLayer.setObjectName("cboTileLayer")
        self.cboTileLayer.addItem("")
        self.cboTileLayer.setItemText(0, "")
        self.cboTileLayer.addItem("")
        self.cboTileLayer.addItem("")
        self.cboTileLayer.addItem("")
        self.cboTileLayer.addItem("")
        self.cboTileLayer.addItem("")
        self.lblProjectFile_2 = QtWidgets.QLabel(CreateProjectDialog)
        self.lblProjectFile_2.setGeometry(QtCore.QRect(317, 62, 240, 20))
        self.lblProjectFile_2.setObjectName("lblProjectFile_2")
        self.cboCRS = QtWidgets.QComboBox(CreateProjectDialog)
        self.cboCRS.setGeometry(QtCore.QRect(160, 153, 231, 21))
        self.cboCRS.setModelColumn(0)
        self.cboCRS.setObjectName("cboCRS")
        self.cboCRS.addItem("")
        self.cboCRS.addItem("")
        self.lblCRS = QtWidgets.QLabel(CreateProjectDialog)
        self.lblCRS.setGeometry(QtCore.QRect(10, 153, 151, 16))
        self.lblCRS.setObjectName("lblCRS")
        self.lblProjectFplder2 = QtWidgets.QLabel(CreateProjectDialog)
        self.lblProjectFplder2.setGeometry(QtCore.QRect(160, 40, 391, 20))
        self.lblProjectFplder2.setObjectName("lblProjectFplder2")

        self.retranslateUi(CreateProjectDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateProjectDialog)
        CreateProjectDialog.setTabOrder(self.txtProjectRootPath, self.btnSelectFolder)
        CreateProjectDialog.setTabOrder(self.btnSelectFolder, self.txtProjectName)
        CreateProjectDialog.setTabOrder(self.txtProjectName, self.txtProjectTitle)
        CreateProjectDialog.setTabOrder(self.txtProjectTitle, self.cboTileLayer)
        CreateProjectDialog.setTabOrder(self.cboTileLayer, self.cboCRS)
        CreateProjectDialog.setTabOrder(self.cboCRS, self.btnSave)
        CreateProjectDialog.setTabOrder(self.btnSave, self.btnCancel)

    def retranslateUi(self, CreateProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateProjectDialog.setWindowTitle(_translate("CreateProjectDialog", "Create Project"))
        self.btnSelectFolder.setText(_translate("CreateProjectDialog", "..."))
        self.lblProjectFolder.setText(_translate("CreateProjectDialog", "Project Folder"))
        self.lblTileLayer.setText(_translate("CreateProjectDialog", "Base Map (Tile)"))
        self.btnSave.setText(_translate("CreateProjectDialog", "Create"))
        self.btnCancel.setText(_translate("CreateProjectDialog", "Cancel"))
        self.lblProjectTitle.setText(_translate("CreateProjectDialog", "Project Title"))
        self.lblProjectFile.setText(_translate("CreateProjectDialog", "Project File Name"))
        self.cboTileLayer.setItemText(1, _translate("CreateProjectDialog", "GSI Map(Standard)"))
        self.cboTileLayer.setItemText(2, _translate("CreateProjectDialog", "GIS Map(Pale)"))
        self.cboTileLayer.setItemText(3, _translate("CreateProjectDialog", "GSI Map(Rerief)"))
        self.cboTileLayer.setItemText(4, _translate("CreateProjectDialog", "GIS Map(Photo)"))
        self.cboTileLayer.setItemText(5, _translate("CreateProjectDialog", "Open Street Map"))
        self.lblProjectFile_2.setText(_translate("CreateProjectDialog", ".qgs  (single-byte character only)"))
        self.cboCRS.setItemText(0, _translate("CreateProjectDialog", "EPSG:4326 (WGS 84)"))
        self.cboCRS.setItemText(1, _translate("CreateProjectDialog", "EPSG:4612 (JGD2000)"))
        self.lblCRS.setText(_translate("CreateProjectDialog", "Project CRS"))
        self.lblProjectFplder2.setText(_translate("CreateProjectDialog", ". (single-byte character only)"))


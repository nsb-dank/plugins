# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_export_library_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExportLibraryDialog(object):
    def setupUi(self, ExportLibraryDialog):
        ExportLibraryDialog.setObjectName("ExportLibraryDialog")
        ExportLibraryDialog.resize(475, 410)
        self.btnClose = QtWidgets.QPushButton(ExportLibraryDialog)
        self.btnClose.setGeometry(QtCore.QRect(360, 360, 93, 31))
        self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClose.setObjectName("btnClose")
        self.btnSave = QtWidgets.QPushButton(ExportLibraryDialog)
        self.btnSave.setEnabled(False)
        self.btnSave.setGeometry(QtCore.QRect(240, 360, 101, 31))
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSave.setObjectName("btnSave")
        self.txtFileName = QtWidgets.QLineEdit(ExportLibraryDialog)
        self.txtFileName.setGeometry(QtCore.QRect(140, 50, 161, 21))
        self.txtFileName.setStyleSheet("background-color: #fff79a")
        self.txtFileName.setPlaceholderText("")
        self.txtFileName.setObjectName("txtFileName")
        self.txtFolderName = QtWidgets.QLineEdit(ExportLibraryDialog)
        self.txtFolderName.setEnabled(True)
        self.txtFolderName.setGeometry(QtCore.QRect(140, 20, 281, 21))
        self.txtFolderName.setStyleSheet("background-color: #fff79a")
        self.txtFolderName.setPlaceholderText("")
        self.txtFolderName.setObjectName("txtFolderName")
        self.lblFolderName = QtWidgets.QLabel(ExportLibraryDialog)
        self.lblFolderName.setGeometry(QtCore.QRect(40, 20, 81, 21))
        self.lblFolderName.setObjectName("lblFolderName")
        self.lblFileName = QtWidgets.QLabel(ExportLibraryDialog)
        self.lblFileName.setGeometry(QtCore.QRect(40, 50, 81, 21))
        self.lblFileName.setObjectName("lblFileName")
        self.btnFolderDialog = QtWidgets.QPushButton(ExportLibraryDialog)
        self.btnFolderDialog.setGeometry(QtCore.QRect(421, 19, 31, 23))
        self.btnFolderDialog.setObjectName("btnFolderDialog")
        self.lblFileName2 = QtWidgets.QLabel(ExportLibraryDialog)
        self.lblFileName2.setGeometry(QtCore.QRect(303, 50, 60, 21))
        self.lblFileName2.setObjectName("lblFileName2")
        self.lstScenario = QtWidgets.QListWidget(ExportLibraryDialog)
        self.lstScenario.setEnabled(False)
        self.lstScenario.setGeometry(QtCore.QRect(40, 130, 411, 41))
        self.lstScenario.setObjectName("lstScenario")
        self.lstSubjet = QtWidgets.QListWidget(ExportLibraryDialog)
        self.lstSubjet.setEnabled(False)
        self.lstSubjet.setGeometry(QtCore.QRect(40, 180, 411, 81))
        self.lstSubjet.setObjectName("lstSubjet")
        self.lstAssociated = QtWidgets.QListWidget(ExportLibraryDialog)
        self.lstAssociated.setEnabled(False)
        self.lstAssociated.setGeometry(QtCore.QRect(40, 270, 411, 81))
        self.lstAssociated.setObjectName("lstAssociated")
        self.label = QtWidgets.QLabel(ExportLibraryDialog)
        self.label.setGeometry(QtCore.QRect(40, 80, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(ExportLibraryDialog)
        QtCore.QMetaObject.connectSlotsByName(ExportLibraryDialog)
        ExportLibraryDialog.setTabOrder(self.btnSave, self.btnClose)

    def retranslateUi(self, ExportLibraryDialog):
        _translate = QtCore.QCoreApplication.translate
        ExportLibraryDialog.setWindowTitle(_translate("ExportLibraryDialog", "Export Library Data"))
        self.btnClose.setText(_translate("ExportLibraryDialog", "Close"))
        self.btnSave.setText(_translate("ExportLibraryDialog", "Save"))
        self.lblFolderName.setText(_translate("ExportLibraryDialog", "Export Foleder"))
        self.lblFileName.setText(_translate("ExportLibraryDialog", "FIle Name"))
        self.btnFolderDialog.setText(_translate("ExportLibraryDialog", "..."))
        self.lblFileName2.setText(_translate("ExportLibraryDialog", ".zip"))
        self.label.setText(_translate("ExportLibraryDialog", "Sorry, This function is under-constructing!!"))


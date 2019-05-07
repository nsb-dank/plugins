# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_html_edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HtmlEditDialog(object):
    def setupUi(self, HtmlEditDialog):
        HtmlEditDialog.setObjectName("HtmlEditDialog")
        HtmlEditDialog.resize(600, 700)
        self.btnEdit = QtWidgets.QPushButton(HtmlEditDialog)
        self.btnEdit.setGeometry(QtCore.QRect(380, 610, 93, 28))
        self.btnEdit.setObjectName("btnEdit")
        self.btnCancel = QtWidgets.QPushButton(HtmlEditDialog)
        self.btnCancel.setGeometry(QtCore.QRect(480, 650, 93, 28))
        self.btnCancel.setObjectName("btnCancel")
        self.treeView = QtWidgets.QTreeView(HtmlEditDialog)
        self.treeView.setGeometry(QtCore.QRect(20, 70, 560, 500))
        self.treeView.setObjectName("treeView")
        self.lblPathName = QtWidgets.QLabel(HtmlEditDialog)
        self.lblPathName.setGeometry(QtCore.QRect(150, 30, 331, 21))
        self.lblPathName.setFrameShape(QtWidgets.QFrame.Box)
        self.lblPathName.setText("")
        self.lblPathName.setObjectName("lblPathName")
        self.lblFileName = QtWidgets.QLabel(HtmlEditDialog)
        self.lblFileName.setGeometry(QtCore.QRect(150, 614, 221, 20))
        self.lblFileName.setFrameShape(QtWidgets.QFrame.Box)
        self.lblFileName.setText("")
        self.lblFileName.setObjectName("lblFileName")
        self.lblPath = QtWidgets.QLabel(HtmlEditDialog)
        self.lblPath.setGeometry(QtCore.QRect(19, 30, 131, 21))
        self.lblPath.setObjectName("lblPath")
        self.lblFileName_2 = QtWidgets.QLabel(HtmlEditDialog)
        self.lblFileName_2.setGeometry(QtCore.QRect(20, 578, 131, 21))
        self.lblFileName_2.setObjectName("lblFileName_2")
        self.btnNew = QtWidgets.QPushButton(HtmlEditDialog)
        self.btnNew.setGeometry(QtCore.QRect(380, 576, 91, 28))
        self.btnNew.setObjectName("btnNew")
        self.txtNewFileName = QtWidgets.QLineEdit(HtmlEditDialog)
        self.txtNewFileName.setGeometry(QtCore.QRect(150, 578, 171, 21))
        self.txtNewFileName.setObjectName("txtNewFileName")
        self.lblSelectedFileName = QtWidgets.QLabel(HtmlEditDialog)
        self.lblSelectedFileName.setGeometry(QtCore.QRect(20, 614, 131, 21))
        self.lblSelectedFileName.setObjectName("lblSelectedFileName")
        self.btnPreview = QtWidgets.QPushButton(HtmlEditDialog)
        self.btnPreview.setGeometry(QtCore.QRect(480, 610, 93, 28))
        self.btnPreview.setObjectName("btnPreview")
        self.btnExplorer = QtWidgets.QPushButton(HtmlEditDialog)
        self.btnExplorer.setGeometry(QtCore.QRect(490, 25, 101, 31))
        self.btnExplorer.setObjectName("btnExplorer")
        self.label = QtWidgets.QLabel(HtmlEditDialog)
        self.label.setGeometry(QtCore.QRect(330, 580, 50, 20))
        self.label.setObjectName("label")

        self.retranslateUi(HtmlEditDialog)
        QtCore.QMetaObject.connectSlotsByName(HtmlEditDialog)
        HtmlEditDialog.setTabOrder(self.btnExplorer, self.treeView)
        HtmlEditDialog.setTabOrder(self.treeView, self.txtNewFileName)
        HtmlEditDialog.setTabOrder(self.txtNewFileName, self.btnNew)
        HtmlEditDialog.setTabOrder(self.btnNew, self.btnEdit)
        HtmlEditDialog.setTabOrder(self.btnEdit, self.btnPreview)
        HtmlEditDialog.setTabOrder(self.btnPreview, self.btnCancel)

    def retranslateUi(self, HtmlEditDialog):
        _translate = QtCore.QCoreApplication.translate
        HtmlEditDialog.setWindowTitle(_translate("HtmlEditDialog", "Scenario Edit Dialog"))
        self.btnEdit.setText(_translate("HtmlEditDialog", "Edit"))
        self.btnCancel.setText(_translate("HtmlEditDialog", "Close"))
        self.lblPath.setText(_translate("HtmlEditDialog", "Path"))
        self.lblFileName_2.setText(_translate("HtmlEditDialog", "File Name"))
        self.btnNew.setText(_translate("HtmlEditDialog", "New"))
        self.lblSelectedFileName.setText(_translate("HtmlEditDialog", "Selected File Name"))
        self.btnPreview.setText(_translate("HtmlEditDialog", "Preview"))
        self.btnExplorer.setText(_translate("HtmlEditDialog", "Explorer"))
        self.label.setText(_translate("HtmlEditDialog", ".html"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(521, 414)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        self.btnOK = QtWidgets.QPushButton(SettingsDialog)
        self.btnOK.setGeometry(QtCore.QRect(300, 360, 93, 28))
        self.btnOK.setObjectName("btnOK")
        self.btnCancel = QtWidgets.QPushButton(SettingsDialog)
        self.btnCancel.setGeometry(QtCore.QRect(400, 360, 93, 28))
        self.btnCancel.setObjectName("btnCancel")
        self.groupStrike = QtWidgets.QGroupBox(SettingsDialog)
        self.groupStrike.setGeometry(QtCore.QRect(10, 10, 491, 331))
        self.groupStrike.setObjectName("groupStrike")
        self.lbIContourInterval = QtWidgets.QLabel(self.groupStrike)
        self.lbIContourInterval.setGeometry(QtCore.QRect(30, 50, 171, 21))
        self.lbIContourInterval.setObjectName("lbIContourInterval")
        self.spnContourInterval = QtWidgets.QDoubleSpinBox(self.groupStrike)
        self.spnContourInterval.setGeometry(QtCore.QRect(200, 50, 70, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnContourInterval.sizePolicy().hasHeightForWidth())
        self.spnContourInterval.setSizePolicy(sizePolicy)
        self.spnContourInterval.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnContourInterval.setDecimals(2)
        self.spnContourInterval.setMaximum(100.0)
        self.spnContourInterval.setProperty("value", 10.0)
        self.spnContourInterval.setObjectName("spnContourInterval")
        self.lblLineLength = QtWidgets.QLabel(self.groupStrike)
        self.lblLineLength.setGeometry(QtCore.QRect(30, 80, 171, 21))
        self.lblLineLength.setObjectName("lblLineLength")
        self.lblLineNum = QtWidgets.QLabel(self.groupStrike)
        self.lblLineNum.setGeometry(QtCore.QRect(30, 110, 171, 21))
        self.lblLineNum.setObjectName("lblLineNum")
        self.spnLineLength = QtWidgets.QDoubleSpinBox(self.groupStrike)
        self.spnLineLength.setGeometry(QtCore.QRect(200, 80, 71, 21))
        self.spnLineLength.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnLineLength.setDecimals(0)
        self.spnLineLength.setMaximum(100000.0)
        self.spnLineLength.setSingleStep(100.0)
        self.spnLineLength.setProperty("value", 5000.0)
        self.spnLineLength.setObjectName("spnLineLength")
        self.spnLineNum = QtWidgets.QSpinBox(self.groupStrike)
        self.spnLineNum.setGeometry(QtCore.QRect(200, 110, 70, 21))
        self.spnLineNum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnLineNum.setProperty("value", 10)
        self.spnLineNum.setObjectName("spnLineNum")
        self.spnLineWidth = QtWidgets.QSpinBox(self.groupStrike)
        self.spnLineWidth.setGeometry(QtCore.QRect(200, 140, 70, 21))
        self.spnLineWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnLineWidth.setProperty("value", 1)
        self.spnLineWidth.setObjectName("spnLineWidth")
        self.lblLineWidth = QtWidgets.QLabel(self.groupStrike)
        self.lblLineWidth.setGeometry(QtCore.QRect(30, 140, 171, 21))
        self.lblLineWidth.setObjectName("lblLineWidth")
        self.lblExtensionLine = QtWidgets.QLabel(self.groupStrike)
        self.lblExtensionLine.setGeometry(QtCore.QRect(30, 290, 171, 21))
        self.lblExtensionLine.setObjectName("lblExtensionLine")
        self.chkExtensionLine = QtWidgets.QCheckBox(self.groupStrike)
        self.chkExtensionLine.setGeometry(QtCore.QRect(200, 290, 16, 16))
        self.chkExtensionLine.setText("")
        self.chkExtensionLine.setObjectName("chkExtensionLine")
        self.lbColor = QtWidgets.QLabel(self.groupStrike)
        self.lbColor.setGeometry(QtCore.QRect(40, 190, 161, 21))
        self.lbColor.setObjectName("lbColor")
        self.lbColorH = QtWidgets.QLabel(self.groupStrike)
        self.lbColorH.setGeometry(QtCore.QRect(40, 220, 161, 21))
        self.lbColorH.setObjectName("lbColorH")
        self.lbColorL = QtWidgets.QLabel(self.groupStrike)
        self.lbColorL.setGeometry(QtCore.QRect(40, 250, 161, 21))
        self.lbColorL.setObjectName("lbColorL")
        self.spnColorR = QtWidgets.QSpinBox(self.groupStrike)
        self.spnColorR.setGeometry(QtCore.QRect(200, 190, 60, 21))
        self.spnColorR.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnColorR.setMaximum(255)
        self.spnColorR.setObjectName("spnColorR")
        self.spnColorB = QtWidgets.QSpinBox(self.groupStrike)
        self.spnColorB.setGeometry(QtCore.QRect(340, 190, 60, 21))
        self.spnColorB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnColorB.setMaximum(255)
        self.spnColorB.setObjectName("spnColorB")
        self.spnColorG = QtWidgets.QSpinBox(self.groupStrike)
        self.spnColorG.setGeometry(QtCore.QRect(270, 190, 60, 21))
        self.spnColorG.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnColorG.setMaximum(255)
        self.spnColorG.setObjectName("spnColorG")
        self.label = QtWidgets.QLabel(self.groupStrike)
        self.label.setGeometry(QtCore.QRect(220, 166, 15, 24))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupStrike)
        self.label_2.setGeometry(QtCore.QRect(287, 166, 16, 24))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupStrike)
        self.label_3.setGeometry(QtCore.QRect(360, 166, 15, 24))
        self.label_3.setObjectName("label_3")
        self.spnColorHB = QtWidgets.QSpinBox(self.groupStrike)
        self.spnColorHB.setGeometry(QtCore.QRect(340, 220, 60, 21))
        self.spnColorHB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnColorHB.setMaximum(255)
        self.spnColorHB.setObjectName("spnColorHB")
        self.spnColorHG = QtWidgets.QSpinBox(self.groupStrike)
        self.spnColorHG.setGeometry(QtCore.QRect(270, 220, 60, 21))
        self.spnColorHG.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnColorHG.setMaximum(255)
        self.spnColorHG.setObjectName("spnColorHG")
        self.spnColorHR = QtWidgets.QSpinBox(self.groupStrike)
        self.spnColorHR.setGeometry(QtCore.QRect(200, 220, 60, 21))
        self.spnColorHR.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnColorHR.setMaximum(255)
        self.spnColorHR.setObjectName("spnColorHR")
        self.spnColorLB = QtWidgets.QSpinBox(self.groupStrike)
        self.spnColorLB.setGeometry(QtCore.QRect(340, 250, 60, 21))
        self.spnColorLB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnColorLB.setMaximum(255)
        self.spnColorLB.setObjectName("spnColorLB")
        self.spnColorLG = QtWidgets.QSpinBox(self.groupStrike)
        self.spnColorLG.setGeometry(QtCore.QRect(270, 250, 60, 21))
        self.spnColorLG.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnColorLG.setMaximum(255)
        self.spnColorLG.setObjectName("spnColorLG")
        self.spnColorLR = QtWidgets.QSpinBox(self.groupStrike)
        self.spnColorLR.setGeometry(QtCore.QRect(200, 250, 60, 21))
        self.spnColorLR.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnColorLR.setMaximum(255)
        self.spnColorLR.setObjectName("spnColorLR")

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)
        SettingsDialog.setTabOrder(self.spnContourInterval, self.spnLineLength)
        SettingsDialog.setTabOrder(self.spnLineLength, self.spnLineNum)
        SettingsDialog.setTabOrder(self.spnLineNum, self.spnLineWidth)
        SettingsDialog.setTabOrder(self.spnLineWidth, self.spnColorR)
        SettingsDialog.setTabOrder(self.spnColorR, self.spnColorG)
        SettingsDialog.setTabOrder(self.spnColorG, self.spnColorB)
        SettingsDialog.setTabOrder(self.spnColorB, self.spnColorHR)
        SettingsDialog.setTabOrder(self.spnColorHR, self.spnColorHG)
        SettingsDialog.setTabOrder(self.spnColorHG, self.spnColorHB)
        SettingsDialog.setTabOrder(self.spnColorHB, self.spnColorLR)
        SettingsDialog.setTabOrder(self.spnColorLR, self.spnColorLG)
        SettingsDialog.setTabOrder(self.spnColorLG, self.spnColorLB)
        SettingsDialog.setTabOrder(self.spnColorLB, self.chkExtensionLine)
        SettingsDialog.setTabOrder(self.chkExtensionLine, self.btnOK)
        SettingsDialog.setTabOrder(self.btnOK, self.btnCancel)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.btnOK.setText(_translate("SettingsDialog", "OK"))
        self.btnCancel.setText(_translate("SettingsDialog", "Cancel"))
        self.groupStrike.setTitle(_translate("SettingsDialog", "Draw strike line"))
        self.lbIContourInterval.setText(_translate("SettingsDialog", "Contour interval (m)"))
        self.spnContourInterval.setToolTip(_translate("SettingsDialog", "Polyline interpolation tolerance in map units."))
        self.lblLineLength.setText(_translate("SettingsDialog", "Length of line (m)"))
        self.lblLineNum.setText(_translate("SettingsDialog", "Number of line"))
        self.lblLineWidth.setText(_translate("SettingsDialog", "Line width(point)"))
        self.lblExtensionLine.setText(_translate("SettingsDialog", "Show extension line"))
        self.lbColor.setText(_translate("SettingsDialog", "Line Color(Base)"))
        self.lbColorH.setText(_translate("SettingsDialog", "Line Color(High)"))
        self.lbColorL.setText(_translate("SettingsDialog", "Line Color(Low)"))
        self.label.setText(_translate("SettingsDialog", "R"))
        self.label_2.setText(_translate("SettingsDialog", "G"))
        self.label_3.setText(_translate("SettingsDialog", "B"))


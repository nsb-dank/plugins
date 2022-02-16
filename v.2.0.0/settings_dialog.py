# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSettings, QObject
from PyQt5.QtWidgets import QDialog, QFileDialog
import os.path

from qgis.core import  QgsProject
from .ui_settings_dialog import Ui_SettingsDialog


class SettingsDialog(QDialog, Ui_SettingsDialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface

        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.settings = QSettings()
        self.contour_interval = self.settings.value("geolib3/contourInterval", 10)
        self.strike_line_length = self.settings.value("geolib3/strikeLineLength" , 5000)
        self.strike_line_num = self.settings.value("geolib3/strikeLineNum", 10)
        self.line_width= self.settings.value("geolib3/LineWidth", 3)
        self.line_color_R = self.settings.value("geolib3/LineColorR",255)
        self.line_color_G = self.settings.value("geolib3/LineColorG",128)
        self.line_color_B = self.settings.value("geolib3/LineColorB",0)
        self.line_color_HR = self.settings.value("geolib3/LineColorHR",255)
        self.line_color_HG = self.settings.value("geolib3/LineColorHG",0)
        self.line_color_HB = self.settings.value("geolib3/LineColorHB",0)
        self.line_color_LR = self.settings.value("geolib3/LineColorLR",0)
        self.line_color_LG = self.settings.value("geolib3/LineColorLG",0)
        self.line_color_LB = self.settings.value("geolib3/LineColorLB",255)
        self.show_ext_line = self.settings.value("geolib3/ShowExtLine",True)

        self.ui.spnContourInterval.setValue(float(self.contour_interval))
        self.ui.spnLineLength.setValue(float(self.strike_line_length))
        self.ui.spnLineNum.setValue(int(self.strike_line_num))
        self.ui.spnLineWidth.setValue(int(self.line_width))
        self.ui.spnColorR.setValue(int(self.line_color_R))
        self.ui.spnColorG.setValue(int(self.line_color_G))
        self.ui.spnColorB.setValue(int(self.line_color_B))
        self.ui.spnColorHR.setValue(int(self.line_color_HR))
        self.ui.spnColorHG.setValue(int(self.line_color_HG))
        self.ui.spnColorHB.setValue(int(self.line_color_HB))
        self.ui.spnColorLR.setValue(int(self.line_color_LR))
        self.ui.spnColorLG.setValue(int(self.line_color_LG))
        self.ui.spnColorLB.setValue(int(self.line_color_LB))
        self.ui.chkExtensionLine.setChecked(True if self.show_ext_line == True else False)
        
        # シグナル
        self.ui.btnOK.clicked.connect(self.btn_ok_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)

    def btn_ok_clicked(self):
        self.settings.setValue("geolib3/contourInterval", self.ui.spnContourInterval.value())
        self.settings.setValue("geolib3/strikeLineLength", self.ui.spnLineLength.value())
        self.settings.setValue("geolib3/strikeLineNum", self.ui.spnLineNum.value())
        self.settings.setValue("geolib3/LineWidth", self.ui.spnLineWidth.value())
        self.settings.setValue("geolib3/LineColorR", self.ui.spnColorR.value())
        self.settings.setValue("geolib3/LineColorG", self.ui.spnColorG.value())
        self.settings.setValue("geolib3/LineColorB", self.ui.spnColorB.value())
        self.settings.setValue("geolib3/LineColorHR", self.ui.spnColorHR.value())
        self.settings.setValue("geolib3/LineColorHG", self.ui.spnColorHG.value())
        self.settings.setValue("geolib3/LineColorHB", self.ui.spnColorHB.value())
        self.settings.setValue("geolib3/LineColorLR", self.ui.spnColorLR.value())
        self.settings.setValue("geolib3/LineColorLG", self.ui.spnColorLG.value())
        self.settings.setValue("geolib3/LineColorLB", self.ui.spnColorLB.value())
        self.settings.setValue("geolib3/ShowExtLine", self.ui.chkExtensionLine.isChecked())

        self.close()

    def btn_cancel_clicked(self):
        self.close()
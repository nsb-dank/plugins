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

        self.ui.tab.setVisible(False)
        self.ui.tab_3.setVisible(False)

        self.settings = QSettings()
        self.editor_program = self.settings.value("geolib3/editorProgram","")
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
        self.use_cloud = self.settings.value("geolib3/UseCloud",True)
        self.use_custom = self.settings.value("geolib3/UseCustom",False)
        self.host_name = self.settings.value("geolib3/HostName","")
        self.db_name = self.settings.value("geolib3/DbName","")
        self.port_no = self.settings.value("geolib3/PortNo","")
        self.db_user_id = self.settings.value("geolib3/DbUserId","")
        self.db_password = self.settings.value("geolib3/DbPassword","")
        self.user_id = self.settings.value("geolib3/userId","test@test.com")
        self.password = self.settings.value("geolib3/password","")

        self.ui.txtEditorProgram.setText(self.editor_program)
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
        self.ui.rdoUseCloud.setChecked(True if self.use_cloud == True else False)
        self.ui.rdoUseCustom.setChecked(True if self.use_custom == True else False)
        self.ui.txtHostName.setText(self.host_name)
        self.ui.txtDbName.setText(self.db_name)
        self.ui.txtPortNo.setText(self.port_no)
        self.ui.txtDbUserId.setText(self.db_user_id)
        self.ui.txtDbPassword.setText(self.db_password)
        self.ui.txtUserId.setText(self.user_id)
        self.ui.txtPassword.setText(self.password)
        
        # シグナル
        self.ui.btnFileSelect.clicked.connect(self.btn_fileSelect_clicked)
        self.ui.btnOK.clicked.connect(self.btn_ok_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)
        self.ui.rdoUseCloud.clicked.connect(self.rdo_changed)
        self.ui.rdoUseCustom.clicked.connect(self.rdo_changed)

    def btn_fileSelect_clicked(self):
        # ファイル選択ダイアログを開く
        project_path, ext = os.path.splitext(QgsProject.instance().fileName())
        file_name,_ = QFileDialog.getOpenFileName(self, "Select Execution file", project_path, "Execution files (*.exe;*.bat)")
        if file_name:
            self.ui.txtEditorProgram.setText(file_name)

    def rdo_changed(self):
        if self.ui.rdoUseCloud.isChecked():
            self.ui.txtHostName.setEnabled(False)
            self.ui.txtDbName.setEnabled(False)
            self.ui.txtPortNo.setEnabled(False)
            self.ui.txtDbUserId.setEnabled(False)
            self.ui.txtDbPassword.setEnabled(False)
        elif self.ui.rdoUseCustom.isChecked():
            self.ui.txtHostName.setEnabled(True)
            self.ui.txtDbName.setEnabled(True)
            self.ui.txtPortNo.setEnabled(True)
            self.ui.txtDbUserId.setEnabled(True)
            self.ui.txtDbPassword.setEnabled(True)

    def btn_ok_clicked(self):
        self.settings.setValue("geolib3/editorProgram", self.ui.txtEditorProgram.text())
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
        self.settings.setValue("geolib3/userId", self.ui.txtUserId.text())
        self.settings.setValue("geolib3/password", self.ui.txtPassword.text())
        self.settings.setValue("geolib3/UseCloud",self.ui.rdoUseCloud.isChecked())
        self.settings.setValue("geolib3/UseCustom",self.ui.rdoUseCustom.isChecked())
        if self.ui.rdoUseCloud.isChecked():
            self.settings.setValue("geolib3/HostName", "")
            self.settings.setValue("geolib3/DbName", "")
            self.settings.setValue("geolib3/PortNo", "")
            self.settings.setValue("geolib3/DbUserId","")
            self.settings.setValue("geolib3/DbPassword","")
        elif self.ui.rdoUseCustom.isChecked():
            self.settings.setValue("geolib3/HostName", self.ui.txtHostName.text())
            self.settings.setValue("geolib3/DbName", self.ui.txtDbName.text())
            self.settings.setValue("geolib3/PortNo", self.ui.txtPortNo.text())
            self.settings.setValue("geolib3/DbUserId",self.ui.txtDbUserId.text())
            self.settings.setValue("geolib3/DbPassword",self.ui.txtDbPassword.text())

        self.close()

    def btn_cancel_clicked(self):
        self.close()
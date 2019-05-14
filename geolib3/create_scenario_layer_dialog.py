# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CreateScenarioLayerDialog
                                 A QGIS plugin
 This plugin captures the field survey and creates a geological map.
                             -------------------
        begin                : 2019-5-12
        git sha              : $Format:%H$
        copyright            : (C) 2019 by =Dank Co., Ltd.
        email                : yukihiko.karata@nsb-dank.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt5.QtCore import QSettings, QObject
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
import os

from qgis.core import QgsProject
from .ui_create_layer_dialog import Ui_CreateLayerDialog
from .geolib_util import GeolibUtil
from nose2.result import PASS
from _ast import Pass
geolib3 = GeolibUtil()

class CreateScenarioLayerDialog(QDialog, Ui_CreateLayerDialog):

    browsePathSetting = "/plugins/geolib/BrowsePath"

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface

        self.ui = Ui_CreateLayerDialog()
        self.ui.setupUi(self)

        settings = QSettings()
        self._home = settings.value(CreateScenarioLayerDialog.browsePathSetting, '')

        self.ui.cboMapType.addItems([
                    self.tr('New Scenario Map'),
                    self.tr('Import Scenario Map')
                ])
        self.ui.frmFileSelect.setVisible(False)

        # show the dialog
        self.show()

        # シグナル
        self.ui.cboMapType.currentIndexChanged.connect(self.map_type_changed)
        self.ui.btnFileSelect.clicked.connect(self.btn_file_select_clicked)
        self.ui.btnCreate.clicked.connect(self.btn_create_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)

    ##########################
    #　イベントメソッド
    ##########################
    def map_type_changed(self):
        # マップタイプ 選択時
        _map_type_index = self.ui.cboMapType.currentIndex()
        if _map_type_index == 0:  #新規シナリオマップ
            self.ui.frmFileSelect.setVisible(False)
            self.ui.lblFile.setText('')
        elif _map_type_index == 1:  #既存シナリオマップ
            self.setFilter = "GeoPackage(*.gpkg);";
            self.ui.frmFileSelect.setVisible(True)
            self.ui.lblFile.setText(self.tr('Select FIle'))

    def btn_file_select_clicked(self):
        # ファイル選択ダイアログを表示
        _select_file =QFileDialog.getOpenFileName(self,'','',self.setFilter)
        self.ui.txtFileSelect.setText(_select_file[0])

    def btn_create_clicked(self):
        #入力チェック
        if self.ui.txtMapTitle.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The map name not been entered. Please enter."))
        elif self.ui.txtMapName.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The file name has not been entered. Please enter."))
        else:
            # シナリオマップ の追加
            _layer_type_name = 'Scenario Map'
            _layer_type ='Scenario'

            _map_title = self.ui.txtMapTitle.text()
            _map_name = self.ui.txtMapName.text()
            _map_filename = _map_name + '.gpkg'

            _project_root_path, ext = os.path.splitext(QgsProject.instance().fileName())
            _layer_type_folder_path = os.path.join(_project_root_path, _layer_type)
            _map_folder_path = os.path.join(_layer_type_folder_path, _map_name)
            _map_file_path = os.path.join(_layer_type_folder_path, _map_filename)
            _template_name = 'scenario'
            
            #シナリオノード配下にマップノードを作成する
            geolib3.createSubNode(_layer_type_name, _map_title)
            
            #シナリオフォルダ配下にマップフォルダを作成する
            geolib3.createFolder(_map_folder_path)
            
            _map_type_index = self.ui.cboMapType.currentIndex()
            
            if (_map_type_index == 0):                              # シナリオマップ新規作成の場合
                #シナリオテンプレートファイルからシナリオマップフォルダ配下にコピーする
                geolib3.copyTemplateFile( _template_name, _map_folder_path, _map_name)
            elif (_map_type_index == 1):                           #既存ファイルから作成の場合
                # 既存ファイルをシナリオフォルダ配下にコピーする
                _source_file_path = self.ui.txtFileSelect.text()
                geolib3.copyFile(_source_file_path, _map_folder_path, _map_name)
                    
            #テンプレートのスタイルファイルをマップフォルダ配下にコピーしてレイヤーに適用する
            geolib3.copyTemplateStyle(_template_name, _map_folder_path)
                
            geolib3.addGeoPackageLayerTree(_map_folder_path, 'point', _layer_type_name, _map_title, _map_name, _template_name)
            geolib3.addGeoPackageLayerTree(_map_folder_path, 'line', _layer_type_name, _map_title, _map_name, _template_name)
            geolib3.addGeoPackageLayerTree(_map_folder_path, 'polygon', _layer_type_name, _map_title, _map_name, _template_name)

        #ダイアログを閉じる
        self.close()

    def btn_cancel_clicked(self):
        # ダイアログを閉じる
        self.close()


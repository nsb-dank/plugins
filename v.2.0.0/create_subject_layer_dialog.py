# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CreateSubjectLayerDialog
                                 A QGIS plugin
 This plugin captures the field survey and creates a geological map.
                             -------------------
        begin                : 2019-5-12
        last update          : 2022-02-06
        git sha              : $Format:%H$
        copyright            : (C) 2022 by =Dank Co., Ltd.
        email                : ykarata@geotrekking.jp
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
from .ui_create_subject_layer_dialog import Ui_CreateSubjectLayerDialog
from .geolib_util import GeolibUtil
from nose2.result import PASS
from _ast import Pass
geolib3 = GeolibUtil()

class CreateSubjectLayerDialog(QDialog, Ui_CreateSubjectLayerDialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface

        self.ui = Ui_CreateSubjectLayerDialog()
        self.ui.setupUi(self)

        self.ui.cboMapType.addItems([
                    self.tr(u'Create new geologial map layer'),
                    self.tr(u'Import existing geological map layer')
                ])
        self.ui.frmFileSelect.setVisible(False)

        self.show()

        # シグナル
        self.ui.cboMapType.currentIndexChanged.connect(self.map_type_changed)
        self.ui.btnFolderSelect.clicked.connect(self.btn_folder_select_clicked)
        self.ui.btnFileSelect.clicked.connect(self.btn_file_select_clicked)
        self.ui.btnCreate.clicked.connect(self.btn_create_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)

    ##########################
    #　イベントメソッド
    ##########################    
    def map_type_changed(self):
        # マップタイプ 選択時
        _map_type_index = self.ui.cboMapType.currentIndex()
        if _map_type_index == 0:  #新規
            self.ui.frmFileSelect.setVisible(False)
            self.ui.lblFile.setText('')
        elif _map_type_index == 1:  #既存
            self.setFilter = "GeoPackage(*.gpkg);;GeoJson(*.geojson)"
            self.ui.frmFileSelect.setVisible(True)
            self.ui.lblFile.setText(self.tr(u'Select File'))

    def btn_file_select_clicked(self):
        # ファイル選択ダイアログを表示
        _select_file =QFileDialog.getOpenFileName(self,'','',self.setFilter)
        self.ui.txtFileSelect.setText(_select_file[0])

    def btn_folder_select_clicked(self):
        # フォルダ選択ダイアログを表示
        rootpath = os.path.abspath(os.path.dirname("__file__"))
        _select_folder =QFileDialog.getExistingDirectory(None, "rootpath", rootpath)
        self.ui.txtFolderSelect.setText(_select_folder)    

    def btn_create_clicked(self):
        #入力チェック
        if self.ui.txtFolderSelect.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u'The folder name has not been entered. Please enter.'))   
        elif self.ui.txtMapName.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u'The file name has not been entered.Please enter.'))     
        elif self.ui.txtMapTitle.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u'Layer group name has not been entered.Please enter.'))
        else:
            # 主題図マップ の追加
            _map_folder_path = self.ui.txtFolderSelect.text()
            _map_title = self.ui.txtMapTitle.text()
            _map_name = self.ui.txtMapName.text()
            _map_filename = _map_name + '.gpkg'
            _map_file_path = os.path.join(_map_folder_path, _map_filename)
            _template_name = 'geomap'          
            
            #マップノードを作成する
            geolib3.createNode(_map_title)
            
            #データファイルを作成する          
            _map_type_index = self.ui.cboMapType.currentIndex()
            if (_map_type_index == 0):                              # シナリオマップ新規作成の場合
                #シナリオテンプレートファイルからマップフォルダ配下にコピーする
                geolib3.copyTemplateFile( _template_name, _map_folder_path, _map_name)
            elif (_map_type_index == 1):                           #既存ファイルから作成の場合
                # 既存ファイルをマップフォルダ配下にコピーする
                _source_file_path = self.ui.txtFileSelect.text()
                geolib3.copyFile(_source_file_path, _map_folder_path, _map_name)
                    
            #テンプレートのスタイルファイルをマップフォルダ配下にコピーしてレイヤーに適用する
            geolib3.copyTemplateStyle(_template_name, _map_folder_path)

            # if _map_category_index == 0:
            geolib3.addGeoPackageLayerTree(_map_folder_path, 'pnt', _map_title, _map_title, _map_name, _template_name)
            geolib3.addGeoPackageLayerTree(_map_folder_path, 'strdip', _map_title, _map_title, _map_name, _template_name)
            geolib3.addGeoPackageLayerTree(_map_folder_path, 'geo_L', _map_title, _map_title, _map_name, _template_name)
            geolib3.addGeoPackageLayerTree(_map_folder_path, 'geo_A', _map_title, _map_title, _map_name, _template_name)

        #ダイアログを閉じる
        self.close()

    def btn_cancel_clicked(self):
        # ダイアログを閉じる
        self.close()


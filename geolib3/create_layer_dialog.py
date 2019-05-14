# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CreateLayerDialog
                                 A QGIS plugin
 This plugin captures the field survey and creates a geological map.
                             -------------------
        begin                : 2018-12-10
        git sha              : $Format:%H$
        copyright            : (C) 2018 by =Dank Co., Ltd.
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

class CreateLayerDialog(QDialog, Ui_CreateLayerDialog):

    browsePathSetting = "/plugins/geolib/BrowsePath"

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface

        self.ui = Ui_CreateLayerDialog()
        self.ui.setupUi(self)

        settings = QSettings()
        self._home = settings.value(CreateLayerDialog.browsePathSetting, '')

        self.ui.cboLayerType.addItems(['',self.tr('Scenario'),self.tr('Subject'),self.tr('Associated')])
        self.ui.frmFileSelect.setVisible(False)

        # show the dialog
        self.show()

        # シグナル
        self.ui.cboLayerType.currentIndexChanged.connect(self.layer_type_changed)
        self.ui.cboMapType.currentIndexChanged.connect(self.map_type_changed)
        self.ui.btnFileSelect.clicked.connect(self.btn_file_select_clicked)
        self.ui.btnCreate.clicked.connect(self.btn_create_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)

    ##########################
    #　イベントメソッド
    ##########################
    def layer_type_changed(self):
        #レイヤータイプ選択時
        self.ui.cboMapType.clear()
        _layer_type_index = self.ui.cboLayerType.currentIndex()
        # cboMapType に Item をセット
        if _layer_type_index == 1:
            self.ui.cboMapType.addItems([
                    self.tr('New Scenario Map'),
                    self.tr('Import Scenario Map')
                ])
        elif _layer_type_index == 2:
            self.ui.cboMapType.addItems([
                    self.tr('New Geological Map'),
                    self.tr('Import Geological Map'),
                    self.tr('New Hazard Map'),
                    self.tr('Import Hazard Map')
                ])
        elif _layer_type_index == 3:
            self.ui.cboMapType.addItems([
                    self.tr('Import geoTIFF'),
                    self.tr('XYZ Tiles'),
                    self.tr('WMS')
                ])

    def map_type_changed(self):
        # マップタイプ 選択時
        _layer_type_index = self.ui.cboLayerType.currentIndex()
        _map_type_index = self.ui.cboMapType.currentIndex()
        if _layer_type_index == 1: # シナリオ
            if _map_type_index == 0:  #新規シナリオマップ
                self.ui.frmFileSelect.setVisible(False)
                self.ui.lblFile.setText('')
            elif _map_type_index == 1:  #既存シナリオマップ
                self.setFilter = "GeoPackage(*.gpkg);;GeoJson(*.geojson)";
                self.ui.frmFileSelect.setVisible(True)
                self.ui.lblFile.setText(self.tr('Select FIle'))
                self.ui.txtUrl.setVisible(False)
                
        elif _layer_type_index == 2:  #主題図
            if _map_type_index == 0:  #新規地質図
                self.ui.frmFileSelect.setVisible(False)
                self.ui.lblFile.setText('')
            elif _map_type_index == 1:  #新規ハザードマップ
                self.ui.frmFileSelect.setVisible(False)
                self.ui.lblFile.setText('')
            elif _map_type_index == 2: #既存地質図
                self.setFilter = "GeoPackage(*.gpkg);;GeoJson(*.geojson)";
                self.ui.frmFileSelect.setVisible(True)
                self.ui.lblFile.setText(self.tr('Select FIle'))
                self.ui.txtUrl.setVisible(False)
            elif _map_type_index == 3: #既存ハザードマップ
                self.setFilter = "GeoPackage(*.gpkg);;GeoJson(*.geojson)";
                self.ui.frmFileSelect.setVisible(True)
                self.ui.lblFile.setText(self.tr('Select FIle'))
                self.ui.txtUrl.setVisible(False)
                
        elif _layer_type_index == 3:  #関連図
            if _map_type_index == 0: #既存ラスター
                self.setFilter = "GeoTIFF(*.tif *.tiff))";
                self.ui.frmFileSelect.setVisible(True)
                self.ui.lblFile.setText(self.tr('Select FIle'))
                self.ui.txtUrl.setVisible(False)
            else: # XYZ, WMS
                self.ui.frmFileSelect.setVisible(True)
                self.ui.lblFile.setText(self.tr('URL'))
                self.ui.txtUrl.setVisible(True)


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
            _layer_type_index = self.ui.cboLayerType.currentIndex()
            _map_type_index = self.ui.cboMapType.currentIndex()
            _map_title = self.ui.txtMapTitle.text()
            _map_name = self.ui.txtMapName.text()
            #geolib3 = GeolibUtil()
            _project_root_path, ext = os.path.splitext(QgsProject.instance().fileName())

            # シナリオマップ の追加
            if (_layer_type_index == 1):
                #シナリオルート配下にレイヤーグループを作成する
                _layer_type_name = 'Scenario Map'
                _layer_type ='Scenario'
                _layer_type_path = os.path.join(_project_root_path, _layer_type)
                geolib3.createSubNode(_layer_type_name, _map_title)
                
                if (_map_type_index == 0):
                    # シナリオマップ新規作成の場合、シナリオテンプレートファイルをシナリオフォルダ配下にコピーする
                    _template_name = 'scenario'
                    geolib3.copyTemplateFile(  _template_name, _layer_type_path, _map_name)
                else :
                    #既存ファイルをシナリオフォルダ配下にコピーする
                    _source_file_path = self.ui.txtFileSelect.text()
                    geolib3.copyFile(_source_file_path, _layer_type_path, _map_name)
                    
                #テンプレートのスタイルファイルをマップフォルダ配下にコピーしてレイヤーに適用する
                _style_path = os.path.join(_layer_type_path, _map_name, 'style')
                geolib3.copyTemplateStyle(_template_name, _style_path)
                
                geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name,'point',_style_path)
                geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name,'line',_style_path)
                geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name,'polygon',_style_path)

            # 主題図の追加
            elif (_layer_type_index == 2):
                #主題図ルート配下にレイヤーグループを作成する
                _layer_type_name = 'Subject Map'
                _layer_type ='Subject'
                _layer_type_path = os.path.join(_project_root_path, _layer_type)
                geolib3.createSubNode(_layer_type_name,_map_title)
                
                if (_map_type_index == 0):
                    #地質図新規作成の場合、地質図テンプレートファイルを主題図フォルダ配下にコピーする
                    _template_name = 'geomap'
                    geolib3.copyTemplateFile( _template_name, _layer_type_path, _map_name)
                    #テンプレートスタイルファイルをマップフォルダ配下にコピーしてレイヤーに適用する
                    _style_path = os.path.join(_layer_type_path, _map_name, 'style')
                    geolib3.copyTemplateStyle(_template_name, _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name,'pnt', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'strdip', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'geo_L', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'geo_A', _style_path)
                elif (_map_type_index == 1):
                    #ハザード新規作成の場合、ハザードマップテンプレートファイルを主題図フォルダ配下にコピーする
                    _template_name = 'hazardmap'
                    geolib3.copyTemplateFile( _template_name, _layer_type_path, _map_name)
                    #テンプレートスタイルファイルをマップフォルダ配下にコピーしてレイヤーに適用する
                    _style_path = os.path.join(_layer_type_path, _map_name, 'style')
                    geolib3.copyTemplateStyle(_template_name, _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name,'pnt', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'geo_L', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'geo_A', _style_path)
                elif (_map_type_index == 2):
                    #既存地質図ファイルを主題図フォルダ配下にコピーする
                    _template_name = 'geomap'
                    _source_file_path = self.ui.txtFileSelect.text()
                    geolib3.copyFile(_source_file_path, _layer_type_path, _map_name)
                    #テンプレートスタイルファイルをマップフォルダ配下にコピーしてレイヤーに適用する
                    _style_path = os.path.join(_layer_type_path, _map_name, 'style')
                    geolib3.copyTemplateStyle(_template_name, _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name,'pnt', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'strdip', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'geo_L', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'geo_A', _style_path)
                elif  (_map_type_index == 3):
                    #既存ハザードマップファイルを主題図フォルダ配下にコピーする
                    _template_name = 'hazardmap'
                    _source_file_path = self.ui.txtFileSelect.text()
                    geolib3.copyFile(_source_file_path, _layer_type_path, _map_name)
                    #テンプレートスタイルファイルをマップフォルダ配下にコピーしてレイヤーに適用する
                    _style_path = os.path.join(_layer_type_path, _map_name, 'style')
                    geolib3.copyTemplateStyle(_template_name, _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name,'pnt', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'strdip', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'geo_L', _style_path)
                    geolib3.addGeoPackageLayer(_layer_type_path,_layer_type_name,_map_title,_map_name, 'geo_A', _style_path)

            # 関連図の追加
            elif (_layer_type_index == 3):
                #関連図ルート配下にレイヤーグループを作成する
                _layer_type_name = 'Associated Map'
                _layer_type ='Associated'
                _layer_type_path = os.path.join(_project_root_path, _layer_type)
                geolib3.createSubNode(_layer_type_name, _map_title)
                if (_map_type_index == 0):
                    #GioTiffファイルを追加する
                    _source_file_path = self.ui.txtFileSelect.text()
                    geolib3.copyFile(_source_file_path, _layer_type_path, _map_name)
                    #レイヤーツリーに追加する
                    _map_file_path = os.path.join(_layer_type_path, _map_name, (_map_name + '.tiff'))
                    geolib3.addGeoTiffLayerTree(_layer_type_name, _map_title, _map_name, _map_file_path)                    

                elif (_map_type_index == 1):
                    _source_url = self.ui.txtUrl.text()
                    # レイヤーツリーにXYZ Tile URLを追加する
                    geolib3.addWmsLayerTree(_layer_type_name, _map_title, _map_name, _source_url)

                elif (_map_type_index == 2):
                    # レイヤーツリーにWMS URLを追加する
                    _source_url = self.ui.txtUrl.text()
                    geolib3.addWmsLayerTree(_layer_type_name, _map_title, _map_name, _source_url)
                    
            else:
                QMessageBox.information(self, "geolib3 error", self.tr(u"Please enter the layer type."))

            #ダイアログを閉じる
            self.close()

    def btn_cancel_clicked(self):
        # ダイアログを閉じる
        self.close()


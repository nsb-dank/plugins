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
geolib = GeolibUtil()

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


    def layer_type_changed(self):
        #レイヤータイプ選択時
        self.ui.cboMapType.clear()
        layerTypeIndex = self.ui.cboLayerType.currentIndex()
        # cboMapType に Item をセット
        if layerTypeIndex == 1:
            self.ui.cboMapType.addItems([
                    self.tr('New Scenario Map'),
                    self.tr('Import Vector Map')
                ])
        elif layerTypeIndex == 2:
            self.ui.cboMapType.addItems([
                    self.tr('New Geological Map'),
                    self.tr('New Hazard Map'),
                    self.tr('Import Vector Map')
                ])
        elif layerTypeIndex == 3:
            self.ui.cboMapType.addItems([
                    self.tr('Import geoTIFF'),
                    self.tr('XYZ Tiles'),
                    self.tr('WMS')
                ])

    def map_type_changed(self):
        # マップタイプ 選択時
        layerTypeIndex = self.ui.cboLayerType.currentIndex()
        mapTypeIndex = self.ui.cboMapType.currentIndex()
        if layerTypeIndex == 1: # シナリオ
            if mapTypeIndex == 0:  #新規シナリオマップ
                self.ui.frmFileSelect.setVisible(False)
                self.ui.lblFile.setText('')
            elif mapTypeIndex == 1:  #既存シナリオマップ
                self.setFilter = "GeoPackage(*.gpkg);;GeoJson(*.geojson)";
                self.ui.frmFileSelect.setVisible(True)
                self.ui.lblFile.setText(self.tr('Select FIle'))
                self.ui.txtUrl.setVisible(False)
        elif layerTypeIndex == 2:  #主題図
            if mapTypeIndex == 0:  #新規地質図
                self.ui.frmFileSelect.setVisible(False)
                self.ui.lblFile.setText('')
            elif mapTypeIndex == 1:  #新規ハザードマップ
                self.ui.frmFileSelect.setVisible(False)
                self.ui.lblFile.setText('')
            elif mapTypeIndex == 2: #既存ベクター
                self.setFilter = "GeoPackage(*.gpkg);;GeoJson(*.geojson)";
                self.ui.frmFileSelect.setVisible(True)
                self.ui.lblFile.setText(self.tr('Select FIle'))
                self.ui.txtUrl.setVisible(False)

        elif layerTypeIndex == 3:  #関連図
            if mapTypeIndex == 0: #既存ラスター
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
        self.select_file =QFileDialog.getOpenFileName(self,'','',self.setFilter)
        self.ui.txtFileSelect.setText(self.select_file[0])

    def btn_create_clicked(self):
        #入力チェック
        if self.ui.txtMapName.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The map name not been entered. Please enter."))
        elif self.ui.txtFileName.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The file name has not been entered. Please enter."))
        else:
            layerTypeIndex = self.ui.cboLayerType.currentIndex()
            mapTypeIndex = self.ui.cboMapType.currentIndex()
            mapName = self.ui.txtMapName.text()
            fileName = self.ui.txtFileName.text()
            #geolib = GeolibUtil()
            projectPath, ext = os.path.splitext(QgsProject.instance().fileName())

            # シナリオマップ の追加
            if (layerTypeIndex == 1):
                #シナリオルート配下にレイヤーグループを作成する
                layerType = 'Scenario Map'
                rootName ='Scenario'
                rootPath = os.path.join(projectPath, rootName)
                geolib.createSubNode(rootName,mapName)
                if (mapTypeIndex == 0):
                    # シナリオテンプレートファイルをシナリオフォルダ配下にコピーする
                    templateName = 'scenario'
                    geolib.copyTemplateFile(layerType, rootPath, templateName, fileName)
                    #テンプレートのスタイルファイルをコピーしてレイヤーに適用する
                    stylePath = os.path.join(projectPath, 'style','scenario')
                    geolib.copyTemplateStyle(templateName, stylePath)

                    geolib.addLayer(rootPath,layerType,fileName,mapName,'point',stylePath)
                    geolib.addLayer(rootPath,layerType,fileName,mapName,'line',stylePath)
                    geolib.addLayer(rootPath,layerType,fileName,mapName,'polygon',stylePath)
                else :
                    #既存ファイルをシナリオフォルダ配下にコピーする
                    sourceFile = self.ui.txtFileSelect.text()
                    geolib.copyFile(sourceFile,rootPath,fileName)

            # 主題図の追加
            elif (layerTypeIndex == 2):
                #主題図ルート配下にレイヤーグループを作成する
                layerType = 'Subject Map'
                rootName ='Subject'
                rootPath = os.path.join(projectPath, rootName)
                geolib.createSubNode(rootName,mapName)
                if (mapTypeIndex == 0):
                    #地質図テンプレートファイルを主題図フォルダ配下にコピーする
                    templateName = 'geomap'
                    geolib.copyTemplateFile(layerType, rootPath, templateName, fileName)
                    stylePath = os.path.join(projectPath, 'style','geomap')
                    geolib.copyTemplateStyle(templateName, stylePath)
                    geolib.addLayer(rootPath,layerType,fileName,mapName,'pnt', stylePath)
                    geolib.addLayer(rootPath,layerType,fileName,mapName, 'strdip', stylePath)
                    geolib.addLayer(rootPath,layerType,fileName,mapName, 'geo_L', stylePath)
                    geolib.addLayer(rootPath,layerType,fileName,mapName, 'geo_A', stylePath)
                elif (mapTypeIndex == 1):
                    #ハザードマップテンプレートファイルを主題図フォルダ配下にコピーする
                    templateName = 'hazardmap'
                    geolib.copyTemplateFile(layerType, rootPath, templateName, fileName)
                    stylePath = os.path.join(projectPath, 'style','hazardmap')
                    geolib.copyTemplateStyle(templateName, stylePath)
                    geolib.addLayer(rootPath,layerType,fileName,mapName,'pnt', stylePath)
                    geolib.addLayer(rootPath,layerType,fileName,mapName, 'geo_L', stylePath)
                    geolib.addLayer(rootPath,layerType,fileName,mapName, 'geo_A', stylePath)
                else:
                    #既存ベクターファイルを主題図フォルダ配下にコピーする
                    sourceFile = self.ui.txtFileSelect.text()
                    geolib.copyFile(sourceFile,rootPath,fileName)

            # 関連図の追加
            elif (layerTypeIndex == 3):
                #関連図ルート配下にレイヤーグループを作成する
                layerType = 'Associated Map'
                rootName ='Associated'
                rootPath = os.path.join(projectPath, rootName)
                geolib.createSubNode(rootName,mapName)
                if (mapTypeIndex == 0):
                    #GioTiffを追加する
                    pass
                else:
                    # URLを追加する
                    pass
            else:
                QMessageBox.information(self, "geolib error", self.tr(u"Please enter the layer type."))

            #ダイアログを閉じる
            self.close()

    def btn_cancel_clicked(self):
        # ダイアログを閉じる
        self.close()


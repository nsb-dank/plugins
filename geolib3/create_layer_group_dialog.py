# -*- coding: utf-8 -*-
"""
/***************************************************************************
 importGeoClinoDialog
                                 A QGIS plugin
 This plugin captures the field survey and creates a geological map.
                             -------------------
        begin                : 2017-05-31
        git sha              : $Format:%H$
        copyright            : (C) 2017 by =Dank Co., Ltd.
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
from PyQt5.QtWidgets import QDialog, QMessageBox
import os

from qgis.core import QgsProject
from .ui_create_layer_group_dialog import Ui_CreateLayerGroupDialog
from .geolib_util import GeolibUtil
geolib = GeolibUtil()

class CreateLayerGroupDialog(QDialog, Ui_CreateLayerGroupDialog):

    browsePathSetting = "/plugins/geolib/BrowsePath"


    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface

        self.ui = Ui_CreateLayerGroupDialog()
        self.ui.setupUi(self)

        settings = QSettings()
        self._home = settings.value(CreateLayerGroupDialog.browsePathSetting, '')

        self.ui.cboLayerType.addItems(['','Scenario','Subject','Associated'])

        # show the dialog
        self.show()

        # シグナル
        self.ui.cboLayerType.currentIndexChanged.connect(self.layer_type_changed)
        self.ui.cboMapType.currentIndexChanged.connect(self.map_type_changed)
        self.ui.btnCreate.clicked.connect(self.btn_create_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)


    def layer_type_changed(self):
        #レイヤータイプ選択時
        self.ui.cboMapType.clear()
        layerType = self.ui.cboLayerType.currentText()
        if layerType == 'Scenario':
            self.ui.cboMapType.addItems(['Scenario Map','Vector Map'])
        elif layerType == 'Subject':
            self.ui.cboMapType.addItems(['Geological Map','Vector Map','geoTIFF'])
        elif layerType == 'Associated':
            self.ui.cboMapType.addItems(['XYZ Tiles','WMS'])

    def map_type_changed(self):
        pass

    def btn_create_clicked(self):
        #入力チェック
        if self.ui.txtGroupName.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The group name not been entered. Please enter."))
        elif self.ui.txtGeoPackageName.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The geopackage name has not been entered. Please enter."))
        else:
            layerType = self.ui.cboLayerType.currentText()
            groupName = self.ui.txtGroupName.text()
            geoPackageName = self.ui.txtGeoPackageName.text()
            #geolib = GeolibUtil()
            projectPath, ext = os.path.splitext(QgsProject.instance().fileName())

            if (layerType == 'Scenario Map'):
                #テンプレートファイルをシナリオフォルダ配下にコピーする
                rootName ='Scenario'
                rootPath = os.path.join(projectPath, rootName)
                geolib.copyGeoPackageFile(layerType, rootPath, geoPackageName)
                #シナリオルート配下にレイヤーグループを作成する
                geolib.createSubNode(rootName,groupName)
                # レイヤーグループにレイヤーを追加する
                style_path = os.path.join(projectPath, "style")
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName,'point',style_path)
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName,'line',style_path)
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName,'polygon',style_path)

            elif (layerType == 'Subject Map'):
                #テンプレートファイルをシナリオフォルダ配下にコピーする
                rootName ='Subject'
                rootPath = os.path.join(projectPath, rootName)
                geolib.copyGeoPackageFile(layerType, rootPath, geoPackageName)
                #シナリオルート配下にレイヤーグループを作成する
                geolib.createSubNode(rootName,groupName)
                # レイヤーグループにレイヤーを追加する
                style_path = os.path.join(projectPath, "style")
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName,'pnt', style_path)
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName, 'strdip', style_path)
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName, 'geo_L', style_path)
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName, 'geo_A', style_path)
            else:
                QMessageBox.information(self, "geolib error", self.tr(u"Please enter the layer type."))

            #ダイアログを閉じる
            self.close()

    def btn_cancel_clicked(self):
        # ダイアログを閉じる
        self.close()

    def createVectorLayer(self):
                #テンプレートファイルをシナリオフォルダ配下にコピーする
                rootName ='Scenario'
                rootPath = os.path.join(projectPath, rootName)
                geolib.copyGeoPackageFile(layerType, rootPath, geoPackageName)
                #シナリオルート配下にレイヤーグループを作成する
                geolib.createSubNode(rootName,groupName)
                # レイヤーグループにレイヤーを追加する
                style_path = os.path.join(projectPath, "style")
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName,'point',style_path)
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName,'line',style_path)
                geolib.addLayer(rootPath,layerType,geoPackageName,groupName,'polygon',style_path)




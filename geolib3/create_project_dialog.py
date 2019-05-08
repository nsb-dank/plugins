# -*- coding: utf-8 -*-
"""
/***************************************************************************
 createProjectDialog
                                 A QGIS plugin
 This plugin captures the field survey and creates a geological map.
                             -------------------
        begin                : 2017-05-31
        git sha              : $Format:%H$
        copyright            : (C) 2017 by =Dank Co., Ltd.
        email                : yukihiko.karata@nsb-dank.com
 ***************************************************************************/

/****************************************************************************
 *                                                                          *
 *   This program is free software; you can redistribute it and/or modify   *
 *   it under the terms of the GNU General Public License as published by   *
 *   the Free Software Foundation; either version 2 of the License, or      *
 *   (at your option) any later version.                                    *
 *                                                                          *
 ***************************************************************************/
"""
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, \
                                                    QFileDialog, \
                                                    QMessageBox
import os
from PyQt5.Qt import QFileInfo
from qgis.core import QgsPointXY, \
                                       QgsRectangle, \
                                       QgsProject, \
                                       QgsLayerTreeGroup, \
                                       QgsCoordinateReferenceSystem, \
                                       QgsRasterLayer
from qgis.utils import iface
from .geolib_util import GeolibUtil
from .ui_create_project_dialog import Ui_CreateProjectDialog

class CreateProjectDialog(QDialog, Ui_CreateProjectDialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface

        self.ui = Ui_CreateProjectDialog()
        self.ui.setupUi(self)

        project_folder = GeolibUtil.project_folder
        project_file = GeolibUtil.project_filename

        # シグナル
        self.ui.btnSelectFolder.clicked.connect(self.btn_selectfolder_clicked)
        self.ui.btnSave.clicked.connect(self.btn_save_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)

    # フォルダ選択ボタン押下時
    def btn_selectfolder_clicked(self):

        # フォルダ選択ダイアログを表示
        self.select_folder =QFileDialog.getExistingDirectory(self)
        self.ui.txtProjectFolder.setText(self.select_folder)

    # 保存ボタン押下時
    def btn_save_clicked(self):
        #入力チェック
        if self.ui.txtProjectFolder.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The project folder not been entered. Please enter."))
        elif self.ui.txtProjectFile.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The project file name has not been entered. Please enter."))
        elif self.ui.txtProjectTitle.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The project title has not been entered. Please enter."))
        else:
            # レイヤパネルにレイヤが存在しているときはメッセージを表示
            layer = [layer for layer in QgsProject.instance().mapLayers().values()]
            if len(layer) > 0:
                _reply = QMessageBox.question(self, self.tr(u"Confirmation"),
                    self.tr(u"When I create a new project, the map canvas data will be discarded.\n Are you sure?"),
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if _reply == QMessageBox.Yes:
                    #既存のレイヤをすべて削除
                    root = QgsProject.instance().layerTreeRoot()
                    for child in root.children():
                        if isinstance(child, QgsLayerTreeGroup):
                            root.removeChildNode(child)
                    QgsProject.instance().removeAllMapLayers()
                    #プロジェクトを作成
                    self.create_project()
            else:
                #プロジェクトを作成
                self.create_project()

            #キャンバスを表示
            #print self.rlayer
            canvas = self.iface.mapCanvas()
            #self.canvas.setCenter(QgsPoint(139.767052, 35.681167))
            canvas.setCenter(QgsPointXY(140, 36))
            canvas.zoomScale(1000000)
            for layer in canvas.layers():
                layer.triggerRepaint()
            #print "Project Created."

            self.close()


    def btn_cancel_clicked(self):
        self.close()

    def create_project(self):
        # プロジェクトファイル（.qgs）を作成し保存する
        project_folder = self.ui.txtProjectFolder.text()
        project_file = self.ui.txtProjectFile.text() +'.qgs'
        project_title = self.ui.txtProjectTitle.text()

        project_name = self.ui.txtProjectFile.text()
        #project_path = os.path.join(project_folder, project_name,"layer")

        # プロジェクトフォルダを作成する
        geolib = GeolibUtil()
        geolib.createProjectDirectory(project_folder, project_name)

        #サブフォルダを作成する
        #geolib.createSubFolder(os.path.join(project_folder, project_name, "Route_Map"))
        #geolib.createSubFolder(os.path.join(project_folder, project_name, "Scenario"))
        geolib.createFolder(os.path.join(project_folder, project_name, "Scenario","html"))
        #スタイルファイルをコピーする
        #style_path = os.path.join(project_folder, project_name,"style")
        #geolib.copyStyleFile(style_path)

        #背景地図タイルを作成する
        tile_layer = self.ui.cboTileLayer.currentText()
        #_map_name = u'GSI Map(Standard)'
        rlayer = None
        if tile_layer != "":
            if tile_layer == u"GSI Map(Standard)":
                urlWithParams = 'contextualWMSLegend=0&crs=EPSG:3857&' + \
                                'dpiMode=7&featureCount=10&format=image/png&' + \
                                'layers=std&styles=default&tileMatrixSet=z2to18&' + \
                                'url=http://gsi-cyberjapan.github.io/experimental_wmts/gsitiles_wmts.xml'
            elif tile_layer == u"GIS Map(Pale)":
                urlWithParams = 'contextualWMSLegend=0&crs=EPSG:3857&' + \
                                'dpiMode=7&featureCount=10&format=image/png&' + \
                                'layers=pale&styles=default&tileMatrixSet=z2to18&' + \
                                'url=http://gsi-cyberjapan.github.io/experimental_wmts/gsitiles_wmts.xml'
            elif tile_layer == u"GSI Map(Rerief)":
                urlWithParams = 'contextualWMSLegend=0&crs=EPSG:3857&' + \
                                'dpiMode=7&featureCount=10&format=image/png&' + \
                                'layers=relief&styles=default&tileMatrixSet=z2to15&' + \
                                'url=http://gsi-cyberjapan.github.io/experimental_wmts/gsitiles_wmts.xml'
            elif tile_layer == u"GIS Map(Photo)":
                urlWithParams = 'contextualWMSLegend=0&crs=EPSG:3857&' + \
                                'dpiMode=7&featureCount=10&format=image/jpg&' + \
                                'layers=seamlessphoto&styles=default&tileMatrixSet=z2to18&' + \
                                'url=http://gsi-cyberjapan.github.io/experimental_wmts/gsitiles_wmts.xml'
            elif tile_layer == u"Open Street Map":
                urlWithParams = 'type=xyz&url=http://c.tile.openstreetmap.org/{z}/{x}/{y}.png'
            else:
                tile_layer = ""

            if tile_layer != "":
                rlayer = QgsRasterLayer(urlWithParams, tile_layer, 'wms')
                rlayer.setCustomProperty("labeling", "pal")
                rlayer.setCustomProperty("labeling/enabled", "true")
                rlayer.setCustomProperty("labeling/fontFamily", "Arial")
                rlayer.setCustomProperty("labeling/fontSize", "10")
                rlayer.setCustomProperty("labeling/fieldName", "ename")
                rlayer.setCustomProperty("labeling/placement", "2")
                rlayer.setMaximumScale(1000000.0)
                QgsProject.instance().addMapLayer(rlayer)
        else:
            #print u"Base Map is not selected."
            None

        # グループツリーおよびレイヤを作成する
        #root_name ='Geological Map'
        #group_name = ''
        #geolib.createRootNode(root_name)
        #geolib.createLayer(project_path,root_name,group_name,'Point' ,'pnt',self.tr(u'pnt'),style_path)
        #geolib.createLayer(project_path,root_name,group_name,'Point' ,'strdip',self.tr(u'strdip'),style_path)
        #geolib.createLayer(project_path,root_name,group_name,'LineString' ,'geo_L',self.tr(u'geo_L'),style_path)
        #geolib.createLayer(project_path,root_name,group_name,'Polygon' ,'geo_A',self.tr(u'geo_A'),style_path)
        geolib.createRootNode('Associated')
        geolib.createRootNode('Subject')
        geolib.createRootNode('Scenario')

        #プロジェクトを定義する
                #プロジェクトCRSを設定
        selectCrs = self.ui.cboCRS.currentText()
        projectCrs = QgsCoordinateReferenceSystem(4326) #default CRS
        if (selectCrs == 'EPSG:4326 (WGS 84)'):
            projectCrs = QgsCoordinateReferenceSystem(4326)
        if (selectCrs == 'EPSG:4612 (JGD2000)'):
            projectCrs = QgsCoordinateReferenceSystem(4612)
        if (selectCrs == 'EPSG:3857 (WGS 84 / Pseudo Mercator)'):
            projectCrs = QgsCoordinateReferenceSystem(3857)

        QgsProject.instance().setTitle(project_title)
        QgsProject.instance().setCrs(projectCrs)

        canvas = self.iface.mapCanvas()
        rect = QgsRectangle( QgsPointXY( 132, 34), QgsPointXY( 145, 40))
        canvas.setExtent(rect)
        canvas.zoomScale(1000000)

        canvas.refresh()

        #プロジェクトを保存
        QgsProject.instance().write(os.path.join(project_folder,project_file))




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
 *                                                                                                                                 *
 *   This program is free software; you can redistribute it and/or modify          *
 *   it under the terms of the GNU General Public License as published by       *
 *   the Free Software Foundation; either version 2 of the License, or                 *
 *   (at your option) any later version.                                                                     *
 *                                                                                                                                 *
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

        # シグナル
        self.ui.btnSelectFolder.clicked.connect(self.btn_selectfolder_clicked)
        self.ui.btnSave.clicked.connect(self.btn_save_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)

    ##########################
    #　イベントメソッド
    ##########################
    # フォルダ選択ボタン押下時
    def btn_selectfolder_clicked(self):
        # フォルダ選択ダイアログを表示
        _select_path =QFileDialog.getExistingDirectory(self)
        self.ui.txtProjectRootPath.setText(_select_path)

    # 保存ボタン押下時
    def btn_save_clicked(self):
        #入力チェック
        if self.ui.txtProjectRootPath.text() == '':
            QMessageBox.warning(self, self.tr(u"Warning"), self.tr(u"The project folder not been entered. Please enter."))
        elif self.ui.txtProjectName.text() == '':
            QMessageBox.warning(self, self.tr(u"Warning"), self.tr(u"The project file name has not been entered. Please enter."))
        elif self.ui.txtProjectTitle.text() == '':
            QMessageBox.warning(self, self.tr(u"Warning"), self.tr(u"The project title has not been entered. Please enter."))
        else:
            # レイヤパネルにレイヤが存在しているときはメッセージを表示
            layer = [layer for layer in QgsProject.instance().mapLayers().values()]
            if len(layer) > 0:
                _reply = QMessageBox.question(self, self.tr(u"Confirmation"),
                    self.tr(u"When I create a new project, the map canvas data will be discarded.\n Are you sure?"),
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if _reply == QMessageBox.Yes:
                    #Yesの場合、既存のレイヤをすべて削除してプロジェクトを作成
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
            canvas = self.iface.mapCanvas()
            canvas.setCenter(QgsPointXY(140, 36))
            canvas.zoomScale(1000000)
            for layer in canvas.layers():
                layer.triggerRepaint()

            self.close()

    # キャンセルボタン押下時
    def btn_cancel_clicked(self):
        self.close()

    ##########################
    # プロジェクト作成メソッド
    ##########################
    def create_project(self):
        geolib3 = GeolibUtil()

        # プロジェクト定義を設定
        _project_root_path = self.ui.txtProjectRootPath.text()
        _project_name = self.ui.txtProjectName.text()
        _project_path = os.path.join(_project_root_path, _project_name)
        _project_filename = self.ui.txtProjectName.text() +'.qgs'
        _project_title = self.ui.txtProjectTitle.text()

        QgsProject.instance().setTitle(_project_title)

        # グループツリーおよびレイヤを作成する
        geolib3.createRootNode('Associated Map')
        geolib3.createRootNode('Subject Map')
        geolib3.createRootNode('Scenario Map')

        # プロジェクトフォルダおよびシナリオフォルダを作成する
        geolib3.createFolder(_project_path)
        geolib3.createFolder(os.path.join(_project_path, "Scenario"))
        geolib3.createFolder(os.path.join(_project_path,"Subject"))
        geolib3.createFolder(os.path.join(_project_path, "Associated"))
        geolib3.createFolder(os.path.join(_project_path, "Scenario","html"))

         #プロジェクトCRSを設定
        _select_crs = self.ui.cboCRS.currentText()
        _project_crs = QgsCoordinateReferenceSystem(4326) #default CRS
        if (_select_crs == 'EPSG:4326 (WGS 84)'):
            _project_crs = QgsCoordinateReferenceSystem(4326)
        if (_select_crs == 'EPSG:4612 (JGD2000)'):
            _project_crs = QgsCoordinateReferenceSystem(4612)
        if (_select_crs == 'EPSG:3857 (WGS 84 / Pseudo Mercator)'):
            _project_crs = QgsCoordinateReferenceSystem(3857)
        QgsProject.instance().setCrs(_project_crs)

        #背景地図タイルを作成する
        _tile_layer = self.ui.cboTileLayer.currentText()
        geolib3.loadBaseMap(_tile_layer)

        # キャンバスを表示する
        canvas = self.iface.mapCanvas()
        rect = QgsRectangle( QgsPointXY( 132, 34), QgsPointXY( 145, 40))
        canvas.setExtent(rect)
        canvas.zoomScale(1000000)

        canvas.refresh()

        #プロジェクトを保存
        QgsProject.instance().write(os.path.join(_project_root_path, _project_filename))




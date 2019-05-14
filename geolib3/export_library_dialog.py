# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ExportLibraryDialog
                                 A QGIS plugin
 This plugin captures the field survey and creates a geological map.
                             -------------------
        begin                : 2019-02-18
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
from PyQt5.QtCore import  QSettings, QObject, QUrl, Qt, QDateTime
from PyQt5.QtWidgets import QDialog,QTableView,QMessageBox, QFileDialog
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel
from qgis.core import QgsProject, QgsVectorFileWriter, QgsLayerTreeModel,QgsLayerTreeLayer,QgsLayerTreeNode,QgsVectorLayer, QgsRasterLayer


import os
import ftplib
import glob
from pathlib import Path

from .ui_export_library_dialog import Ui_ExportLibraryDialog
from .geolib_util import GeolibUtil

class ExportLibraryDialog(QDialog, Ui_ExportLibraryDialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.ui = Ui_ExportLibraryDialog()
        self.ui.setupUi(self)
        # show the dialog

        #シグナル
        self.ui.btnFolderDialog.clicked.connect(self.btn_folder_dialog_clicked)
        self.ui.btnSave.clicked.connect(self.btn_save_clicked)
        self.ui.btnClose.clicked.connect(self.btn_close_clicked)

        self.dispLstScenario()

    def dispLstScenario(self):
        root = QgsProject.instance().layerTreeRoot()
        node = root.findGroup('Scenario Map')
        group = []
        groupName = None
        for group in node.children():
            groupName = group.name()
            self.ui.lstScenario.addItem(groupName)


    def btn_folder_dialog_clicked(self):
        # フォルダ選択ダイアログを表示
        self.select_folder =QFileDialog.getExistingDirectory(self)
        self.ui.txtFolderName.setText(self.select_folder)

    def btn_save_clicked(self):
        pass

    def btn_close_clicked(self):
        # ダイアログを閉じる
        self.close()

    def createMapFile(self):
        # 選択したレイヤーのエクスポート用ファイルを作成する
        pass



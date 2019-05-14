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
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
import os
from xml.dom import minidom
from qgis.core import QgsLayerTreeGroup, \
                                QgsLayerTreeLayer, \
                                QgsFeature, \
                                QgsPointXY, \
                                QgsGeometry, \
                                QgsProject

from .ui_import_geoclino_dialog import Ui_ImportGeoclinoDialog
from .geolib_util import GeolibUtil


class ImportGeoclinoDialog(QDialog, Ui_ImportGeoclinoDialog):

    browsePathSetting = "/plugins/geolib3/BrowsePath"

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface

        self.ui = Ui_ImportGeoclinoDialog()
        self.ui.setupUi(self)

        settings = QSettings()
        self._home = settings.value(ImportGeoclinoDialog.browsePathSetting, '')

        # PREPARE COMBO BOX
        self.ui.cboDestinationLayer.clear()
        _root = QgsProject.instance().layerTreeRoot()
        _node = _root.findGroup("Subject Map")
        group = []
        groupName = None
        for _group in _node.children():
            #if isinstance(group, QgsLayerTreeGroup):
            for _layer in _group.children():
                if _layer.name().find('strdip')>-1:
                    _layer_name = _layer.name()
                    self.ui.cboDestinationLayer.addItem(_layer_name, _layer)

        # show the dialog
        self.show()

        self.ui.btnBrowseFile.clicked.connect(self.btn_browseFile_clicked)
        self.ui.btnImport.clicked.connect(self.btn_import_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)

    def btn_browseFile_clicked(self):
        # ファイル選択ダイアログを開く
        _select_file  = QFileDialog.getOpenFileName(self, "Select GeoClino Data file(XML)",
            self._home, "GeoClino Data files (*.xml)")
        self.ui.txtFileName.setText(_select_file[0])

    def btn_import_clicked(self):
        #入力チェック
        if self.ui.txtFileName.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The xml file name not been entered. Please enter."))
        else:
            # インポートを実行する
            xml_file_name = self.ui.txtFileName.text()
            homedir = os.path.dirname(xml_file_name)
            settings = QSettings()
            settings.setValue(ImportGeoclinoDialog.browsePathSetting, homedir)
            if not xml_file_name:
                QMessageBox.information(self, "geolib error", self.tr(u"You must specify a GeoClino Data file to import"))
                return
            if not os.path.exists(xml_file_name):
                QMessageBox.information(self, "geolib error", self.tr(u"Cannot open file: " )+ xml_file_name)
                return

            xml_data = minidom.parse(xml_file_name)
            geolib3 = GeolibUtil()
            #指定したcboDestinationLayerに地物を追加
            layerName = self.ui.cboDestinationLayer.currentText()
            print(layerName)
            layerTree = self.ui.cboDestinationLayer.currentData()
            print (layerTree)
            layer = QgsProject.instance().mapLayer(layerTree.layerId())
            print(layer)
            provider = layer.dataProvider()
            geolib3.addFeatureGeoclino(provider, xml_data)

            # ダイアログを閉じる
            self.close()

    def btn_cancel_clicked(self):
        # ダイアログを閉じる
        self.close()


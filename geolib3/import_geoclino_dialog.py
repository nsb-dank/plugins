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

    browsePathSetting = "/plugins/geoMapping/BrowsePath"

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface

        self.ui = Ui_ImportGeoclinoDialog()
        self.ui.setupUi(self)

        settings = QSettings()
        self._home = settings.value(self.browsePathSetting, '')

        # PREPARE COMBO BOX
        self.ui.cboDestinationLayer.clear()
        root = QgsProject.instance().layerTreeRoot()
        node = root.findGroup("Subject")
        group = []
        groupName = None
        for group in node.children():
            #if isinstance(group, QgsLayerTreeGroup):
            for layer in group.children():
                if layer.name().find('strdip')>-1:
                    groupName = layer.name()
                    self.ui.cboDestinationLayer.addItem(groupName)

        # show the dialog
        self.show()

        self.ui.btnBrowseFile.clicked.connect(self.btn_browseFile_clicked)
        self.ui.btnImport.clicked.connect(self.btn_import_clicked)
        self.ui.btnCancel.clicked.connect(self.btn_cancel_clicked)

    def btn_browseFile_clicked(self):
        # ファイル選択ダイアログを開く
        xmlFilePath,_ = QFileDialog.getOpenFileName(self, "Select GeoClino Data file(XML)",
            self._home, "GeoClino Data files (*.xml)")
        if xmlFilePath:
            self.ui.txtFileName.setText(str(xmlFilePath))
            xml_file_path, ext = os.path.splitext( os.path.basename(xmlFilePath) )

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
            #try:
            xml_data = minidom.parse(xml_file_name)
            geolib = GeolibUtil()

            #指定したcboDestinationLayerに地物を追加

            project_path, ext = os.path.splitext(QgsProject.instance().fileName())
            group_name = self.ui.cboDestinationLayer.currentText()
            routemap_path = os.path.join(project_path,"Subject",group_name)
            layerName = self.ui.cboDestinationLayer.currentText()

            #地物の追加
            root = QgsProject.instance().layerTreeRoot()
            node = root.findGroup("Subject")
            for group in node.children():
                #children = node.children()
                for layer in group.children():
                    layer_name = layer.name()
                    if layer_name ==layerName:
                        routemap_layer = layer

            if routemap_layer is not None:
                layer = QgsProject.instance().mapLayer(routemap_layer.layerId())
                provider = layer.dataProvider()
                geolib.addFeatureGeoclino(provider, xml_data)

            # ダイアログを閉じる
            self.close()

    def btn_cancel_clicked(self):
        # ダイアログを閉じる
        self.close()


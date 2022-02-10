# -*- coding: utf-8 -*-
"""
geolib3.py
    Created                : 2018-07-05
    copyright         : (C) 2018 Dank Co., Ltd.
    email                : yukihiko.karata@nsb-dank.com
/***************************************************************************
 *   This program is free software; you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation; either version 2 of the License, or
 *   (at your option) any later version.
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

from qgis.PyQt.QtCore import  QSettings, QTranslator, qVersion, QCoreApplication,QVariant,Qt
from qgis.PyQt.QtGui import QIcon, QColor
from qgis.PyQt.QtWidgets import QDockWidget,QWidget,QAction,QMenu,QToolButton,QMessageBox
from qgis.core import  QgsApplication, \
                                QgsProject, \
                                QgsMapLayer, \
                                QgsWkbTypes, \
                                QgsPoint,QgsGeometry, \
                                QgsSimpleMarkerSymbolLayer, \
                                QgsSvgMarkerSymbolLayer, \
                                QgsSimpleLineSymbolLayer, \
                                QgsSimpleFillSymbolLayer
from qgis.gui import QgsRubberBand

import os.path
import shutil
from distutils import dir_util
from .geolib_util import GeolibUtil
from geolib3.edit_attribute_dockwidget import EditAttributeDockWidget
from geolib3.draw_boundary_dockwidget import DrawBoundaryDockWidget

class Geolib3:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.plugin_dir = os.path.dirname(__file__)
        self.locale = QSettings().value("locale/userLocale")[0:2]
        self.locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'geolib3_{}.qm'.format(self.locale))
        if os.path.exists(self.locale_path):
            self.translator = QTranslator()
            self.translator.load(self.locale_path)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # 初期設定値
        self.settings = QSettings()
        self.editor_program = self.settings.value("geolib3/editorProgram","")
        self.contour_interval = self.settings.value("geolib3/contourInterval", 10)
        self.strike_line_length = self.settings.value("geolib3/strikeLineLength" , 5000)
        self.strike_line_num = self.settings.value("geolib3/strikeLineNum", 10)
        self.line_width= self.settings.value("geolib3/LineWidth", 3)
        self.line_color_R = self.settings.value("geolib3/LineColorR",255)
        self.line_color_G = self.settings.value("geolib3/LineColorG",128)
        self.line_color_B = self.settings.value("geolib3/LineColorB",0)
        self.line_color_HR = self.settings.value("geolib3/LineColorHR",255)
        self.line_color_HG = self.settings.value("geolib3/LineColorHG",0)
        self.line_color_HB = self.settings.value("geolib3/LineColorHB",0)
        self.line_color_LR = self.settings.value("geolib3/LineColorLR",0)
        self.line_color_LG = self.settings.value("geolib3/LineColorLG",0)
        self.line_color_LB = self.settings.value("geolib3/LineColorLB",255)
        self.show_ext_line = self.settings.value("geolib3/ShowExtLine",True)
        self.use_cloud = self.settings.value("geolib3/UseCloud",True)
        self.use_custom = self.settings.value("geolib3/UseCustom",False)
        self.host_name = self.settings.value("geolib3/HostName","")
        self.db_name = self.settings.value("geolib3/DbName","")
        self.port_no = self.settings.value("geolib3/PortNo","")
        self.db_user_id = self.settings.value("geolib3/DbUserId","")
        self.db_password = self.settings.value("geolib3/DbPassword","")
        self.user_id = self.settings.value("geolib3/userId","test@test.com")
        self.password = self.settings.value("geolib3/password","")

        #templateのsvgファイルをQGISのsvgフォルダにコピー
        geolib3 = GeolibUtil()
        _svgPath = os.path.join(QgsApplication.prefixPath(),'svg').replace('/','\\')
        _templatePath = os.path.join(geolib3.pluginpath,'template','svg').replace('/','\\')
        geolib3.createFolder(_svgPath)
        dir_util.copy_tree(_templatePath, _svgPath)

        # インスタンス属性を宣言
        self.actions = []
        self.menu = QMenu(self.tr('&Geolibraray Tools'))
        self.toolbar = self.iface.addToolBar(self.tr('Geolibrary Tools'))
        self.toolbar.setObjectName(self.tr('Geolibrary Tools'))

        self.pluginIsActive = False
        self.iface.currentLayerChanged.connect(self.menuControl)
        self.qgsProject = QgsProject.instance()
        self.qgsProject.layersAdded.connect(self.menuControl)

        # 現在の選択レイヤを確認
        self.currentlayer = None

        self.editFeatureDockwidget = None
        self.drawBoundaryDockwidget = None

    def tr(self, message):
        return QCoreApplication.translate('geolib3', message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        status_tip=None,
        whats_this=None,
        checkable=False,
        shortcut=None,
        parent = None):
        icon = QIcon(icon_path)
        action = QAction(icon, text ,parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)
        if checkable:
            action.setCheckable(True)
        if status_tip is not None:
            action.setStatusTip(status_tip)
        if whats_this is not None:
            action.setWhatsThis(whats_this)
        if shortcut:
            action.setShortcut(shortcut)
        self.actions.append(action)
        return action

    def initGui(self):
        #プロジェクトツール --------
        self.menuProjectTool = QMenu(self.tr('Project Tool'))
        self.menu.addMenu(self.menuProjectTool)
        self.toolProjectTool = QToolButton()
        self.toolProjectTool.setIcon(QIcon(os.path.join(self.plugin_dir, 'icons', 'project_tool.png')))
        self.toolProjectTool.setMenu(self.menuProjectTool)
        self.toolProjectTool.setPopupMode(QToolButton.InstantPopup)
        self.toolbar.addWidget(self.toolProjectTool)
        #新規プロジェクト
        self.actionNewProject = self.add_action(
                        os.path.join(self.plugin_dir, 'icons', 'new.png'),
                        text=self.tr('New'),
                        callback=self.newProject,
                        status_tip=self.tr('New Project'),
                        checkable=False,
                        enabled_flag=True
                        )
        self.menuProjectTool.addAction(self.actionNewProject)
        #self.toolbar.addAction(self.actionNewProject)
        #プロジェクトを開く
        self.actionOpenProject = self.add_action(os.path.join(self.plugin_dir, 'icons', 'open.png'),
                        text=self.tr('Open...'),
                        callback=self.openProject,
                        status_tip=self.tr('Open Project'),
                        checkable=False,
                        enabled_flag=True
                        )
        self.menuProjectTool.addAction(self.actionOpenProject)
        #self.toolbar.addAction(self.actionOpenProject)

        #レイヤーツール -------
        self.toolbar.addSeparator()
        self.menu.addSeparator()
        self.menuLayerTool = QMenu(self.tr('Layer Tool'))
        self.menu.addMenu(self.menuLayerTool)
        self.toolLayerTool = QToolButton()
        self.toolLayerTool.setIcon(QIcon(os.path.join(self.plugin_dir, 'icons', 'layer_tool.png')))
        self.toolLayerTool.setMenu(self.menuLayerTool)
        self.toolLayerTool.setPopupMode(QToolButton.InstantPopup)
        self.toolbar.addWidget(self.toolLayerTool)
        #シナリオレイヤーの追加
        self.actionAddScenarioLayer = self.add_action(os.path.join(self.plugin_dir, 'icons', 'add_group.png'),
                        text=self.tr('Add Scenario Layer'),
                        callback=self.addScenarioLayer,
                        status_tip=self.tr('Add Scenario Layer'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menuLayerTool.addAction(self.actionAddScenarioLayer)

        #シナリオ編集
        self.actionEditHtml = self.add_action(os.path.join(self.plugin_dir, 'icons', 'edit_html.png'),
                        text=self.tr('Show Contents Folder'),
                        callback=self.editHtml,
                        status_tip=self.tr('Open Contents Folder dialog'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menuLayerTool.addAction(self.actionEditHtml)
        #主題図レイヤの追加
        self.actionAddSubjectLayer = self.add_action(os.path.join(self.plugin_dir, 'icons', 'add_group.png'),
                        text=self.tr('Add Subject Layer'),
                        callback=self.addSubjectLayer,
                        status_tip=self.tr('Add Layer'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menuLayerTool.addAction(self.actionAddSubjectLayer)        
        #Geoclinoからインポート
        self.actionImportGeoclino = self.add_action(os.path.join(self.plugin_dir, 'icons', 'import_geoclino.png'),
                        text=self.tr('Import Geoclino Data'),
                        callback=self.importGeoclino,
                        status_tip=self.tr('Geoclino for iPhone XML Data Import'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menuLayerTool.addAction(self.actionImportGeoclino)
        #編集ツール -------
        self.toolbar.addSeparator()
        self.menu.addSeparator()
        #レイヤ保存
        self.actionSaveLayer = self.add_action(os.path.join(self.plugin_dir, 'icons', 'save.png'),
                        text=self.tr('Save Layer Data'),
                        callback=self.saveLayer,
                        status_tip=self.tr('Update the data of the selected layer'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionSaveLayer)
        self.toolbar.addAction(self.actionSaveLayer)
        #地物の追加
        self.actionAddFeature = self.add_action(os.path.join(self.plugin_dir, 'icons', 'add_feature.png'),
                        text=self.tr('Add Feature'),
                        callback=self.addFeature,
                        status_tip=self.tr('Add feature to the active layer'),
                        checkable=True,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionAddFeature)
        self.toolbar.addAction(self.actionAddFeature)
        #地物の移動
        self.actionMoveFeature = self.add_action(os.path.join(self.plugin_dir, 'icons', 'move_feature.png'),
                        text=self.tr('Move Feature'),
                        callback=self.moveFeature,
                        status_tip=self.tr('Move selected feature'),
                        checkable=True,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionMoveFeature)
        self.toolbar.addAction(self.actionMoveFeature)
        #ノード編集
        self.actionEditNode = self.add_action(os.path.join(self.plugin_dir, 'icons', 'edit_node.png'),
                        text=self.tr('Vertex Tool'),
                        callback=self.editNode,
                        status_tip=self.tr('Edit Vertex'),
                        checkable=True,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionEditNode)
        self.toolbar.addAction(self.actionEditNode)
        #地物の分割
        self.actionSplitFeature = self.add_action(os.path.join(self.plugin_dir, 'icons', 'split_feature.png'),
                        text=self.tr('Split Features'),
                        callback=self.splitFeature,
                        status_tip=self.tr('Split Features'),
                        checkable=True,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionSplitFeature)
        self.toolbar.addAction(self.actionSplitFeature)
        #地物の結合
        self.actionMergeFeatures = self.add_action(os.path.join(self.plugin_dir, 'icons', 'merge_features.png'),
                        text=self.tr('Merge Features'),
                        callback=self.mergeFeatures,
                        status_tip=self.tr('Merge selected features'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionMergeFeatures)
        self.toolbar.addAction(self.actionMergeFeatures)
        #地物の削除
        self.actionDeleteFeature = self.add_action(os.path.join(self.plugin_dir, 'icons', 'delete.png'),
                        text=self.tr('Delete Featues'),
                        callback=self.deleteFeature,
                        status_tip=self.tr('Delete selected features'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionDeleteFeature)
        self.toolbar.addAction(self.actionDeleteFeature)

        #地物のコピー
        self.actionCopyFeatures = self.add_action(os.path.join(self.plugin_dir, 'icons', 'copy_features.png'),
                        text=self.tr('Copy Features'),
                        callback=self.copyFeatures,
                        status_tip=self.tr('Copy selected features to clip board'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionCopyFeatures)
        self.toolbar.addAction(self.actionCopyFeatures)
        #地物のペースト
        self.actionPasteFeatures = self.add_action(os.path.join(self.plugin_dir, 'icons', 'paste_features.png'),
                        text=self.tr('Paste Features'),
                        callback=self.pasteFeatures,
                        status_tip=self.tr('Paste features from clip board'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionPasteFeatures)
        self.toolbar.addAction(self.actionPasteFeatures)

        self.toolbar.addSeparator()
        self.menu.addSeparator()

        #地物属性の編集
        self.actionEditFeature = self.add_action(os.path.join(self.plugin_dir, 'icons', 'edit_attribute.png'),
                        text=self.tr('Edit Attribute'),
                        callback=self.editFeature,
                        status_tip=self.tr('Opent attribute widget '),
                        checkable=True,
                        enabled_flag=False,
                        parent=self.iface.mainWindow())
        self.menu.addAction(self.actionEditFeature)
        self.toolbar.addAction(self.actionEditFeature)

                #地質図ツール --------
        self.toolbar.addSeparator()
        self.menu.addSeparator()

        # 地層境界線の描画
        self.actionDrawBoundary = self.add_action(os.path.join(self.plugin_dir, 'icons', 'draw_trend.png'),
                        text=self.tr('Draw Strike Line'),
                        callback=self.drawBoundary,
                        status_tip=self.tr('Open strike line widget'),
                        checkable=True,
                        enabled_flag=False,
                        parent=self.iface.mainWindow())
        self.menu.addAction(self.actionDrawBoundary)
        self.toolbar.addAction(self.actionDrawBoundary)

        # -------------------------------------------------------------
        #オプション -------
        self.toolbar.addSeparator()
        self.menu.addSeparator()
        #データエクスポート
        self.actionExportData = self.add_action(os.path.join(self.plugin_dir, 'icons', 'export_data.png'),
                        text=self.tr('Export to Web library'),
                        callback=self.exportData,
                        status_tip=self.tr('Create export data for web library'),
                        checkable=False,
                        enabled_flag=False
                        )
        self.menu.addAction(self.actionExportData)
        self.toolbar.addAction(self.actionExportData)

        self.toolbar.addSeparator()
        self.menu.addSeparator()
        #設定を開く
        self.actionOpenSettings = self.add_action(os.path.join(self.plugin_dir, 'icons', 'settings.png'),
                        text=self.tr('Settings'),
                        callback=self.openSettings,
                        status_tip=self.tr('Open settings dialog'),
                        checkable=False,
                        enabled_flag=True
                        )
        self.menu.addAction(self.actionOpenSettings)
        self.toolbar.addAction(self.actionOpenSettings)
        #ヘルプを開く
        self.actionOpenHelp = self.add_action(os.path.join(self.plugin_dir, 'icons', 'help.png'),
                        text=self.tr('Geolib3 Help'),
                        callback=self.openHelp,
                        status_tip=self.tr('Open Geolib3 help file'),
                        checkable=False,
                        enabled_flag=True
                        )
        self.menu.addAction(self.actionOpenHelp)
        self.toolbar.addAction(self.actionOpenHelp)

    #--------------------------------------------------------------------------

        menu_bar = self.iface.mainWindow().menuBar()
        actions = menu_bar.actions()
        lastAction = actions[ len( actions ) - 1 ]
        menu_bar.insertMenu( lastAction, self.menu )

    def onClosePlugin(self):
        self.pluginIsActive = False

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        for action in self.actions:
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar
        del self.menu

        self.iface.currentLayerChanged.disconnect(self.menuControl)
        self.qgsProject.layersAdded.disconnect(self.menuControl)

    # --------------------------------------------------------------------------

    def run(self):
        """Run method that loads and starts the plugin"""
        if not self.pluginIsActive:
            self.pluginIsActive = True

    #--------------------------------------------------------------------------
    # メニューアクション定義
    #--------------------------------------------------------------------------
    def newProject(self):
        #　新規プロジェクト作成ダイアログを開く
        from .create_project_dialog import CreateProjectDialog
        dlg = CreateProjectDialog(self.iface)
        dlg.show()
        dlg.exec_()

    def openProject(self):
        #プロジェクトを開く
        self.iface.actionOpenProject().trigger()

    def addScenarioLayer(self):
        # シナリオマップ作成ダイアログを開く
        from .create_scenario_layer_dialog import CreateScenarioLayerDialog
        dlg = CreateScenarioLayerDialog(self.iface)
        dlg.show()
        dlg.exec_()

    def addSubjectLayer(self):
        #新規主題図作成ダイアログを開く
        from .create_subject_layer_dialog import CreateSubjectLayerDialog
        dlg = CreateSubjectLayerDialog(self.iface)
        dlg.show()
        dlg.exec_()
        
    def editHtml(self):
        #HTML編集ダイアログを開く
        from .html_edit_dialog import HtmlEditDialog
        dlg = HtmlEditDialog(self.iface)
        dlg.show()
        dlg.exec_()

    def importGeoclino(self):
        #Geolicinoデータインポートダイアログを開く
        from .import_geoclino_dialog import ImportGeoclinoDialog
        dlg = ImportGeoclinoDialog(self.iface)
        dlg.show()
        dlg.exec_()

    def saveLayer(self):
        #選択レイヤの地物のスタイル属性を一括更新
        _layer = self.iface.activeLayer()
        _layer_name = _layer.name()
        _map_folder_path = os.path.dirname(_layer.source())
        #シンボルレンダラを取得
        renderer = _layer.renderer()
        categories = renderer.categories()
        # SVGマーカーの場合はマップフォルダにSVGを保存
        for category in categories:
            if ( type(category.symbol().symbolLayer(0)) == QgsSvgMarkerSymbolLayer):
                source_file = category.symbol().symbolLayer(0).path()
                svg_filename = os.path.basename(source_file)
                shutil.copyfile(source_file, os.path.join(_map_folder_path, svg_filename))
                
        # styleファイルをマップフォルダに保存
        _layer.saveNamedStyle(os.path.join(_map_folder_path,_layer.name()+'.qml'))
        
        #選択レイヤの地物のシンボル属性を取得してスタイル属性を更新
        _layer.startEditing()
        features = _layer.getFeatures()
        for feature in features:
            attr = ''
            # pntレイヤ
            if _layer_name.find('pnt')>-1:
                attr = feature['attribute']
            # strdipレイヤ
            elif _layer_name.find('strdip')>-1:
                attr = feature['attribute']
            # Geo_Lレイヤ
            elif _layer_name.find('geo_L')>1:
                attr = feature['major_code']
            # Geo_Aレイヤ
            elif _layer_name.find('geo_A')>1:
                attr = feature['symbol']
            # Scenarioレイヤ
            else:
                attr = feature['symbol']

            #スタイル属属性の初期化
            _markerType = ""
            _className = ""
            _stroke = "True"
            _color = ""
            _weight = ""
            _opacity = ""
            _fillOpacity = ""
            _fill = ""
            _fillColor = ""
            _dashArray =""
            _lineCap ="round"
            _lineJoin = "round"
            _clickable = "True"
            _iconUrl =""
            _iconSize = ""
            _iconAnchor = ""
            _iconSize = ""
            _html = ""
            _radius =""

            for category in categories:
                if category.value() == attr:
                    #選択したスタイル属性を取得
                    _className = category.label()
                    symbol = category.symbol().symbolLayer(0)
                    if(type(symbol) == QgsSimpleFillSymbolLayer):           #塗りつぶしマーカーの場合
                        _markerType = ""
                        _weight = str(symbol.strokeWidth())
                        _fill = "true"
                        if symbol.strokeStyle()==0:
                            _stroke = "false"
                        _opacity = "0.0"
                        _fillOpacity = "0.5"
                        _color = symbol.strokeColor().name()
                        _fillColor = symbol.fillColor().name()
                    if(type(symbol) == QgsSimpleLineSymbolLayer):         #ラインマーカーの場合
                        _markerType = ""
                        _weight = str(symbol.width())
                        _stroke = "True"
                        _opacity = "0.5"
                        _fillOpacity = ""
                        _color = symbol.color().name()
                        if symbol.penStyle() != 1:
                            _dashArray = "5,10"
                    if(type(symbol) == QgsSvgMarkerSymbolLayer):          #SVGマーカーの場合
                        _markerType = "Icon"
                        _iconSize = "[20,20]"
                        _iconUrl = os.path.basename(symbol.path())
                        #SVGの場合はstyleフォルダにコピー

                    if(type(symbol) == QgsSimpleMarkerSymbolLayer):     #シンプルマーカーの場合
                        _markerType = "Circle"
                        _weight = "1"
                        _color = symbol.strokeColor().name()
                        _fillColor = symbol.color().name()
                        _radius = str(symbol.size())

            #スタイル属性をセット
            feature['_markerType'] = _markerType
            feature['_className'] = _className
            feature['_stroke'] = _stroke
            feature['_color'] = _color
            feature['_weight'] = _weight
            feature['_opacity'] = _opacity
            #self.feature['_fillOpacity'] = self._opacity
            feature['_fill'] = _fill
            feature['_fillColor'] = _fillColor
            feature['_dashArray'] = _dashArray
            feature['_lineCap'] = _lineCap
            feature['_lineJoin'] = _lineJoin
            feature['_clickable'] = _clickable
            feature['_iconUrl'] = _iconUrl
            feature['_iconSize'] = _iconSize
            feature['_iconAnchor'] = _iconAnchor
            feature['_iconSize'] = _iconSize
            feature['_html'] = _html
            feature['_radius'] = _radius

            _layer.updateFeature(feature)
        #Call commit to save the changes
        _layer.commitChanges()

        #プロジェクトを保存する

        QgsProject.instance().write()

    def addFeature(self):
        #地物追加モードにする
        _layer = self.iface.activeLayer()
        if self.actionAddFeature.isChecked():
            self.actionEditNode.setChecked(False)
            self.actionMoveFeature.setChecked(False)
            self.actionSplitFeature.setChecked(False)
            _layer.startEditing()
            self.iface.actionAddFeature().trigger()
        else:
            _layer.commitChanges()
            _layer.endEditCommand()

    def moveFeature(self):
        #地物移動モードにする
        _layer = self.iface.activeLayer()
        if self.actionMoveFeature.isChecked():
            self.actionAddFeature.setChecked(False)
            self.actionEditNode.setChecked(False)
            self.actionSplitFeature.setChecked(False)

            _layer.startEditing()
            self.iface.actionMoveFeature().trigger()
        else:
            _layer.commitChanges()
            _layer.endEditCommand()

    def editNode(self):
        #ノード編集モードにする
        _layer = self.iface.activeLayer()
        if self.actionEditNode.isChecked():
            self.actionAddFeature.setChecked(False)
            self.actionMoveFeature.setChecked(False)
            self.actionSplitFeature.setChecked(False)

            _layer.startEditing()
            self.iface.actionVertexTool().trigger()
        else:
            _layer.commitChanges()
            _layer.endEditCommand()

    def splitFeature(self):
        #地物分割ツールを起動する
        _layer = self.iface.activeLayer()
        if self.actionSplitFeature.isChecked():
            self.actionAddFeature.setChecked(False)
            self.actionEditNode.setChecked(False)
            self.actionMoveFeature.setChecked(False)

            _layer.startEditing()
            self.iface.actionSplitFeatures().trigger()
        else:
            _layer.commitChanges()
            _layer.endEditCommand()

    def mergeFeatures(self):
        #地物結合ツールを起動する
        _layer = self.iface.activeLayer()
        feats_count = _layer.selectedFeatureCount()
        if feats_count >1:
            _layer.startEditing()
            self.iface.mainWindow().findChild( QAction, 'mActionMergeFeatures' ).trigger()
            _layer.commitChanges()
            _layer.endEditCommand()
        else:
            QMessageBox.information(None, "Infoemation:", self.tr("The feature to be merged is not selected.Please select two or more features."))

    def deleteFeature(self):
        #地物削除ツールを起動する
        _layer = self.iface.activeLayer()
        feats_count = _layer.selectedFeatureCount()
        if feats_count >0:
            _layer.startEditing()
            self.iface.actionDeleteSelected().trigger()
            _layer.commitChanges()
            _layer.endEditCommand()
        else:
            QMessageBox.information(None, "Infoemation:", self.tr("Feature not selected.Please select."))

    def editFeature(self):
        # 地物編集フォームを表示する
        if self.actionEditFeature.isChecked():
            if self.editFeatureDockwidget == None:
                self.editFeatureDockwidget= EditAttributeDockWidget()
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.editFeatureDockwidget)
            self.editFeatureDockwidget.show()
            #else:
            #    QMessageBox.information(None, "Infoemation:", self.tr("Feature not selected.Please select."))
            #    self.actionEditFeature.setChecked(False)
        else:
            self.editFeatureDockwidget.hide()
            self.actionEditFeature.setChecked(False)

    def drawBoundary(self):
        # 地質境界線を引く
        #from .draw_boundary_dockwidget import DrawBoundaryDockWidget
        if self.actionDrawBoundary.isChecked():
            if self.drawBoundaryDockwidget == None:
                # Create the dockwidget (after translation) and keep reference
                self.drawBoundaryDockwidget= DrawBoundaryDockWidget()
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.drawBoundaryDockwidget)
            self.drawBoundaryDockwidget.show()
        else:
            self.drawBoundaryDockwidget.hide()
            self.actionDrawBoundary.setChecked(False)

    def copyFeatures(self):
        #地物コピーツールを起動する
        _layer = self.iface.activeLayer()
        _layer.startEditing()
        self.iface.actionCopyFeatures().trigger()
        _layer.commitChanges()
        _layer.endEditCommand()

    def pasteFeatures(self):
        #地物ペーストツールを起動する
        _layer = self.iface.activeLayer()
        _layer.startEditing()
        self.iface.actionPasteFeatures().trigger()
        _layer.commitChanges()
        _layer.endEditCommand()

    def exportData(self):
        #データエクスポートダイアログを開く
        from .export_library_dialog import ExportLibraryDialog
        dlg = ExportLibraryDialog(self.iface)
        dlg.show()
        dlg.exec_()

    def openSettings(self):
        #設定ダイアログを開く
        from .settings_dialog import SettingsDialog
        dlg = SettingsDialog(self.iface)
        dlg.show()
        dlg.exec_()

    def  openHelp(self):
        #ヘルプを開く
        import webbrowser
        webbrowser.open(self.plugin_dir + "/help/index.html")

    def menuControl(self):
        project = QgsProject.instance().fileName()
        if len(project) >0:
            # プロジェクトが読み込まれている時
            self.actionAddScenarioLayer.setEnabled(True)
            self.actionAddSubjectLayer.setEnabled(True)
            self.actionEditHtml.setEnabled(True)
            self.actionImportGeoclino.setEnabled(True)
            self.actionExportData.setEnabled(True)
            #アクティブレイヤを取得
            _layer = self.iface.activeLayer()
            if _layer is not None and _layer.type() == QgsMapLayer.VectorLayer:
                # アクティブレイヤがベクタレイヤの場合
                self.currentlayer = _layer
                self.iface.actionSelect().trigger()
                #action 活性化
                self.actionSaveLayer.setEnabled(True)
                self.actionAddFeature.setEnabled(True)
                self.actionMoveFeature.setEnabled(True)
                self.actionEditNode.setEnabled(True)
                self.actionSplitFeature.setEnabled(True)
                self.actionMergeFeatures.setEnabled(True)
                self.actionDeleteFeature.setEnabled(True)
                self.actionCopyFeatures.setEnabled(True)
                self.actionPasteFeatures.setEnabled(True)
                self.actionEditFeature.setEnabled(True)
                self.actionDrawBoundary.setEnabled(True)
            else:
                #action 非活性化
                self.actionSaveLayer.setEnabled(False)
                self.actionAddFeature.setEnabled(False)
                self.actionMoveFeature.setEnabled(False)
                self.actionEditNode.setEnabled(False)
                self.actionSplitFeature.setEnabled(False)
                self.actionMergeFeatures.setEnabled(False)
                self.actionDeleteFeature.setEnabled(False)
                self.actionCopyFeatures.setEnabled(False)
                self.actionPasteFeatures.setEnabled(False)
                self.actionEditFeature.setEnabled(False)
                self.actionDrawBoundary.setEnabled(False)
        else:
            self.actionAddScenarioLayer.setEnabled(False)
            self.actionAddSubjectLayer.setEnabled(False)
            self.actionEditHtml.setEnabled(False)
            self.actionImportGeoclino.setEnabled(False)
            self.actionExportData.setEnabled(False)





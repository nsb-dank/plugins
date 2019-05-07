# -*- coding: utf-8 -*-

import os.path
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDockWidget,QFileDialog,QMessageBox
from qgis.core import QgsProject, \
                                QgsVectorLayer, \
                                QgsRasterLayer, \
                                QgsSimpleMarkerSymbolLayer, \
                                QgsSvgMarkerSymbolLayer, \
                                QgsSimpleLineSymbolLayer, \
                                QgsSimpleFillSymbolLayer, \
                                QgsGeometry, \
                                QgsPointXY
import qgis.core
from qgis.gui import QgsIFeatureSelectionManager, \
                                    QgsVertexMarker, \
                                     QgsRubberBand
from .ui_edit_attribute_dockwidget import Ui_EditAttributeDockWidget
from .geolib_util import MapToolUtil
from qgis.utils import iface

class EditAttributeDockWidget(QDockWidget, Ui_EditAttributeDockWidget):
    def __init__(self , parent = None):
        super(EditAttributeDockWidget, self).__init__(parent)
        self.iface = iface
        self.ui = Ui_EditAttributeDockWidget()
        self.ui.setupUi(self)

        self.layer = self.iface.activeLayer()
        self.oldLayer = self.layer
        if self.layer is not None:
            self.setFormItem()
            self.layer.selectionChanged.connect(self.selection_changed)
        else:
            self.layer.selectionChanged.disconnect()

        #self.marker = None
        self.rubber = None

        #シグナル
        self.iface.currentLayerChanged.connect(self.setFormItem)
        self.ui.cboSymbol.currentIndexChanged.connect(self.cbo_symbol_changed)
        self.ui.btnFileSelect.clicked.connect(self.btn_fileSelect_clicked)
        self.ui.btnPreview.clicked.connect(self.btn_preview_clicked)
        self.ui.btnSelectCancel.clicked.connect(self.btn_selectCancel_clicked)
        self.ui.btnUpdate.clicked.connect(self.btn_ok_clicked)


    # 画面を閉じたときに確認画面を表示するイベントハンドラ
    def closeEvent(self, event):
        #メッセージ画面の設定いろいろ
        reply = QMessageBox.question(self, 'Message',
            self.tr("Are you sure to quit?"), QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()




    def selection_changed(self):
        #アクティブレイヤーを取得
        layer = self.iface.activeLayer()
        selectedFeatureCount = 0
        if layer is not None:
            self.layerName = layer.name()
            selectedFeatureCount = layer.selectedFeatureCount()
            self.feature = None
            if selectedFeatureCount > 0:
                #選択地物を取得
                self.feature = layer.selectedFeatures()[0]
                featureId = str(self.feature.id())
                #属性値を取得してフォームにセット
                self.ui.txtFeature.setText(featureId)
                self.getFeatureValue(layer, self.feature)
                self.ui.btnSelectCancel.setEnabled(True)
                self.ui.btnUpdate.setEnabled(True)
            else:
                self.ui.txtFeature.setText(self.tr('No selected feature'))
                self.ui.btnSelectCancel.setEnabled(False)
                self.ui.btnUpdate.setEnabled(False)
                #各フィールド値をクリア
                self. clearFeatureValue()



    #シンボルコンボ変更時の処理
    def cbo_symbol_changed(self):
        idx = self.ui.cboSymbol.currentIndex()
        for self.category in self.categories:
            if self.category.value() == self.ui.cboSymbol.itemData(idx):
                #スタイル属属性の初期化
                self._markerType = ""
                self._className = ""
                self._stroke = "True"
                self._color = ""
                self._weight = ""
                self._opacity = ""
                self._fillOpacity = ""
                self._fill = ""
                self._fillColor = ""
                self._dashArray =""
                self._lineCap ="round"
                self._lineJoin = "round"
                self._clickable = "True"
                self._iconUrl =""
                self._iconSize = ""
                self._iconAnchor = ""
                self._iconSize = ""
                self._html = ""
                self._radius =""

                #選択したスタイル属性を取得
                self._className = self.category.label()
                self.ui.txtLegend01.setText(self._className)
                symbol = self.category.symbol().symbolLayer(0)
                if(type(symbol) == QgsSimpleFillSymbolLayer):           #塗りつぶしマーカーの場合
                    self._markerType = ""
                    self._weight = str(symbol.strokeWidth())
                    self._fill = "true"
                    if symbol.strokeStyle()==0:
                        self._stroke = "false"
                    self._opacity = "0.0"
                    self._fillOpacity = "0.5"
                    self._color = symbol.strokeColor().name()
                    self._fillColor = symbol.fillColor().name()

                if(type(symbol) == QgsSimpleLineSymbolLayer):         #ラインマーカーの場合
                    self._markerType = ""
                    self._weight = str(symbol.width())
                    self._stroke = "True"
                    self._opacity = "0.5"
                    self._fillOpacity = ""
                    self._color = symbol.color().name()
                    if symbol.penStyle() != 1:
                        self._dashArray = "5,10"

                if(type(symbol) == QgsSvgMarkerSymbolLayer):          #SVGマーカーの場合
                    self._markerType = "Icon"
                    self._iconSize = "[20,20]"
                    self._iconUrl = os.path.basename(symbol.path())

                if(type(symbol) == QgsSimpleMarkerSymbolLayer):     #シンプルマーカーの場合
                    self._markerType = "Circle"
                    self._weight = "1"
                    self._color = symbol.strokeColor().name()
                    self._fillColor = symbol.color().name()
                    self._radius = str(symbol.size())

    # ファイル選択ボタン押下時の処理
    def btn_fileSelect_clicked(self):
        # ファイル選択ダイアログを開く
        project_path, ext = os.path.splitext(QgsProject.instance().fileName())
        html_path = project_path + "/Scenario" + "/html/"
        html_file_name,_ = QFileDialog.getOpenFileName(self, "Select HTML file(HTML)",
            html_path, "HTML File(*.html;*.htm) ;; PDF File(*.pdf) ;; All File(*.*)")
        if html_file_name:
            self.filename = html_file_name.replace(html_path,"")
            self.ui.txtFilename.setText(self.filename)

    def btn_preview_clicked(self):
        import webbrowser
        project_path, ext = os.path.splitext(QgsProject.instance().fileName())
        html_path = project_path + "/Scenario" + "/html/"
        self.filename = self.ui.txtFilename.text()
        html_file_name = html_path + self.filename
        webbrowser.open(html_file_name)

    def btn_selectCancel_clicked(self):
        self.ui.btnSelectCancel.setEnabled(False)
        layer = self.iface.activeLayer()
        layer.removeSelection()

        #self.hideHighlight(self.feature)
        self.selection_changed()



    def btn_ok_clicked(self):
        #フォームの入力内容で地物を更新
        mapTool = MapToolUtil()
        layerName = self.layer.name()
        #self.hideHighlight(self.feature)
        self.layer.startEditing()
        # pntレイヤ
        if layerName.find('pnt')>-1:
            self.feature['remarks'] = self.ui.txtDescription.toPlainText()
            idx = self.ui.cboSymbol.currentIndex()
            self.feature['attribute'] = self.ui.cboSymbol.itemData(idx)
            self.feature['legend01'] = self.ui.txtLegend01.text()
        # strdipレイヤ
        elif layerName.find('strdip')>-1:
            self.feature['remarks'] = self.ui.txtDescription.toPlainText()
            idx = self.ui.cboSymbol.currentIndex()
            self.feature['attribute'] = self.ui.cboSymbol.itemData(idx)
            self.feature['legend01'] = self.ui.txtLegend01.text()
            cbo_strike1 = self.ui.cboStrike1.currentText()
            spn_strike = self.ui.spnStrike.value()
            cbo_strike2 = self.ui.cboStrike2.currentText()
            spn_dip = self.ui.spnDip.value()
            cbo_dip = self.ui.cboDip.currentText()
            strike_val, dip_value = mapTool.setStrDipValue(cbo_strike1, spn_strike, cbo_strike2, spn_dip, cbo_dip)
            self.feature['strike_value'] = strike_val
            self.feature['dip_value'] = dip_value
        # Geo_Lレイヤ
        elif layerName.find('geo_L')>1:
            self.feature['description'] = self.ui.txtDescription.toPlainText()
            idx = self.ui.cboSymbol.currentIndex()
            self.feature['major_code'] = self.ui.cboSymbol.itemData(idx)
            self.feature['legend01'] = self.ui.txtLegend01.text()
        # Geo_Aレイヤ
        elif layerName.find('geo_A')>1:
            self.feature['description'] = self.ui.txtDescription.toPlainText()
            idx = self.ui.cboSymbol.currentIndex()
            self.feature['symbol'] = self.ui.cboSymbol.itemData(idx)
            self.feature['legend01'] = self.ui.txtLegend01.text()
            self.feature['legend02'] = self.ui.txtLegend02.text()
            self.feature['legend03'] = self.ui.txtLegend03.text()
            self.feature['legend04'] = self.ui.txtLegend04.text()
            self.feature['legend05'] = self.ui.txtLegend05.text()
            self.feature['legend06'] = self.ui.txtLegend06.text()
            self.feature['legend07'] = self.ui.txtLegend07.text()
        # Scenarioレイヤ
        else:
            idx = self.ui.cboSymbol.currentIndex()
            self.feature['symbol'] = self.ui.cboSymbol.itemData(idx)
            self.feature['filename'] = self.ui.txtFilename.text()
            self.feature['remarks'] = self.ui.txtDescription.toPlainText()

        #スタイル属性をセット
        self.feature['_markerType'] = self._markerType
        self.feature['_className'] = self._className
        self.feature['_stroke'] = self._stroke
        self.feature['_color'] = self._color
        self.feature['_weight'] = self._weight
        self.feature['_opacity'] = self._opacity
        #self.feature['_fillOpacity'] = self._opacity
        self.feature['_fill'] = self._fill
        self.feature['_fillColor'] = self._fillColor
        self.feature['_dashArray'] = self._dashArray
        self.feature['_lineCap'] = self._lineCap
        self.feature['_lineJoin'] = self._lineJoin
        self.feature['_clickable'] = self._clickable
        self.feature['_iconUrl'] = self._iconUrl
        self.feature['_iconSize'] = self._iconSize
        self.feature['_iconAnchor'] = self._iconAnchor
        self.feature['_iconSize'] = self._iconSize
        self.feature['_html'] = self._html
        self.feature['_radius'] = self._radius

        self.layer.updateFeature(self.feature)
        #Call commit to save the changes
        self.layer.commitChanges()

        #self.close()

    # フォーム表示制御（レイヤー種類によって表示属性を変える）
    def setFormItem(self):
        if isinstance(self.oldLayer,QgsVectorLayer):
            self.oldLayer.removeSelection()
        #self.oldLayer.selectionChanged.disconnect()

        #self.hideHighlight()

        self.layer = self.iface.activeLayer()
        if self.layer is not None:
            layerName =  self.layer.name()
            if isinstance(self.layer,QgsVectorLayer):
                self.layer.removeSelection()
                self.layer.selectionChanged.connect(self.selection_changed)

                self.ui.txtLayerName.setText(layerName)
                self.ui.lblSymbol.setVisible(True)
                self.ui.cboSymbol.setVisible(True)
                self.ui.lblLegend01.setVisible(False)
                self.ui.txtLegend01.setVisible(False)
                self.ui.frmScenario.setVisible(False)
                self.ui.frmLegend.setVisible(False)
                self.ui.frmStrDip.setVisible(False)

                if layerName.find('pnt')>-1:
                    self.ui.lblLegend01.setVisible(True)
                    self.ui.txtLegend01.setVisible(True)

                elif layerName.find('strdip')>-1:
                    self.ui.lblLegend01.setVisible(True)
                    self.ui.txtLegend01.setVisible(True)
                    self.ui.frmStrDip.setVisible(True)

                elif layerName.find('geo_L')>1:
                    self.ui.lblLegend01.setVisible(True)
                    self.ui.txtLegend01.setVisible(True)

                elif layerName.find('geo_A')>1:
                    self.ui.lblLegend01.setVisible(True)
                    self.ui.txtLegend01.setVisible(True)
                    self.ui.frmLegend.setVisible(True)
                else:
                    self.ui.frmScenario.setVisible(True)

                #シンボルレンダラを取得
                self.ui.cboSymbol.clear()
                renderer = self.layer.renderer()
                self.categories = renderer.categories()
                for self.category in self.categories:
                    self.ui.cboSymbol.addItem(self.category.label(), self.category.value())

                self.selection_changed()
                self.oldLayer = self.layer

        else:
            self.ui.txtLayerName.setText(self.tr('Please Select Vector Layer'))

    #地物の属性値を取得してフォームにセット（レイヤー種類によって取得属性を変える）
    def getFeatureValue(self, layer, feature):
        self.feature = feature
        layerName = self.layer.name()
        mapTool = MapToolUtil()

        #ハイライト消去
        #self.hideHighlight(self.feature)

        #シンボルレンダラを取得
        renderer = layer.renderer()
        categories = renderer.categories()
        self.ui.cboSymbol.clear()
        for category in categories:
            self.ui.cboSymbol.addItem(category.label(), category.value())

        #feature = None
        selectedFeatureCount = layer.selectedFeatureCount()
        if selectedFeatureCount > 0:
            #ハイライト
            #self.showHighlight(self.feature)
            # pntレイヤ
            if layerName.find('pnt')>-1:
                symbol = self.feature["attribute"]
                legend01 = self.feature['legend01'] if self.feature['legend01'] != qgis.core.NULL else""
                description = self.feature["remarks"]

                self.ui.txtLegend01.setText(legend01)

            # strdipレイヤ
            elif layerName.find('strdip')>-1:
                symbol = self.feature["attribute"]
                legend01 = self.feature['legend01'] if self.feature['legend01'] != qgis.core.NULL else""
                description = self.feature["remarks"]
                strike = self.feature['strike_value'] if  self.feature["strike_value"] != qgis.core.NULL else 0
                dip = self.feature['dip_value'] if self.feature['dip_value'] != qgis.core.NULL else 0
                cbo_strike1,spn_strike,cbo_strike2,spn_dip,cbo_dip = mapTool.setStrDipText(strike, dip)

                self.ui.txtLegend01.setText(legend01)
                self.ui.cboStrike1.setCurrentIndex(self.ui.cboStrike1.findText(cbo_strike1))
                self.ui.spnStrike.setValue(spn_strike)
                self.ui.cboStrike2.setCurrentIndex(self.ui.cboStrike2.findText(cbo_strike2))
                self.ui.spnDip.setValue(spn_dip)
                self.ui.cboDip.setCurrentIndex(self.ui.cboDip.findText(cbo_dip))

            # Geo_Lレイヤ
            elif layerName.find('geo_L')>1:
                symbol = self.feature["major_code"]
                legend01 = self.feature['legend01'] if self.feature['legend01'] != qgis.core.NULL else""
                description = self.feature["description"]

                self.ui.txtLegend01.setText(legend01)

            # Geo_Aレイヤ
            elif layerName.find('geo_A')>1:
                symbol = self.feature["symbol"]
                legend01 = self.feature['legend01'] if self.feature['legend01'] != qgis.core.NULL else""
                legend02 = self.feature['legend02'] if self.feature['legend02'] != qgis.core.NULL else""
                legend03 = self.feature['legend03'] if self.feature['legend03'] != qgis.core.NULL else""
                legend04 = self.feature['legend04'] if self.feature['legend04'] != qgis.core.NULL else""
                legend05 = self.feature['legend05'] if self.feature['legend05'] != qgis.core.NULL else""
                legend06 = self.feature['legend06'] if self.feature['legend06'] != qgis.core.NULL else""
                legend07 = self.feature['legend07'] if self.feature['legend07'] != qgis.core.NULL else""
                description = self.feature["description"]

                self.ui.txtLegend01.setText(legend01)
                self.ui.txtLegend02.setText(legend02)
                self.ui.txtLegend03.setText(legend03)
                self.ui.txtLegend04.setText(legend04)
                self.ui.txtLegend05.setText(legend05)
                self.ui.txtLegend06.setText(legend06)
                self.ui.txtLegend07.setText(legend07)

            # Scenarioレイヤ
            else:
                symbol = self.feature["symbol"]
                filename =  self.feature['filename']
                description = self.feature["remarks"]

                if filename != qgis.core.NULL:
                    self.ui.txtFilename.setText(filename)
                    project_path, ext = os.path.splitext(QgsProject.instance().fileName())
                    html_path = project_path + "/Scenario" + "/html/"
                    html_file_name = html_path + filename

            # レイヤ共通の属性をセット
            if description != qgis.core.NULL:
                self.ui.txtDescription.setPlainText(description)

            #シンボル属性を取得してセット
            index = self.ui.cboSymbol.findData(symbol)
            self.ui.cboSymbol.setCurrentIndex(index)

            #スタイル属性を取得
            self._markerType = self.feature['_markerType']
            self._className = self.feature['_className']
            self._stroke = self.feature['_stroke']
            self._color = self.feature['_color']
            self._weight = self.feature['_weight']
            self._opacity = self.feature['_opacity']
    #     self._fillOpacity = self.feature['_fillOpacity']
            self._fill = self.feature['_fill']
            self._fillColor = self.feature['_fillColor']
            self._dashArray = self.feature['_dashArray']
            self._lineCap = self.feature['_lineCap']
            self._lineJoin = self.feature['_lineJoin']
            self._clickable = self.feature['_clickable']
            self._iconUrl = self.feature['_iconUrl']
            self._iconSize = self.feature['_iconSize']
            self._iconAnchor = self.feature['_iconAnchor']
            self._iconSize = self.feature['_iconSize']
            self._html = self.feature['_html']
            self._radius = self.feature['_radius']

    def clearFeatureValue(self):
        self.ui.cboSymbol.clear()
        self.ui.txtLegend01.setText('')
        self.ui.txtLegend02.setText('')
        self.ui.txtLegend03.setText('')
        self.ui.txtLegend04.setText('')
        self.ui.txtLegend05.setText('')
        self.ui.txtLegend06.setText('')
        self.ui.txtLegend07.setText('')
        self.ui.txtDescription.setPlainText('')
        self.ui.cboStrike1.setCurrentIndex(0)
        self.ui.spnStrike.setValue(0)
        self.ui.cboStrike2.setCurrentIndex(0)
        self.ui.spnDip.setValue(0)
        self.ui.cboDip.setCurrentIndex(0)
        self.ui.txtFilename.setText('')


    # 選択地物ハイライト（レイヤー種類によって表示属性を変える）
    def showHighlight(self,feature):
        #選択地物をハイライト表示
        if feature is not None:
            geom = feature.geometry()
            if geom.wkbType() == 4: #QGis.WKBMultiPoint
                # Pointの場合（VertexMarker)
                point = geom.asMultiPoint()[0]
                self.marker = QgsVertexMarker(self.iface.mapCanvas())
                self.marker.setColor(QColor(0, 255, 0))
                self.marker.setIconSize(5)

                p = QgsPointXY(point.x(),point.y())
                self.marker.setCenter(p)
                self.marker.setIconType(QgsVertexMarker.ICON_BOX) # or ICON_CROSS, ICON_X
                self.marker.setPenWidth(5)
                self.marker.show()

                #self.rubber = QgsRubberBand(self.iface.mapCanvas(), True)  # True = a polygon
                #self.rubber.setToGeometry(QgsGeometry.fromMultiPolygonXY(point), None)
                #self.rubber.setColor(QColor(0, 255, 0))
                #self.rubber.setWidth(3)

            elif geom.wkbType() == 5: #QGis.WKBMultiPolyline
                # Polylineの場合（Rubberband)
                point = geom.asMultiPolyline()
                self.rubber = QgsRubberBand(self.iface.mapCanvas(), False)  # False = not a polygon
                self.rubber.setToGeometry(QgsGeometry.fromMultiPolylineXY(point), None)
                self.rubber.setColor(QColor(0, 255, 0))
                self.rubber.setWidth(3)
            elif geom.wkbType() == 6: #QGis.WKBMultiPolygone
                # Polygonの場合（Rubberband)
                point = geom.asMultiPolygon()
                self.rubber = QgsRubberBand(self.iface.mapCanvas(), True)  # True = a polygon
                self.rubber.setToGeometry(QgsGeometry.fromMultiPolygonXY(point), None)
                self.rubber.setColor(QColor(0, 255, 0))
                self.rubber.setWidth(3)

    def hideHighlight(self,feature):
        if feature is not None:
            geom = feature.geometry()
            if geom.wkbType() == 4:
                self.marker.hide()
            else:
                self.rubber.reset()

# -*- coding: utf-8 -*-

from qgis.PyQt.QtCore import  QSettings
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from qgis.PyQt.QtGui import QColor
from PyQt5.QtWidgets import QDockWidget,QMessageBox
from qgis.core import QgsProject,QgsMapLayer,QgsVectorLayer,QgsRasterLayer, QgsRaster,QgsWkbTypes,QgsPoint,QgsGeometry,QgsCoordinateTransform, QgsCoordinateReferenceSystem
from qgis.gui import QgsRubberBand,QgsMapTool,QgsVertexMarker
from qgis.utils import iface
import os
import math
import pyproj
import urllib.request, urllib.error, urllib.parse
import json
from .geolib_util import MapToolUtil

from .ui_draw_boundary_dockwidget import Ui_DrawBoundaryDockWidget

class DrawBoundaryDockWidget(QDockWidget, Ui_DrawBoundaryDockWidget):

    def __init__(self, parent = None):
        """Constructor."""
        super(DrawBoundaryDockWidget, self).__init__(parent)
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.ui = Ui_DrawBoundaryDockWidget()
        self.ui.setupUi(self)

        #初期表示
        self.ui.btnSelectFeature.setEnabled(False)
        self.ui.btnCancelFeature.setEnabled(False)

        self.ui.btnSelectPoints.setEnabled(True)
        self.ui.btnCalculate.setEnabled(False)
        self.ui.btnCancelPoints.setEnabled(False)

        self.ui.btnDrawStrike.setEnabled(False)
        self.ui.btnCancel.setEnabled(False)

        self.addCboLayerItem()

        #使用座標
        self.wgs84 = pyproj.Proj(init='EPSG:4326') # WGS84 緯度経度
        self.rect6 = pyproj.Proj(init='EPSG:3857') # 平面直角座標6系

        #シグナル
        self.ui.cboTargerLayer.currentIndexChanged.connect(self.activateStrdipLayer)
        self.ui.btnSelectFeature.clicked.connect(self.getStrikeDipValue)
        self.ui.btnCancelFeature.clicked.connect(self.releaseStrikeDipValue)
        self.ui.btnSelectPoints.clicked.connect(self.selectPointsExecution)
        self.ui.btnCancelPoints.clicked.connect(self.cancelPointsExecution)
        self.ui.btnCalculate.clicked.connect(self.calculateStrikeDipValue)
        self.ui.btnDrawStrike.clicked.connect(self.drawStrikeExecution)
        self.ui.btnCancel.clicked.connect(self.removeStrikeExecution)
        self.ui.btnSettings.clicked.connect(self.btn_settings_clicked)

    # 設定ボタン押下時の処理
    def btn_settings_clicked(self):
        #設定ダイアログを開く
        from .settings_dialog import SettingsDialog
        dlg = SettingsDialog(self.iface)
        dlg.show()
        dlg.exec_()

    #コンボボックスに値をセット
    def addCboLayerItem(self):
        layers = QgsProject.instance().mapLayers().values()
        # DEM Layer Combobox
        self.ui.cboDemLayer.clear()
        self.ui.cboDemLayer.addItem(self.tr(u'GSI DEM Tile (Default)'))
        for layer in layers:
            if isinstance(layer, QgsRasterLayer):
                self.ui.cboDemLayer.addItem(layer.name())
        #Target Layer Combobox
        self.ui.cboTargerLayer.clear()
        self.ui.cboTargerLayer.addItem(self.tr(u'(Select strdip Layer)'))
        for layer in layers:
            if isinstance(layer,QgsVectorLayer) and layer.name().find('strdip')>-1:
                self.ui.cboTargerLayer.addItem(layer.name())

    # 走向傾斜レイヤーをアクティブにする
    def activateStrdipLayer(self):
        if self.ui.cboTargerLayer.currentIndex() >0:
            layerName = self.ui.cboTargerLayer.currentText()
            layer = QgsProject.instance().mapLayersByName(layerName)[0]
            self.iface.setActiveLayer(layer)
            self.ui.btnSelectFeature.setEnabled(True)
            self.ui.btnCancelFeature.setEnabled(True)

    # 選択している走向傾斜地物から値を取得
    def getStrikeDipValue(self):
        self.layer = self.iface.activeLayer()
        self.features = self.layer.selectedFeatures()
        if len(self.features) > 0:
            feature = self.features[0]
            self.p1 = feature.geometry().asMultiPoint()[0]
            self.strike = float(feature["strike_value"])
            self.dip = float(feature["dip_value"])

            print (self.p1.x(),self.p1.y())
            self.dispStrikeDipValue(self.strike, self.dip)

            self.ui.btnSelectFeature.setEnabled(False)
            self.ui.btnDrawStrike.setEnabled(True)
            self.ui.btnCancel.setEnabled(False)
        else:
            QMessageBox.information(None, "Information:", self.tr(u'Feature has not been selected.Please select.'))
            self.ui.txtStrike.setText('')
            self.ui.txtDip.setText('')

            self.ui.btnDrawStrike.setEnabled(False)
            self.ui.btnCancel.setEnabled(False)


    def selectPointsExecution(self):
        self.point_count = 0
        self.ui.btnCalculate.setEnabled(False)
        self.ui.btnCancelPoints.setEnabled(True)
        self.toolClick = QgsMapToolClick(self.iface, self.canvas,self.ui,self.point_count)
        self.canvas.setMapTool(self.toolClick)

    def calculateStrikeDipValue(self):
        # WGS84緯度経度から、平面直角座標6系のXY座標に変換
        P1x,P1y = pyproj.transform(self.wgs84, self.rect6, float(self.ui.txtP1x.text()), float(self.ui.txtP1y.text()))
        P1z = float(self.ui.txtP1z.text())
        P2x ,P2y = pyproj.transform(self.wgs84, self.rect6, float(self.ui.txtP2x.text()), float(self.ui.txtP2y.text()))
        P2z = float(self.ui.txtP2z.text())
        P3x, P3y = pyproj.transform(self.wgs84, self.rect6, float(self.ui.txtP3x.text()), float(self.ui.txtP3y.text()))
        P3z = float(self.ui.txtP3z.text())

        a=(P2y - P1y)*(P3z - P1z) - (P3y - P1y)*(P2z - P1z)
        b=(P2z - P1z)*(P3x - P1x) - (P3z - P1z)*(P2x - P1x)
        c=(P2x - P1x)*(P3y - P1y) - (P3x - P1x)*(P2y - P1y)
        d=-(a*P1x +b*P1y+c*P1z)
        p = -a/c
        q=-b/c

        self.p1 = QgsPoint(float(self.ui.txtP1x.text()), float(self.ui.txtP1y.text()))

        tan_dip = math.sqrt(p*p+q*q)
        self.dip = math.degrees(math.atan(tan_dip))

        sin_strike=-p/math.sqrt(p*p+q*q)
        cos_strike=-q/math.sqrt(p*p+q*q)
        if  sin_strike >= 0 and cos_strike >= 0:
            self.strike =math.degrees(math.asin(sin_strike)) - 90
        elif sin_strike >= 0 and cos_strike <= 0:
            self.strike =180 - math.degrees(math.asin(sin_strike)) -90
        elif sin_strike <= 0 and cos_strike <= 0:
            self.strike =180 - math.degrees(math.asin(sin_strike)) - 90
        elif sin_strike <= 0 and cos_strike >= 0:
            self.strike = 360 - math.degrees(math.asin(-sin_strike)) -90

        print (self.p1.x(),self.p1.y())
        print ('strike:'+str(self.strike) + '  dip:'+str(self.dip))

        if self.strike < 0:
            self.strike = 360 + self.strike



        self.dispStrikeDipValue(self.strike, self.dip)

        self.ui.btnCancelPoints.setEnabled(True)
        self.ui.btnDrawStrike.setEnabled(True)
        self.ui.btnCancel.setEnabled(False)

    def cancelPointsExecution(self):

        """
        self.point_count = 0
        self.ui.btnCalculate.setEnabled(False)
        self.ui.btnCancelPoints.setEnabled(True)
        self.toolClick = QgsMapToolClick(self.iface, self.canvas,self.ui,self.point_count)
        self.canvas.setMapTool(self.toolClick)
        """
        
        self.ui.txtP1x.setText('')
        self.ui.txtP2x.setText('')
        self.ui.txtP3x.setText('')
        self.ui.txtP1y.setText('')
        self.ui.txtP2y.setText('')
        self.ui.txtP3y.setText('')
        self.ui.txtP1z.setText('')
        self.ui.txtP2z.setText('')
        self.ui.txtP3z.setText('')
        if isinstance(self.toolClick,QgsMapToolClick):
            self.toolClick.rubberPoint1.reset()
            self.toolClick.rubberPoint.reset()
            self.canvas.unsetMapTool(self.toolClick)

        self.ui.btnSelectPoints.setEnabled(True)
        self.ui.btnCalculate.setEnabled(False)
        self.ui.btnCancelPoints.setEnabled(False)
        self.releaseStrikeDipValue()

    # 走向・傾斜値の表示
    def dispStrikeDipValue(self,strike,dip):
            mapTool = MapToolUtil()
            cbo_strike1,spn_strike,cbo_strike2,spn_dip,cbo_dip = mapTool.setStrDipText(strike, dip)
            self.ui.txtStrike.setText(cbo_strike1 + ' ' +str(int(spn_strike)) + ' ' + cbo_strike2)
            self.ui.txtDip.setText(str(int(spn_dip)) + ' ' + cbo_dip)

    # 走向傾斜の選択を解除
    def releaseStrikeDipValue(self):
        if self.ui.cboTargerLayer.currentIndex() >0:
            layerName = self.ui.cboTargerLayer.currentText()
            layer = QgsProject.instance().mapLayersByName(layerName)[0]
            self.iface.setActiveLayer(layer)
        layer = self.iface.activeLayer()
        layer.removeSelection()
        self.ui.txtStrike.setText('')
        self.ui.txtDip.setText('')
        self.ui.btnSelectFeature.setEnabled(True)
        self.ui.btnDrawStrike.setEnabled(False)
        self.ui.btnCancel.setEnabled(False)

    # 走向線描画
    def drawStrikeExecution(self):
        # 設定値をセット
        self.settings = QSettings()
        self.contour_interval = float(self.settings.value("geolib3/contourInterval", 10))
        self.strike_line_length = float(self.settings.value("geolib3/strikeLineLength" , 5000))
        self.strike_line_num = int(self.settings.value("geolib3/strikeLineNum", 10))
        self.line_width= int(self.settings.value("geolib3/LineWidth", 3))
        self.line_color_R = int(self.settings.value("geolib3/LineColorR",255))
        self.line_color_G = int(self.settings.value("geolib3/LineColorG",128))
        self.line_color_B = int(self.settings.value("geolib3/LineColorB",0))
        self.line_color_HR = int(self.settings.value("geolib3/LineColorHR",255))
        self.line_color_HG = int(self.settings.value("geolib3/LineColorHG",0))
        self.line_color_HB = int(self.settings.value("geolib3/LineColorHB",0))
        self.line_color_LR = int(self.settings.value("geolib3/LineColorLR",0))
        self.line_color_LG = int(self.settings.value("geolib3/LineColorLG",0))
        self.line_color_LB = int(self.settings.value("geolib3/LineColorLB",255))
        self.show_ext_line = self.settings.value("geolib3/ShowExtLine",True)

        self.length = float(self.strike_line_length)#  * 0.00001  # 走向線の長さ
        self.interval = float(self.contour_interval)# * 0.00001      #等高線の間隔
        #self.strike = float(feature["strike_value"])
        #self.dip = float(feature["dip_value"])
        if self.dip != 0:
            self.dist = self.interval / math.tan(math.radians(self.dip))
        else:
            self.dist = self.interval

        print (self.p1.x(),self.p1.y())
        #平面座標に変換
        p1x,p1y = pyproj.transform(self.wgs84, self.rect6, self.p1.x(),self.p1.y())

        #始点と終点を指定
        msx = p1x + self.length*math.sin(math.radians(self.strike))
        msy = p1y + self.length*math.cos(math.radians(self.strike))
        mex = p1x - self.length*math.sin(math.radians(self.strike))
        mey = p1y - self.length*math.cos(math.radians(self.strike))
        msx,msy = pyproj.transform( self.rect6, self.wgs84, msx,msy)
        mex,mey = pyproj.transform( self.rect6, self.wgs84, mex,mey)
        ms = QgsPoint(msx,msy)
        me = QgsPoint(mex,mey)
        line = QgsGeometry.fromPolyline([ms, me])

        #ラバーバンドにラインを描画
        self.layer = self.iface.activeLayer()
        if self.layer is not None:
            self.rubber = QgsRubberBand(self.canvas, QgsWkbTypes.LineGeometry)
            self.rubber.setColor(QColor(self.line_color_R, self.line_color_G, self.line_color_B, 100))
            self.rubber.setWidth(self.line_width)
            self.rubber.reset(QgsWkbTypes.LineGeometry)
            self.rubber.addGeometry(line,self.layer)

            # 走向線を描画
            self.rubberH = QgsRubberBand(self.canvas, QgsWkbTypes.LineGeometry)
            self.rubberH.setColor(QColor(self.line_color_HR, self.line_color_HG, self.line_color_HB, 100))
            self.rubberH.setWidth(self.line_width)
            self.rubberL = QgsRubberBand(self.canvas, QgsWkbTypes.LineGeometry)
            self.rubberL.setColor(QColor(self.line_color_LR, self.line_color_LG, self.line_color_LB, 100))
            self.rubberL.setWidth(self.line_width)

            for i in range(self.strike_line_num):
                d = i + 1
                nx = p1x + self.dist * d * math.sin(math.radians(self.strike + 90))
                ny = p1y + self.dist * d * math.cos(math.radians(self.strike + 90))
                nsx = nx + self.length*math.sin(math.radians(self.strike))
                nsy = ny + self.length*math.cos(math.radians(self.strike))
                nex = nx - self.length*math.sin(math.radians(self.strike))
                ney = ny - self.length*math.cos(math.radians(self.strike))

                nsx,nsy = pyproj.transform( self.rect6, self.wgs84, nsx,nsy)
                nex,ney = pyproj.transform( self.rect6, self.wgs84, nex,ney)
                ns = QgsPoint(nsx,nsy)
                ne = QgsPoint(nex,ney)

                line = QgsGeometry.fromPolyline([ns, ne])
                self.rubberL.addGeometry(line,self.layer)

                nx = p1x - self.dist * d * math.sin(math.radians(self.strike + 90))
                ny = p1y - self.dist * d * math.cos(math.radians(self.strike + 90))
                nsx = nx + self.length*math.sin(math.radians(self.strike))
                nsy = ny + self.length*math.cos(math.radians(self.strike))
                nex = nx - self.length*math.sin(math.radians(self.strike))
                ney = ny - self.length*math.cos(math.radians(self.strike))

                nsx,nsy = pyproj.transform( self.rect6, self.wgs84, nsx,nsy)
                nex,ney = pyproj.transform( self.rect6, self.wgs84, nex,ney)
                ns = QgsPoint(nsx,nsy)
                ne = QgsPoint(nex,ney)

                line = QgsGeometry.fromPolyline([ns, ne])
                self.rubberH.addGeometry(line,self.layer)

            #補助走向線を描画
            self.rubberEH = QgsRubberBand(self.canvas, QgsWkbTypes.LineGeometry)
            self.rubberEH.setColor(QColor(self.line_color_HR, self.line_color_HG, self.line_color_HB, 100))
            self.rubberEH.setWidth(1)
            self.rubberEL = QgsRubberBand(self.canvas, QgsWkbTypes.LineGeometry)
            self.rubberEL.setColor(QColor(self.line_color_LR, self.line_color_LG, self.line_color_LB, 100))
            self.rubberEL.setWidth(1)

            if self.show_ext_line == True:
                for i in range(self.strike_line_num):
                    d = i + 1 - 0.5
                    nx = p1x + self.dist * d * math.sin(math.radians(self.strike + 90))
                    ny = p1y + self.dist * d * math.cos(math.radians(self.strike + 90))
                    nsx = nx + self.length*math.sin(math.radians(self.strike))
                    nsy = ny + self.length*math.cos(math.radians(self.strike))
                    nex = nx - self.length*math.sin(math.radians(self.strike))
                    ney = ny - self.length*math.cos(math.radians(self.strike))

                    nsx,nsy = pyproj.transform( self.rect6, self.wgs84, nsx,nsy)
                    nex,ney = pyproj.transform( self.rect6, self.wgs84, nex,ney)
                    ns = QgsPoint(nsx,nsy)
                    ne = QgsPoint(nex,ney)

                    line = QgsGeometry.fromPolyline([ns, ne])
                    self.rubberEL.addGeometry(line,self.layer)

                    nx = p1x - self.dist * d * math.sin(math.radians(self.strike + 90))
                    ny = p1y - self.dist * d * math.cos(math.radians(self.strike + 90))
                    nsx = nx + self.length*math.sin(math.radians(self.strike))
                    nsy = ny + self.length*math.cos(math.radians(self.strike))
                    nex = nx - self.length*math.sin(math.radians(self.strike))
                    ney = ny - self.length*math.cos(math.radians(self.strike))

                    nsx,nsy = pyproj.transform( self.rect6, self.wgs84, nsx,nsy)
                    nex,ney = pyproj.transform( self.rect6, self.wgs84, nex,ney)
                    ns = QgsPoint(nsx,nsy)
                    ne = QgsPoint(nex,ney)

                    line = QgsGeometry.fromPolyline([ns, ne])
                    self.rubberEH.addGeometry(line,self.layer)

            self.ui.cboTargerLayer.setEnabled(False)
            self.ui.btnCancelFeature.setEnabled(False)
            self.ui.btnSelectPoints.setEnabled(False)
            self.ui.btnCalculate.setEnabled(False)
            self.ui.btnCancelPoints.setEnabled(False)
            self.ui.btnDrawStrike.setEnabled(False)
            self.ui.btnCancel.setEnabled(True)

    def removeStrikeExecution(self):
        self.rubber.reset()
        self.rubberH.reset()
        self.rubberL.reset()
        self.rubberEH.reset()
        self.rubberEL.reset()

        self.ui.txtStrike.setText('')
        self.ui.txtDip.setText('')

        self.ui.cboTargerLayer.setEnabled(True)
        self.ui.btnSelectFeature.setEnabled(True)
        self.ui.btnCancelFeature.setEnabled(True)
        self.ui.btnCancelPoints.setEnabled(True)
        self.ui.btnDrawStrike.setEnabled(False)
        self.ui.btnCancel.setEnabled(False)

class QgsMapToolClick(QgsMapTool):
    def __init__(self, iface, canvas, ui, count):
        QgsMapTool.__init__(self, canvas)
        self.iface = iface
        self.canvas = canvas
        self.rubberPoint1 = QgsRubberBand(self.canvas,QgsWkbTypes.PointGeometry)
        self.rubberPoint1.setColor(QColor(255, 0, 0))
        self.rubberPoint1.setWidth(5)
        self.rubberPoint = QgsRubberBand(self.canvas,QgsWkbTypes.PointGeometry)
        self.rubberPoint.setColor(QColor(255, 128, 0))

        self.ui = ui
        self.point_count = count

    def canvasPressEvent(self, mouseEvent):
        if self.point_count < 3:
            dPos = mouseEvent.pos()
            mPosBefore = self.toMapCoordinates(dPos)
            destcrs = self.iface.mapCanvas().mapSettings().destinationCrs()
            Tf = QgsCoordinateTransform(destcrs, QgsCoordinateReferenceSystem(4326), QgsProject.instance())
            mPos = Tf.transform(mPosBefore)
            lon = mPos.x()
            lat = mPos.y()
            elevation = ''

            #選択したDEMレイヤでポイントの標高を取得
            if self.ui.cboDemLayer.currentIndex() == 0:
                URL = "http://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon=" + str(lon) + "&lat=" + str(lat) +"&outtype=JSON"
                data_all = urllib.request.urlopen(URL)
                data = json.loads(data_all.read())
                elevation = str(data['elevation'])
                #elevationtext = data[u'hsrc']
                data_all.close()
            else:
                demLayerName = self.ui.cboDemLayer.currentText()
                demLayer = QgsProject.instance().mapLayersByName(demLayerName)[0]
                if type(demLayer) is QgsRasterLayer:
                    ident = demLayer.dataProvider().identify(mPos, QgsRaster.IdentifyFormatValue)
                    if ident.isValid():
                        elevation = ''.join(str(r) for r in ident.results().values())
                    else:
                        elevation = ""

            if elevation == '':
                QMessageBox.information(None, "Information:", self.tr(u'Elevation data cannot be obtained.Please specify a valid DEM.'))
            else:
                #Add text to the row
                if self.point_count == 0:
                    self.ui.txtP1x.setText('{:.4f}'.format(lon))
                    self.ui.txtP1y.setText('{:.4f}'.format(lat))
                    self.ui.txtP1z.setText(str(elevation))
                    self.rubberPoint1.addPoint(mPosBefore)
                elif self.point_count == 1:
                    self.ui.txtP2x.setText('{:.4f}'.format(lon))
                    self.ui.txtP2y.setText('{:.4f}'.format(lat))
                    self.ui.txtP2z.setText(str(elevation))
                    self.rubberPoint.setWidth(3)
                    self.rubberPoint.addPoint(mPosBefore)
                elif self.point_count == 2:
                    self.ui.txtP3x.setText('{:.4f}'.format(lon))
                    self.ui.txtP3y.setText('{:.4f}'.format(lat))
                    self.ui.txtP3z.setText(str(elevation))
                    self.rubberPoint.setWidth(3)
                    self.rubberPoint.addPoint(mPosBefore)

                    self.ui.btnCalculate.setEnabled(True)
                print (mPosBefore)
                self.point_count += 1
        else:
            self.ui.btnCalculate.setEnabled(True)

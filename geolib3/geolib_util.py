
# -*- coding: utf-8 -*-

#######################################################
#
# geolib_util.py
# Python implementation of the Class GeolibUtil
# Created on:      2017/09/10 16:57:02
# Original author: yukihiko Karata
#
#######################################################

#from distutils import dir_util
"""
GeoLibユーティリティ
"""

from PyQt5.QtCore import QVariant, QSettings,Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel
import os
import shutil
import ftplib

from qgis.core import   QgsField, \
                                        QgsFields, \
                                        QgsFeature, \
                                        QgsPointXY, \
                                        QgsGeometry, \
                                        QgsVectorFileWriter, \
                                        QgsVectorLayer, \
                                        QgsRasterLayer, \
                                        QgsProject, \
                                        QgsCoordinateReferenceSystem, \
                                        QgsLayerTreeLayer, \
                                        QgsWkbTypes
from qgis.utils import iface

from qgis.gui import QgsMapTool,QgsRubberBand


class GeolibUtil:
    project = QgsProject.instance()
    project_folder,project_filename = os.path.split(project.fileName())

    project_crs = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId)
    pluginpath = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        pass

    def createProjectDirectory(self,project_folder, project_name):
        # 指定したロジェクトフォルダ配下にディレクトリ構造を作成する
        # すでにディレクトリが存在している場合は処理をスキップする
        if bool(len(project_folder) > 0 and len(project_name) > 0):
            project_path = os.path.join(project_folder, project_name)
            # project_filename = os.path.join(project_folder, project_name + '.qgs')
            if not(os.path.exists(project_path)):
                os.mkdir(project_path)
            if not(os.path.exists(os.path.join(project_path, "Scenario"))):
                os.mkdir(os.path.join(project_path, "Scenario"))
            if not(os.path.exists(os.path.join(project_path, "Subject"))):
                os.mkdir(os.path.join(project_path, "Subject"))
            if not(os.path.exists(os.path.join(project_path, "Associated"))):
                os.mkdir(os.path.join(project_path, "Associated"))
            if not(os.path.exists(os.path.join(project_path, "style"))):
                os.mkdir(os.path.join(project_path, "style"))
        else:
            QMessageBox.information(self, u"Warning", self.tr(u"Folder name or file name is not specified."))

    def createFolder(self,folder_path):
        # 指定したフォルダを作成する
        # すでにフォルダが存在してい場合は処理をスキップする
        if len(folder_path) > 0:
            if not(os.path.exists(folder_path)):
                os.mkdir(folder_path)
        else:
            QMessageBox.information(self, u"Warning", self.tr(u"Folder name is not specified."))

    def copyStyleFile(self, style_path):
        #プラグインフォルダにあるスタイルファイルをプロジェクトフォルダににコピーする
        shutil.copyfile(
                        os.path.join(GeolibUtil.pluginpath,"template\style\point.qml"),
                        os.path.join(style_path,"point.qml"))
        shutil.copyfile(
                        os.path.join(GeolibUtil.pluginpath,"template\style\line.qml"),
                        os.path.join(style_path,"line.qml"))
        shutil.copyfile(
                        os.path.join(GeolibUtil.pluginpath,"template\style\polygon.qml"),
                        os.path.join(style_path,"polygon.qml"))
        shutil.copyfile(
                        os.path.join(GeolibUtil.pluginpath,"template\style\pnt.qml"),
                        os.path.join(style_path,"pnt.qml"))
        shutil.copyfile(
                        os.path.join(GeolibUtil.pluginpath,"template\style\strdip.qml"),
                        os.path.join(style_path,"strdip.qml"))
        shutil.copyfile(
                        os.path.join(GeolibUtil.pluginpath,"template\style\geo_L.qml"),
                        os.path.join(style_path,"geo_L.qml"))
        shutil.copyfile(
                        os.path.join(GeolibUtil.pluginpath,"template\style\geo_A.qml"),
                        os.path.join(style_path,"geo_A.qml"))

    def copyTemplateStyle(self,template_name, style_path):
        shutil.copytree(
            os.path.join(GeolibUtil.pluginpath,'template','style',template_name),
             style_path)

    def copyTemplateFile(self,layer_type,root_path,template_name,file_name):
        #プラグインテンプレートフォルダにあるGeopackageファイルをプロジェクトフォルダにコピーする
        templateName = template_name +'.gpkg'
        fileName = file_name + '.gpkg'
        shutil.copyfile(
                    os.path.join(GeolibUtil.pluginpath,"template",templateName),
                    os.path.join(root_path, fileName))

    def copyGeoPackageFile(self,layer_type,root_path,package_name):
        #プラグインフォルダにあるGeopackageファイルをプロジェクトフォルダにコピーする
        if (layer_type == 'Scenario Map'):
            geoPackageName = package_name +'.gpkg'
            shutil.copyfile(
                        os.path.join(GeolibUtil.pluginpath,"template\scenario.gpkg"),
                        os.path.join(root_path, geoPackageName))
        if (layer_type == 'Subject Map'):
            geoPackageName = package_name +'.gpkg'
            shutil.copyfile(
                        os.path.join(GeolibUtil.pluginpath,"template\geomap.gpkg"),
                        os.path.join(root_path, geoPackageName))

    def copyFile(self,source_file,root_path,file_name):
        sourcePath, ext = os.path.splitext(source_file)
        fileName = file_name + ext
        shutil.copyfile(
                    source_file,
                    os.path.join(root_path, fileName))

    def createRootNode(self, root_name):
        # レイヤーツリーのRootノードにグループを作成する
        root = QgsProject.instance().layerTreeRoot()
        root.insertGroup(0, root_name)

    def createSubNode(self,root_name, sub_name):
        # Rootノード配下にSubノードグループを作成する
        root = QgsProject.instance().layerTreeRoot()
        node = root.findGroup(root_name)
        node.insertGroup(0, sub_name)

    def addLayer(self, root_path, layer_type, geopackage_name, group_name, layer_name, style_path) :
        layerName = geopackage_name + '-' + layer_name
        layer = QgsVectorLayer(os.path.join(root_path, geopackage_name+'.gpkg|layername='+layer_name),layerName, "ogr")
        #if (style_path != ''):
        uri = os.path.join(style_path, layer_name+".qml")
        layer.loadNamedStyle(uri)
        layer.triggerRepaint()

        root_name = 'Scenario'
        if (layer_type == 'Scenario Map'):
            root_name = 'Scenario'
        elif (layer_type == 'Subject Map'):
            root_name = 'Subject'
        root = QgsProject.instance().layerTreeRoot()
        root_node = root.findGroup(root_name)
        node = root_node.findGroup(group_name)
        map_layer = QgsProject.instance().addMapLayer(layer,False)
        node_layer = QgsLayerTreeLayer(map_layer)
        node.addChildNode(node_layer)

    def loadBaseMap(self,tile_layer):
        # 指定したタイルレイヤをキャンバスにロードする
        _map_name = self.tr('GSI Map(Standard)')
        rlayer = None
        if tile_layer != "":
            if tile_layer == self.tr('GSI Map(Standard)'):
                urlWithParams = 'contextualWMSLegend=0&crs=EPSG:3857&' + \
                                'dpiMode=7&featureCount=10&format=image/png&' + \
                                'layers=std&styles=default&tileMatrixSet=z2to18&' + \
                                'url=http://gsi-cyberjapan.github.io/experimental_wmts/gsitiles_wmts.xml'
            elif tile_layer == self.tr('GIS Map(Pale)'):
                urlWithParams = 'contextualWMSLegend=0&crs=EPSG:3857&' + \
                                'dpiMode=7&featureCount=10&format=image/png&' + \
                                'layers=pale&styles=default&tileMatrixSet=z2to18&' + \
                                'url=http://gsi-cyberjapan.github.io/experimental_wmts/gsitiles_wmts.xml'
            elif tile_layer == self.tr('GSI Map(Rerief)'):
                urlWithParams = 'contextualWMSLegend=0&crs=EPSG:3857&' + \
                                'dpiMode=7&featureCount=10&format=image/png&' + \
                                'layers=relief&styles=default&tileMatrixSet=z2to15&' + \
                                'url=http://gsi-cyberjapan.github.io/experimental_wmts/gsitiles_wmts.xml'
            elif tile_layer == self.tr('GIS Map(Photo)'):
                urlWithParams = 'contextualWMSLegend=0&crs=EPSG:3857&' + \
                                'dpiMode=7&featureCount=10&format=image/jpg&' + \
                                'layers=seamlessphoto&styles=default&tileMatrixSet=z2to18&' + \
                                'url=http://gsi-cyberjapan.github.io/experimental_wmts/gsitiles_wmts.xml'
            elif tile_layer == self.tr('Open Street Map'):
                urlWithParams = 'type=xyz&url=http://c.tile.openstreetmap.org/{z}/{x}/{y}.png'
            else:
                tile_layer = ""

            if tile_layer != "":
                rlayer = QgsRasterLayer(urlWithParams, _map_name, 'wms')
                rlayer.setCustomProperty("labeling", "pal")
                rlayer.setCustomProperty("labeling/enabled", "true")
                rlayer.setCustomProperty("labeling/fontFamily", "Arial")
                rlayer.setCustomProperty("labeling/fontSize", "10")
                rlayer.setCustomProperty("labeling/fieldName", "ename")
                rlayer.setCustomProperty("labeling/placement", "2")
                rlayer.setMaximumScale(1000000.0)
                QgsProject.nstance().addMapLayer(rlayer)
        else:
            #print u"Base Map is not selected."
            None

        return rlayer

    def defQgsFields(self, layer_name):
        #レイヤーフィールド定義
        fields = QgsFields()
        if ((layer_name == 'point') or (layer_name == 'line') or (layer_name == 'polygon')):
            fields.append(QgsField("no", QVariant.Int))
            fields.append(QgsField("symbol", QVariant.String))
            fields.append(QgsField("filename", QVariant.String))
            fields.append(QgsField("remarks", QVariant.String))
            fields.append(QgsField("_markerType", QVariant.String))   #Icon/DivIcon/Circle/CircleMarker
            fields.append(QgsField("_className", QVariant.String))     #L.Pathの仕様による
            fields.append(QgsField("_stroke", QVariant.String))            #L.Pathの仕様による
            fields.append(QgsField("_color", QVariant.String))              #L.Pathの仕様による
            fields.append(QgsField("_weight", QVariant.String))           #L.Pathの仕様による
            fields.append(QgsField("_opacity", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_fill", QVariant.String))                 #L.Pathの仕様による
            fields.append(QgsField("_fillColor", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_dashArray", QVariant.String))      #L.Pathの仕様による
            fields.append(QgsField("_lineCap", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_lineJoin", QVariant.String))         #L.Pathの仕様による
            fields.append(QgsField("_clickable", QVariant.String))        #L.Pathの仕様による
            fields.append(QgsField("_iconUrl", QVariant.String))          #L.Iconの仕様による
            fields.append(QgsField("_iconSize", QVariant.String))         #L.Iconの仕様による
            fields.append(QgsField("_iconAnchor", QVariant.String))      #L.Iconの仕様による
            fields.append(QgsField("_html", QVariant.String))             #L.DivIconの仕様による
            fields.append(QgsField("_radius", QVariant.String))           #L.Circle, L.CircleMarkerの仕様による

        if(layer_name == 'pnt'):
            fields.append(QgsField("no", QVariant.Int))
            fields.append(QgsField("attribute", QVariant.Int))
            fields.append(QgsField("remarks", QVariant.String))
            fields.append(QgsField("legend01", QVariant.String))
            fields.append(QgsField("legend01e", QVariant.String))
            fields.append(QgsField("_markerType", QVariant.String))   #Icon/DivIcon/Circle/CircleMarker
            fields.append(QgsField("_className", QVariant.String))     #L.Pathの仕様による
            fields.append(QgsField("_stroke", QVariant.String))            #L.Pathの仕様による
            fields.append(QgsField("_color", QVariant.String))              #L.Pathの仕様による
            fields.append(QgsField("_weight", QVariant.String))           #L.Pathの仕様による
            fields.append(QgsField("_opacity", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_fill", QVariant.String))                 #L.Pathの仕様による
            fields.append(QgsField("_fillColor", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_dashArray", QVariant.String))      #L.Pathの仕様による
            fields.append(QgsField("_lineCap", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_lineJoin", QVariant.String))         #L.Pathの仕様による
            fields.append(QgsField("_clickable", QVariant.String))        #L.Pathの仕様による
            fields.append(QgsField("_iconUrl", QVariant.String))          #L.Iconの仕様による
            fields.append(QgsField("_iconSize", QVariant.String))         #L.Iconの仕様による
            fields.append(QgsField("_iconAnchor", QVariant.String))      #L.Iconの仕様による
            fields.append(QgsField("_html", QVariant.String))             #L.DivIconの仕様による
            fields.append(QgsField("_radius", QVariant.String))           #L.Circle, L.CircleMarkerの仕様による

        if(layer_name == 'strdip'):
            fields.append(QgsField("no", QVariant.Int))
            fields.append(QgsField("strike_value", QVariant.Double))
            fields.append(QgsField("dip_value", QVariant.Double))
            fields.append(QgsField("remarks", QVariant.String))
            fields.append(QgsField("attribute", QVariant.Int))
            fields.append(QgsField("legend01", QVariant.String))
            fields.append(QgsField("legend01e", QVariant.String))
            fields.append(QgsField("_markerType", QVariant.String))   #Icon/DivIcon/Circle/CircleMarker
            fields.append(QgsField("_className", QVariant.String))     #L.Pathの仕様による
            fields.append(QgsField("_stroke", QVariant.String))            #L.Pathの仕様による
            fields.append(QgsField("_color", QVariant.String))              #L.Pathの仕様による
            fields.append(QgsField("_weight", QVariant.String))           #L.Pathの仕様による
            fields.append(QgsField("_opacity", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_fill", QVariant.String))                 #L.Pathの仕様による
            fields.append(QgsField("_fillColor", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_dashArray", QVariant.String))      #L.Pathの仕様による
            fields.append(QgsField("_lineCap", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_lineJoin", QVariant.String))         #L.Pathの仕様による
            fields.append(QgsField("_clickable", QVariant.String))        #L.Pathの仕様による
            fields.append(QgsField("_iconUrl", QVariant.String))          #L.Iconの仕様による
            fields.append(QgsField("_iconSize", QVariant.String))         #L.Iconの仕様による
            fields.append(QgsField("_iconAnchor", QVariant.String))      #L.Iconの仕様による
            fields.append(QgsField("_html", QVariant.String))             #L.DivIconの仕様による
            fields.append(QgsField("_radius", QVariant.String))           #L.Circle, L.CircleMarkerの仕様による

        if(layer_name == 'geo_L'):
            fields.append(QgsField("major_code", QVariant.Int))
            fields.append(QgsField("minor_code", QVariant.Int))
            fields.append(QgsField("description", QVariant.String))
            fields.append(QgsField("legend01", QVariant.String))
            fields.append(QgsField("legend01e", QVariant.String))
            fields.append(QgsField("_markerType", QVariant.String))   #Icon/DivIcon/Circle/CircleMarker
            fields.append(QgsField("_className", QVariant.String))     #L.Pathの仕様による
            fields.append(QgsField("_stroke", QVariant.String))            #L.Pathの仕様による
            fields.append(QgsField("_color", QVariant.String))              #L.Pathの仕様による
            fields.append(QgsField("_weight", QVariant.String))           #L.Pathの仕様による
            fields.append(QgsField("_opacity", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_fill", QVariant.String))                 #L.Pathの仕様による
            fields.append(QgsField("_fillColor", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_dashArray", QVariant.String))      #L.Pathの仕様による
            fields.append(QgsField("_lineCap", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_lineJoin", QVariant.String))         #L.Pathの仕様による
            fields.append(QgsField("_clickable", QVariant.String))        #L.Pathの仕様による
            fields.append(QgsField("_iconUrl", QVariant.String))          #L.Iconの仕様による
            fields.append(QgsField("_iconSize", QVariant.String))         #L.Iconの仕様による
            fields.append(QgsField("_iconAnchor", QVariant.String))      #L.Iconの仕様による
            fields.append(QgsField("_html", QVariant.String))             #L.DivIconの仕様による
            fields.append(QgsField("_radius", QVariant.String))           #L.Circle, L.CircleMarkerの仕様による

        if(layer_name == 'geo_A'):
            fields.append(QgsField("major_code", QVariant.Int))
            fields.append(QgsField("minor_code", QVariant.Int))
            fields.append(QgsField("description", QVariant.String))
            fields.append(QgsField("symbol", QVariant.String))
            fields.append(QgsField("legend01", QVariant.String))
            fields.append(QgsField("legend01e", QVariant.String))
            fields.append(QgsField("legend02", QVariant.String))
            fields.append(QgsField("legend02e", QVariant.String))
            fields.append(QgsField("legend03", QVariant.String))
            fields.append(QgsField("legend03e", QVariant.String))
            fields.append(QgsField("legend04", QVariant.String))
            fields.append(QgsField("legend04e", QVariant.String))
            fields.append(QgsField("legend05", QVariant.String))
            fields.append(QgsField("legend05e", QVariant.String))
            fields.append(QgsField("legend06", QVariant.String))
            fields.append(QgsField("legend06e", QVariant.String))
            fields.append(QgsField("legend07", QVariant.String))
            fields.append(QgsField("legend07e", QVariant.String))
            fields.append(QgsField("_markerType", QVariant.String))   #Icon/DivIcon/Circle/CircleMarker
            fields.append(QgsField("_className", QVariant.String))     #L.Pathの仕様による
            fields.append(QgsField("_stroke", QVariant.String))            #L.Pathの仕様による
            fields.append(QgsField("_color", QVariant.String))              #L.Pathの仕様による
            fields.append(QgsField("_weight", QVariant.String))           #L.Pathの仕様による
            fields.append(QgsField("_opacity", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_fill", QVariant.String))                 #L.Pathの仕様による
            fields.append(QgsField("_fillColor", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_dashArray", QVariant.String))      #L.Pathの仕様による
            fields.append(QgsField("_lineCap", QVariant.String))          #L.Pathの仕様による
            fields.append(QgsField("_lineJoin", QVariant.String))         #L.Pathの仕様による
            fields.append(QgsField("_clickable", QVariant.String))        #L.Pathの仕様による
            fields.append(QgsField("_iconUrl", QVariant.String))          #L.Iconの仕様による
            fields.append(QgsField("_iconSize", QVariant.String))         #L.Iconの仕様による
            fields.append(QgsField("_iconAnchor", QVariant.String))      #L.Iconの仕様による
            fields.append(QgsField("_html", QVariant.String))             #L.DivIconの仕様による
            fields.append(QgsField("_radius", QVariant.String))           #L.Circle, L.CircleMarkerの仕様による

        return fields

    def createLayer(self,path, root_name, group_name, layer_type, layer_name, layer_title, style_path):
        #レイヤーを作成する
        layer = QgsVectorLayer(layer_type + "?crs=EPSG:4612", layer_name, "memory")
        fields = GeolibUtil().defQgsFields(layer_name)
        provider = layer.dataProvider()
        layer.startEditing()
        provider.addAttributes(fields)
        layer.updateFields()
        # add a feature
        fet = QgsFeature()
        #if(layer_type == 'Point'):
        #    fet.setGeometry(QgsGeometry.asMultiPoint([]))
        #if(layer_type == 'LineString'):
        #    fet.setGeometry(QgsGeometry.asMultiPolyline([]))
        #if(layer_type == 'Polygon'):
        #    fet.setGeometry(QgsGeometry.asMultiPolygon([]))
        fet.setAttributes([])
        provider.addFeatures([fet])
        layer.updateExtents()

        # geopackage を作成する
        QgsVectorFileWriter.writeAsVectorFormat(layer, os.path.join(path, layer_name+".geojson"), "utf-8", layer.crs(), "GeoJSON")
        layer = QgsVectorLayer(os.path.join(path, layer_name+".geojson"), layer_title, "ogr")

        # geojson を作成する
        #QgsVectorFileWriter.writeAsVectorFormat(layer, os.path.join(path, layer_name+".geojson"), "utf-8", layer.crs(), "GeoJSON")
        #layer = QgsVectorLayer(os.path.join(path, layer_name+".geojson"), layer_title, "ogr")

        #スタイルファイルを適用
        uri = os.path.join(style_path, layer_name+".qml")
        layer.loadNamedStyle(uri)
        layer.triggerRepaint()

        # RootノードGroup下にベクターレイヤノ―ドを追加する
        root = QgsProject.instance().layerTreeRoot()
        root_node = root.findGroup(root_name)
        if (group_name == ''):
            node = root_node
        else:
            node = root_node.findGroup(group_name)
        map_layer = QgsProject.instance().addMapLayer(layer,False)
        node_layer = QgsLayerTreeLayer(map_layer)
        node.addChildNode(node_layer)

    def addFeatureGeoclino(self,provider,xml_data):
        # 地物を追加
        data = xml_data.getElementsByTagName("point")
        for i, element in enumerate(data):
            GeoClinoId = (element.getElementsByTagName("Id"))[0].childNodes[0].data
            Latitude = (element.getElementsByTagName("Latitude"))[0].childNodes[0].data
            Longitude = (element.getElementsByTagName("Longitude"))[0].childNodes[0].data
            Strike = (element.getElementsByTagName("Strike"))[0].childNodes[0].data
            Dip = (element.getElementsByTagName("Dip"))[0].childNodes[0].data
            Strike_Value = int(round(float(Strike)))
            if (Dip.find("(-)")):
                Dip =Dip.replace("(-)","")
                Dip_Value = - int(round(float(Dip)))
            else:
                Dip_Value = int(round(float(Dip)))

            if (Dip_Value < 0):
                Dip_Value = - Dip_Value
                if(Strike_Value > 180):
                    Strike_Value = Strike_Value - 180

            Trend = (element.getElementsByTagName("Trend"))[0].childNodes[0].data
            Plunge = (element.getElementsByTagName("Plunge"))[0].childNodes[0].data
            Rake = (element.getElementsByTagName("Rake"))[0].childNodes[0].data
            CreateDate = (element.getElementsByTagName("Date"))[0].childNodes[0].data
            Attr = 1
            Declinat = (element.getElementsByTagName("Declination"))[0].childNodes[0].data
            Type = (element.getElementsByTagName("Type"))[0].childNodes[0].data

            feature = QgsFeature()
            feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(float(Longitude), float(Latitude))))
            feature.setAttributes([ '',\
                                   GeoClinoId, \
                                   Strike_Value, \
                                   Dip_Value, \
                                   GeoClinoId + ':' + CreateDate, \
                                   Attr
            ])
            provider.addFeatures([feature])

    def ftpLogin(self):
        #FTPログイン
        ftp = ftplib.FTP("gis.nsb-dank.com")
        ftp.set_pasv("true")
        # ユーザ名とパスワードを設定してログイン
        ftp.login("qgis_user", "qgis_user")
        return ftp

    def ftpCreateFolder(self, path):
        #サーバーの指定フォルダがない場合は作成する
        ftp=self.ftpLogin()
        try:
            ftp.cwd(path)
        except:
            ftp.mkd(path)
        ftp.quit()

    def ftpDeleteFolder(self, path):
        #サーバーの指定フォルダを削除する
        ftp=self.ftpLogin()
        #try:
        ftp.rmd(path)
        #except:
        #    print(path + ":The folder could not be deleted.")
        ftp.quit()

    def ftpRmTree(self, path):
        ftp=self.ftpLogin()
        """Recursively delete a directory tree on a remote server."""
        wd = ftp.pwd()

        try:
            names = ftp.nlst(path)
        except ftplib.all_errors as e:
            # some FTP servers complain when you try and list non-existent paths
            print('FtpRmTree: Could not remove {0}: {1}'.format(path, e))
            return

        for name in names:
            if os.path.split(name)[1] in ('.', '..'): continue

            print('FtpRmTree: Checking {0}'.format(name))

            try:
                ftp.cwd(name)  # if we can cwd to it, it's a folder
                ftp.cwd(wd)  # don't try a nuke a folder we're in
                self.ftpRmTree(self, name)
            except ftplib.all_errors:
                ftp.delete(name)

        try:
            ftp.rmd(path)
        except ftplib.all_errors as e:
            print('FtpRmTree: Could not remove {0}: {1}'.format(path, e))

    def ftpUploadFile(self, file_path,dest_path):
        #サーバーにファイルを転送する（バイナリ形式）
        ftp = self.ftpLogin()
        file_name = os.path.basename(file_path)
        fp = open(file_path,'rb')
        ftp.storbinary("STOR ./" +dest_path+file_name,fp)
        fp.close()
        ftp.quit()

    def ftpFileCount(self, folder_name):
        #サーバーの指定フォルダ内のファイル数を返す
        # ftp接続
        ftp = self.ftpLogin()
        # folder_name 内のファイル数をカウント
        items = ftp.nlst(folder_name + '/')
        count = len(items)
        ftp.close()
        return count

    def dbConnect(self,host_name,db_name,port_no,db_user_id,db_password):
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName(host_name)
        db.setPort(int(port_no))
        db.setDatabaseName(db_name)
        db.setUserName(db_user_id)
        db.setPassword(db_password)
        return db

"""
マップツールユーティリティ
"""
class MapToolUtil:

    def setStrDipText(self,strike,dip):
        spn_dip = dip
        spn_strike = strike
        if strike == 0:
            cbo_strike1 = 'N'
            cbo_strike2 = 'S'
            spn_strike = 0
            cbo_dip = 'E'

        elif strike >= 0 and strike < 45:
            cbo_strike1 = 'N'
            cbo_strike2 = 'E'
            spn_strike = strike
            cbo_dip = 'E'

        elif strike >= 45 and strike < 90:
            cbo_strike1 = 'N'
            cbo_strike2 = 'E'
            spn_strike = strike
            cbo_dip = 'S'

        elif strike == 90:
            cbo_strike1 = 'N'
            cbo_strike2 = 'E'
            spn_strike = 90
            cbo_dip = 'S'

        elif  strike >= 90 and strike < 135:
            cbo_strike1 = 'N'
            cbo_strike2 = 'W'
            spn_strike = 180 - strike
            cbo_dip = 'S'

        elif  strike >= 135 and strike < 180:
            cbo_strike1 = 'N'
            cbo_strike2 = 'W'
            spn_strike = 180 - strike
            cbo_dip = 'W'

        elif strike == 180:
            cbo_strike1 = 'N'
            cbo_strike2 = 'S'
            spn_strike = 0
            cbo_dip = 'W'

        elif  strike >= 180 and strike < 225:
            cbo_strike1 = 'N'
            cbo_strike2 = 'E'
            spn_strike = strike - 180
            cbo_dip = 'W'

        elif  strike >= 225 and strike < 270:
            cbo_strike1 = 'N'
            cbo_strike2 = 'E'
            spn_strike = strike - 180
            cbo_dip = 'N'

        elif strike == 270:
            cbo_strike1 = 'N'
            cbo_strike2 = 'W'
            spn_strike = 90
            cbo_dip = 'N'

        elif strike >= 270 and strike < 315:
            cbo_strike1 = 'N'
            cbo_strike2 = 'W'
            spn_strike = 360 - strike
            cbo_dip = 'N'

        elif strike >= 315 and strike < 360:
            cbo_strike1 = 'N'
            cbo_strike2 = 'W'
            spn_strike = 360 - strike
            cbo_dip = 'E'

        return cbo_strike1,spn_strike,cbo_strike2,spn_dip,cbo_dip

    def setStrDipValue(self, cbo_strike1, spn_strike, cbo_strike2, spn_dip, cbo_dip):
        dip = spn_dip
        strike = spn_strike

        if spn_strike == 0:
            if cbo_dip == 'E':
                strike = 0
            elif  cbo_dip == 'W':
                strike = 180

        elif spn_strike > 0 and spn_strike <= 45:
            if cbo_dip == 'E':
                if cbo_strike2 == 'E':
                    strike = spn_strike
                elif cbo_strike2 == 'W':
                    strike = 360 - spn_strike
            elif  cbo_dip == 'W':
                if cbo_strike2 == 'E':
                    strike = 180 + spn_strike
                elif cbo_strike2 == 'W':
                    strike = 180 - spn_strike

        elif spn_strike> 45 and spn_strike < 90:
            if cbo_dip == 'S':
                if cbo_strike2 == 'E':
                    strike = spn_strike
                elif cbo_strike2 == 'W':
                    strike = 180 - spn_strike
            elif  cbo_dip == 'N':
                if cbo_strike2 == 'E':
                    strike = 180 + spn_strike
                elif cbo_strike2 == 'W':
                    strike = 360 - spn_strike
        elif spn_strike == 90:
            if cbo_dip == 'S':
                strike = 90
            elif  cbo_dip == 'N':
                strike = 270

        return strike, dip


class SelectTool(QgsMapTool):
    def __init__(self, iface, canvas):
        QgsMapTool.__init__(self, canvas)
        self.iface = iface
        self.canvas = canvas
        self.rubberPoint = QgsRubberBand(canvas, QgsWkbTypes.PointGeometry)
        self.rubberPoint.setColor(QColor(255, 0, 0, 100))
        # ラバーバンドの作成と色を決定
        self.last_point = None
        # ダブルクリックなどで点を二重に入力しないための変数

    def canvasPressEvent(self, event):
        # 地図を押した時に呼び出される
        pos = event.pos()
        # UI上の座標を取得
        point = self.get_canvas_point(pos)
        # 地図上の座標を取得
        # point = event.mapPoint()
        # APIドキュメントでは上記で地図上の座標を取得できるが
        # Pythonでは、返り値がQMouseEventのためできない
        # ドキュメントではQgsMapMouseEventが返り値

        button_type = event.button()
        # 押したボタンの種類
        point_count = self.rubberPoint.numberOfVertices()
        # ポイントの数取得
        if button_type == Qt.LeftButton and self.last_point != point:
            # 左クリックで、最後に入力したポイントと同じで無ければ
            self.rubberPoint.addPoint(point)
            # ラバーバンドにポイントを追加
            self.last_point = point
        if button_type == Qt.RightButton and point_count < 2:
            # 右クリックの場合
            self.last_point = None
            # 最終入力ポイントのリセット
            self.rubberPoint.reset(QgsWkbTypes.PointGeometry)
            # ラバーバンドのリセット

    def canvasMoveEvent(self, event):
        # カーソルが地図上を移動すると呼び出される関数
        pos = event.pos()
        point = self.get_canvas_point(pos)
        point_count = self.rubberPoint.numberOfVertices()
        if point_count == 0:
            # ポイントが一点もない場合落とす
            return
        self.rubberPoint.movePoint(point)
        # 最後に追加したポイントをカーソルの位置に移動させる

    def get_canvas_point(self, position):
        # 地図上のポイントに変換する関数
        x = position.x()
        y = position.y()
        trans = self.canvas.getCoordinateTransform()
        return trans.toMapCoordinates(x, y)
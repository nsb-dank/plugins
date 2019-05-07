# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Qgis2threejs
                                 A QGIS plugin
 export terrain data, map canvas image and vector data to web browser
                              -------------------
        begin                : 2014-01-16
        copyright            : (C) 2014 Minoru Akagi
        email                : akaginch@gmail.com
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
import json
from PyQt5.QtCore import QVariant
from qgis.core import QgsCoordinateTransform, QgsFeatureRequest, QgsGeometry, QgsProject, QgsRenderContext, QgsWkbTypes

from .conf import BLOCK_FEATURES, DEBUG_MODE
from .datamanager import MaterialManager, ModelManager
from .buildlayer import LayerBuilder
from .geometry import Geometry, PointGeometry, LineGeometry, PolygonGeometry, TriangleMesh
from .propertyreader import VectorPropertyReader
from .qgis2threejstools import logMessage
from .vectorobject import objectTypeRegistry


def json_default(o):
  if isinstance(o, QVariant):
    return repr(o)
  raise TypeError(repr(o) + " is not JSON serializable")


class VectorLayerBuilder(LayerBuilder):

  gt2str = {QgsWkbTypes.PointGeometry: "point",
            QgsWkbTypes.LineGeometry: "line",
            QgsWkbTypes.PolygonGeometry: "polygon"}

  def __init__(self, settings, imageManager, layer, pathRoot=None, urlRoot=None, progress=None, modelManager=None):
    LayerBuilder.__init__(self, settings, imageManager, layer, pathRoot, urlRoot, progress)

    self.materialManager = MaterialManager(settings.materialType())    #TODO: takes imageManager
    self.modelManager = ModelManager(settings)

    self.mapTo3d = settings.mapTo3d()
    self.geomType = self.layer.mapLayer.geometryType()
    self.fidx = None

    self.demSize = None

  def build(self, build_blocks=False):
    mapLayer = self.layer.mapLayer
    if mapLayer is None:
      return

    properties = self.layer.properties
    baseExtent = self.settings.baseExtent
    mapSettings = self.settings.mapSettings
    renderContext = QgsRenderContext.fromMapSettings(mapSettings)

    self.prop = VectorPropertyReader(objectTypeRegistry(), renderContext, mapLayer, properties)
    if self.prop.objType is None:
      logMessage("Object type not found")
      return

    # prepare triangle mesh
    if self.prop.objType.name == "Overlay" and self.prop.isHeightRelativeToDEM():
      # get the grid size of the DEM layer which polygons overlay
      demProp = self.settings.getPropertyReaderByLayerId(properties.get("comboBox_altitudeMode"))
      if demProp:
        self.demSize = demProp.demSize(mapSettings.outputSize())

    layer = VectorLayer(self.settings, mapLayer, self.prop, self.materialManager, self.modelManager)
    self._layer = layer

    self.hasLabel = layer.hasLabel()
    self.clipGeom = None

    # feature request
    request = QgsFeatureRequest()
    if properties.get("radioButton_IntersectingFeatures", False):
      request.setFilterRect(layer.transform.transformBoundingBox(baseExtent.boundingBox(), QgsCoordinateTransform.ReverseTransform))

      # geometry for clipping
      if properties.get("checkBox_Clip") and self.prop.objType.name != "Triangular Mesh":
        extent = baseExtent.clone().scale(0.999999)   # clip with slightly smaller extent than map canvas extent
        self.clipGeom = extent.geometry()

    # initialize symbol rendering, and then get features (geometry, attributes, color, etc.)
    mapLayer.renderer().startRender(renderContext, mapLayer.fields())
    self.features = layer.features(request)
    mapLayer.renderer().stopRender(renderContext)

    # materials/models
    data = {}
    if self.prop.objType.name != "Model File":
      for feat in self.features:
        feat.material = self.prop.objType.material(self.settings, layer, feat)
        feat.model = None
      data["materials"] = self.materialManager.buildAll(self.imageManager, self.pathRoot, self.urlRoot, base64=self.settings.base64)

    else:
      for feat in self.features:
        feat.material = None
        feat.model = self.prop.objType.model(self.settings, layer, feat)
      data["models"] = self.modelManager.build(self.pathRoot is not None)

    if build_blocks:
      data["blocks"] = [block.build() for block in self.blocks()]

    d = {
      "type": "layer",
      "id": self.layer.jsLayerId,
      "properties": self.layerProperties(),
      "data": data
      }

    if DEBUG_MODE:
      d["PROPERTIES"] = properties
    return d

  def layerProperties(self):
    p = LayerBuilder.layerProperties(self)
    p["type"] = self.gt2str.get(self.layer.mapLayer.geometryType())
    p["objType"] = self.prop.objType.name

    if self._layer.writeAttrs:
      p["propertyNames"] = self._layer.fieldNames

      if self._layer.labelAttrIndex is not None:
        p["label"] = {"index": self._layer.labelAttrIndex,
                      "relative": self.properties.get("labelHeightWidget", {}).get("comboData", 0) == 1}

    # object-type-specific properties
    #p.update(self.prop.objType.layerProperties(self.settings, self))
    return p

  def blocks(self):
    index = 0

    def createBlockBuilder(blockIndex, features):
      return FeatureBlockBuilder(blockIndex, {
        "type": "block",
        "layer": self.layer.jsLayerId,
        "block": blockIndex,
        "features": features
        }, self.pathRoot, self.urlRoot)

    demProvider = None
    if self.prop.isHeightRelativeToDEM():
      demProvider = self.settings.demProviderByLayerId(self.layer.properties.get("comboBox_altitudeMode"))

    if self.layer.properties.get("radioButton_zValue"):
      useZM = Geometry.UseZ
    elif self.layer.properties.get("radioButton_mValue"):
      useZM = Geometry.UseM
    else:
      useZM = Geometry.NotUseZM

    feats = []
    for feat in self.features or []:
      geom = feat.geometry(self.mapTo3d, useZM, demProvider, self.clipGeom, self.settings.baseExtent, self.demSize)
      if geom is None:
        continue

      f = {}
      f["geom"] = self.prop.objType.geometry(self.settings, self._layer, feat, geom)

      if feat.material is not None:
        f["mtl"] = feat.material
      elif feat.model is not None:
        f["model"] = feat.model
      else:   # no material nor model
        continue

      if feat.attributes is not None:
        f["prop"] = feat.attributes

        if feat.labelHeight is not None:
          f["lh"] = feat.labelHeight

      feats.append(f)

      if len(feats) == BLOCK_FEATURES:
        yield createBlockBuilder(index, feats)
        index += 1
        feats = []

    if len(feats) or index == 0:
      yield createBlockBuilder(index, feats)


class FeatureBlockBuilder:
  
  def __init__(self, blockIndex, data, pathRoot=None, urlRoot=None):
    self.blockIndex = blockIndex
    self.data = data
    self.pathRoot = pathRoot
    self.urlRoot = urlRoot

  def build(self):
    if self.pathRoot is not None:
      with open(self.pathRoot + "{0}.json".format(self.blockIndex), "w", encoding="utf-8") as f:
        json.dump(self.data, f, ensure_ascii=False, indent=2 if DEBUG_MODE else None, default=json_default)

      url = self.urlRoot + "{0}.json".format(self.blockIndex)
      return {"url": url}

    else:
      return self.data


class Feature:

  def __init__(self, layer, qGeom, altitude, propValues, attrs=None, labelHeight=None):
    self.layerProp = layer.prop
    self.geom = qGeom
    self.geomType = layer.geomType
    self.geomClass = layer.geomType2Class.get(layer.geomType)
    self.altitude = altitude
    self.values = propValues
    self.attributes = attrs
    self.labelHeight = labelHeight

    self.material = -1

  def geometry(self, mapTo3d, useZM=Geometry.NotUseZM, demProvider=None, clipGeom=None, baseExtent=None, demSize=None):
    """demSize: grid size of the DEM layer which polygons overlay"""
    geom = self.geom
    rotation = baseExtent.rotation()

    if demProvider:
      if self.layerProp.objType.name == "Overlay":
        center = baseExtent.center()
        half_width, half_height = baseExtent.width() / 2, baseExtent.height() / 2
        xmin, ymin = center.x() - half_width, center.y() - half_height
        xmax, ymax = center.x() + half_width, center.y() + half_height
        xres, yres = baseExtent.width() / (demSize.width() - 1), baseExtent.height() / (demSize.height() - 1)
        tmesh = TriangleMesh(xmin, ymin, xmax, ymax, demSize.width() - 1, demSize.height() - 1)
        z_func = lambda x, y: demProvider.readValueOnTriangles(x, y, xmin, ymin, xres, yres) + self.altitude
      else:
        z_func = lambda x, y: demProvider.readValue(x, y) + self.altitude
    else:
      z_func = lambda x, y: self.altitude

    # clip geometry
    if clipGeom and self.geomType in [QgsWkbTypes.LineGeometry, QgsWkbTypes.PolygonGeometry]:
      geom = geom.intersection(clipGeom)
      if geom is None:
        return None

    # skip if geometry is empty or null
    if geom.isEmpty() or geom.isNull():
      logMessage("empty/null geometry skipped")
      return None

    if self.geomType == QgsWkbTypes.PolygonGeometry:
      if self.layerProp.objType.name == "Triangular Mesh":
        return self.geomClass.fromQgsGeometry(geom, z_func, mapTo3d.transform, useZM=useZM)

      if self.layerProp.objType.name == "Overlay" and self.layerProp.isHeightRelativeToDEM():

        if rotation:
          geom.rotate(rotation, baseExtent.center())
        geom = tmesh.splitPolygon(geom)
        if rotation:
          geom.rotate(-rotation, baseExtent.center())

        useCentroidHeight = False
        centroidPerPolygon = False
      else:
        useCentroidHeight = True
        centroidPerPolygon = True

      return self.geomClass.fromQgsGeometry(geom, z_func, mapTo3d.transform, useCentroidHeight, centroidPerPolygon)

    return self.geomClass.fromQgsGeometry(geom, z_func, mapTo3d.transform, useZM=useZM)


class VectorLayer:

  geomType2Class = {QgsWkbTypes.PointGeometry: PointGeometry, QgsWkbTypes.LineGeometry: LineGeometry, QgsWkbTypes.PolygonGeometry: PolygonGeometry}

  def __init__(self, settings, layer, prop, materialManager, modelManager):
    self.settings = settings
    self.layer = layer
    self.prop = prop
    self.name = layer.name() if layer else "no title"
    self.materialManager = materialManager
    self.modelManager = modelManager

    self.transform = QgsCoordinateTransform(layer.crs(), settings.crs, QgsProject.instance())
    self.geomType = layer.geometryType()
    self.geomClass = self.geomType2Class.get(self.geomType)

    # attributes
    self.writeAttrs = prop.properties.get("checkBox_ExportAttrs", False)
    self.labelAttrIndex = prop.properties.get("comboBox_Label", None)
    self.fieldIndices = []
    self.fieldNames = []

    if self.writeAttrs:
      for index, field in enumerate(layer.fields()):
        if field.editorWidgetSetup().type() != "Hidden":
          self.fieldIndices.append(index)
          self.fieldNames.append(field.displayName())

  def hasLabel(self):
    return bool(self.labelAttrIndex is not None)

  def features(self, request=None):
    mapTo3d = self.settings.mapTo3d()
    baseExtent = self.settings.baseExtent
    baseExtentGeom = baseExtent.geometry()
    rotation = baseExtent.rotation()
    prop = self.prop
    fields = self.layer.fields()

    feats = []
    for f in self.layer.getFeatures(request or QgsFeatureRequest()):
      geometry = f.geometry()
      if geometry is None:
        logMessage("null geometry skipped")
        continue

      # coordinate transformation - layer crs to project crs
      geom = QgsGeometry(geometry)
      if geom.transform(self.transform) != 0:
        logMessage("Failed to transform geometry")
        continue

      # check if geometry intersects with the base extent (rotated rect)
      if rotation and not baseExtentGeom.intersects(geom):
        continue

      # set feature to expression context
      prop.setContextFeature(f)

      # evaluate expression
      altitude = prop.altitude()
      propVals = prop.values(f)

      attrs = labelHeight = None
      if self.writeAttrs:
        attrs = [fields[i].displayString(f.attribute(i)) for i in self.fieldIndices]

        if self.hasLabel():
          labelHeight = prop.labelHeight() * mapTo3d.multiplierZ

      # create a feature object
      feat = Feature(self, geom, altitude, propVals, attrs, labelHeight)
      feats.append(feat)

    return feats

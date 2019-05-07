<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="0" simplifyLocal="1" minScale="1e+8" readOnly="0" version="3.0.3-Girona" simplifyAlgorithm="0" labelsEnabled="1" simplifyDrawingTol="1" simplifyMaxScale="1">
  <renderer-v2 enableorderby="0" type="categorizedSymbol" symbollevels="1" forceraster="0" attr="Attribute">
    <categories>
      <category symbol="0" render="true" value="1" label="地層の走向・傾斜"/>
      <category symbol="1" render="true" value="2" label="逆転層の走向・傾斜"/>
      <category symbol="2" render="true" value="3" label="垂直層の走向・傾斜"/>
      <category symbol="3" render="true" value="4" label="水平層の走向・傾斜"/>
      <category symbol="4" render="true" value="99" label="走向線描画用"/>
      <category symbol="5" render="true" value="" label="未定義"/>
    </categories>
    <symbols>
      <symbol clip_to_extent="1" alpha="1" name="0" type="marker">
        <layer locked="0" enabled="1" class="SvgMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="geolib/bedding.svg" k="name"/>
          <prop v="-0.6000000000000002,-0.60000000000000009" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="255,255,255,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="strike_value" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" alpha="1" name="1" type="marker">
        <layer locked="0" enabled="1" class="SvgMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="geolib/overturned_bedding.svg" k="name"/>
          <prop v="-0.60000000000000009,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="255,255,255,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="strike_value" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" alpha="1" name="2" type="marker">
        <layer locked="0" enabled="1" class="SvgMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="geolib/vertical_bedding.svg" k="name"/>
          <prop v="-0.60000000000000009,-0.60000000000000009" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="strike_value" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" alpha="1" name="3" type="marker">
        <layer locked="0" enabled="1" class="SvgMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="geolib/horizontal_bedding.svg" k="name"/>
          <prop v="-0.60000000000000009,-0.60000000000000009" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="255,255,255,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="strike_value" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" alpha="1" name="4" type="marker">
        <layer locked="0" enabled="1" class="SvgMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="0,0,255,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="geolib/bedding.svg" k="name"/>
          <prop v="0.10000000000000001,0.10000000000000001" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="strike_value" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" enabled="1" class="FilledMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="60,204,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="cross_fill" k="name"/>
          <prop v="0.10000000000000001,0.10000000000000001" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="10" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="strike_value" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" alpha="1" name="@4@1" type="fill">
            <layer locked="0" enabled="1" class="SimpleFill" pass="0">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="60,204,0,255" k="color"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="Pixel" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="Pixel" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" alpha="1" name="5" type="marker">
        <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="40,160,108,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="10" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol clip_to_extent="1" alpha="1" name="0" type="marker">
        <layer locked="0" enabled="1" class="SvgMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" enabled="1" class="SvgMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" enabled="1" class="SvgMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="" k="name"/>
          <prop v="0.20000000000000001,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" enabled="1" class="SvgMarker" pass="0">
          <prop v="0" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="0" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </source-symbol>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings>
      <text-style fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" previewBkgrdColor="#ffffff" fontStrikeout="0" fontWordSpacing="0" fontCapitals="0" fieldName="to_int(dip_value)" useSubstitutions="0" fontWeight="50" textColor="14,1,150,255" textOpacity="1" fontItalic="0" fontFamily="MS UI Gothic" isExpression="1" fontSizeUnit="Point" fontSize="12" fontLetterSpacing="0" blendMode="0" multilineHeight="1" namedStyle="Normal">
        <text-buffer bufferOpacity="1" bufferDraw="1" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="0" bufferColor="255,255,255,255" bufferSizeUnits="MM" bufferJoinStyle="128" bufferSize="0.6"/>
        <background shapeSizeType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeType="0" shapeFillColor="255,255,255,255" shapeRotation="0" shapeSizeUnit="MM" shapeOffsetX="0" shapeBorderColor="128,128,128,255" shapeRadiiUnit="MM" shapeOffsetY="0" shapeSizeX="0" shapeSVGFile="" shapeDraw="0" shapeJoinStyle="64" shapeRadiiX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeRadiiY="0" shapeBorderWidth="0" shapeBorderWidthUnit="MM"/>
        <shadow shadowOffsetAngle="135" shadowDraw="0" shadowRadiusUnit="MM" shadowOffsetUnit="MapUnit" shadowOffsetGlobal="1" shadowScale="100" shadowColor="255,255,255,255" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="1" shadowOffsetDist="1" shadowRadius="3.5" shadowBlendMode="0" shadowRadiusAlphaOnly="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0"/>
        <substitutions/>
      </text-style>
      <text-format plussign="0" addDirectionSymbol="0" decimals="3" wrapChar="" rightDirectionSymbol=">" reverseDirectionSymbol="0" formatNumbers="0" placeDirectionSymbol="0" leftDirectionSymbol="&lt;" multilineAlign="0"/>
      <placement fitInPolygonOnly="0" dist="0" offsetUnits="MapUnit" repeatDistance="0" repeatDistanceUnits="MM" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" centroidWhole="0" placement="6" maxCurvedCharAngleOut="-25" xOffset="3" distMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" quadOffset="4" maxCurvedCharAngleIn="25" preserveRotation="1" centroidInside="0" offsetType="0" placementFlags="10" yOffset="-3" priority="5" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" distUnits="Pixel"/>
      <rendering obstacleFactor="1" obstacle="1" scaleVisibility="0" minFeatureSize="0" upsidedownLabels="0" zIndex="0" maxNumLabels="2000" displayAll="0" fontLimitPixelSize="0" fontMaxPixelSize="10000" limitNumLabels="0" scaleMin="1" labelPerPart="0" fontMinPixelSize="3" mergeLines="0" drawLabels="1" scaleMax="10000000" obstacleType="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" value="" type="QString"/>
          <Option name="properties" type="Map">
            <Option name="LabelRotation" type="Map">
              <Option name="active" value="true" type="bool"/>
              <Option name="field" value="strike_value" type="QString"/>
              <Option name="type" value="2" type="int"/>
            </Option>
            <Option name="OffsetQuad" type="Map">
              <Option name="active" value="false" type="bool"/>
              <Option name="field" value="Strike" type="QString"/>
              <Option name="type" value="2" type="int"/>
            </Option>
            <Option name="Rotation" type="Map">
              <Option name="active" value="false" type="bool"/>
              <Option name="field" value="Strike" type="QString"/>
              <Option name="type" value="2" type="int"/>
            </Option>
          </Option>
          <Option name="type" value="collection" type="QString"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions" value="COALESCE(&quot;Dip_Value&quot;, '&lt;NULL>')"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory maxScaleDenominator="1e+8" minimumSize="0" rotationOffset="270" labelPlacementMethod="XHeight" opacity="1" penColor="#000000" lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" diagramOrientation="Up" minScaleDenominator="0" barWidth="5" backgroundAlpha="255" penWidth="0" height="15" lineSizeType="MM" scaleDependency="Area" scaleBasedVisibility="0" enabled="0" sizeScale="3x:0,0,0,0,0,0" penAlpha="255" sizeType="MM" width="15">
      <fontProperties style="" description="MS UI Gothic,9,-1,5,50,0,0,0,0,0"/>
      <attribute field="" label="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="2" placement="0" priority="0" obstacle="0" dist="0" showAll="1" zIndex="0">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="no">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="strike_value">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dip_value">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="remarks">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="attribute">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="legend01">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="legend01e">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_markerType">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_className">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_stroke">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_color">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_weight">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_opacity">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_fill">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_fillColor">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_dashArray">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_lineCap">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_lineJoin">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_clickable">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_iconUrl">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_iconSize">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_iconAnchor">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_html">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="_radius">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" index="0" name=""/>
    <alias field="no" index="1" name=""/>
    <alias field="strike_value" index="2" name=""/>
    <alias field="dip_value" index="3" name=""/>
    <alias field="remarks" index="4" name=""/>
    <alias field="attribute" index="5" name=""/>
    <alias field="legend01" index="6" name=""/>
    <alias field="legend01e" index="7" name=""/>
    <alias field="_markerType" index="8" name=""/>
    <alias field="_className" index="9" name=""/>
    <alias field="_stroke" index="10" name=""/>
    <alias field="_color" index="11" name=""/>
    <alias field="_weight" index="12" name=""/>
    <alias field="_opacity" index="13" name=""/>
    <alias field="_fill" index="14" name=""/>
    <alias field="_fillColor" index="15" name=""/>
    <alias field="_dashArray" index="16" name=""/>
    <alias field="_lineCap" index="17" name=""/>
    <alias field="_lineJoin" index="18" name=""/>
    <alias field="_clickable" index="19" name=""/>
    <alias field="_iconUrl" index="20" name=""/>
    <alias field="_iconSize" index="21" name=""/>
    <alias field="_iconAnchor" index="22" name=""/>
    <alias field="_html" index="23" name=""/>
    <alias field="_radius" index="24" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="fid" expression="" applyOnUpdate="0"/>
    <default field="no" expression="" applyOnUpdate="0"/>
    <default field="strike_value" expression="" applyOnUpdate="0"/>
    <default field="dip_value" expression="" applyOnUpdate="0"/>
    <default field="remarks" expression="" applyOnUpdate="0"/>
    <default field="attribute" expression="" applyOnUpdate="0"/>
    <default field="legend01" expression="" applyOnUpdate="0"/>
    <default field="legend01e" expression="" applyOnUpdate="0"/>
    <default field="_markerType" expression="" applyOnUpdate="0"/>
    <default field="_className" expression="" applyOnUpdate="0"/>
    <default field="_stroke" expression="" applyOnUpdate="0"/>
    <default field="_color" expression="" applyOnUpdate="0"/>
    <default field="_weight" expression="" applyOnUpdate="0"/>
    <default field="_opacity" expression="" applyOnUpdate="0"/>
    <default field="_fill" expression="" applyOnUpdate="0"/>
    <default field="_fillColor" expression="" applyOnUpdate="0"/>
    <default field="_dashArray" expression="" applyOnUpdate="0"/>
    <default field="_lineCap" expression="" applyOnUpdate="0"/>
    <default field="_lineJoin" expression="" applyOnUpdate="0"/>
    <default field="_clickable" expression="" applyOnUpdate="0"/>
    <default field="_iconUrl" expression="" applyOnUpdate="0"/>
    <default field="_iconSize" expression="" applyOnUpdate="0"/>
    <default field="_iconAnchor" expression="" applyOnUpdate="0"/>
    <default field="_html" expression="" applyOnUpdate="0"/>
    <default field="_radius" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="fid" exp_strength="0" constraints="3" notnull_strength="1" unique_strength="1"/>
    <constraint field="no" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="strike_value" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="dip_value" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="remarks" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="attribute" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="legend01" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="legend01e" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_markerType" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_className" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_stroke" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_color" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_weight" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_opacity" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_fill" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_fillColor" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_dashArray" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_lineCap" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_lineJoin" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_clickable" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_iconUrl" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_iconSize" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_iconAnchor" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_html" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="_radius" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="fid" desc="" exp=""/>
    <constraint field="no" desc="" exp=""/>
    <constraint field="strike_value" desc="" exp=""/>
    <constraint field="dip_value" desc="" exp=""/>
    <constraint field="remarks" desc="" exp=""/>
    <constraint field="attribute" desc="" exp=""/>
    <constraint field="legend01" desc="" exp=""/>
    <constraint field="legend01e" desc="" exp=""/>
    <constraint field="_markerType" desc="" exp=""/>
    <constraint field="_className" desc="" exp=""/>
    <constraint field="_stroke" desc="" exp=""/>
    <constraint field="_color" desc="" exp=""/>
    <constraint field="_weight" desc="" exp=""/>
    <constraint field="_opacity" desc="" exp=""/>
    <constraint field="_fill" desc="" exp=""/>
    <constraint field="_fillColor" desc="" exp=""/>
    <constraint field="_dashArray" desc="" exp=""/>
    <constraint field="_lineCap" desc="" exp=""/>
    <constraint field="_lineJoin" desc="" exp=""/>
    <constraint field="_clickable" desc="" exp=""/>
    <constraint field="_iconUrl" desc="" exp=""/>
    <constraint field="_iconSize" desc="" exp=""/>
    <constraint field="_iconAnchor" desc="" exp=""/>
    <constraint field="_html" desc="" exp=""/>
    <constraint field="_radius" desc="" exp=""/>
  </constraintExpressions>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="&quot;_iconSize&quot;" actionWidgetStyle="dropDown" sortOrder="1">
    <columns>
      <column width="-1" hidden="1" type="actions"/>
      <column width="-1" hidden="0" name="no" type="field"/>
      <column width="-1" hidden="0" name="dip_value" type="field"/>
      <column width="-1" hidden="0" name="remarks" type="field"/>
      <column width="-1" hidden="0" name="attribute" type="field"/>
      <column width="-1" hidden="0" name="legend01" type="field"/>
      <column width="-1" hidden="0" name="legend01e" type="field"/>
      <column width="-1" hidden="0" name="strike_value" type="field"/>
      <column width="-1" hidden="0" name="_markerType" type="field"/>
      <column width="-1" hidden="0" name="_className" type="field"/>
      <column width="-1" hidden="0" name="_stroke" type="field"/>
      <column width="-1" hidden="0" name="_color" type="field"/>
      <column width="-1" hidden="0" name="_weight" type="field"/>
      <column width="-1" hidden="0" name="_opacity" type="field"/>
      <column width="-1" hidden="0" name="_fill" type="field"/>
      <column width="-1" hidden="0" name="_fillColor" type="field"/>
      <column width="-1" hidden="0" name="_dashArray" type="field"/>
      <column width="-1" hidden="0" name="_lineCap" type="field"/>
      <column width="-1" hidden="0" name="_lineJoin" type="field"/>
      <column width="-1" hidden="0" name="_clickable" type="field"/>
      <column width="118" hidden="0" name="_iconUrl" type="field"/>
      <column width="-1" hidden="0" name="_iconSize" type="field"/>
      <column width="-1" hidden="0" name="_iconAnchor" type="field"/>
      <column width="-1" hidden="0" name="_html" type="field"/>
      <column width="-1" hidden="0" name="_radius" type="field"/>
      <column width="-1" hidden="0" name="fid" type="field"/>
    </columns>
  </attributetableconfig>
  <editform>E:/ProjectFIles/5万分1地質図幅/GSJ_MAP_G050_08084_1998_v02_横須賀ベクトルデータ</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>E:/ProjectFIles/5万分1地質図幅/GSJ_MAP_G050_08084_1998_v02_横須賀ベクトルデータ</editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
フォームが開かれた時に呼び出されるPython関数を使用してフォームにエクストラロジックを追加することができます.
"Python初期化関数"フィールドに関数の名前を入力します.
例は次のとおりです:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="_className" editable="1"/>
    <field name="_clickable" editable="1"/>
    <field name="_color" editable="1"/>
    <field name="_dashArray" editable="1"/>
    <field name="_fill" editable="1"/>
    <field name="_fillColor" editable="1"/>
    <field name="_html" editable="1"/>
    <field name="_iconAnchor" editable="1"/>
    <field name="_iconSize" editable="1"/>
    <field name="_iconUrl" editable="1"/>
    <field name="_lineCap" editable="1"/>
    <field name="_lineJoin" editable="1"/>
    <field name="_markerType" editable="1"/>
    <field name="_opacity" editable="1"/>
    <field name="_radius" editable="1"/>
    <field name="_stroke" editable="1"/>
    <field name="_weight" editable="1"/>
    <field name="attribute" editable="1"/>
    <field name="dip_value" editable="1"/>
    <field name="fid" editable="1"/>
    <field name="legend01" editable="1"/>
    <field name="legend01e" editable="1"/>
    <field name="no" editable="1"/>
    <field name="remarks" editable="1"/>
    <field name="strike_value" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="_className" labelOnTop="0"/>
    <field name="_clickable" labelOnTop="0"/>
    <field name="_color" labelOnTop="0"/>
    <field name="_dashArray" labelOnTop="0"/>
    <field name="_fill" labelOnTop="0"/>
    <field name="_fillColor" labelOnTop="0"/>
    <field name="_html" labelOnTop="0"/>
    <field name="_iconAnchor" labelOnTop="0"/>
    <field name="_iconSize" labelOnTop="0"/>
    <field name="_iconUrl" labelOnTop="0"/>
    <field name="_lineCap" labelOnTop="0"/>
    <field name="_lineJoin" labelOnTop="0"/>
    <field name="_markerType" labelOnTop="0"/>
    <field name="_opacity" labelOnTop="0"/>
    <field name="_radius" labelOnTop="0"/>
    <field name="_stroke" labelOnTop="0"/>
    <field name="_weight" labelOnTop="0"/>
    <field name="attribute" labelOnTop="0"/>
    <field name="dip_value" labelOnTop="0"/>
    <field name="fid" labelOnTop="0"/>
    <field name="legend01" labelOnTop="0"/>
    <field name="legend01e" labelOnTop="0"/>
    <field name="no" labelOnTop="0"/>
    <field name="remarks" labelOnTop="0"/>
    <field name="strike_value" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <expressionfields/>
  <previewExpression>COALESCE("Dip_Value", '&lt;NULL>')</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>

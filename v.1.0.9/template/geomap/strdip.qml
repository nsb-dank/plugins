<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" labelsEnabled="1" simplifyDrawingHints="0" simplifyMaxScale="1" version="3.6.1-Noosa" styleCategories="AllStyleCategories" simplifyAlgorithm="0" maxScale="0" minScale="1e+08" simplifyDrawingTol="1" simplifyLocal="1" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="categorizedSymbol" attr="Attribute" enableorderby="0" symbollevels="1" forceraster="0">
    <categories>
      <category value="1" label="地層の走向・傾斜" render="true" symbol="0"/>
      <category value="2" label="逆転層の走向・傾斜" render="true" symbol="1"/>
      <category value="3" label="垂直層の走向・傾斜" render="true" symbol="2"/>
      <category value="4" label="水平層の走向・傾斜" render="true" symbol="3"/>
      <category value="10" label="走向・傾斜（線構造つき）" render="true" symbol="4"/>
      <category value="99" label="走向線描画用" render="true" symbol="5"/>
      <category value="" label="未定義" render="true" symbol="6"/>
    </categories>
    <symbols>
      <symbol name="0" force_rhr="0" type="marker" alpha="1" clip_to_extent="1">
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="geomap/bedding.svg"/>
          <prop k="offset" v="-0.6000000000000002,-0.60000000000000009"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="255,255,255,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="30"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
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
      <symbol name="1" force_rhr="0" type="marker" alpha="1" clip_to_extent="1">
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="geomap/overturned_bedding.svg"/>
          <prop k="offset" v="-0.60000000000000009,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="255,255,255,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="30"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
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
      <symbol name="2" force_rhr="0" type="marker" alpha="1" clip_to_extent="1">
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="geomap/vertical_bedding.svg"/>
          <prop k="offset" v="-0.60000000000000009,-0.60000000000000009"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="30"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
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
      <symbol name="3" force_rhr="0" type="marker" alpha="1" clip_to_extent="1">
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="geomap/horizontal_bedding.svg"/>
          <prop k="offset" v="-0.60000000000000009,-0.60000000000000009"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="255,255,255,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="30"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
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
      <symbol name="4" force_rhr="0" type="marker" alpha="1" clip_to_extent="1">
        <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="160,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="line"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="1,149,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="15"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="2"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="trend_value" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="231,113,72,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="geomap/bedding.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="30"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
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
      <symbol name="5" force_rhr="0" type="marker" alpha="1" clip_to_extent="1">
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,255,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="geomap/bedding.svg"/>
          <prop k="offset" v="0.10000000000000001,0.10000000000000001"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="30"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
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
        <layer pass="0" locked="0" enabled="1" class="FilledMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="60,204,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="cross_fill"/>
          <prop k="offset" v="0.10000000000000001,0.10000000000000001"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="10"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
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
          <symbol name="@5@1" force_rhr="0" type="fill" alpha="1" clip_to_extent="1">
            <layer pass="0" locked="0" enabled="1" class="SimpleFill">
              <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color" v="60,204,0,255"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="Pixel"/>
              <prop k="outline_color" v="35,35,35,255"/>
              <prop k="outline_style" v="no"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="Pixel"/>
              <prop k="style" v="solid"/>
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
      <symbol name="6" force_rhr="0" type="marker" alpha="1" clip_to_extent="1">
        <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="40,160,108,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="10"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
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
      <symbol name="0" force_rhr="0" type="marker" alpha="1" clip_to_extent="1">
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v=""/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v=""/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v=""/>
          <prop k="offset" v="0.20000000000000001,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer pass="0" locked="0" enabled="1" class="SvgMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="fixedAspectRatio" v="0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v=""/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="0"/>
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
      <text-style fontWordSpacing="0" multilineHeight="1" fontSizeUnit="Point" fieldName="to_int(dip_value)" fontWeight="50" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" textOpacity="1" fontItalic="0" fontFamily="MS UI Gothic" fontCapitals="0" useSubstitutions="0" fontSize="12" previewBkgrdColor="#ffffff" isExpression="1" fontLetterSpacing="0" fontUnderline="0" textColor="14,1,150,255" blendMode="0" namedStyle="Normal">
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferSizeUnits="MM" bufferSize="0.6" bufferOpacity="1" bufferNoFill="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferBlendMode="0"/>
        <background shapeOffsetUnit="MM" shapeBorderWidthUnit="MM" shapeSizeUnit="MM" shapeFillColor="255,255,255,255" shapeOpacity="1" shapeOffsetY="0" shapeSizeY="0" shapeRadiiY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeRadiiX="0" shapeDraw="0" shapeSizeX="0" shapeSizeType="0" shapeJoinStyle="64" shapeRotationType="0" shapeBorderColor="128,128,128,255" shapeBlendMode="0" shapeSVGFile="" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeRadiiUnit="MM" shapeBorderWidth="0"/>
        <shadow shadowDraw="0" shadowUnder="0" shadowOffsetGlobal="1" shadowScale="100" shadowOffsetAngle="135" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowColor="255,255,255,255" shadowRadius="3.5" shadowRadiusUnit="MM" shadowOffsetDist="1" shadowRadiusAlphaOnly="1" shadowOpacity="1" shadowOffsetUnit="MapUnit" shadowBlendMode="0"/>
        <substitutions/>
      </text-style>
      <text-format placeDirectionSymbol="0" addDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" wrapChar="" plussign="0" multilineAlign="0" autoWrapLength="0" leftDirectionSymbol="&lt;" formatNumbers="0" decimals="3" rightDirectionSymbol=">" reverseDirectionSymbol="0"/>
      <placement rotationAngle="0" priority="5" placement="6" offsetUnits="MapUnit" maxCurvedCharAngleIn="25" distMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-25" repeatDistance="0" dist="0" placementFlags="10" distUnits="Pixel" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidInside="0" xOffset="3" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" yOffset="-3" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" quadOffset="4" repeatDistanceUnits="MM" offsetType="0" fitInPolygonOnly="0" centroidWhole="0"/>
      <rendering scaleMin="1" mergeLines="0" labelPerPart="0" minFeatureSize="0" obstacle="1" upsidedownLabels="0" fontMinPixelSize="3" scaleVisibility="0" maxNumLabels="2000" scaleMax="10000000" obstacleType="0" drawLabels="1" fontMaxPixelSize="10000" obstacleFactor="1" limitNumLabels="0" fontLimitPixelSize="0" zIndex="0" displayAll="0"/>
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
    <property key="dualview/previewExpressions">
      <value>COALESCE("Dip_Value", '&lt;NULL>')</value>
    </property>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory lineSizeType="MM" height="15" rotationOffset="270" opacity="1" penColor="#000000" diagramOrientation="Up" barWidth="5" sizeScale="3x:0,0,0,0,0,0" maxScaleDenominator="1e+08" sizeType="MM" enabled="0" penWidth="0" width="15" penAlpha="255" backgroundColor="#ffffff" scaleDependency="Area" labelPlacementMethod="XHeight" backgroundAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" scaleBasedVisibility="0" minimumSize="0" minScaleDenominator="0">
      <fontProperties description="MS UI Gothic,9,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" label="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="2" zIndex="0" showAll="1" placement="0" obstacle="0" dist="0" priority="0">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
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
    <field name="attribute">
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
    <field name="trend_value">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="plunge_value">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="rake_value">
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
    <alias field="fid" name="" index="0"/>
    <alias field="no" name="" index="1"/>
    <alias field="attribute" name="" index="2"/>
    <alias field="strike_value" name="" index="3"/>
    <alias field="dip_value" name="" index="4"/>
    <alias field="trend_value" name="" index="5"/>
    <alias field="plunge_value" name="" index="6"/>
    <alias field="rake_value" name="" index="7"/>
    <alias field="remarks" name="" index="8"/>
    <alias field="legend01" name="" index="9"/>
    <alias field="legend01e" name="" index="10"/>
    <alias field="_markerType" name="" index="11"/>
    <alias field="_className" name="" index="12"/>
    <alias field="_stroke" name="" index="13"/>
    <alias field="_color" name="" index="14"/>
    <alias field="_weight" name="" index="15"/>
    <alias field="_opacity" name="" index="16"/>
    <alias field="_fill" name="" index="17"/>
    <alias field="_fillColor" name="" index="18"/>
    <alias field="_dashArray" name="" index="19"/>
    <alias field="_lineCap" name="" index="20"/>
    <alias field="_lineJoin" name="" index="21"/>
    <alias field="_clickable" name="" index="22"/>
    <alias field="_iconUrl" name="" index="23"/>
    <alias field="_iconSize" name="" index="24"/>
    <alias field="_iconAnchor" name="" index="25"/>
    <alias field="_html" name="" index="26"/>
    <alias field="_radius" name="" index="27"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="fid" expression="" applyOnUpdate="0"/>
    <default field="no" expression="" applyOnUpdate="0"/>
    <default field="attribute" expression="" applyOnUpdate="0"/>
    <default field="strike_value" expression="" applyOnUpdate="0"/>
    <default field="dip_value" expression="" applyOnUpdate="0"/>
    <default field="trend_value" expression="" applyOnUpdate="0"/>
    <default field="plunge_value" expression="" applyOnUpdate="0"/>
    <default field="rake_value" expression="" applyOnUpdate="0"/>
    <default field="remarks" expression="" applyOnUpdate="0"/>
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
    <constraint field="attribute" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="strike_value" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="dip_value" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="trend_value" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="plunge_value" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="rake_value" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="remarks" exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0"/>
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
    <constraint field="attribute" desc="" exp=""/>
    <constraint field="strike_value" desc="" exp=""/>
    <constraint field="dip_value" desc="" exp=""/>
    <constraint field="trend_value" desc="" exp=""/>
    <constraint field="plunge_value" desc="" exp=""/>
    <constraint field="rake_value" desc="" exp=""/>
    <constraint field="remarks" desc="" exp=""/>
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
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="&quot;_iconSize&quot;" actionWidgetStyle="dropDown" sortOrder="1">
    <columns>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" name="no" type="field" hidden="0"/>
      <column width="-1" name="dip_value" type="field" hidden="0"/>
      <column width="-1" name="remarks" type="field" hidden="0"/>
      <column width="-1" name="attribute" type="field" hidden="0"/>
      <column width="-1" name="legend01" type="field" hidden="0"/>
      <column width="-1" name="legend01e" type="field" hidden="0"/>
      <column width="-1" name="strike_value" type="field" hidden="0"/>
      <column width="-1" name="_markerType" type="field" hidden="0"/>
      <column width="-1" name="_className" type="field" hidden="0"/>
      <column width="-1" name="_stroke" type="field" hidden="0"/>
      <column width="-1" name="_color" type="field" hidden="0"/>
      <column width="-1" name="_weight" type="field" hidden="0"/>
      <column width="-1" name="_opacity" type="field" hidden="0"/>
      <column width="-1" name="_fill" type="field" hidden="0"/>
      <column width="-1" name="_fillColor" type="field" hidden="0"/>
      <column width="-1" name="_dashArray" type="field" hidden="0"/>
      <column width="-1" name="_lineCap" type="field" hidden="0"/>
      <column width="-1" name="_lineJoin" type="field" hidden="0"/>
      <column width="-1" name="_clickable" type="field" hidden="0"/>
      <column width="118" name="_iconUrl" type="field" hidden="0"/>
      <column width="-1" name="_iconSize" type="field" hidden="0"/>
      <column width="-1" name="_iconAnchor" type="field" hidden="0"/>
      <column width="-1" name="_html" type="field" hidden="0"/>
      <column width="-1" name="_radius" type="field" hidden="0"/>
      <column width="-1" name="fid" type="field" hidden="0"/>
      <column width="-1" name="trend_value" type="field" hidden="0"/>
      <column width="-1" name="plunge_value" type="field" hidden="0"/>
      <column width="-1" name="rake_value" type="field" hidden="0"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
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
    <field name="plunge_value" editable="1"/>
    <field name="rake_value" editable="1"/>
    <field name="remarks" editable="1"/>
    <field name="strike_value" editable="1"/>
    <field name="trend_value" editable="1"/>
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
    <field name="plunge_value" labelOnTop="0"/>
    <field name="rake_value" labelOnTop="0"/>
    <field name="remarks" labelOnTop="0"/>
    <field name="strike_value" labelOnTop="0"/>
    <field name="trend_value" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>COALESCE("Dip_Value", '&lt;NULL>')</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>

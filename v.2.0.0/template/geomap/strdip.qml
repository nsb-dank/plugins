<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="1" simplifyDrawingHints="0" readOnly="0" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" simplifyLocal="1" simplifyMaxScale="1" minScale="100000000" maxScale="0" simplifyAlgorithm="0" version="3.18.3-Zürich">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal mode="0" durationField="" durationUnit="min" enabled="0" startField="" startExpression="" accumulate="0" endField="" endExpression="" fixedDuration="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 symbollevels="1" attr="Attribute" type="categorizedSymbol" enableorderby="0" forceraster="0">
    <categories>
      <category value="1" label="地層の走向・傾斜" symbol="0" render="true"/>
      <category value="2" label="逆転層の走向・傾斜" symbol="1" render="true"/>
      <category value="3" label="垂直層の走向・傾斜" symbol="2" render="true"/>
      <category value="4" label="水平層の走向・傾斜" symbol="3" render="true"/>
      <category value="10" label="走向・傾斜（線構造つき）" symbol="4" render="true"/>
      <category value="99" label="走向線描画用" symbol="5" render="true"/>
      <category value="" label="未定義" symbol="6" render="true"/>
    </categories>
    <symbols>
      <symbol force_rhr="0" type="marker" clip_to_extent="1" name="0" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="0,0,0,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="C:/Users/ykara/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/geolib3/template/svg/geomap/bedding.svg" type="QString" name="name"/>
            <Option value="-0.6000000000000002,-0.60000000000000009" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="offset_unit"/>
            <Option value="255,255,255,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="30" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="C:/Users/ykara/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/geolib3/template/svg/geomap/bedding.svg" k="name"/>
          <prop v="-0.6000000000000002,-0.60000000000000009" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="255,255,255,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="strike_value" type="QString" name="field"/>
                  <Option value="2" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" clip_to_extent="1" name="1" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="0,0,0,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0ib3ZlcnR1cm5lZF9iZWRkaW5nLnN2ZyI+CiAgPGRlZnMKICAgICBpZD0iZGVmczE0IiAvPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBpZD0iYmFzZSIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VvcGFjaXR5PSIwLjAiCiAgICAgaW5rc2NhcGU6cGFnZXNoYWRvdz0iMiIKICAgICBpbmtzY2FwZTp6b29tPSIwLjk0MjM2MzMyIgogICAgIGlua3NjYXBlOmN4PSIyMi41Njg0NDciCiAgICAgaW5rc2NhcGU6Y3k9IjI1LjU4ODc2OCIKICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0icHgiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ibGF5ZXIxIgogICAgIHNob3dncmlkPSJ0cnVlIgogICAgIHVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSJ0cnVlIgogICAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtbWlkcG9pbnRzPSJmYWxzZSIKICAgICBpbmtzY2FwZTpzbmFwLWNlbnRlcj0idHJ1ZSIKICAgICBpbmtzY2FwZTpzbmFwLWdyaWRzPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtdG8tZ3VpZGVzPSJ0cnVlIgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMTY4MCIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMDI3IgogICAgIGlua3NjYXBlOndpbmRvdy14PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3cteT0iLTgiCiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgICBpbmtzY2FwZTpzbmFwLW90aGVycz0iZmFsc2UiCiAgICAgaW5rc2NhcGU6c25hcC1ub2Rlcz0iZmFsc2UiCiAgICAgaW5rc2NhcGU6c25hcC1nbG9iYWw9ImZhbHNlIj4KICAgIDxpbmtzY2FwZTpncmlkCiAgICAgICB0eXBlPSJ4eWdyaWQiCiAgICAgICBpZD0iZ3JpZDMyIiAvPgogIDwvc29kaXBvZGk6bmFtZWR2aWV3PgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTE3Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZwogICAgIGlua3NjYXBlOmxhYmVsPSLjg6zjgqTjg6Tjg7wgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwtMjgwLjA2NjY1KSIKICAgICBzdHlsZT0iZGlzcGxheTppbmxpbmUiPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MjgiCiAgICAgICB3aWR0aD0iMC43OTM3NDk4NyIKICAgICAgIGhlaWdodD0iMTYuOTMzMzIxIgogICAgICAgeD0iNy45Mzc1IgogICAgICAgeT0iMjgwLjA2NjY1IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjI1OTIzNzcxIiAvPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MzAiCiAgICAgICB3aWR0aD0iMy45Njg3NTAyIgogICAgICAgaGVpZ2h0PSIwLjc5Mzc0NTU4IgogICAgICAgeD0iOC43MzEyNDk4IgogICAgICAgeT0iMjg4LjEzNjQ0IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjM5Njg3MzkyIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJkaXNwbGF5OmlubGluZTtzdHJva2Utd2lkdGg6MC43NjA0MjA1NiIKICAgICAgIGQ9Ik0gMjkuOTkyMTg4IDMwLjUgQSA4LjUwMDI0MjQgNy40OTk4ODk1IDAgMCAwIDIyLjYyNSAzNC4yNDgwNDcgQSA4LjUwMDI0MjQgNy40OTk4ODk1IDAgMCAwIDIyLjYyNjk1MyA0MS43NTE5NTMgQSA4LjUwMDI0MjQgNy40OTk4ODk1IDAgMCAwIDI5Ljk5MjE4OCA0NS41IEwgMjkuOTkyMTg4IDMwLjUgeiBNIDI5Ljk0MTQwNiAzMy40MzU1NDcgTCAyOS45NTMxMjUgNDIuNDM1NTQ3IEEgNS4yNzk0MjQ5IDQuNTAwMzc1OSAwLjAyMTc1MTYyNCAwIDEgMjQuNjk5MjE5IDM3LjkzOTQ1MyBBIDUuMjc5NDI0OSA0LjUwMDM3NTkgMC4wMjE3NTE2MjQgMCAxIDI5Ljk0MTQwNiAzMy40MzU1NDcgeiAiCiAgICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI2NDU4MzM0LDAsMCwwLjI2NDU4MzM0LDAsMjgwLjA2NjY1KSIKICAgICAgIGlkPSJwYXRoMzcxNS0xIiAvPgogIDwvZz4KPC9zdmc+Cg==" type="QString" name="name"/>
            <Option value="-0.60000000000000009,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="offset_unit"/>
            <Option value="255,255,255,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="30" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0ib3ZlcnR1cm5lZF9iZWRkaW5nLnN2ZyI+CiAgPGRlZnMKICAgICBpZD0iZGVmczE0IiAvPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBpZD0iYmFzZSIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VvcGFjaXR5PSIwLjAiCiAgICAgaW5rc2NhcGU6cGFnZXNoYWRvdz0iMiIKICAgICBpbmtzY2FwZTp6b29tPSIwLjk0MjM2MzMyIgogICAgIGlua3NjYXBlOmN4PSIyMi41Njg0NDciCiAgICAgaW5rc2NhcGU6Y3k9IjI1LjU4ODc2OCIKICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0icHgiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ibGF5ZXIxIgogICAgIHNob3dncmlkPSJ0cnVlIgogICAgIHVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSJ0cnVlIgogICAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtbWlkcG9pbnRzPSJmYWxzZSIKICAgICBpbmtzY2FwZTpzbmFwLWNlbnRlcj0idHJ1ZSIKICAgICBpbmtzY2FwZTpzbmFwLWdyaWRzPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtdG8tZ3VpZGVzPSJ0cnVlIgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMTY4MCIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMDI3IgogICAgIGlua3NjYXBlOndpbmRvdy14PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3cteT0iLTgiCiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgICBpbmtzY2FwZTpzbmFwLW90aGVycz0iZmFsc2UiCiAgICAgaW5rc2NhcGU6c25hcC1ub2Rlcz0iZmFsc2UiCiAgICAgaW5rc2NhcGU6c25hcC1nbG9iYWw9ImZhbHNlIj4KICAgIDxpbmtzY2FwZTpncmlkCiAgICAgICB0eXBlPSJ4eWdyaWQiCiAgICAgICBpZD0iZ3JpZDMyIiAvPgogIDwvc29kaXBvZGk6bmFtZWR2aWV3PgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTE3Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZwogICAgIGlua3NjYXBlOmxhYmVsPSLjg6zjgqTjg6Tjg7wgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwtMjgwLjA2NjY1KSIKICAgICBzdHlsZT0iZGlzcGxheTppbmxpbmUiPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MjgiCiAgICAgICB3aWR0aD0iMC43OTM3NDk4NyIKICAgICAgIGhlaWdodD0iMTYuOTMzMzIxIgogICAgICAgeD0iNy45Mzc1IgogICAgICAgeT0iMjgwLjA2NjY1IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjI1OTIzNzcxIiAvPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MzAiCiAgICAgICB3aWR0aD0iMy45Njg3NTAyIgogICAgICAgaGVpZ2h0PSIwLjc5Mzc0NTU4IgogICAgICAgeD0iOC43MzEyNDk4IgogICAgICAgeT0iMjg4LjEzNjQ0IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjM5Njg3MzkyIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJkaXNwbGF5OmlubGluZTtzdHJva2Utd2lkdGg6MC43NjA0MjA1NiIKICAgICAgIGQ9Ik0gMjkuOTkyMTg4IDMwLjUgQSA4LjUwMDI0MjQgNy40OTk4ODk1IDAgMCAwIDIyLjYyNSAzNC4yNDgwNDcgQSA4LjUwMDI0MjQgNy40OTk4ODk1IDAgMCAwIDIyLjYyNjk1MyA0MS43NTE5NTMgQSA4LjUwMDI0MjQgNy40OTk4ODk1IDAgMCAwIDI5Ljk5MjE4OCA0NS41IEwgMjkuOTkyMTg4IDMwLjUgeiBNIDI5Ljk0MTQwNiAzMy40MzU1NDcgTCAyOS45NTMxMjUgNDIuNDM1NTQ3IEEgNS4yNzk0MjQ5IDQuNTAwMzc1OSAwLjAyMTc1MTYyNCAwIDEgMjQuNjk5MjE5IDM3LjkzOTQ1MyBBIDUuMjc5NDI0OSA0LjUwMDM3NTkgMC4wMjE3NTE2MjQgMCAxIDI5Ljk0MTQwNiAzMy40MzU1NDcgeiAiCiAgICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjI2NDU4MzM0LDAsMCwwLjI2NDU4MzM0LDAsMjgwLjA2NjY1KSIKICAgICAgIGlkPSJwYXRoMzcxNS0xIiAvPgogIDwvZz4KPC9zdmc+Cg==" k="name"/>
          <prop v="-0.60000000000000009,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="255,255,255,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="strike_value" type="QString" name="field"/>
                  <Option value="2" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" clip_to_extent="1" name="2" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="0,0,0,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0idmVydGljYWxfYmVkZGluZy5zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxNCIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9ImJhc2UiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6em9vbT0iOS45MjQ3NTM4IgogICAgIGlua3NjYXBlOmN4PSIyMi41Njg0NDciCiAgICAgaW5rc2NhcGU6Y3k9IjI1LjU4ODc2OCIKICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0icHgiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ibGF5ZXIxIgogICAgIHNob3dncmlkPSJ0cnVlIgogICAgIHVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSJ0cnVlIgogICAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtbWlkcG9pbnRzPSJmYWxzZSIKICAgICBpbmtzY2FwZTpzbmFwLWNlbnRlcj0idHJ1ZSIKICAgICBpbmtzY2FwZTpzbmFwLWdyaWRzPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtdG8tZ3VpZGVzPSJ0cnVlIgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMTY4MCIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMDI3IgogICAgIGlua3NjYXBlOndpbmRvdy14PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3cteT0iLTgiCiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgICBpbmtzY2FwZTpzbmFwLW90aGVycz0iZmFsc2UiCiAgICAgaW5rc2NhcGU6c25hcC1ub2Rlcz0iZmFsc2UiCiAgICAgaW5rc2NhcGU6c25hcC1nbG9iYWw9ImZhbHNlIj4KICAgIDxpbmtzY2FwZTpncmlkCiAgICAgICB0eXBlPSJ4eWdyaWQiCiAgICAgICBpZD0iZ3JpZDMyIiAvPgogIDwvc29kaXBvZGk6bmFtZWR2aWV3PgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTE3Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZwogICAgIGlua3NjYXBlOmxhYmVsPSLjg6zjgqTjg6Tjg7wgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwtMjgwLjA2NjY1KSIKICAgICBzdHlsZT0iZGlzcGxheTppbmxpbmUiPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MjgiCiAgICAgICB3aWR0aD0iMC43OTM3NDk4NyIKICAgICAgIGhlaWdodD0iMTYuOTMzMzIxIgogICAgICAgeD0iNy45Mzc1IgogICAgICAgeT0iMjgwLjA2NjY1IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjI1OTIzNzcxIiAvPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MzAiCiAgICAgICB3aWR0aD0iOC4xNTQyMDI1IgogICAgICAgaGVpZ2h0PSIwLjc5Mzc0NTU4IgogICAgICAgeD0iNC4yNzkyMDgyIgogICAgICAgeT0iMjg4LjEzNjQ0IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjU2ODg3NDQyIiAvPgogIDwvZz4KPC9zdmc+Cg==" type="QString" name="name"/>
            <Option value="-0.60000000000000009,-0.60000000000000009" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="offset_unit"/>
            <Option value="0,0,0,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="30" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0idmVydGljYWxfYmVkZGluZy5zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxNCIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9ImJhc2UiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6em9vbT0iOS45MjQ3NTM4IgogICAgIGlua3NjYXBlOmN4PSIyMi41Njg0NDciCiAgICAgaW5rc2NhcGU6Y3k9IjI1LjU4ODc2OCIKICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0icHgiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ibGF5ZXIxIgogICAgIHNob3dncmlkPSJ0cnVlIgogICAgIHVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSJ0cnVlIgogICAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtbWlkcG9pbnRzPSJmYWxzZSIKICAgICBpbmtzY2FwZTpzbmFwLWNlbnRlcj0idHJ1ZSIKICAgICBpbmtzY2FwZTpzbmFwLWdyaWRzPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtdG8tZ3VpZGVzPSJ0cnVlIgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMTY4MCIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMDI3IgogICAgIGlua3NjYXBlOndpbmRvdy14PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3cteT0iLTgiCiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgICBpbmtzY2FwZTpzbmFwLW90aGVycz0iZmFsc2UiCiAgICAgaW5rc2NhcGU6c25hcC1ub2Rlcz0iZmFsc2UiCiAgICAgaW5rc2NhcGU6c25hcC1nbG9iYWw9ImZhbHNlIj4KICAgIDxpbmtzY2FwZTpncmlkCiAgICAgICB0eXBlPSJ4eWdyaWQiCiAgICAgICBpZD0iZ3JpZDMyIiAvPgogIDwvc29kaXBvZGk6bmFtZWR2aWV3PgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTE3Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZwogICAgIGlua3NjYXBlOmxhYmVsPSLjg6zjgqTjg6Tjg7wgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwtMjgwLjA2NjY1KSIKICAgICBzdHlsZT0iZGlzcGxheTppbmxpbmUiPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MjgiCiAgICAgICB3aWR0aD0iMC43OTM3NDk4NyIKICAgICAgIGhlaWdodD0iMTYuOTMzMzIxIgogICAgICAgeD0iNy45Mzc1IgogICAgICAgeT0iMjgwLjA2NjY1IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjI1OTIzNzcxIiAvPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MzAiCiAgICAgICB3aWR0aD0iOC4xNTQyMDI1IgogICAgICAgaGVpZ2h0PSIwLjc5Mzc0NTU4IgogICAgICAgeD0iNC4yNzkyMDgyIgogICAgICAgeT0iMjg4LjEzNjQ0IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjU2ODg3NDQyIiAvPgogIDwvZz4KPC9zdmc+Cg==" k="name"/>
          <prop v="-0.60000000000000009,-0.60000000000000009" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="strike_value" type="QString" name="field"/>
                  <Option value="2" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" clip_to_extent="1" name="3" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="0,0,0,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0iaG9yaXpvbnRhbF9iZWRkaW5nLnN2ZyI+CiAgPGRlZnMKICAgICBpZD0iZGVmczE0IiAvPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBpZD0iYmFzZSIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VvcGFjaXR5PSIwLjAiCiAgICAgaW5rc2NhcGU6cGFnZXNoYWRvdz0iMiIKICAgICBpbmtzY2FwZTp6b29tPSI5LjkyNDc1MzgiCiAgICAgaW5rc2NhcGU6Y3g9IjIyLjU2ODQ0NyIKICAgICBpbmtzY2FwZTpjeT0iMjUuNTg4NzY4IgogICAgIGlua3NjYXBlOmRvY3VtZW50LXVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJsYXllcjEiCiAgICAgc2hvd2dyaWQ9InRydWUiCiAgICAgdW5pdHM9InB4IgogICAgIGlua3NjYXBlOnBhZ2VjaGVja2VyYm9hcmQ9InRydWUiCiAgICAgaW5rc2NhcGU6c2hvd3BhZ2VzaGFkb3c9InRydWUiCiAgICAgaW5rc2NhcGU6c25hcC1taWRwb2ludHM9ImZhbHNlIgogICAgIGlua3NjYXBlOnNuYXAtY2VudGVyPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtZ3JpZHM9InRydWUiCiAgICAgaW5rc2NhcGU6c25hcC10by1ndWlkZXM9InRydWUiCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxNjgwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjEwMjciCiAgICAgaW5rc2NhcGU6d2luZG93LXg9Ii04IgogICAgIGlua3NjYXBlOndpbmRvdy15PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIgogICAgIGlua3NjYXBlOnNuYXAtb3RoZXJzPSJmYWxzZSIKICAgICBpbmtzY2FwZTpzbmFwLW5vZGVzPSJmYWxzZSIKICAgICBpbmtzY2FwZTpzbmFwLWdsb2JhbD0iZmFsc2UiPgogICAgPGlua3NjYXBlOmdyaWQKICAgICAgIHR5cGU9Inh5Z3JpZCIKICAgICAgIGlkPSJncmlkMzIiIC8+CiAgPC9zb2RpcG9kaTpuYW1lZHZpZXc+CiAgPG1ldGFkYXRhCiAgICAgaWQ9Im1ldGFkYXRhMTciPgogICAgPHJkZjpSREY+CiAgICAgIDxjYzpXb3JrCiAgICAgICAgIHJkZjphYm91dD0iIj4KICAgICAgICA8ZGM6Zm9ybWF0PmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdD4KICAgICAgICA8ZGM6dHlwZQogICAgICAgICAgIHJkZjpyZXNvdXJjZT0iaHR0cDovL3B1cmwub3JnL2RjL2RjbWl0eXBlL1N0aWxsSW1hZ2UiIC8+CiAgICAgICAgPGRjOnRpdGxlPjwvZGM6dGl0bGU+CiAgICAgIDwvY2M6V29yaz4KICAgIDwvcmRmOlJERj4KICA8L21ldGFkYXRhPgogIDxnCiAgICAgaW5rc2NhcGU6bGFiZWw9IuODrOOCpOODpOODvCAxIgogICAgIGlua3NjYXBlOmdyb3VwbW9kZT0ibGF5ZXIiCiAgICAgaWQ9ImxheWVyMSIKICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLC0yODAuMDY2NjUpIgogICAgIHN0eWxlPSJkaXNwbGF5OmlubGluZSI+CiAgICA8cmVjdAogICAgICAgaWQ9InJlY3QyOCIKICAgICAgIHdpZHRoPSIwLjc5Mzc0OTg3IgogICAgICAgaGVpZ2h0PSIxNi45MzMzMjEiCiAgICAgICB4PSI3LjkzNzUiCiAgICAgICB5PSIyODAuMDY2NjUiCiAgICAgICBzdHlsZT0ic3Ryb2tlLXdpZHRoOjAuMjU5MjM3NzEiIC8+CiAgICA8cmVjdAogICAgICAgaWQ9InJlY3QzMCIKICAgICAgIHdpZHRoPSIxNi44NDUwMTUiCiAgICAgICBoZWlnaHQ9IjAuNzkzNzQ1NTgiCiAgICAgICB4PSIwLjA2NzA5NjkzNCIKICAgICAgIHk9IjI4OC4xMzY0NCIKICAgICAgIHN0eWxlPSJzdHJva2Utd2lkdGg6MC44MTc2Mzg1MiIgLz4KICA8L2c+Cjwvc3ZnPgo=" type="QString" name="name"/>
            <Option value="-0.60000000000000009,-0.60000000000000009" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="offset_unit"/>
            <Option value="255,255,255,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="30" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0iaG9yaXpvbnRhbF9iZWRkaW5nLnN2ZyI+CiAgPGRlZnMKICAgICBpZD0iZGVmczE0IiAvPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBpZD0iYmFzZSIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VvcGFjaXR5PSIwLjAiCiAgICAgaW5rc2NhcGU6cGFnZXNoYWRvdz0iMiIKICAgICBpbmtzY2FwZTp6b29tPSI5LjkyNDc1MzgiCiAgICAgaW5rc2NhcGU6Y3g9IjIyLjU2ODQ0NyIKICAgICBpbmtzY2FwZTpjeT0iMjUuNTg4NzY4IgogICAgIGlua3NjYXBlOmRvY3VtZW50LXVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJsYXllcjEiCiAgICAgc2hvd2dyaWQ9InRydWUiCiAgICAgdW5pdHM9InB4IgogICAgIGlua3NjYXBlOnBhZ2VjaGVja2VyYm9hcmQ9InRydWUiCiAgICAgaW5rc2NhcGU6c2hvd3BhZ2VzaGFkb3c9InRydWUiCiAgICAgaW5rc2NhcGU6c25hcC1taWRwb2ludHM9ImZhbHNlIgogICAgIGlua3NjYXBlOnNuYXAtY2VudGVyPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtZ3JpZHM9InRydWUiCiAgICAgaW5rc2NhcGU6c25hcC10by1ndWlkZXM9InRydWUiCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxNjgwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjEwMjciCiAgICAgaW5rc2NhcGU6d2luZG93LXg9Ii04IgogICAgIGlua3NjYXBlOndpbmRvdy15PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIgogICAgIGlua3NjYXBlOnNuYXAtb3RoZXJzPSJmYWxzZSIKICAgICBpbmtzY2FwZTpzbmFwLW5vZGVzPSJmYWxzZSIKICAgICBpbmtzY2FwZTpzbmFwLWdsb2JhbD0iZmFsc2UiPgogICAgPGlua3NjYXBlOmdyaWQKICAgICAgIHR5cGU9Inh5Z3JpZCIKICAgICAgIGlkPSJncmlkMzIiIC8+CiAgPC9zb2RpcG9kaTpuYW1lZHZpZXc+CiAgPG1ldGFkYXRhCiAgICAgaWQ9Im1ldGFkYXRhMTciPgogICAgPHJkZjpSREY+CiAgICAgIDxjYzpXb3JrCiAgICAgICAgIHJkZjphYm91dD0iIj4KICAgICAgICA8ZGM6Zm9ybWF0PmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdD4KICAgICAgICA8ZGM6dHlwZQogICAgICAgICAgIHJkZjpyZXNvdXJjZT0iaHR0cDovL3B1cmwub3JnL2RjL2RjbWl0eXBlL1N0aWxsSW1hZ2UiIC8+CiAgICAgICAgPGRjOnRpdGxlPjwvZGM6dGl0bGU+CiAgICAgIDwvY2M6V29yaz4KICAgIDwvcmRmOlJERj4KICA8L21ldGFkYXRhPgogIDxnCiAgICAgaW5rc2NhcGU6bGFiZWw9IuODrOOCpOODpOODvCAxIgogICAgIGlua3NjYXBlOmdyb3VwbW9kZT0ibGF5ZXIiCiAgICAgaWQ9ImxheWVyMSIKICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLC0yODAuMDY2NjUpIgogICAgIHN0eWxlPSJkaXNwbGF5OmlubGluZSI+CiAgICA8cmVjdAogICAgICAgaWQ9InJlY3QyOCIKICAgICAgIHdpZHRoPSIwLjc5Mzc0OTg3IgogICAgICAgaGVpZ2h0PSIxNi45MzMzMjEiCiAgICAgICB4PSI3LjkzNzUiCiAgICAgICB5PSIyODAuMDY2NjUiCiAgICAgICBzdHlsZT0ic3Ryb2tlLXdpZHRoOjAuMjU5MjM3NzEiIC8+CiAgICA8cmVjdAogICAgICAgaWQ9InJlY3QzMCIKICAgICAgIHdpZHRoPSIxNi44NDUwMTUiCiAgICAgICBoZWlnaHQ9IjAuNzkzNzQ1NTgiCiAgICAgICB4PSIwLjA2NzA5NjkzNCIKICAgICAgIHk9IjI4OC4xMzY0NCIKICAgICAgIHN0eWxlPSJzdHJva2Utd2lkdGg6MC44MTc2Mzg1MiIgLz4KICA8L2c+Cjwvc3ZnPgo=" k="name"/>
          <prop v="-0.60000000000000009,-0.60000000000000009" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="255,255,255,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="strike_value" type="QString" name="field"/>
                  <Option value="2" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" clip_to_extent="1" name="4" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="160,0,0,255" type="QString" name="color"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="line" type="QString" name="name"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="1,149,255,255" type="QString" name="outline_color"/>
            <Option value="solid" type="QString" name="outline_style"/>
            <Option value="1.4" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="outline_width_unit"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="15" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="size_unit"/>
            <Option value="2" type="QString" name="vertical_anchor_point"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="160,0,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="line" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="1,149,255,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="15" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="2" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="trend_value" type="QString" name="field"/>
                  <Option value="2" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="231,113,72,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0iYmVkZGluZy5zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxNCIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9ImJhc2UiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6em9vbT0iOCIKICAgICBpbmtzY2FwZTpjeD0iMjIuNTY4NDQ3IgogICAgIGlua3NjYXBlOmN5PSI0OSIKICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0icHgiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ibGF5ZXIxIgogICAgIHNob3dncmlkPSJ0cnVlIgogICAgIHVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSJ0cnVlIgogICAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtbWlkcG9pbnRzPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtY2VudGVyPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtZ3JpZHM9InRydWUiCiAgICAgaW5rc2NhcGU6c25hcC10by1ndWlkZXM9InRydWUiCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxNjgwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjEwMjciCiAgICAgaW5rc2NhcGU6d2luZG93LXg9Ii04IgogICAgIGlua3NjYXBlOndpbmRvdy15PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIj4KICAgIDxpbmtzY2FwZTpncmlkCiAgICAgICB0eXBlPSJ4eWdyaWQiCiAgICAgICBpZD0iZ3JpZDMyIiAvPgogIDwvc29kaXBvZGk6bmFtZWR2aWV3PgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTE3Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZwogICAgIGlua3NjYXBlOmxhYmVsPSLjg6zjgqTjg6Tjg7wgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwtMjgwLjA2NjY1KSIKICAgICBzdHlsZT0iZGlzcGxheTppbmxpbmUiPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MjgiCiAgICAgICB3aWR0aD0iMC43OTM3NDk4NyIKICAgICAgIGhlaWdodD0iMTYuOTMzMzIxIgogICAgICAgeD0iNy45Mzc1IgogICAgICAgeT0iMjgwLjA2NjY1IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjI1OTIzNzcxIiAvPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MzAiCiAgICAgICB3aWR0aD0iMy45Njg3NTAyIgogICAgICAgaGVpZ2h0PSIwLjc5Mzc0NTU4IgogICAgICAgeD0iOC43MzEyNDk4IgogICAgICAgeT0iMjg4LjEzNjQ0IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjM5Njg3MzkyIiAvPgogIDwvZz4KPC9zdmc+Cg==" type="QString" name="name"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="35,35,35,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="30" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="231,113,72,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0iYmVkZGluZy5zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxNCIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9ImJhc2UiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6em9vbT0iOCIKICAgICBpbmtzY2FwZTpjeD0iMjIuNTY4NDQ3IgogICAgIGlua3NjYXBlOmN5PSI0OSIKICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0icHgiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ibGF5ZXIxIgogICAgIHNob3dncmlkPSJ0cnVlIgogICAgIHVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSJ0cnVlIgogICAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtbWlkcG9pbnRzPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtY2VudGVyPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtZ3JpZHM9InRydWUiCiAgICAgaW5rc2NhcGU6c25hcC10by1ndWlkZXM9InRydWUiCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxNjgwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjEwMjciCiAgICAgaW5rc2NhcGU6d2luZG93LXg9Ii04IgogICAgIGlua3NjYXBlOndpbmRvdy15PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIj4KICAgIDxpbmtzY2FwZTpncmlkCiAgICAgICB0eXBlPSJ4eWdyaWQiCiAgICAgICBpZD0iZ3JpZDMyIiAvPgogIDwvc29kaXBvZGk6bmFtZWR2aWV3PgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTE3Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZwogICAgIGlua3NjYXBlOmxhYmVsPSLjg6zjgqTjg6Tjg7wgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwtMjgwLjA2NjY1KSIKICAgICBzdHlsZT0iZGlzcGxheTppbmxpbmUiPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MjgiCiAgICAgICB3aWR0aD0iMC43OTM3NDk4NyIKICAgICAgIGhlaWdodD0iMTYuOTMzMzIxIgogICAgICAgeD0iNy45Mzc1IgogICAgICAgeT0iMjgwLjA2NjY1IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjI1OTIzNzcxIiAvPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MzAiCiAgICAgICB3aWR0aD0iMy45Njg3NTAyIgogICAgICAgaGVpZ2h0PSIwLjc5Mzc0NTU4IgogICAgICAgeD0iOC43MzEyNDk4IgogICAgICAgeT0iMjg4LjEzNjQ0IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjM5Njg3MzkyIiAvPgogIDwvZz4KPC9zdmc+Cg==" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="strike_value" type="QString" name="field"/>
                  <Option value="2" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" clip_to_extent="1" name="5" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="0,0,255,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0iYmVkZGluZy5zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxNCIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9ImJhc2UiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6em9vbT0iOCIKICAgICBpbmtzY2FwZTpjeD0iMjIuNTY4NDQ3IgogICAgIGlua3NjYXBlOmN5PSI0OSIKICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0icHgiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ibGF5ZXIxIgogICAgIHNob3dncmlkPSJ0cnVlIgogICAgIHVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSJ0cnVlIgogICAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtbWlkcG9pbnRzPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtY2VudGVyPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtZ3JpZHM9InRydWUiCiAgICAgaW5rc2NhcGU6c25hcC10by1ndWlkZXM9InRydWUiCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxNjgwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjEwMjciCiAgICAgaW5rc2NhcGU6d2luZG93LXg9Ii04IgogICAgIGlua3NjYXBlOndpbmRvdy15PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIj4KICAgIDxpbmtzY2FwZTpncmlkCiAgICAgICB0eXBlPSJ4eWdyaWQiCiAgICAgICBpZD0iZ3JpZDMyIiAvPgogIDwvc29kaXBvZGk6bmFtZWR2aWV3PgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTE3Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZwogICAgIGlua3NjYXBlOmxhYmVsPSLjg6zjgqTjg6Tjg7wgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwtMjgwLjA2NjY1KSIKICAgICBzdHlsZT0iZGlzcGxheTppbmxpbmUiPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MjgiCiAgICAgICB3aWR0aD0iMC43OTM3NDk4NyIKICAgICAgIGhlaWdodD0iMTYuOTMzMzIxIgogICAgICAgeD0iNy45Mzc1IgogICAgICAgeT0iMjgwLjA2NjY1IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjI1OTIzNzcxIiAvPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MzAiCiAgICAgICB3aWR0aD0iMy45Njg3NTAyIgogICAgICAgaGVpZ2h0PSIwLjc5Mzc0NTU4IgogICAgICAgeD0iOC43MzEyNDk4IgogICAgICAgeT0iMjg4LjEzNjQ0IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjM5Njg3MzkyIiAvPgogIDwvZz4KPC9zdmc+Cg==" type="QString" name="name"/>
            <Option value="0.10000000000000001,0.10000000000000001" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="offset_unit"/>
            <Option value="35,35,35,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="30" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="0,0,255,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iNjQiCiAgIGhlaWdodD0iNjQiCiAgIHZpZXdCb3g9IjAgMCAxNi45MzMzMzMgMTYuOTMzMzM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcyMCIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMC45Mi4xIHIxNTM3MSIKICAgc29kaXBvZGk6ZG9jbmFtZT0iYmVkZGluZy5zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxNCIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9ImJhc2UiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6em9vbT0iOCIKICAgICBpbmtzY2FwZTpjeD0iMjIuNTY4NDQ3IgogICAgIGlua3NjYXBlOmN5PSI0OSIKICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0icHgiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ibGF5ZXIxIgogICAgIHNob3dncmlkPSJ0cnVlIgogICAgIHVuaXRzPSJweCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSJ0cnVlIgogICAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtbWlkcG9pbnRzPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtY2VudGVyPSJ0cnVlIgogICAgIGlua3NjYXBlOnNuYXAtZ3JpZHM9InRydWUiCiAgICAgaW5rc2NhcGU6c25hcC10by1ndWlkZXM9InRydWUiCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxNjgwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjEwMjciCiAgICAgaW5rc2NhcGU6d2luZG93LXg9Ii04IgogICAgIGlua3NjYXBlOndpbmRvdy15PSItOCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIj4KICAgIDxpbmtzY2FwZTpncmlkCiAgICAgICB0eXBlPSJ4eWdyaWQiCiAgICAgICBpZD0iZ3JpZDMyIiAvPgogIDwvc29kaXBvZGk6bmFtZWR2aWV3PgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTE3Ij4KICAgIDxyZGY6UkRGPgogICAgICA8Y2M6V29yawogICAgICAgICByZGY6YWJvdXQ9IiI+CiAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9zdmcreG1sPC9kYzpmb3JtYXQ+CiAgICAgICAgPGRjOnR5cGUKICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIiAvPgogICAgICAgIDxkYzp0aXRsZT48L2RjOnRpdGxlPgogICAgICA8L2NjOldvcms+CiAgICA8L3JkZjpSREY+CiAgPC9tZXRhZGF0YT4KICA8ZwogICAgIGlua3NjYXBlOmxhYmVsPSLjg6zjgqTjg6Tjg7wgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwtMjgwLjA2NjY1KSIKICAgICBzdHlsZT0iZGlzcGxheTppbmxpbmUiPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MjgiCiAgICAgICB3aWR0aD0iMC43OTM3NDk4NyIKICAgICAgIGhlaWdodD0iMTYuOTMzMzIxIgogICAgICAgeD0iNy45Mzc1IgogICAgICAgeT0iMjgwLjA2NjY1IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjI1OTIzNzcxIiAvPgogICAgPHJlY3QKICAgICAgIGlkPSJyZWN0MzAiCiAgICAgICB3aWR0aD0iMy45Njg3NTAyIgogICAgICAgaGVpZ2h0PSIwLjc5Mzc0NTU4IgogICAgICAgeD0iOC43MzEyNDk4IgogICAgICAgeT0iMjg4LjEzNjQ0IgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDowLjM5Njg3MzkyIiAvPgogIDwvZz4KPC9zdmc+Cg==" k="name"/>
          <prop v="0.10000000000000001,0.10000000000000001" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="30" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="strike_value" type="QString" name="field"/>
                  <Option value="2" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="FilledMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="60,204,0,255" type="QString" name="color"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="cross_fill" type="QString" name="name"/>
            <Option value="0.10000000000000001,0.10000000000000001" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="10" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
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
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="strike_value" type="QString" name="field"/>
                  <Option value="2" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="fill" clip_to_extent="1" name="@5@1" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer class="SimpleFill" enabled="1" pass="0" locked="0">
              <Option type="Map">
                <Option value="3x:0,0,0,0,0,0" type="QString" name="border_width_map_unit_scale"/>
                <Option value="60,204,0,255" type="QString" name="color"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="Pixel" type="QString" name="offset_unit"/>
                <Option value="35,35,35,255" type="QString" name="outline_color"/>
                <Option value="no" type="QString" name="outline_style"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="Pixel" type="QString" name="outline_width_unit"/>
                <Option value="solid" type="QString" name="style"/>
              </Option>
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" clip_to_extent="1" name="6" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="40,160,108,255" type="QString" name="color"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="circle" type="QString" name="name"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="offset_unit"/>
            <Option value="0,0,0,255" type="QString" name="outline_color"/>
            <Option value="solid" type="QString" name="outline_style"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="outline_width_unit"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="10" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="Pixel" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol force_rhr="0" type="marker" clip_to_extent="1" name="0" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="255,0,0,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="" type="QString" name="name"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="0,0,0,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="2" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="MM" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
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
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="255,0,0,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="" type="QString" name="name"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="0,0,0,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="2" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="MM" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
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
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="255,0,0,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="" type="QString" name="name"/>
            <Option value="0.20000000000000001,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="0,0,0,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="2" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="MM" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
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
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SvgMarker" enabled="1" pass="0" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="255,0,0,255" type="QString" name="color"/>
            <Option value="0" type="QString" name="fixedAspectRatio"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="" type="QString" name="name"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="0,0,0,255" type="QString" name="outline_color"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option name="parameters"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="2" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="MM" type="QString" name="size_unit"/>
            <Option value="0" type="QString" name="vertical_anchor_point"/>
          </Option>
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
          <prop v="" k="parameters"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="0" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </source-symbol>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style blendMode="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWeight="50" isExpression="1" textOrientation="horizontal" namedStyle="Normal" fieldName="to_int(dip_value)" fontStrikeout="0" previewBkgrdColor="255,255,255,255" useSubstitutions="0" fontWordSpacing="0" fontSizeUnit="Point" textColor="14,1,150,255" textOpacity="1" allowHtml="0" fontFamily="MS UI Gothic" fontLetterSpacing="0" fontKerning="1" fontUnderline="0" multilineHeight="1" fontSize="12" fontItalic="0" capitalization="0">
        <text-buffer bufferColor="255,255,255,255" bufferNoFill="0" bufferJoinStyle="128" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0" bufferDraw="1" bufferSizeUnits="MM" bufferOpacity="1" bufferSize="0.6"/>
        <text-mask maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskOpacity="1" maskedSymbolLayers="" maskType="0" maskSizeUnits="MM" maskEnabled="0" maskSize="0" maskJoinStyle="128"/>
        <background shapeDraw="0" shapeSizeType="0" shapeBorderWidth="0" shapeRotationType="0" shapeOffsetX="0" shapeRadiiUnit="MM" shapeRadiiY="0" shapeOpacity="1" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeType="0" shapeRotation="0" shapeSVGFile="" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeRadiiX="0" shapeOffsetUnit="MM" shapeOffsetY="0" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeJoinStyle="64">
          <symbol force_rhr="0" type="marker" clip_to_extent="1" name="markerSymbol" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="231,113,72,255" type="QString" name="color"/>
                <Option value="1" type="QString" name="horizontal_anchor_point"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="circle" type="QString" name="name"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="35,35,35,255" type="QString" name="outline_color"/>
                <Option value="solid" type="QString" name="outline_style"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
                <Option value="MM" type="QString" name="outline_width_unit"/>
                <Option value="diameter" type="QString" name="scale_method"/>
                <Option value="2" type="QString" name="size"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
                <Option value="MM" type="QString" name="size_unit"/>
                <Option value="1" type="QString" name="vertical_anchor_point"/>
              </Option>
              <prop v="0" k="angle"/>
              <prop v="231,113,72,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowOffsetGlobal="1" shadowBlendMode="0" shadowUnder="0" shadowOffsetAngle="135" shadowOffsetUnit="MapUnit" shadowOpacity="1" shadowRadius="3.5" shadowColor="255,255,255,255" shadowScale="100" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusAlphaOnly="1" shadowDraw="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusUnit="MM"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format autoWrapLength="0" useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" formatNumbers="0" plussign="0" rightDirectionSymbol=">" multilineAlign="0" placeDirectionSymbol="0" wrapChar="" decimals="3" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0"/>
      <placement quadOffset="4" layerType="PointGeometry" geometryGenerator="" fitInPolygonOnly="0" xOffset="3" placementFlags="10" offsetType="0" lineAnchorType="0" rotationAngle="0" overrunDistance="0" repeatDistance="0" centroidInside="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" yOffset="-3" preserveRotation="1" overrunDistanceUnit="MM" lineAnchorPercent="0.5" geometryGeneratorType="PointGeometry" maxCurvedCharAngleIn="25" distUnits="Pixel" priority="5" geometryGeneratorEnabled="0" distMapUnitScale="3x:0,0,0,0,0,0" placement="6" repeatDistanceUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" maxCurvedCharAngleOut="-25" polygonPlacementFlags="2" offsetUnits="MapUnit"/>
      <rendering obstacleType="0" fontLimitPixelSize="0" drawLabels="1" obstacle="1" maxNumLabels="2000" scaleVisibility="0" labelPerPart="0" fontMinPixelSize="3" limitNumLabels="0" zIndex="0" scaleMin="1" fontMaxPixelSize="10000" scaleMax="10000000" obstacleFactor="1" mergeLines="0" minFeatureSize="0" upsidedownLabels="0" displayAll="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" type="QString" name="name"/>
          <Option type="Map" name="properties">
            <Option type="Map" name="LabelRotation">
              <Option value="true" type="bool" name="active"/>
              <Option value="strike_value" type="QString" name="field"/>
              <Option value="2" type="int" name="type"/>
            </Option>
            <Option type="Map" name="OffsetQuad">
              <Option value="false" type="bool" name="active"/>
              <Option value="Strike" type="QString" name="field"/>
              <Option value="2" type="int" name="type"/>
            </Option>
            <Option type="Map" name="Rotation">
              <Option value="false" type="bool" name="active"/>
              <Option value="Strike" type="QString" name="field"/>
              <Option value="2" type="int" name="type"/>
            </Option>
          </Option>
          <Option value="collection" type="QString" name="type"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" type="QString" name="anchorPoint"/>
          <Option type="Map" name="ddProperties">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
          <Option value="false" type="bool" name="drawToAllParts"/>
          <Option value="0" type="QString" name="enabled"/>
          <Option value="point_on_exterior" type="QString" name="labelAnchorPoint"/>
          <Option value="&lt;symbol force_rhr=&quot;0&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; name=&quot;symbol&quot; alpha=&quot;1&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; type=&quot;QString&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; type=&quot;QString&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; pass=&quot;0&quot; locked=&quot;0&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;align_dash_pattern&quot;/>&lt;Option value=&quot;square&quot; type=&quot;QString&quot; name=&quot;capstyle&quot;/>&lt;Option value=&quot;5;2&quot; type=&quot;QString&quot; name=&quot;customdash&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;customdash_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;customdash_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;dash_pattern_offset&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;dash_pattern_offset_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;draw_inside_polygon&quot;/>&lt;Option value=&quot;bevel&quot; type=&quot;QString&quot; name=&quot;joinstyle&quot;/>&lt;Option value=&quot;60,60,60,255&quot; type=&quot;QString&quot; name=&quot;line_color&quot;/>&lt;Option value=&quot;solid&quot; type=&quot;QString&quot; name=&quot;line_style&quot;/>&lt;Option value=&quot;0.3&quot; type=&quot;QString&quot; name=&quot;line_width&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;line_width_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;offset&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;offset_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;offset_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;ring_filter&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;use_custom_dash&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;width_map_unit_scale&quot;/>&lt;/Option>&lt;prop v=&quot;0&quot; k=&quot;align_dash_pattern&quot;/>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;dash_pattern_offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;dash_pattern_offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; type=&quot;QString&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; type=&quot;QString&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString" name="lineSymbol"/>
          <Option value="0" type="double" name="minLength"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="minLengthMapUnitScale"/>
          <Option value="MM" type="QString" name="minLengthUnit"/>
          <Option value="0" type="double" name="offsetFromAnchor"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromAnchorMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromAnchorUnit"/>
          <Option value="0" type="double" name="offsetFromLabel"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromLabelMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromLabelUnit"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties>
    <property value="COALESCE(&quot;Dip_Value&quot;, '&lt;NULL>')" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" maxScaleDenominator="1e+08" penColor="#000000" rotationOffset="270" width="15" spacingUnitScale="3x:0,0,0,0,0,0" minimumSize="0" sizeScale="3x:0,0,0,0,0,0" barWidth="5" showAxis="0" penAlpha="255" spacing="0" scaleDependency="Area" enabled="0" minScaleDenominator="0" lineSizeType="MM" direction="1" backgroundAlpha="255" labelPlacementMethod="XHeight" scaleBasedVisibility="0" opacity="1" sizeType="MM" penWidth="0" height="15" spacingUnit="MM" diagramOrientation="Up">
      <fontProperties description="MS UI Gothic,9,-1,5,50,0,0,0,0,0" style=""/>
      <attribute color="#000000" label="" field=""/>
      <axisSymbol>
        <symbol force_rhr="0" type="line" clip_to_extent="1" name="" alpha="1">
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <layer class="SimpleLine" enabled="1" pass="0" locked="0">
            <Option type="Map">
              <Option value="0" type="QString" name="align_dash_pattern"/>
              <Option value="square" type="QString" name="capstyle"/>
              <Option value="5;2" type="QString" name="customdash"/>
              <Option value="3x:0,0,0,0,0,0" type="QString" name="customdash_map_unit_scale"/>
              <Option value="MM" type="QString" name="customdash_unit"/>
              <Option value="0" type="QString" name="dash_pattern_offset"/>
              <Option value="3x:0,0,0,0,0,0" type="QString" name="dash_pattern_offset_map_unit_scale"/>
              <Option value="MM" type="QString" name="dash_pattern_offset_unit"/>
              <Option value="0" type="QString" name="draw_inside_polygon"/>
              <Option value="bevel" type="QString" name="joinstyle"/>
              <Option value="35,35,35,255" type="QString" name="line_color"/>
              <Option value="solid" type="QString" name="line_style"/>
              <Option value="0.26" type="QString" name="line_width"/>
              <Option value="MM" type="QString" name="line_width_unit"/>
              <Option value="0" type="QString" name="offset"/>
              <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
              <Option value="MM" type="QString" name="offset_unit"/>
              <Option value="0" type="QString" name="ring_filter"/>
              <Option value="0" type="QString" name="tweak_dash_pattern_on_corners"/>
              <Option value="0" type="QString" name="use_custom_dash"/>
              <Option value="3x:0,0,0,0,0,0" type="QString" name="width_map_unit_scale"/>
            </Option>
            <prop v="0" k="align_dash_pattern"/>
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="dash_pattern_offset"/>
            <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
            <prop v="MM" k="dash_pattern_offset_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="tweak_dash_pattern_on_corners"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" zIndex="0" placement="0" priority="0" dist="0" showAll="1" linePlacementFlags="2">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="no">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="attribute">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="strike_value">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="dip_value">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="trend_value">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="plunge_value">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="rake_value">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="remarks">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="legend01">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="legend01e">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_markerType">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_className">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_stroke">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_color">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_weight">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_opacity">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_fill">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_fillColor">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_dashArray">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_lineCap">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_lineJoin">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_clickable">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_iconUrl">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_iconSize">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_iconAnchor">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_html">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="_radius">
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
    <alias field="attribute" index="2" name=""/>
    <alias field="strike_value" index="3" name=""/>
    <alias field="dip_value" index="4" name=""/>
    <alias field="trend_value" index="5" name=""/>
    <alias field="plunge_value" index="6" name=""/>
    <alias field="rake_value" index="7" name=""/>
    <alias field="remarks" index="8" name=""/>
    <alias field="legend01" index="9" name=""/>
    <alias field="legend01e" index="10" name=""/>
    <alias field="_markerType" index="11" name=""/>
    <alias field="_className" index="12" name=""/>
    <alias field="_stroke" index="13" name=""/>
    <alias field="_color" index="14" name=""/>
    <alias field="_weight" index="15" name=""/>
    <alias field="_opacity" index="16" name=""/>
    <alias field="_fill" index="17" name=""/>
    <alias field="_fillColor" index="18" name=""/>
    <alias field="_dashArray" index="19" name=""/>
    <alias field="_lineCap" index="20" name=""/>
    <alias field="_lineJoin" index="21" name=""/>
    <alias field="_clickable" index="22" name=""/>
    <alias field="_iconUrl" index="23" name=""/>
    <alias field="_iconSize" index="24" name=""/>
    <alias field="_iconAnchor" index="25" name=""/>
    <alias field="_html" index="26" name=""/>
    <alias field="_radius" index="27" name=""/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="fid" expression=""/>
    <default applyOnUpdate="0" field="no" expression=""/>
    <default applyOnUpdate="0" field="attribute" expression=""/>
    <default applyOnUpdate="0" field="strike_value" expression=""/>
    <default applyOnUpdate="0" field="dip_value" expression=""/>
    <default applyOnUpdate="0" field="trend_value" expression=""/>
    <default applyOnUpdate="0" field="plunge_value" expression=""/>
    <default applyOnUpdate="0" field="rake_value" expression=""/>
    <default applyOnUpdate="0" field="remarks" expression=""/>
    <default applyOnUpdate="0" field="legend01" expression=""/>
    <default applyOnUpdate="0" field="legend01e" expression=""/>
    <default applyOnUpdate="0" field="_markerType" expression=""/>
    <default applyOnUpdate="0" field="_className" expression=""/>
    <default applyOnUpdate="0" field="_stroke" expression=""/>
    <default applyOnUpdate="0" field="_color" expression=""/>
    <default applyOnUpdate="0" field="_weight" expression=""/>
    <default applyOnUpdate="0" field="_opacity" expression=""/>
    <default applyOnUpdate="0" field="_fill" expression=""/>
    <default applyOnUpdate="0" field="_fillColor" expression=""/>
    <default applyOnUpdate="0" field="_dashArray" expression=""/>
    <default applyOnUpdate="0" field="_lineCap" expression=""/>
    <default applyOnUpdate="0" field="_lineJoin" expression=""/>
    <default applyOnUpdate="0" field="_clickable" expression=""/>
    <default applyOnUpdate="0" field="_iconUrl" expression=""/>
    <default applyOnUpdate="0" field="_iconSize" expression=""/>
    <default applyOnUpdate="0" field="_iconAnchor" expression=""/>
    <default applyOnUpdate="0" field="_html" expression=""/>
    <default applyOnUpdate="0" field="_radius" expression=""/>
  </defaults>
  <constraints>
    <constraint constraints="3" field="fid" notnull_strength="1" exp_strength="0" unique_strength="1"/>
    <constraint constraints="0" field="no" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="attribute" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="strike_value" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="dip_value" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="trend_value" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="plunge_value" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="rake_value" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="remarks" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="legend01" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="legend01e" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_markerType" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_className" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_stroke" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_color" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_weight" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_opacity" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_fill" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_fillColor" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_dashArray" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_lineCap" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_lineJoin" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_clickable" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_iconUrl" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_iconSize" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_iconAnchor" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_html" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="_radius" notnull_strength="0" exp_strength="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="fid"/>
    <constraint exp="" desc="" field="no"/>
    <constraint exp="" desc="" field="attribute"/>
    <constraint exp="" desc="" field="strike_value"/>
    <constraint exp="" desc="" field="dip_value"/>
    <constraint exp="" desc="" field="trend_value"/>
    <constraint exp="" desc="" field="plunge_value"/>
    <constraint exp="" desc="" field="rake_value"/>
    <constraint exp="" desc="" field="remarks"/>
    <constraint exp="" desc="" field="legend01"/>
    <constraint exp="" desc="" field="legend01e"/>
    <constraint exp="" desc="" field="_markerType"/>
    <constraint exp="" desc="" field="_className"/>
    <constraint exp="" desc="" field="_stroke"/>
    <constraint exp="" desc="" field="_color"/>
    <constraint exp="" desc="" field="_weight"/>
    <constraint exp="" desc="" field="_opacity"/>
    <constraint exp="" desc="" field="_fill"/>
    <constraint exp="" desc="" field="_fillColor"/>
    <constraint exp="" desc="" field="_dashArray"/>
    <constraint exp="" desc="" field="_lineCap"/>
    <constraint exp="" desc="" field="_lineJoin"/>
    <constraint exp="" desc="" field="_clickable"/>
    <constraint exp="" desc="" field="_iconUrl"/>
    <constraint exp="" desc="" field="_iconSize"/>
    <constraint exp="" desc="" field="_iconAnchor"/>
    <constraint exp="" desc="" field="_html"/>
    <constraint exp="" desc="" field="_radius"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="&quot;_iconSize&quot;" actionWidgetStyle="dropDown" sortOrder="1">
    <columns>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" type="field" hidden="0" name="no"/>
      <column width="-1" type="field" hidden="0" name="dip_value"/>
      <column width="-1" type="field" hidden="0" name="remarks"/>
      <column width="-1" type="field" hidden="0" name="attribute"/>
      <column width="-1" type="field" hidden="0" name="legend01"/>
      <column width="-1" type="field" hidden="0" name="legend01e"/>
      <column width="-1" type="field" hidden="0" name="strike_value"/>
      <column width="-1" type="field" hidden="0" name="_markerType"/>
      <column width="-1" type="field" hidden="0" name="_className"/>
      <column width="-1" type="field" hidden="0" name="_stroke"/>
      <column width="-1" type="field" hidden="0" name="_color"/>
      <column width="-1" type="field" hidden="0" name="_weight"/>
      <column width="-1" type="field" hidden="0" name="_opacity"/>
      <column width="-1" type="field" hidden="0" name="_fill"/>
      <column width="-1" type="field" hidden="0" name="_fillColor"/>
      <column width="-1" type="field" hidden="0" name="_dashArray"/>
      <column width="-1" type="field" hidden="0" name="_lineCap"/>
      <column width="-1" type="field" hidden="0" name="_lineJoin"/>
      <column width="-1" type="field" hidden="0" name="_clickable"/>
      <column width="118" type="field" hidden="0" name="_iconUrl"/>
      <column width="-1" type="field" hidden="0" name="_iconSize"/>
      <column width="-1" type="field" hidden="0" name="_iconAnchor"/>
      <column width="-1" type="field" hidden="0" name="_html"/>
      <column width="-1" type="field" hidden="0" name="_radius"/>
      <column width="-1" type="field" hidden="0" name="fid"/>
      <column width="-1" type="field" hidden="0" name="trend_value"/>
      <column width="-1" type="field" hidden="0" name="plunge_value"/>
      <column width="-1" type="field" hidden="0" name="rake_value"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
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
    <field editable="1" name="_className"/>
    <field editable="1" name="_clickable"/>
    <field editable="1" name="_color"/>
    <field editable="1" name="_dashArray"/>
    <field editable="1" name="_fill"/>
    <field editable="1" name="_fillColor"/>
    <field editable="1" name="_html"/>
    <field editable="1" name="_iconAnchor"/>
    <field editable="1" name="_iconSize"/>
    <field editable="1" name="_iconUrl"/>
    <field editable="1" name="_lineCap"/>
    <field editable="1" name="_lineJoin"/>
    <field editable="1" name="_markerType"/>
    <field editable="1" name="_opacity"/>
    <field editable="1" name="_radius"/>
    <field editable="1" name="_stroke"/>
    <field editable="1" name="_weight"/>
    <field editable="1" name="attribute"/>
    <field editable="1" name="dip_value"/>
    <field editable="1" name="fid"/>
    <field editable="1" name="legend01"/>
    <field editable="1" name="legend01e"/>
    <field editable="1" name="no"/>
    <field editable="1" name="plunge_value"/>
    <field editable="1" name="rake_value"/>
    <field editable="1" name="remarks"/>
    <field editable="1" name="strike_value"/>
    <field editable="1" name="trend_value"/>
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
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>COALESCE("Dip_Value", '&lt;NULL>')</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>

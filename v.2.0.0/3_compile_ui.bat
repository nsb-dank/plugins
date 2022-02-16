rem uiファイルのコンパイル
rem OSGeo4 Shellより、このバッチファイルを実行
cd "c:\Program Files\QGIS\bin\"
call "c:\Program Files\QGIS\bin\o4w_env.bat"
call "c:\Program Files\QGIS\bin\qt5_env.bat"
call "c:\Program Files\QGIS\bin\py3_env.bat"

cd "C:\Users\ykara\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\geolib3"
pyuic5 -o ui_create_subject_layer_dialog.py ui_create_subject_layer_dialog.ui
pyuic5 -o ui_import_geoclino_dialog.py ui_import_geoclino_dialog.ui
pyuic5 -o ui_settings_dialog.py ui_settings_dialog.ui
pyuic5 -o ui_draw_boundary_dockwidget.py ui_draw_boundary_dockwidget.ui
pyuic5 -o ui_edit_attribute_dockwidget.py ui_edit_attribute_dockwidget.ui

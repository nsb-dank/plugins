CD /d %~dp0
call pyuic5.bat ui_create_project_dialog.ui -o ui_create_project_dialog.py
call pyuic5.bat ui_create_layer_dialog.ui -o ui_create_layer_dialog.py
call pyuic5.bat ui_create_subject_layer_dialog.ui -o ui_create_subject_layer_dialog.py
call pyuic5.bat ui_import_geoclino_dialog.ui -o ui_import_geoclino_dialog.py
call pyuic5.bat ui_settings_dialog.ui -o ui_settings_dialog.py
call pyuic5.bat ui_html_edit_dialog.ui -o ui_html_edit_dialog.py
call pyuic5.bat ui_export_to_geolib_dialog.ui -o ui_export_to_geolib_dialog.py
call pyuic5.bat ui_export_library_dialog.ui -o ui_export_library_dialog.py
call pyuic5.bat ui_draw_boundary_dockwidget.ui -o ui_draw_boundary_dockwidget.py
call pyuic5.bat ui_edit_attribute_dockwidget.ui -o ui_edit_attribute_dockwidget.py
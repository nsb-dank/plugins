@echo off
call "C:\Program Files\QGIS\bin\o4w_env.bat"
call "C:\Program Files\QGIS\bin\qt5_env.bat"
call "C:\Program Files\QGIS\bin\py3_env.bat"

@echo on
pyrcc5  -o resources.py resources.qrc
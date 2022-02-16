rem OSGeo4 Shellより、このバッチファイルを実行
cd "c:\Program Files\QGIS\bin\"
call "c:\Program Files\QGIS\bin\o4w_env.bat"
call "c:\Program Files\QGIS\bin\qt5_env.bat"
call "c:\Program Files\QGIS\bin\py3_env.bat"

cd "C:\Users\ykara\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\geolib3"

rem pylupdate5 geolib3.py -ts i18n/geolib3_ja.ts

pylupdate5 geolib3.pro

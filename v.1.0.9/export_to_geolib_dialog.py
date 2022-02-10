# -*- coding: utf-8 -*-
"""
/***************************************************************************
 postRouteMapDialog
                                 A QGIS plugin
 This plugin captures the field survey and creates a geological map.
                             -------------------
        begin                : 2017-05-31
        git sha              : $Format:%H$
        copyright            : (C) 2017 by =Dank Co., Ltd.
        email                : yukihiko.karata@nsb-dank.com
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
from PyQt5.QtCore import  QSettings, QObject, QUrl, Qt, QDateTime
from PyQt5.QtWidgets import QDialog,QTableView,QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel
from qgis.core import QgsProject, QgsVectorFileWriter,QgsLayerTreeLayer,QgsLayerTreeNode,QgsVectorLayer, QgsRasterLayer

import os
import ftplib
import glob
from pathlib import Path

from .ui_export_to_geolib_dialog import Ui_ExportToGeolibDialog
from .geolib_util import GeolibUtil

class ExportToGeolibDialog(QDialog, Ui_ExportToGeolibDialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.ui = Ui_ExportToGeolibDialog()
        self.ui.setupUi(self)
        # show the dialog
        self.settings = QSettings()
        self.email = self.settings.value("geolib3/userId","")
        self.password = self.settings.value("geolib3/password","")
        self.use_cloud = self.settings.value("geolib3/UseCloud","")
        self.use_custom = self.settings.value("geolib3/UseCustom","")
        self.host_name = self.settings.value("geolib3/HostName","")
        self.port_no = self.settings.value("geolib3/PortNo","")
        self.db_name = self.settings.value("geolib3/DbName","")
        self.db_user_id = self.settings.value("geolib3/DbUserId","")
        self.db_password = self.settings.value("geolib3/DbPassword","")
        if self.use_cloud == True:
            self.host_name = "gis.nsb-dank.com"
            self.port_no = "3306"
            self.db_name = "geolib"
            self.db_user_id = "qgis_user"
            self.db_password = "qgis_user"

        #self.ui.webView.load(QUrl(self.host_name))
        self.project_path, ext = os.path.splitext(QgsProject.instance().fileName())
        self.projectCrs = QgsProject.instance().crs()

        self.ui.tblArticles.setVisible(False)
        self.ui.btnNew.setVisible(False)
        self.ui.btnEdit.setVisible(False)
        self.ui.wgtExportMap.setVisible(False)
        self.ui.grpArticle.setVisible(False)
        self.ui.grpMapData.setVisible(False)

        #シグナル
        self.ui.btnConnect.clicked.connect(self.btn_connect_clicked)
        self.ui.btnEdit.clicked.connect(self.btn_edit_clicked)
        self.ui.btnNew.clicked.connect(self.btn_new_clicked)
        self.ui.btnSave.clicked.connect( self.btn_save_clicked)
        self.ui.btnUpload.clicked.connect( self.btn_upload_clicked)
        self.ui.btnClose.clicked.connect(self.btn_close_clicked)
        self.ui.tblArticles.doubleClicked.connect(self.btn_edit_clicked)
        self.ui.btnNewMap.clicked.connect(self.btn_new_map_clicked)
        self.ui.tblScenarioMap.doubleClicked.connect(self.edit_scenario_map)
        self.ui.tblSubjectMap.doubleClicked.connect(self.edit_subject_map)
        self.ui.tblAssociatedMap.doubleClicked.connect(self.edit_associated_map)
        self.ui.cboMapType.currentIndexChanged.connect(self.addCboLayerItem)
        self.ui.btnMapSave.clicked.connect(self.btn_map_save_clicked)
        self.ui.btnMapCancel.clicked.connect(self.btn_map_cancel_clicked)
        self.ui.btnDelete.clicked.connect(self.btn_delete_clicked)
        self.ui.btnMapDelete.clicked.connect(self.btn_map_delete_clicked)

    def btn_connect_clicked(self):
    # 接続ボタン押下時の処理
        self.getUserInfo()

    def getUserInfo(self):
        #DBに接続
        geolib = GeolibUtil()
        db = geolib.dbConnect(self.host_name, self.db_name, self.port_no, self.db_user_id, self.db_password)
        if db.open():
            self.ui.lblConnectMessage.setText("Successful connection to " + self.host_name)
            query = QSqlQuery()
            # ユーザー情報を取得
            get_user_sql = "select id, email, username from geolib.users where email = '" + self.email + "' and password = '" + self.password + "'"
            #print get_user_sql
            query.exec(get_user_sql)
            #self.ui.lblMessage.setText(get_user_sql)
            if query.size()>0:
                while query.next():
                    self.user_id = str(query.value(0))
                    #user_mail = str(query.value(1))
                    user_name = str(query.value(2))
                    self.ui.lblMessage.setText(self.tr("[ %s ] Article list:") % user_name )
            db.close()
            self.ui.tblArticles.setVisible(True)
            self.ui.btnNew.setVisible(True)
            #self.ui.btnEdit.setVisible(True)
            self.dispArticlesTable()
        else:
            err = db.lastError()
            self.ui.lblConnectMessage.setText(err.driverText())

    def dispArticlesTable(self):
        #DBに接続
        geolib = GeolibUtil()
        db = geolib.dbConnect(self.host_name, self.db_name, self.port_no, self.db_user_id, self.db_password)
        if db.open():
            #Article情報を取得してテーブルに表示
            articles =  QSqlQueryModel()
            get_articles_sql = "select id, libraryname,title,abstract from articles where user_id = " + self.user_id +" order by id"
            articles.setQuery(get_articles_sql)
            db.close()
        else:
            err = db.lastError()
            self.ui.lblConnectMessage.setText(err.driverText())

        articles.setHeaderData(1, Qt.Horizontal, self.tr("Name"))
        articles.setHeaderData(2, Qt.Horizontal, self.tr("Title"))
        articles.setHeaderData(3, Qt.Horizontal, self.tr("Abstract"))

        self.ui.tblArticles.setModel(articles)
        self.ui.tblArticles.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tblArticles.setColumnWidth(0, 0)
        self.ui.tblArticles.setColumnWidth(1, 150)
        self.ui.tblArticles.setColumnWidth(2, 150)
        self.ui.tblArticles.show()

    def btn_edit_clicked(self):
    # 編集ボタン押下時の処理
        # 選択行のarticleを取得して表示

        idx = self.ui.tblArticles.selectedIndexes()
        article_id = str(self.ui.tblArticles.model().data(idx[0]))
        self.current_article_id = article_id


        self.ui.tblArticles.setVisible(False)
        self.ui.grpArticle.setVisible(True)
        self.ui.btnDelete.setVisible(True)

        self.ui.grpMapData.setVisible(True)
        self.dispArticleData(article_id)
        self.dispMapData(article_id)


    def dispArticleData(self,article_id):
        geolib = GeolibUtil()
        db= geolib.dbConnect(self.host_name, self.db_name, self.port_no, self.db_user_id, self.db_password)
        self.current_article_id = article_id
        if db.open():
            query =  QSqlQuery()
            get_article_sql = "select * from articles where id = '" + article_id + "'"
            query.exec(get_article_sql)
            if query.size()>0:
                while query.next():
                    self.article_id = int(article_id)
                    self.user_id = str(query.value(1))
                    article_name = query.value(2)
                    title = query.value(3)
                    slug = query.value(4)
                    area_id  = int(query.value(5))
                    level_id = int(query.value(6))
                    abstract = query.value(7)
                    geom = query.value(8)
                    filename = query.value(9)
                    published = bool(query.value(10))
                    created = (query.value(11)).toString('yyyy/MM/dd h:m:s')
                    modified = (query.value(12)).toString('yyyy/MM/dd h:m:s')
            else:
                self.ui.lblMessage.setText(self.tr("No Data"))

            #コンボボックスアイテムをセット
            self.addComboBoxItem()
            #現在のマップキャンバスの表示領域を取得
            self.getGeometry()
            #article情報を表示
            self.ui.txtName.setText(article_name)
            self.ui.txtTitle.setText(title)
            self.ui.cboArea.setCurrentIndex(int(area_id) - 1)
            self.ui.cboLevel.setCurrentIndex(int(level_id) - 1)
            self.ui.txtAbstract.setText(abstract)
            self.ui.chkPublished.setChecked(published)
            self.ui.lblCreateDate.setText(str(created))
            self.ui.lblModifiedDate.setText(str(modified))
        else:
            self.ui.lblMessage.setText(self.tr("Database connect error!"))
        db.close()

    def dispMapData(self,article_id):
        #map情報を取得
        geolib = GeolibUtil()
        db = geolib.dbConnect(self.host_name, self.db_name, self.port_no, self.db_user_id, self.db_password)
        if db.open():
            #scenario map
            scenarioMaps =  QSqlQueryModel()
            get_scenario_maps_sql = "select id, title, sourcetype, foldername from maps where article_id = '" + article_id +"' and maptype = 'Scenario' order by foldername"
            scenarioMaps.setQuery(get_scenario_maps_sql)
            self.ui.tblScenarioMap.setModel(scenarioMaps)
            self.ui.tblScenarioMap.setSelectionBehavior(QTableView.SelectRows)
            self.ui.tblScenarioMap.setColumnWidth(0, 0)
            self.ui.tblScenarioMap.setColumnWidth(1, 180)
            self.ui.tblScenarioMap.show()

            #subject map
            subjectMaps =  QSqlQueryModel()
            get_subject_maps_sql = "select id, title, sourcetype, foldername from maps where article_id = '" + article_id +"' and maptype = 'Subject' order by foldername"
            subjectMaps.setQuery(get_subject_maps_sql)
            self.ui.tblSubjectMap.setModel(subjectMaps)
            self.ui.tblSubjectMap.setSelectionBehavior(QTableView.SelectRows)
            self.ui.tblSubjectMap.setColumnWidth(0, 0)
            self.ui.tblSubjectMap.setColumnWidth(1, 180)
            self.ui.tblSubjectMap.show()

            #AssociatedMap
            associatedMaps =  QSqlQueryModel()
            get_associated_maps_sql = "select id, title, foldername, script, attribution from maps where article_id = '" + article_id +"' and maptype = 'Associated' order by title"
            associatedMaps.setQuery(get_associated_maps_sql)
            self.ui.tblAssociatedMap.setModel(associatedMaps)
            self.ui.tblAssociatedMap.setSelectionBehavior(QTableView.SelectRows)
            self.ui.tblAssociatedMap.setColumnWidth(0, 0)
            self.ui.tblAssociatedMap.setColumnWidth(1, 180)
            self.ui.tblAssociatedMap.show()

        else:
            self.ui.lblMessage.setText(self.tr("Database connect error!"))

        db.close()

        #html files
        htmlPath = str(self.user_id)+'/' + str(self.article_id) + '/scenario/html'
        htmlCount = geolib.ftpFileCount(htmlPath)
        if htmlCount >0:
            self.ui.lblScenarioMessage.setText(str(htmlCount) + self.tr(' files are registed.'))
        #symbol files
        iconPath = str(self.user_id)+'/' + str(self.article_id) + '/icon'
        iconCount = geolib.ftpFileCount(iconPath)
        if iconCount >0:
            self.ui.lblSymbolMessage.setText(str(iconCount) + self.tr(' files are registed.'))


    # 新規ボタン押下時の処理
    def btn_new_clicked(self):
        #コンボボックスアイテムをセット
        geolib = GeolibUtil()
        db = geolib.dbConnect(self.host_name, self.db_name, self.port_no, self.db_user_id, self.db_password)
        if db.open():
            self.addComboBoxItem()
            db.close()
        #現在のマップキャンバスの表示領域を取得
        self.getGeometry()

        # 入力フォームを表示
        self.ui.grpArticle.setVisible(True)
        self.ui.btnDelete.setVisible(False)
        self.ui.grpMapData.setVisible(False)
        self.article_id  = 0
        self.ui.txtName.setText("")
        self.ui.txtTitle.setText("")
        self.ui.cboArea.setCurrentIndex(0)
        self.ui.cboLevel.setCurrentIndex(0)
        self.ui.txtAbstract.setText("")
        self.ui.chkPublished.setChecked(False)
        self.ui.lblCreateDate.setText(QDateTime.currentDateTime().toString("yyyy/MM/dd hh:mm:ss"))
        self.ui.lblModifiedDate.setText(QDateTime.currentDateTime().toString("yyyy/MM/dd hh:mm:ss"))

        self.dispArticlesTable()

    def btn_save_clicked(self):
    # 保存ボタン押下時の処理
        #入力チェック
        if self.ui.txtName.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The library name has not been entered. Please enter."))
        elif self.ui.txtTitle.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The library title has not been entered. Please enter."))
        else:
            geolib = GeolibUtil()
            db = geolib.dbConnect(self.host_name, self.db_name, self.port_no, self.db_user_id, self.db_password)
            if db.open():
                #article情報をデータベースに記録
                name = self.ui.txtName.text()
                title = self.ui.txtTitle.text()
                area_id = self.ui.cboArea.currentIndex() + 1
                level_id = self.ui.cboLevel.currentIndex() + 1
                abstract = self.ui.txtAbstract.toPlainText()
                published = self.ui.chkPublished.isChecked()
                created =QDateTime.currentDateTime().toString("yyyy/MM/dd hh:mm:ss")
                modified = QDateTime.currentDateTime().toString("yyyy/MM/dd hh:mm:ss")

                query = QSqlQuery()
                if (self.article_id >0):
                    #更新
                    update_sql = "UPDATE articles SET" \
                                    " libraryname = '" + name + "'" \
                                    ",title = '" + title + "'"\
                                    ",area_id = " + str(area_id) + \
                                    ",level_id  = " + str(level_id) + \
                                    ",abstract =  '" + abstract + "'" \
                                    ",geom = ST_GeomFromText('POLYGON(" + self.geom + ")',4326)" \
                                    ",published = " + str(published) +  \
                                    ",modified = '" + modified + "'" \
                                    " WHERE id = " + str(self.article_id) + \
                                    " AND user_id = " + str(self.user_id) + ";"
                    query.exec_("" + update_sql + "")
                    db.commit()
                else:
                    #新規追加
                    insert_sql = "INSERT INTO articles (user_id,libraryname, title, area_id, level_id, abstract,  published,created,modified,geom)" \
                                    " VALUES (" + str(self.user_id) + "" \
                                    ", '" + name + "'" \
                                    ", '" + title + "'" \
                                    ", " + str(area_id) + "" \
                                    ", " + str(level_id) + "" \
                                    ", '" + abstract + "'" \
                                    ", " + str(published) + "" \
                                    ", '" + created + "'" \
                                    ", '" + created + "'" \
                                    ", ST_GeomFromText('POLYGON(" + self.geom + ")',4326)" \
                                    ");"
                    query.exec_("" + insert_sql + "")
                    db.commit()
                    #dataフォルダを作成

                    get_id_sql ="SELECT LAST_INSERT_ID()";
                    query.exec_(get_id_sql)
                    if query.size()>0:
                        while query.next():
                            article_id = query.value(0)
                    article_path = str(self.user_id) + '/' + str(article_id)
                    geolib.ftpCreateFolder(article_path)
                    geolib.ftpCreateFolder(article_path+'/icon')
                    geolib.ftpCreateFolder(article_path+'/scenario/html')
                    geolib.ftpCreateFolder(article_path+'/subject')
                db.close()
                QMessageBox.information(self, u"Infomation", self.tr(u"Completed to save the library data."))
            else:
                self.ui.lblMessage.setText(self.tr(u"Database connect error!"))
        self.btn_connect_clicked()

    def btn_delete_clicked(self):
    #削除ボタン押下時
        _reply = QMessageBox.question(self, self.tr(u"Confirmation"),
                self.tr(u"All data and files in the library will be deleted.\n Are you sure?"),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if _reply == QMessageBox.Yes:
            #選択したライブラリおよび配下のマップデータを削除
            geolib = GeolibUtil()
            db = geolib.dbConnect(self.host_name, self.db_name, self.port_no, self.db_user_id, self.db_password)
            if db.open():
                query = QSqlQuery()
                if (self.article_id >0):
                    #関連するマップの削除
                    delete_sql = "DELETE FROM maps" \
                                    " WHERE article_id = " + str(self.article_id) + ";"
                    query.exec_("" + delete_sql + "")
                    #ライブラリ削除
                    delete_sql = "DELETE FROM articles" \
                                    " WHERE id = " + str(self.article_id) + ";"
                    query.exec_("" + delete_sql + "")
                    db.commit()
                db.close()
            #フォルダ削除 -- エラーがでるためコメントアウト（別途削除が必要）
            #article_path = str(self.user_id) + '/' + str(self.article_id)
            #geolib.ftpRmTree(article_path)

            self.btn_connect_clicked()

    def btn_upload_clicked(self):
    # アップロードボタン押下時の処理
        _reply = QMessageBox.question(self, self.tr(u"Confirmation"),
            self.tr(u"If uploaded files contain images, uploading may take some time..\n Are you sure?"),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if _reply == QMessageBox.Yes:
            self.article_path = os.path.join(self.project_path, str(self.article_id)).replace('/', os.sep)
            geolib=GeolibUtil()
            #FTPログイン
            # 接続サーバーのホスト名
            ftp = ftplib.FTP("gis.nsb-dank.com")
            ftp.set_pasv("true")
            # ユーザ名とパスワードを設定してログイン
            ftp.login("qgis_user", "qgis_user")

            #シンボルファイルを転送
            if self.ui.chkSymbolIcons.isChecked():
                icon_folder = os.path.join(self.project_path,"style").replace('/', os.sep)   #転送元フォルダ
                dest_icon_folder = "./" + str(self.user_id) + "/"+ str(self.article_id) + "/icon/"  #転送先フォルダ

                icon_files = glob.glob(icon_folder+'/*')
                for icon_file in icon_files:
                    if os.path.isfile(icon_file):
                        file_name = os.path.basename(icon_file)
                        fp = open(icon_file,'rb')
                        ftp.storbinary("STOR " + dest_icon_folder+file_name,fp)

            #シナリオファイルを転送
            if self.ui.chkScenarioFiles.isChecked():
                p = Path(os.path.join(self.project_path,'Scenario','html').replace('/', os.sep))  #転送元フォルダ
                scenario_folder = str(os.path.join(self.project_path,'Scenario','html').replace('/', os.sep))  #転送元フォルダ
                dest_scenario_folder = "./" + str(self.user_id) + "/"+ str(self.article_id) + '/scenario/html/'  #転送先フォルダ
                lists = list(p.glob("**/*"))
                for l in lists:
                    scenario_file = str(l)[len(scenario_folder)+1:]
                    if os.path.isfile(str(l)):
                        #print ("File:" + dest_scenario_folder+scenario_file)
                        fp = open(l,'rb')
                        ftp.storbinary("STOR " + dest_scenario_folder+scenario_file,fp)
                    else:
                        #print("CreateFolder:" + dest_scenario_folder+scenario_file)
                        geolib.ftpCreateFolder(dest_scenario_folder+scenario_file)

            # 終了処理
            QMessageBox.information(self, u"Infomation", self.tr(u"Completed to upload the library files."))
            ftp.close()
            self.btn_connect_clicked()

    def btn_new_map_clicked(self):
        self.map_id  = 0
        self.ui.txtMapTitle.setText('')
        self.ui.txtFolderName.setText('')
        self.ui.txtScript.setText('')
        self.ui.txtAttribution.setText('')

        self.addCboLayerItem()

        self.ui.wgtExportMap.setVisible(True)

    def edit_scenario_map(self):
        #マップエクスポートウィジェットを開く
        row = self.ui.tblScenarioMap.selectedIndexes()
        self.map_id = self.ui.tblScenarioMap.model().data(row[0])
        mapTitle = self.ui.tblScenarioMap.model().data(row[1])
        sourceType = self.ui.tblScenarioMap.model().data(row[2])
        folderName = self.ui.tblScenarioMap.model().data(row[3])
        self.ui.cboMapType.setCurrentIndex(self.ui.cboMapType.findText('Scenario'))
        self.ui.txtMapTitle.setText(mapTitle)
        sourceIndex =  self.ui.cboSourceType.findText(sourceType)
        if sourceIndex >= 0:
            self.ui.cboSourceType.setCurrentIndex(sourceIndex)
        self.ui.txtFolderName.setText(folderName)
        self.addCboLayerItem()

        self.ui.wgtExportMap.setVisible(True)

    def edit_subject_map(self):
        #マップエクスポートウィジェットを開く
        row = self.ui.tblSubjectMap.selectedIndexes()
        self.map_id = self.ui.tblSubjectMap.model().data(row[0])
        mapTitle = self.ui.tblSubjectMap.model().data(row[1])
        sourceType = self.ui.tblSubjectMap.model().data(row[2])
        folderName = self.ui.tblSubjectMap.model().data(row[3])
        self.ui.cboMapType.setCurrentIndex(self.ui.cboMapType.findText('Subject'))
        self.ui.txtMapTitle.setText(mapTitle)
        sourceIndex =  self.ui.cboSourceType.findText(sourceType)
        if sourceIndex >= 0:
            self.ui.cboSourceType.setCurrentIndex(sourceIndex)
        self.ui.txtFolderName.setText(folderName)
        self.addCboLayerItem()

        self.ui.wgtExportMap.setVisible(True)

    def edit_associated_map(self):
        #マップエクスポートウィジェットを開く
        row = self.ui.tblAssociatedMap.selectedIndexes()
        self.map_id = self.ui.tblAssociatedMap.model().data(row[0])
        mapTitle = self.ui.tblAssociatedMap.model().data(row[1])
        folderName = self.ui.tblAssociatedMap.model().data(row[2])
        script = self.ui.tblAssociatedMap.model().data(row[3])
        attribution = self.ui.tblAssociatedMap.model().data(row[4])
        self.ui.cboMapType.setCurrentIndex(self.ui.cboMapType.findText('Associated'))
        self.ui.txtMapTitle.setText(mapTitle)
        self.ui.txtFolderName.setText(folderName)
        self.ui.txtScript.setText(script)
        self.ui.txtAttribution.setText(attribution)
        self.addCboLayerItem()

        self.ui.wgtExportMap.setVisible(True)

    def btn_map_save_clicked(self):
        #マップエクスポートウィジェット保存ボタン押下時
        #入力チェック
        if self.ui.txtMapTitle.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The map title has not been entered. Please enter."))
        elif self.ui.txtFolderName.text() == '':
            QMessageBox.warning(self, u"Warning", self.tr(u"The folder name has not been entered. Please enter."))
        else:
            #map情報をデータベースに記録
            geolib = GeolibUtil()
            db = geolib.dbConnect(self.host_name, self.db_name, self.port_no, self.db_user_id, self.db_password)
            if db.open():
                mapType = self.ui.cboMapType.currentText()
                mapTitle = self.ui.txtMapTitle.text()
                sourceType = self.ui.cboSourceType.currentText()
                folderName = self.ui.txtFolderName.text()
                script = self.ui.txtScript.toPlainText()
                attribution = self.ui.txtAttribution.text()
                created =QDateTime.currentDateTime().toString("yyyy/MM/dd hh:mm:ss")
                modified = QDateTime.currentDateTime().toString("yyyy/MM/dd hh:mm:ss")
                query = QSqlQuery()
                if (self.map_id >0):
                    #更新
                    update_sql = "UPDATE maps SET" \
                                    " maptype = '" + mapType + "'" \
                                    ",title = '" + mapTitle + "'" \
                                    ",sourcetype = '" + sourceType + "'" \
                                    ",foldername  = '" + folderName + "'" \
                                    ",script =  '" + script + "'" \
                                    ",attribution = '" + attribution + "'" \
                                    ",modified = '" + modified + "'" \
                                    " WHERE id = " + str(self.map_id) + ";"
                    query.exec_("" + update_sql + "")
                    db.commit()
                else:
                    #新規追加
                    insert_sql = "INSERT INTO maps (article_id, maptype, title, sourcetype, foldername, script,  attribution, created)" \
                                    " VALUES (" + str(self.article_id) + "" \
                                    ", '" + mapType + "'" \
                                    ", '" + mapTitle + "'" \
                                    ", '" + sourceType + "'" \
                                    ", '" + folderName + "'" \
                                    ", '" + script + "'" \
                                    ", '" + attribution + "'" \
                                    ", '" + created + "'" \
                                    ");"
                    query.exec_("" + insert_sql + "")
                    db.commit()
                db.close()
            else:
                self.ui.lblMessage.setText(self.tr("Database connect error!"))

            #geojsonファイルをアップロード
            geolib = GeolibUtil()
            if mapType == 'Scenario':
                map_type = 'scenario'
            if mapType == 'Subject':
                map_type = 'subject'
            if mapType == 'Associated':
                map_type = 'associated'
            if self.ui.cboLayerData.currentIndex() >0:
                groupName = self.ui.cboLayerData.currentText()
                layer_folder = os.path.join(self.project_path,mapType).replace('/', os.sep)  #転送元フォルダ
                dest_layer_folder =  str(self.user_id) + "/"+ str(self.article_id) + '/'+map_type + '/' +folderName + '/'  #転送先フォルダ
                root = QgsProject.instance().layerTreeRoot()
                node = root.findGroup(mapType)
                group = node.findGroup(groupName)
                for treeLayer in group.children():
                    if isinstance(treeLayer, QgsLayerTreeNode):
                        layerName = treeLayer.name()
                        print (layerName)
                        layer = QgsProject.instance().mapLayersByName(layerName)[0]
                        if (isinstance(layer, QgsVectorLayer) and sourceType =='GeoJSON'):
                            #QgsVectorLayerの場合
                            file_name = os.path.join(layer_folder,layerName + '.geojson').replace('/', os.sep)
                            #GeoJSONを作成
                            QgsVectorFileWriter.writeAsVectorFormat(layer,file_name, 'utf-8', self.projectCrs, 'GeoJSON')
                        elif (isinstance(layer, QgsRasterLayer) and sourceType =='geoTIFF'):
                            #QgsRasterLayerの場合
                            file_name = layer.source().replace('/', os.sep)
                        #FTPで転送
                        geolib.ftpCreateFolder(dest_layer_folder)
                        geolib.ftpUploadFile(file_name, dest_layer_folder)

            self.ui.wgtExportMap.setVisible(False)
            self.dispArticleData(self.current_article_id)
            self.dispMapData(self.current_article_id)
            QMessageBox.information(self, u"Infomation", self.tr(u"Completed to save the map data and upload the map files."))

    def btn_map_delete_clicked(self):
    #マップ削除ボタン押下時
        _reply = QMessageBox.question(self, self.tr(u"Confirmation"),
                self.tr(u"All data and files in the map will be deleted.\n Are you sure?"),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if _reply == QMessageBox.Yes:
            #選択したマップデータおよびファイルをすべて削除
            mapType = self.ui.cboMapType.currentText()
            folderName = self.ui.txtFolderName.text()
            geolib = GeolibUtil()
            db = geolib.dbConnect(self.host_name, self.db_name, self.port_no, self.db_user_id, self.db_password)
            if db.open():
                query = QSqlQuery()
                if (self.map_id >0):
                    #更新
                    delete_sql = "DELETE FROM maps" \
                                    " WHERE id = " + str(self.map_id) + ";"
                    query.exec_("" + delete_sql + "")
                    db.commit()
                db.close()
            #フォルダまるごと削除
            if mapType == 'Scenario':
                map_type = 'scenario'
            if mapType == 'Subject':
                map_type = 'subject'
            if mapType == 'Associated':
                map_type = 'associated'
            map_folder =  str(self.user_id) + "/"+ str(self.article_id) + '/'+map_type + '/' +folderName + '/'  #転送先フォルダ
            geolib.ftpRmTree(map_folder)
            print(map_folder)

            self.ui.wgtExportMap.setVisible(False)
            self.dispArticleData(self.current_article_id)
            self.dispMapData(self.current_article_id)
            QMessageBox.information(self, u"Infomation", self.tr(u"Completed to delete the map data and files."))

    def btn_map_cancel_clicked(self):
        #マップエクスポートウィジェットキャンセルボタン押下時
        self.ui.wgtExportMap.setVisible(False)

    def btn_close_clicked(self):
    # キャンセルボタン押下時の処理
        # ダイアログを閉じる
        self.close()

    #コンボボックスアイテムのセット
    def addComboBoxItem(self):
        query = QSqlQuery()
        get_area_sql = "select title,id from areas order by id"
        query.exec_(get_area_sql)
        cb = self.ui.cboArea
        cb.clear()
        while query.next():
            cb.addItem(query.value(0), query.value(1))
        get_level_sql = "select title,id from levels order by id"
        query.exec_(get_level_sql)
        cb = self.ui.cboLevel
        cb.clear()
        while query.next():
            cb.addItem(query.value(0), query.value(1))

    #マップキャンバスの表示領域を取得
    def getGeometry(self):
        e = self.iface.mapCanvas().extent()
        xmax = str(e.xMaximum())
        ymax = str(e.yMaximum())
        xmin = str(e.xMinimum())
        ymin = str(e.yMinimum())
        self.geom = "(" + xmin + " " +ymin + "," + \
                 xmax + " " + ymin + "," + \
                 xmax + " " + ymax + "," + \
                 xmin + " " + ymax + "," + \
                 xmin + " " +ymin + ")"

    def addCboLayerItem(self):
        mapType = self.ui.cboMapType.currentText()
        if mapType != 'Associated':
            self.ui.cboLayerData.clear()
            self.ui.cboLayerData.addItem(self.tr('Do not export'))
            root = QgsProject.instance().layerTreeRoot()
            node = root.findGroup(mapType)
            group = []
            groupName = None
            for group in node.children():
                groupName = group.name()
                self.ui.cboLayerData.addItem(groupName)
            self.ui.frmScenario.setVisible(True)
            self.ui.frmAssociated.setVisible(False)
        else:
            self.ui.frmScenario.setVisible(False)
            self.ui.frmAssociated.setVisible(True)







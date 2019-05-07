# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDialog, QFileSystemModel,QApplication
import os
import os.path
import subprocess

from qgis.core import QgsProject
from .ui_html_edit_dialog import Ui_HtmlEditDialog


class HtmlEditDialog(QDialog, Ui_HtmlEditDialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface


        self.ui = Ui_HtmlEditDialog()
        self.ui.setupUi(self)
        # create model
        project = QgsProject.instance()
        project_path,ext = os.path.splitext(project.fileName())
        self.scenario_path = os.path.join(project_path,"Scenario","html")
        self.scenario_path =  self.scenario_path.replace('/','\\')
        self.model = QFileSystemModel()
        self.model.setRootPath( self.scenario_path )

        # set the model
        self.ui.lblPathName.setText(self.scenario_path)
        indexRoot = self.model.index(self.model.rootPath())
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(indexRoot)
        self.ui.treeView.setColumnWidth(0, 250)

        # シグナル
        #QObject.connect(self.ui.treeView, SIGNAL("clicked()"),self.tree_changed)
        self.ui.treeView.selectionModel().selectionChanged.connect(self.tree_selected)
        self.ui.btnExplorer.clicked.connect(self.btn_explorer_clicked)
        self.ui.btnNew.clicked.connect( self.btn_new_clicked)
        self.ui.btnEdit.clicked.connect(self.btn_edit_clicked)
        self.ui.btnPreview.clicked.connect( self.btn_preview_clicked)
        self.ui.btnCancel.clicked.connect( self.btn_cancel_clicked)

    #エクスプローラボタン押下時
    def btn_explorer_clicked(self):
        cmd = r'explorer /n ,/root,' + self.scenario_path
        os.system(cmd)

    #ツリー選択変更時の処理
    def tree_selected(self, index, oldIndex):
        indexItem = index.indexes()[0]
        # path or filename selected
        fileName = self.model.fileName(indexItem)
        # full path/filename selected
        filePath = self.model.filePath(indexItem)


        self.ui.lblFileName.setText(fileName)
        base, ext = os.path.splitext(fileName)
        self.ui.btnEdit.setEnabled(False)
        self.ui.btnPreview.setEnabled(False)
        if (ext != ''):
            #QtCore.QTextCodec.setCodecForCStrings( QtCore.QTextCodec.codecForLocale() )
            self.htmlName = self.model.filePath(indexItem)
            self.ui.btnEdit.setEnabled(True)
            self.ui.btnPreview.setEnabled(True)
            self.ui.txtNewFileName.setText("")

    def btn_edit_clicked(self):
        #選択されたファイルを外部プログラムで開く
        self.settings = QSettings()
        self.editor_progam = self.settings.value("geolib/editorProgram","")
        program_path = os.path.dirname(self.editor_progam)
        program_name = os.path.basename(self.editor_progam)
        cmd = program_name + ' "file:///' + self.htmlName + '"'

        #subprocess.Popen(r'"' + self.editor_progam +  ' file:///' + self.htmlName + '"')
        os.system('cd '+ program_path + ' && ' + cmd)

    def btn_preview_clicked(self):
        #選択されたファイルをブラウザで開く
        import webbrowser
        webbrowser.open(self.htmlName)

    def btn_new_clicked(self):
        #HTMLファイルを作成
        self.htmlName = os.path.join(self.scenario_path,(self.ui.txtNewFileName.text() + ".html"))
        htmlFile = open(self.htmlName, "w")
        htmlFile.write("<html><head><meta http-equiv='content-type' content='text/html; charset=UTF-8'></head><body></body></html>")
        htmlFile.close()

        #選択されたファイルを外部プログラムで開く
        self.settings = QSettings("settings.ini", QSettings.IniFormat)
        self.editor_progam = self.settings.value("geolib/editorProgram","")
        program_path = os.path.dirname(self.editor_progam)
        program_name = os.path.basename(self.editor_progam)
        cmd = program_name + ' "file:///' + self.htmlName + '"'

        os.system('cd '+ program_path + ' && ' + cmd)

    def btn_cancel_clicked(self):
        self.close()
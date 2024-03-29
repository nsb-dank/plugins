# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_draw_boundary_dockwidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DrawBoundaryDockWidget(object):
    def setupUi(self, DrawBoundaryDockWidget):
        DrawBoundaryDockWidget.setObjectName("DrawBoundaryDockWidget")
        DrawBoundaryDockWidget.resize(413, 433)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DrawBoundaryDockWidget.sizePolicy().hasHeightForWidth())
        DrawBoundaryDockWidget.setSizePolicy(sizePolicy)
        DrawBoundaryDockWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        DrawBoundaryDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.btnCancel = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnCancel.setGeometry(QtCore.QRect(210, 360, 171, 31))
        self.btnCancel.setObjectName("btnCancel")
        self.btnDrawStrike = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnDrawStrike.setGeometry(QtCore.QRect(30, 360, 171, 31))
        self.btnDrawStrike.setObjectName("btnDrawStrike")
        self.lblDip = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblDip.setGeometry(QtCore.QRect(250, 320, 41, 20))
        self.lblDip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblDip.setObjectName("lblDip")
        self.lblStrike = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblStrike.setGeometry(QtCore.QRect(250, 290, 51, 20))
        self.lblStrike.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblStrike.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblStrike.setObjectName("lblStrike")
        self.txtStrike = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.txtStrike.setGeometry(QtCore.QRect(300, 290, 81, 20))
        self.txtStrike.setMaxLength(10)
        self.txtStrike.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtStrike.setReadOnly(True)
        self.txtStrike.setObjectName("txtStrike")
        self.txtDip = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.txtDip.setGeometry(QtCore.QRect(300, 320, 81, 20))
        self.txtDip.setMaxLength(10)
        self.txtDip.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtDip.setReadOnly(True)
        self.txtDip.setObjectName("txtDip")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 391, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btnSelectFeature = QtWidgets.QPushButton(self.tab)
        self.btnSelectFeature.setGeometry(QtCore.QRect(10, 120, 361, 31))
        self.btnSelectFeature.setObjectName("btnSelectFeature")
        self.btnCancelFeature = QtWidgets.QPushButton(self.tab)
        self.btnCancelFeature.setGeometry(QtCore.QRect(10, 160, 361, 31))
        self.btnCancelFeature.setObjectName("btnCancelFeature")
        self.lblTargetLayer = QtWidgets.QLabel(self.tab)
        self.lblTargetLayer.setGeometry(QtCore.QRect(10, 70, 101, 21))
        self.lblTargetLayer.setObjectName("lblTargetLayer")
        self.cboTargerLayer = QtWidgets.QComboBox(self.tab)
        self.cboTargerLayer.setGeometry(QtCore.QRect(10, 90, 361, 22))
        self.cboTargerLayer.setObjectName("cboTargerLayer")
        self.lblMemo = QtWidgets.QLabel(self.tab)
        self.lblMemo.setGeometry(QtCore.QRect(10, 8, 251, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMemo.setFont(font)
        self.lblMemo.setObjectName("lblMemo")
        self.lblMemo_2 = QtWidgets.QLabel(self.tab)
        self.lblMemo_2.setGeometry(QtCore.QRect(10, 26, 351, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMemo_2.setFont(font)
        self.lblMemo_2.setObjectName("lblMemo_2")
        self.lblMemo_3 = QtWidgets.QLabel(self.tab)
        self.lblMemo_3.setGeometry(QtCore.QRect(10, 45, 351, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMemo_3.setFont(font)
        self.lblMemo_3.setObjectName("lblMemo_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lblDemLayer = QtWidgets.QLabel(self.tab_2)
        self.lblDemLayer.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.lblDemLayer.setObjectName("lblDemLayer")
        self.cboDemLayer = QtWidgets.QComboBox(self.tab_2)
        self.cboDemLayer.setGeometry(QtCore.QRect(80, 10, 291, 22))
        self.cboDemLayer.setObjectName("cboDemLayer")
        self.btnSelectPoints = QtWidgets.QPushButton(self.tab_2)
        self.btnSelectPoints.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.btnSelectPoints.setObjectName("btnSelectPoints")
        self.btnCalculate = QtWidgets.QPushButton(self.tab_2)
        self.btnCalculate.setGeometry(QtCore.QRect(50, 170, 151, 30))
        self.btnCalculate.setObjectName("btnCalculate")
        self.btnCancelPoints = QtWidgets.QPushButton(self.tab_2)
        self.btnCancelPoints.setGeometry(QtCore.QRect(210, 170, 141, 30))
        self.btnCancelPoints.setObjectName("btnCancelPoints")
        self.txtP2x = QtWidgets.QLineEdit(self.tab_2)
        self.txtP2x.setGeometry(QtCore.QRect(150, 100, 91, 20))
        self.txtP2x.setObjectName("txtP2x")
        self.txtP1x = QtWidgets.QLineEdit(self.tab_2)
        self.txtP1x.setGeometry(QtCore.QRect(50, 100, 91, 20))
        self.txtP1x.setObjectName("txtP1x")
        self.txtP3x = QtWidgets.QLineEdit(self.tab_2)
        self.txtP3x.setGeometry(QtCore.QRect(250, 100, 91, 20))
        self.txtP3x.setObjectName("txtP3x")
        self.lblP1 = QtWidgets.QLabel(self.tab_2)
        self.lblP1.setGeometry(QtCore.QRect(60, 80, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblP1.setFont(font)
        self.lblP1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblP1.setObjectName("lblP1")
        self.lblP2x = QtWidgets.QLabel(self.tab_2)
        self.lblP2x.setGeometry(QtCore.QRect(160, 80, 71, 20))
        self.lblP2x.setAlignment(QtCore.Qt.AlignCenter)
        self.lblP2x.setObjectName("lblP2x")
        self.lblP3 = QtWidgets.QLabel(self.tab_2)
        self.lblP3.setGeometry(QtCore.QRect(260, 80, 71, 20))
        self.lblP3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblP3.setObjectName("lblP3")
        self.txtP2y = QtWidgets.QLineEdit(self.tab_2)
        self.txtP2y.setGeometry(QtCore.QRect(150, 120, 91, 20))
        self.txtP2y.setObjectName("txtP2y")
        self.txtP3y = QtWidgets.QLineEdit(self.tab_2)
        self.txtP3y.setGeometry(QtCore.QRect(250, 120, 91, 20))
        self.txtP3y.setObjectName("txtP3y")
        self.txtP1y = QtWidgets.QLineEdit(self.tab_2)
        self.txtP1y.setGeometry(QtCore.QRect(50, 120, 91, 20))
        self.txtP1y.setObjectName("txtP1y")
        self.txtP2z = QtWidgets.QLineEdit(self.tab_2)
        self.txtP2z.setGeometry(QtCore.QRect(150, 140, 91, 20))
        self.txtP2z.setObjectName("txtP2z")
        self.txtP3z = QtWidgets.QLineEdit(self.tab_2)
        self.txtP3z.setGeometry(QtCore.QRect(250, 140, 91, 20))
        self.txtP3z.setObjectName("txtP3z")
        self.txtP1z = QtWidgets.QLineEdit(self.tab_2)
        self.txtP1z.setGeometry(QtCore.QRect(50, 140, 91, 20))
        self.txtP1z.setObjectName("txtP1z")
        self.lblP1_2 = QtWidgets.QLabel(self.tab_2)
        self.lblP1_2.setGeometry(QtCore.QRect(0, 100, 51, 16))
        self.lblP1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblP1_2.setObjectName("lblP1_2")
        self.lblP1_3 = QtWidgets.QLabel(self.tab_2)
        self.lblP1_3.setGeometry(QtCore.QRect(0, 120, 51, 16))
        self.lblP1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblP1_3.setObjectName("lblP1_3")
        self.lblP1_4 = QtWidgets.QLabel(self.tab_2)
        self.lblP1_4.setGeometry(QtCore.QRect(0, 140, 51, 16))
        self.lblP1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblP1_4.setObjectName("lblP1_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(14, 6, 250, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblStrike_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblStrike_2.setGeometry(QtCore.QRect(10, 290, 231, 20))
        self.lblStrike_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStrike_2.setObjectName("lblStrike_2")
        self.btnSettings = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnSettings.setGeometry(QtCore.QRect(30, 320, 70, 28))
        self.btnSettings.setObjectName("btnSettings")
        DrawBoundaryDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DrawBoundaryDockWidget)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DrawBoundaryDockWidget)
        DrawBoundaryDockWidget.setTabOrder(self.tabWidget, self.cboTargerLayer)
        DrawBoundaryDockWidget.setTabOrder(self.cboTargerLayer, self.btnSelectFeature)
        DrawBoundaryDockWidget.setTabOrder(self.btnSelectFeature, self.btnCancelFeature)
        DrawBoundaryDockWidget.setTabOrder(self.btnCancelFeature, self.cboDemLayer)
        DrawBoundaryDockWidget.setTabOrder(self.cboDemLayer, self.btnSelectPoints)
        DrawBoundaryDockWidget.setTabOrder(self.btnSelectPoints, self.btnCalculate)
        DrawBoundaryDockWidget.setTabOrder(self.btnCalculate, self.btnCancelPoints)
        DrawBoundaryDockWidget.setTabOrder(self.btnCancelPoints, self.btnDrawStrike)
        DrawBoundaryDockWidget.setTabOrder(self.btnDrawStrike, self.btnCancel)
        DrawBoundaryDockWidget.setTabOrder(self.btnCancel, self.txtP1x)
        DrawBoundaryDockWidget.setTabOrder(self.txtP1x, self.txtP2y)
        DrawBoundaryDockWidget.setTabOrder(self.txtP2y, self.txtP3x)
        DrawBoundaryDockWidget.setTabOrder(self.txtP3x, self.txtP3y)
        DrawBoundaryDockWidget.setTabOrder(self.txtP3y, self.txtP1y)
        DrawBoundaryDockWidget.setTabOrder(self.txtP1y, self.txtP2z)
        DrawBoundaryDockWidget.setTabOrder(self.txtP2z, self.txtP3z)
        DrawBoundaryDockWidget.setTabOrder(self.txtP3z, self.txtP1z)
        DrawBoundaryDockWidget.setTabOrder(self.txtP1z, self.txtP2x)
        DrawBoundaryDockWidget.setTabOrder(self.txtP2x, self.txtDip)
        DrawBoundaryDockWidget.setTabOrder(self.txtDip, self.txtStrike)

    def retranslateUi(self, DrawBoundaryDockWidget):
        _translate = QtCore.QCoreApplication.translate
        DrawBoundaryDockWidget.setWindowTitle(_translate("DrawBoundaryDockWidget", "Strike line drawing tool"))
        self.btnCancel.setText(_translate("DrawBoundaryDockWidget", "Remove Line"))
        self.btnDrawStrike.setText(_translate("DrawBoundaryDockWidget", "Draw Strike Line"))
        self.lblDip.setText(_translate("DrawBoundaryDockWidget", "Dip"))
        self.lblStrike.setText(_translate("DrawBoundaryDockWidget", "Strike"))
        self.btnSelectFeature.setText(_translate("DrawBoundaryDockWidget", "Get Strike/Dip value from selected point"))
        self.btnCancelFeature.setText(_translate("DrawBoundaryDockWidget", "Cancel"))
        self.lblTargetLayer.setText(_translate("DrawBoundaryDockWidget", "Target Layer"))
        self.lblMemo.setText(_translate("DrawBoundaryDockWidget", "Please set CRS as follows:"))
        self.lblMemo_2.setText(_translate("DrawBoundaryDockWidget", " - Current CRS: EPSG:3857"))
        self.lblMemo_3.setText(_translate("DrawBoundaryDockWidget", " - Source Layer CRS:EPSG:4326"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DrawBoundaryDockWidget", "Draw from Strike/Dip value"))
        self.lblDemLayer.setText(_translate("DrawBoundaryDockWidget", "DEM"))
        self.btnSelectPoints.setText(_translate("DrawBoundaryDockWidget", "Select 3 points on map canvas"))
        self.btnCalculate.setText(_translate("DrawBoundaryDockWidget", "Calculation"))
        self.btnCancelPoints.setText(_translate("DrawBoundaryDockWidget", "Cancel point"))
        self.lblP1.setText(_translate("DrawBoundaryDockWidget", "Point1"))
        self.lblP2x.setText(_translate("DrawBoundaryDockWidget", "Point2"))
        self.lblP3.setText(_translate("DrawBoundaryDockWidget", "Point3"))
        self.lblP1_2.setText(_translate("DrawBoundaryDockWidget", "Lon."))
        self.lblP1_3.setText(_translate("DrawBoundaryDockWidget", "Lat."))
        self.lblP1_4.setText(_translate("DrawBoundaryDockWidget", "Alt."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DrawBoundaryDockWidget", "3 Points Method"))
        self.label.setText(_translate("DrawBoundaryDockWidget", "Draw Strike Line"))
        self.lblStrike_2.setText(_translate("DrawBoundaryDockWidget", "Calculate with the followi:ng values"))
        self.btnSettings.setText(_translate("DrawBoundaryDockWidget", "Settings"))


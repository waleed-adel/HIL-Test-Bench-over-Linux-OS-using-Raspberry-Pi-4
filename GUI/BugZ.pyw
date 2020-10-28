# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BugZ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QRegExpValidator)
from PySide2.QtWidgets import *
from ctypes import *
import sys
import time
import os
from shutil import copy
import subprocess


os.system('cls')

import tkinter as tk
from tkinter import filedialog

global file_path
file_path = ""

global folder_path
folder_path = ""

global runFlag
runFlag = 0

global Connection_Flag
Connection_Flag = 0

##################################################################################
##################################################################################
##################################################################################
def file_explorer():
  global file_path
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename()
  
def folder_explorer():
  global folder_path
  root = tk.Tk()
  root.withdraw()
  folder_path = filedialog.askdirectory()
  
def showdialog():
  global runFlag
  msg = QMessageBox()
  if( runFlag == 1) :
    msg.setIcon(QMessageBox.Information)
    msg.setText("Started Executing Test")
    msg.setInformativeText("TestCase Path: " + str(folder_path) + "\TestCase.py")
  elif (runFlag == 2): 
    msg.setIcon(QMessageBox.Information)
    msg.setText("Started Executing Test")
    msg.setInformativeText("TestCase Path: " + str(file_path))
  else :
    msg.setIcon(QMessageBox.Warning)
    msg.setText("No Test found")
    msg.setDetailedText("Please generate or load a Test before pressing run")
 
  msg.setWindowTitle("Test Execution")
  msg.setStandardButtons(QMessageBox.Ok)
  #msg.buttonClicked.connect(msgbtn)
	
  retval = msg.exec_()
  #print("value of pressed message box button:", retval)
 
def DisconnectFirst_dialog():
  
  msg = QMessageBox()
  msg.setIcon(QMessageBox.Warning)
  msg.setText("Direct Mode is still running")
  msg.setDetailedText("Please diconnect the direct mode and try again")
  msg.setWindowTitle("Test Execution")
  msg.setStandardButtons(QMessageBox.Ok)
  
  #msg.buttonClicked.connect(msgbtn)
	
  retval = msg.exec_()
  #print("value of pressed message box button:", retval)
	
#def msgbtn(i):
 #  print("Button pressed is:",i.text())
##################################################################################
##################################################################################
##################################################################################



class Ui_BugZ(object):
    def setupUi(self, BugZ):
        if BugZ.objectName():
            BugZ.setObjectName(u"BugZ")
        # BugZ.resize(915, 624)
        BugZ.setFixedSize(915, 624)
        BugZ.setMinimumSize(QSize(91, 0))
        font = QFont()
        font.setBold(False)
        font.setWeight(50);
        BugZ.setFont(font)
        self.BenchMode_tabWidget = QTabWidget(BugZ)
        self.BenchMode_tabWidget.setObjectName(u"BenchMode_tabWidget")
        self.BenchMode_tabWidget.setGeometry(QRect(9, 169, 891, 451))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPixelSize(12)
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPixelSize(14)
        self.BenchMode_tabWidget.setFont(font8)
        self.BenchMode_tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #f"
                        "afafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}")
        self.BenchMode_tabWidget.setIconSize(QSize(16, 16))
        self.DirectMode_tab = QWidget()
        self.DirectMode_tab.setObjectName(u"DirectMode_tab")
        self.Peripherals_groupBox = QGroupBox(self.DirectMode_tab)
        self.Peripherals_groupBox.setObjectName(u"Peripherals_groupBox")
        self.Peripherals_groupBox.setGeometry(QRect(8, 12, 871, 411))
        self.Peripherals_groupBox.setFont(font1)
        self.Peripherals_groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color:  rgb(115,115,115);\n"
"	 color: white;\n"
"}")
        self.Peripherals_tabWidget = QTabWidget(self.Peripherals_groupBox)
        self.Peripherals_tabWidget.setObjectName(u"Peripherals_tabWidget")
        self.Peripherals_tabWidget.setGeometry(QRect(11, 20, 851, 381))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Peripherals_tabWidget.sizePolicy().hasHeightForWidth())
        self.Peripherals_tabWidget.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        self.Peripherals_tabWidget.setFont(font2)
        self.Peripherals_tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #f"
                        "afafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}")
        self.Peripherals_tabWidget.setIconSize(QSize(16, 16))
        self.MainFeatures_tab = QWidget()
        self.MainFeatures_tab.setObjectName(u"MainFeatures_tab")
        self.DigitalOutPins_groupBox = QGroupBox(self.MainFeatures_tab)
        self.DigitalOutPins_groupBox.setObjectName(u"DigitalOutPins_groupBox")
        self.DigitalOutPins_groupBox.setGeometry(QRect(10, 14, 401, 91))
        self.DigitalOutPins_groupBox.setFont(font1)
        self.horizontalLayout_10 = QHBoxLayout(self.DigitalOutPins_groupBox)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Channel1_groupBox = QGroupBox(self.DigitalOutPins_groupBox)
        self.Channel1_groupBox.setObjectName(u"Channel1_groupBox")
        sizePolicy.setHeightForWidth(self.Channel1_groupBox.sizePolicy().hasHeightForWidth())
        self.Channel1_groupBox.setSizePolicy(sizePolicy)
        self.Channel1_groupBox.setMaximumSize(QSize(91, 16777215))
        self.Channel1_groupBox.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.Channel1_groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_15 = QLabel(self.Channel1_groupBox)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setFont(font1)

        self.horizontalLayout.addWidget(self.label_15)

        self.Channel1_horizontalSlider = QSlider(self.Channel1_groupBox)
        self.Channel1_horizontalSlider.setObjectName(u"Channel1_horizontalSlider")
        self.Channel1_horizontalSlider.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Channel1_horizontalSlider.sizePolicy().hasHeightForWidth())
        self.Channel1_horizontalSlider.setSizePolicy(sizePolicy)
        self.Channel1_horizontalSlider.setMaximumSize(QSize(31, 16777215))
        self.Channel1_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.Channel1_horizontalSlider.setMaximum(1)
        self.Channel1_horizontalSlider.setValue(0)
        self.Channel1_horizontalSlider.setTracking(True)
        self.Channel1_horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.Channel1_horizontalSlider)

        self.label_16 = QLabel(self.Channel1_groupBox)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setFont(font1)

        self.horizontalLayout.addWidget(self.label_16)


        self.horizontalLayout_10.addWidget(self.Channel1_groupBox)

        self.Channel2_groupBox = QGroupBox(self.DigitalOutPins_groupBox)
        self.Channel2_groupBox.setObjectName(u"Channel2_groupBox")
        sizePolicy.setHeightForWidth(self.Channel2_groupBox.sizePolicy().hasHeightForWidth())
        self.Channel2_groupBox.setSizePolicy(sizePolicy)
        self.Channel2_groupBox.setMaximumSize(QSize(91, 16777215))
        self.Channel2_groupBox.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.Channel2_groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_17 = QLabel(self.Channel2_groupBox)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_17)

        self.Channel2_horizontalSlider = QSlider(self.Channel2_groupBox)
        self.Channel2_horizontalSlider.setObjectName(u"Channel2_horizontalSlider")
        self.Channel2_horizontalSlider.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Channel2_horizontalSlider.sizePolicy().hasHeightForWidth())
        self.Channel2_horizontalSlider.setSizePolicy(sizePolicy)
        self.Channel2_horizontalSlider.setMaximumSize(QSize(31, 16777215))
        self.Channel2_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.Channel2_horizontalSlider.setMaximum(1)
        self.Channel2_horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.Channel2_horizontalSlider)

        self.label_18 = QLabel(self.Channel2_groupBox)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_18)


        self.horizontalLayout_10.addWidget(self.Channel2_groupBox)

        self.Channel3_groupBox = QGroupBox(self.DigitalOutPins_groupBox)
        self.Channel3_groupBox.setObjectName(u"Channel3_groupBox")
        sizePolicy.setHeightForWidth(self.Channel3_groupBox.sizePolicy().hasHeightForWidth())
        self.Channel3_groupBox.setSizePolicy(sizePolicy)
        self.Channel3_groupBox.setMaximumSize(QSize(91, 16777215))
        self.Channel3_groupBox.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.Channel3_groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.Channel3_groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_13)

        self.Channel3_horizontalSlider = QSlider(self.Channel3_groupBox)
        self.Channel3_horizontalSlider.setObjectName(u"Channel3_horizontalSlider")
        self.Channel3_horizontalSlider.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Channel3_horizontalSlider.sizePolicy().hasHeightForWidth())
        self.Channel3_horizontalSlider.setSizePolicy(sizePolicy)
        self.Channel3_horizontalSlider.setMaximumSize(QSize(31, 16777215))
        self.Channel3_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.Channel3_horizontalSlider.setMaximum(1)
        self.Channel3_horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.Channel3_horizontalSlider)

        self.label_14 = QLabel(self.Channel3_groupBox)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_14)


        self.horizontalLayout_10.addWidget(self.Channel3_groupBox)

        self.Channel4_groupBox = QGroupBox(self.DigitalOutPins_groupBox)
        self.Channel4_groupBox.setObjectName(u"Channel4_groupBox")
        sizePolicy.setHeightForWidth(self.Channel4_groupBox.sizePolicy().hasHeightForWidth())
        self.Channel4_groupBox.setSizePolicy(sizePolicy)
        self.Channel4_groupBox.setMaximumSize(QSize(91, 16777215))
        self.Channel4_groupBox.setFont(font1)
        self.horizontalLayout_4 = QHBoxLayout(self.Channel4_groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_19 = QLabel(self.Channel4_groupBox)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_19)

        self.Channel4_horizontalSlider = QSlider(self.Channel4_groupBox)
        self.Channel4_horizontalSlider.setObjectName(u"Channel4_horizontalSlider")
        self.Channel4_horizontalSlider.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Channel4_horizontalSlider.sizePolicy().hasHeightForWidth())
        self.Channel4_horizontalSlider.setSizePolicy(sizePolicy)
        self.Channel4_horizontalSlider.setMaximumSize(QSize(31, 16777215))
        self.Channel4_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.Channel4_horizontalSlider.setMaximum(1)
        self.Channel4_horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.Channel4_horizontalSlider)

        self.label_20 = QLabel(self.Channel4_groupBox)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_20)


        self.horizontalLayout_10.addWidget(self.Channel4_groupBox)

        self.DigitalInPins_groupBox = QGroupBox(self.MainFeatures_tab)
        self.DigitalInPins_groupBox.setObjectName(u"DigitalInPins_groupBox")
        self.DigitalInPins_groupBox.setGeometry(QRect(10, 112, 401, 91))
        self.DigitalInPins_groupBox.setFont(font1)
        self.horizontalLayout_9 = QHBoxLayout(self.DigitalInPins_groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Channel5_groupBox = QGroupBox(self.DigitalInPins_groupBox)
        self.Channel5_groupBox.setObjectName(u"Channel5_groupBox")
        sizePolicy.setHeightForWidth(self.Channel5_groupBox.sizePolicy().hasHeightForWidth())
        self.Channel5_groupBox.setSizePolicy(sizePolicy)
        self.Channel5_groupBox.setMinimumSize(QSize(91, 0))
        self.Channel5_groupBox.setMaximumSize(QSize(91, 16777215))
        self.Channel5_groupBox.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.Channel5_groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Channel5_lcdNumber = QLCDNumber(self.Channel5_groupBox)
        self.Channel5_lcdNumber.setObjectName(u"Channel5_lcdNumber")
        sizePolicy.setHeightForWidth(self.Channel5_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Channel5_lcdNumber.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(9)
        self.Channel5_lcdNumber.setFont(font3)
        self.Channel5_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel5_lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_5.addWidget(self.Channel5_lcdNumber)


        self.horizontalLayout_9.addWidget(self.Channel5_groupBox)

        self.Channel6_groupBox = QGroupBox(self.DigitalInPins_groupBox)
        self.Channel6_groupBox.setObjectName(u"Channel6_groupBox")
        sizePolicy.setHeightForWidth(self.Channel6_groupBox.sizePolicy().hasHeightForWidth())
        self.Channel6_groupBox.setSizePolicy(sizePolicy)
        self.Channel6_groupBox.setMinimumSize(QSize(91, 0))
        self.Channel6_groupBox.setMaximumSize(QSize(91, 16777215))
        self.Channel6_groupBox.setFont(font1)
        self.horizontalLayout_6 = QHBoxLayout(self.Channel6_groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Channel6_lcdNumber = QLCDNumber(self.Channel6_groupBox)
        self.Channel6_lcdNumber.setObjectName(u"Channel6_lcdNumber")
        sizePolicy.setHeightForWidth(self.Channel6_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Channel6_lcdNumber.setSizePolicy(sizePolicy)
        self.Channel6_lcdNumber.setFont(font3)
        self.Channel6_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel6_lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_6.addWidget(self.Channel6_lcdNumber)


        self.horizontalLayout_9.addWidget(self.Channel6_groupBox)

        self.Channel7_groupBox = QGroupBox(self.DigitalInPins_groupBox)
        self.Channel7_groupBox.setObjectName(u"Channel7_groupBox")
        sizePolicy.setHeightForWidth(self.Channel7_groupBox.sizePolicy().hasHeightForWidth())
        self.Channel7_groupBox.setSizePolicy(sizePolicy)
        self.Channel7_groupBox.setMinimumSize(QSize(91, 0))
        self.Channel7_groupBox.setMaximumSize(QSize(91, 16777215))
        self.Channel7_groupBox.setFont(font1)
        self.horizontalLayout_7 = QHBoxLayout(self.Channel7_groupBox)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Channel7_lcdNumber = QLCDNumber(self.Channel7_groupBox)
        self.Channel7_lcdNumber.setObjectName(u"Channel7_lcdNumber")
        sizePolicy.setHeightForWidth(self.Channel7_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Channel7_lcdNumber.setSizePolicy(sizePolicy)
        self.Channel7_lcdNumber.setFont(font3)
        self.Channel7_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel7_lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_7.addWidget(self.Channel7_lcdNumber)


        self.horizontalLayout_9.addWidget(self.Channel7_groupBox)

        self.Channel8_groupBox = QGroupBox(self.DigitalInPins_groupBox)
        self.Channel8_groupBox.setObjectName(u"Channel8_groupBox")
        sizePolicy.setHeightForWidth(self.Channel8_groupBox.sizePolicy().hasHeightForWidth())
        self.Channel8_groupBox.setSizePolicy(sizePolicy)
        self.Channel8_groupBox.setMinimumSize(QSize(91, 0))
        self.Channel8_groupBox.setMaximumSize(QSize(91, 16777215))
        self.Channel8_groupBox.setFont(font1)
        self.horizontalLayout_8 = QHBoxLayout(self.Channel8_groupBox)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Channel8_lcdNumber = QLCDNumber(self.Channel8_groupBox)
        self.Channel8_lcdNumber.setObjectName(u"Channel8_lcdNumber")
        sizePolicy.setHeightForWidth(self.Channel8_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Channel8_lcdNumber.setSizePolicy(sizePolicy)
        self.Channel8_lcdNumber.setFont(font3)
        self.Channel8_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel8_lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_8.addWidget(self.Channel8_lcdNumber)


        self.horizontalLayout_9.addWidget(self.Channel8_groupBox)

        self.PWMInPins_groupBox = QGroupBox(self.MainFeatures_tab)
        self.PWMInPins_groupBox.setObjectName(u"PWMInPins_groupBox")
        self.PWMInPins_groupBox.setGeometry(QRect(440, 14, 401, 191))
        self.PWMInPins_groupBox.setFont(font1)
        self.PWMInPins_groupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.PWMInPins_groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Channel11_groupBox = QGroupBox(self.PWMInPins_groupBox)
        self.Channel11_groupBox.setObjectName(u"Channel11_groupBox")
        self.Channel11_groupBox.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.Channel11_groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Channel11_Frequency_label = QLabel(self.Channel11_groupBox)
        self.Channel11_Frequency_label.setObjectName(u"Channel11_Frequency_label")
        self.Channel11_Frequency_label.setFont(font1)

        self.gridLayout_4.addWidget(self.Channel11_Frequency_label, 0, 0, 1, 1)

        self.Channel11_Frequency_lcdNumber = QLCDNumber(self.Channel11_groupBox)
        self.Channel11_Frequency_lcdNumber.setObjectName(u"Channel11_Frequency_lcdNumber")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Channel11_Frequency_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Channel11_Frequency_lcdNumber.setSizePolicy(sizePolicy2)
        self.Channel11_Frequency_lcdNumber.setMaximumSize(QSize(100, 16777215))
        self.Channel11_Frequency_lcdNumber.setFont(font3)
        self.Channel11_Frequency_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel11_Frequency_lcdNumber.setDigitCount(8)
        self.Channel11_Frequency_lcdNumber.setMode(QLCDNumber.Dec)
        self.Channel11_Frequency_lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.Channel11_Frequency_lcdNumber.setProperty("value", 0.000000000000000)
        self.Channel11_Frequency_lcdNumber.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.Channel11_Frequency_lcdNumber, 0, 1, 1, 1)

        self.Channel11_DutyCycle_label = QLabel(self.Channel11_groupBox)
        self.Channel11_DutyCycle_label.setObjectName(u"Channel11_DutyCycle_label")
        self.Channel11_DutyCycle_label.setFont(font1)

        self.gridLayout_4.addWidget(self.Channel11_DutyCycle_label, 1, 0, 1, 1)

        self.Channel11_DutyCycle_lcdNumber = QLCDNumber(self.Channel11_groupBox)
        self.Channel11_DutyCycle_lcdNumber.setObjectName(u"Channel11_DutyCycle_lcdNumber")
        sizePolicy2.setHeightForWidth(self.Channel11_DutyCycle_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Channel11_DutyCycle_lcdNumber.setSizePolicy(sizePolicy2)
        self.Channel11_DutyCycle_lcdNumber.setMaximumSize(QSize(100, 16777215))
        self.Channel11_DutyCycle_lcdNumber.setFont(font3)
        self.Channel11_DutyCycle_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel11_DutyCycle_lcdNumber.setDigitCount(8)
        self.Channel11_DutyCycle_lcdNumber.setMode(QLCDNumber.Dec)
        self.Channel11_DutyCycle_lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_4.addWidget(self.Channel11_DutyCycle_lcdNumber, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.Channel11_groupBox)

        self.Channel12_groupBox = QGroupBox(self.PWMInPins_groupBox)
        self.Channel12_groupBox.setObjectName(u"Channel12_groupBox")
        self.Channel12_groupBox.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.Channel12_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Channel12_Frequency_label = QLabel(self.Channel12_groupBox)
        self.Channel12_Frequency_label.setObjectName(u"Channel12_Frequency_label")
        self.Channel12_Frequency_label.setFont(font1)

        self.gridLayout_3.addWidget(self.Channel12_Frequency_label, 0, 0, 1, 1)

        self.Channel12_Frequency_lcdNumber = QLCDNumber(self.Channel12_groupBox)
        self.Channel12_Frequency_lcdNumber.setObjectName(u"Channel12_Frequency_lcdNumber")
        sizePolicy2.setHeightForWidth(self.Channel12_Frequency_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Channel12_Frequency_lcdNumber.setSizePolicy(sizePolicy2)
        self.Channel12_Frequency_lcdNumber.setMaximumSize(QSize(100, 16777215))
        self.Channel12_Frequency_lcdNumber.setFont(font3)
        self.Channel12_Frequency_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel12_Frequency_lcdNumber.setDigitCount(8)
        self.Channel12_Frequency_lcdNumber.setMode(QLCDNumber.Dec)
        self.Channel12_Frequency_lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.Channel12_Frequency_lcdNumber, 0, 1, 1, 1)

        self.Channel12_DutyCycle_label = QLabel(self.Channel12_groupBox)
        self.Channel12_DutyCycle_label.setObjectName(u"Channel12_DutyCycle_label")
        self.Channel12_DutyCycle_label.setFont(font1)

        self.gridLayout_3.addWidget(self.Channel12_DutyCycle_label, 1, 0, 1, 1)

        self.Channel12_DutyCycle_lcdNumber = QLCDNumber(self.Channel12_groupBox)
        self.Channel12_DutyCycle_lcdNumber.setObjectName(u"Channel12_DutyCycle_lcdNumber")
        sizePolicy2.setHeightForWidth(self.Channel12_DutyCycle_lcdNumber.sizePolicy().hasHeightForWidth())
        self.Channel12_DutyCycle_lcdNumber.setSizePolicy(sizePolicy2)
        self.Channel12_DutyCycle_lcdNumber.setMaximumSize(QSize(100, 16777215))
        self.Channel12_DutyCycle_lcdNumber.setFont(font3)
        self.Channel12_DutyCycle_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel12_DutyCycle_lcdNumber.setDigitCount(8)
        self.Channel12_DutyCycle_lcdNumber.setMode(QLCDNumber.Dec)
        self.Channel12_DutyCycle_lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_3.addWidget(self.Channel12_DutyCycle_lcdNumber, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.Channel12_groupBox)

        self.PWMOutPins_groupBox = QGroupBox(self.MainFeatures_tab)
        self.PWMOutPins_groupBox.setObjectName(u"PWMOutPins_groupBox")
        self.PWMOutPins_groupBox.setGeometry(QRect(10, 211, 831, 141))
        self.PWMOutPins_groupBox.setFont(font1)
        self.PWMOutPins_groupBox.setStyleSheet(u"")
        self.Channel10_groupBox = QGroupBox(self.PWMOutPins_groupBox)
        self.Channel10_groupBox.setObjectName(u"Channel10_groupBox")
        self.Channel10_groupBox.setGeometry(QRect(420, 30, 401, 91))
        self.Channel10_groupBox.setFont(font1)
        self.Channel10_Frequency_label = QLabel(self.Channel10_groupBox)
        self.Channel10_Frequency_label.setObjectName(u"Channel10_Frequency_label")
        self.Channel10_Frequency_label.setGeometry(QRect(8, 21, 91, 16))
        self.Channel10_Frequency_label.setFont(font1)
        self.Channel10_lcdNumber = QLCDNumber(self.Channel10_groupBox)
        self.Channel10_lcdNumber.setObjectName(u"Channel10_lcdNumber")
        self.Channel10_lcdNumber.setGeometry(QRect(329, 54, 64, 23))
        self.Channel10_lcdNumber.setFont(font3)
        self.Channel10_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel10_lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.Channel10_horizontalSlider = QSlider(self.Channel10_groupBox)
        self.Channel10_horizontalSlider.setObjectName(u"Channel10_horizontalSlider")
        self.Channel10_horizontalSlider.setEnabled(True)
        self.Channel10_horizontalSlider.setGeometry(QRect(100, 54, 221, 22))
        self.Channel10_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.Channel10_horizontalSlider.setMaximum(100)
        self.Channel10_horizontalSlider.setValue(0)
        self.Channel10_horizontalSlider.setTracking(True)
        self.Channel10_horizontalSlider.setOrientation(Qt.Horizontal)
        self.Channel10_DutyCycle_label = QLabel(self.Channel10_groupBox)
        self.Channel10_DutyCycle_label.setObjectName(u"Channel10_DutyCycle_label")
        self.Channel10_DutyCycle_label.setGeometry(QRect(10, 55, 81, 16))
        self.Channel10_DutyCycle_label.setFont(font1)
        self.Channel10_FrequencyRange_lineEdit = QLineEdit(self.Channel10_groupBox)
        self.Channel10_FrequencyRange_lineEdit.setObjectName(u"Channel10_FrequencyRange_lineEdit")
        self.Channel10_FrequencyRange_lineEdit.setGeometry(QRect(252, 23, 141, 20))
        self.Channel10_FrequencyRange_lineEdit.setFont(font1)
        self.Channel10_FrequencyRange_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background: lightblue;\n"
"}\n"
"")
        self.Channel10_FrequencyRange_lineEdit.setReadOnly(True)
        self.Channel10_Frequency_spinBox = QSpinBox(self.Channel10_groupBox)
        self.Channel10_Frequency_spinBox.setObjectName(u"Channel10_Frequency_spinBox")
        self.Channel10_Frequency_spinBox.setGeometry(QRect(103, 22, 81, 21))
        self.Channel10_Frequency_spinBox.setFont(font1)
        self.Channel10_Frequency_spinBox.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QSpinBox::up-button{\n"
"    width: 0\n"
"}\n"
"QSpinBox::down-button{\n"
"    width: 0\n"
"}\n"
"")
        self.Channel10_Frequency_spinBox.setMaximum(30000000)
        self.Channel9_groupBox = QGroupBox(self.PWMOutPins_groupBox)
        self.Channel9_groupBox.setObjectName(u"Channel9_groupBox")
        self.Channel9_groupBox.setGeometry(QRect(10, 30, 401, 91))
        self.Channel9_groupBox.setFont(font1)
        self.Channel9_Frequency_label = QLabel(self.Channel9_groupBox)
        self.Channel9_Frequency_label.setObjectName(u"Channel9_Frequency_label")
        self.Channel9_Frequency_label.setGeometry(QRect(8, 23, 91, 16))
        self.Channel9_Frequency_label.setFont(font1)
        self.Channel9_lcdNumber = QLCDNumber(self.Channel9_groupBox)
        self.Channel9_lcdNumber.setObjectName(u"Channel9_lcdNumber")
        self.Channel9_lcdNumber.setGeometry(QRect(329, 54, 64, 23))
        self.Channel9_lcdNumber.setFont(font3)
        self.Channel9_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel9_lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.Channel9_horizontalSlider = QSlider(self.Channel9_groupBox)
        self.Channel9_horizontalSlider.setObjectName(u"Channel9_horizontalSlider")
        self.Channel9_horizontalSlider.setEnabled(True)
        self.Channel9_horizontalSlider.setGeometry(QRect(100, 54, 221, 22))
        self.Channel9_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.Channel9_horizontalSlider.setMaximum(100)
        self.Channel9_horizontalSlider.setValue(0)
        self.Channel9_horizontalSlider.setTracking(True)
        self.Channel9_horizontalSlider.setOrientation(Qt.Horizontal)
        self.Channel9_DutyCycle_label = QLabel(self.Channel9_groupBox)
        self.Channel9_DutyCycle_label.setObjectName(u"Channel9_DutyCycle_label")
        self.Channel9_DutyCycle_label.setGeometry(QRect(10, 55, 81, 16))
        self.Channel9_DutyCycle_label.setFont(font1)
        self.Channel9_FrequencyRange_lineEdit = QLineEdit(self.Channel9_groupBox)
        self.Channel9_FrequencyRange_lineEdit.setObjectName(u"Channel9_FrequencyRange_lineEdit")
        self.Channel9_FrequencyRange_lineEdit.setGeometry(QRect(252, 22, 141, 20))
        self.Channel9_FrequencyRange_lineEdit.setFont(font1)
        self.Channel9_FrequencyRange_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background: lightblue;\n"
"}\n"
"")
        self.Channel9_FrequencyRange_lineEdit.setReadOnly(True)
        self.Channel9_Frequency_spinBox = QSpinBox(self.Channel9_groupBox)
        self.Channel9_Frequency_spinBox.setObjectName(u"Channel9_Frequency_spinBox")
        self.Channel9_Frequency_spinBox.setGeometry(QRect(101, 22, 81, 21))
        self.Channel9_Frequency_spinBox.setFont(font1)
        self.Channel9_Frequency_spinBox.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QSpinBox::up-button{\n"
"    width: 0\n"
"}\n"
"QSpinBox::down-button{\n"
"    width: 0\n"
"}")
        self.Channel9_Frequency_spinBox.setSuffix(u"")
        self.Channel9_Frequency_spinBox.setMaximum(30000000)
        self.Channel9_Frequency_spinBox.setDisplayIntegerBase(10)
        self.Peripherals_tabWidget.addTab(self.MainFeatures_tab, "")
        self.BasicCommunication_tab = QWidget()
        self.BasicCommunication_tab.setObjectName(u"BasicCommunication_tab")
        self.UART_groupBox = QGroupBox(self.BasicCommunication_tab)
        self.UART_groupBox.setObjectName(u"UART_groupBox")
        self.UART_groupBox.setGeometry(QRect(12, 31, 251, 301))
        sizePolicy.setHeightForWidth(self.UART_groupBox.sizePolicy().hasHeightForWidth())
        self.UART_groupBox.setSizePolicy(sizePolicy)
        self.UART_groupBox.setFont(font1)
        self.UART_Enable_label = QLabel(self.UART_groupBox)
        self.UART_Enable_label.setObjectName(u"UART_Enable_label")
        self.UART_Enable_label.setGeometry(QRect(157, 265, 41, 16))
        self.UART_Enable_label.setFont(font1)
        self.UART_Disable_label = QLabel(self.UART_groupBox)
        self.UART_Disable_label.setObjectName(u"UART_Disable_label")
        self.UART_Disable_label.setGeometry(QRect(61, 263, 41, 20))
        self.UART_Disable_label.setFont(font1)
        self.UART_horizontalSlider = QSlider(self.UART_groupBox)
        self.UART_horizontalSlider.setObjectName(u"UART_horizontalSlider")
        self.UART_horizontalSlider.setEnabled(True)
        self.UART_horizontalSlider.setGeometry(QRect(110, 263, 31, 22))
        self.UART_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.UART_horizontalSlider.setMaximum(1)
        self.UART_horizontalSlider.setValue(0)
        self.UART_horizontalSlider.setTracking(True)
        self.UART_horizontalSlider.setOrientation(Qt.Horizontal)
        self.UART_BaudRate_comboBox = QComboBox(self.UART_groupBox)
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.addItem("")
        self.UART_BaudRate_comboBox.setObjectName(u"UART_BaudRate_comboBox")
        self.UART_BaudRate_comboBox.setGeometry(QRect(132, 31, 101, 21))
        self.UART_BaudRate_comboBox.setFont(font1)
        self.UART_BaudRate_comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"   width: 15px;\n"
"   border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(Down-Arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}")
        self.UART_BaudRate_label = QLabel(self.UART_groupBox)
        self.UART_BaudRate_label.setObjectName(u"UART_BaudRate_label")
        self.UART_BaudRate_label.setGeometry(QRect(16, 32, 101, 16))
        self.UART_BaudRate_label.setFont(font1)
        self.UART_DataSend_label = QLabel(self.UART_groupBox)
        self.UART_DataSend_label.setObjectName(u"UART_DataSend_label")
        self.UART_DataSend_label.setGeometry(QRect(16, 82, 111, 21))
        self.UART_DataSend_label.setFont(font1)
        self.UART_DataReceived_label = QLabel(self.UART_groupBox)
        self.UART_DataReceived_label.setObjectName(u"UART_DataReceived_label")
        self.UART_DataReceived_label.setGeometry(QRect(16, 190, 111, 21))
        # self.UART_DataReceived_label.setGeometry(QRect(16, 190, 101, 21))
        self.UART_DataReceived_label.setFont(font1)
        self.UART_DataSend_lineEdit = QLineEdit(self.UART_groupBox)
        '''
        Changes added from .py
        '''
        validator = QRegExpValidator("[0-9A-Fa-f]+")
        self.UART_DataSend_lineEdit.setValidator(validator)
        # End of Changes
        self.UART_DataSend_lineEdit.setObjectName(u"UART_DataSend_lineEdit")
        self.UART_DataSend_lineEdit.setEnabled(True)
        self.UART_DataSend_lineEdit.setGeometry(QRect(13, 107, 221, 31))
        self.UART_DataSend_lineEdit.setFont(font2)
        self.UART_DataSend_lineEdit.setAutoFillBackground(False)
        self.UART_DataSend_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.UART_DataSend_lineEdit.setFrame(True)
        self.UART_DataSend_lineEdit.setReadOnly(False)
        self.UART_DataSend_lineEdit.setClearButtonEnabled(True)
        self.UART_DataReceived_lineEdit = QLineEdit(self.UART_groupBox)
        self.UART_DataReceived_lineEdit.setObjectName(u"UART_DataReceived_lineEdit")
        self.UART_DataReceived_lineEdit.setEnabled(True)
        self.UART_DataReceived_lineEdit.setGeometry(QRect(13, 215, 221, 31))
        self.UART_DataReceived_lineEdit.setFont(font2)
        self.UART_DataReceived_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"")
        self.UART_DataReceived_lineEdit.setFrame(True)
        self.UART_DataReceived_lineEdit.setReadOnly(True)
        self.UART_DataReceived_lineEdit.setClearButtonEnabled(True)
        self.UART_SendData_pushButton = QPushButton(self.UART_groupBox)
        self.UART_SendData_pushButton.setObjectName(u"UART_SendData_pushButton")
        self.UART_SendData_pushButton.setGeometry(QRect(77, 150, 101, 21))
        sizePolicy.setHeightForWidth(self.UART_SendData_pushButton.sizePolicy().hasHeightForWidth())
        self.UART_SendData_pushButton.setSizePolicy(sizePolicy)
        self.UART_SendData_pushButton.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(7)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50);
        self.UART_SendData_pushButton.setFont(font4)
        self.UART_SendData_pushButton.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"	background-color: #05B8CC;\n"
"	border: 2px solid grey;\n"
"    border-width: 0px;\n"
"    border-radius: 10px;    \n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border-style: inset;\n"
"}")
        self.SPI_Channel_1_groupBox = QGroupBox(self.BasicCommunication_tab)
        self.SPI_Channel_1_groupBox.setObjectName(u"SPI_Channel_1_groupBox")
        self.SPI_Channel_1_groupBox.setGeometry(QRect(299, 31, 251, 301))
        self.SPI_Channel_1_groupBox.setFont(font1)
        self.SPI_Channel_1_Enable_label = QLabel(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_Enable_label.setObjectName(u"SPI_Channel_1_Enable_label")
        self.SPI_Channel_1_Enable_label.setGeometry(QRect(159, 265, 41, 16))
        self.SPI_Channel_1_Enable_label.setFont(font1)
        self.SPI_Channel_1_Disable_label = QLabel(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_Disable_label.setObjectName(u"SPI_Channel_1_Disable_label")
        self.SPI_Channel_1_Disable_label.setGeometry(QRect(63, 263, 41, 20))
        self.SPI_Channel_1_Disable_label.setFont(font1)
        self.SPI_Channel_1_horizontalSlider = QSlider(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_horizontalSlider.setObjectName(u"SPI_Channel_1_horizontalSlider")
        self.SPI_Channel_1_horizontalSlider.setEnabled(True)
        self.SPI_Channel_1_horizontalSlider.setGeometry(QRect(112, 263, 31, 22))
        self.SPI_Channel_1_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.SPI_Channel_1_horizontalSlider.setMaximum(1)
        self.SPI_Channel_1_horizontalSlider.setValue(0)
        self.SPI_Channel_1_horizontalSlider.setTracking(True)
        self.SPI_Channel_1_horizontalSlider.setOrientation(Qt.Horizontal)
        self.SPI_Channel_1_BaudRate_label = QLabel(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_BaudRate_label.setObjectName(u"SPI_Channel_1_BaudRate_label")
        self.SPI_Channel_1_BaudRate_label.setGeometry(QRect(16, 31, 101, 16))
        self.SPI_Channel_1_BaudRate_label.setFont(font1)
        self.SPI_Channel_1_DataSend_label = QLabel(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_DataSend_label.setObjectName(u"SPI_Channel_1_DataSend_label")
        self.SPI_Channel_1_DataSend_label.setGeometry(QRect(16, 82, 111, 21))
        self.SPI_Channel_1_DataSend_label.setFont(font1)
        self.SPI_Channel_1_DataReceived_label = QLabel(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_DataReceived_label.setObjectName(u"SPI_Channel_1_DataReceived_label")
        self.SPI_Channel_1_DataReceived_label.setGeometry(QRect(16, 190, 111, 21))
        self.SPI_Channel_1_DataReceived_label.setFont(font1)
        self.SPI_Channel_1_DataSend_lineEdit = QLineEdit(self.SPI_Channel_1_groupBox)
        '''
        Changes added from .py
        '''
        validator = QRegExpValidator("[0-9A-Fa-f]+")
        self.SPI_Channel_1_DataSend_lineEdit.setValidator(validator)
        # End of Changes
        self.SPI_Channel_1_DataSend_lineEdit.setObjectName(u"SPI_Channel_1_DataSend_lineEdit")
        self.SPI_Channel_1_DataSend_lineEdit.setEnabled(True)
        self.SPI_Channel_1_DataSend_lineEdit.setGeometry(QRect(13, 107, 221, 31))
        self.SPI_Channel_1_DataSend_lineEdit.setFont(font2)
        self.SPI_Channel_1_DataSend_lineEdit.setAutoFillBackground(False)
        self.SPI_Channel_1_DataSend_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.SPI_Channel_1_DataSend_lineEdit.setFrame(True)
        self.SPI_Channel_1_DataSend_lineEdit.setReadOnly(False)
        self.SPI_Channel_1_DataSend_lineEdit.setClearButtonEnabled(True)
        self.SPI_Channel_1_DataReceived_lineEdit = QLineEdit(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_DataReceived_lineEdit.setObjectName(u"SPI_Channel_1_DataReceived_lineEdit")
        self.SPI_Channel_1_DataReceived_lineEdit.setEnabled(True)
        self.SPI_Channel_1_DataReceived_lineEdit.setGeometry(QRect(13, 215, 221, 31))
        self.SPI_Channel_1_DataReceived_lineEdit.setFont(font2)
        self.SPI_Channel_1_DataReceived_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"")
        self.SPI_Channel_1_DataReceived_lineEdit.setFrame(True)
        self.SPI_Channel_1_DataReceived_lineEdit.setReadOnly(True)
        self.SPI_Channel_1_DataReceived_lineEdit.setClearButtonEnabled(True)
        self.SPI_Channel_1_BaudRate_spinBox = QSpinBox(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_BaudRate_spinBox.setObjectName(u"SPI_Channel_1_BaudRate_spinBox")
        self.SPI_Channel_1_BaudRate_spinBox.setGeometry(QRect(120, 31, 121, 21))
        self.SPI_Channel_1_BaudRate_spinBox.setFont(font1)
        self.SPI_Channel_1_BaudRate_spinBox.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QSpinBox::up-button{\n"
"    width: 0\n"
"}\n"
"QSpinBox::down-button{\n"
"    width: 0\n"
"}")
        self.SPI_Channel_1_BaudRate_spinBox.setSuffix(u"")
        self.SPI_Channel_1_BaudRate_spinBox.setMinimum(32000)
        self.SPI_Channel_1_BaudRate_spinBox.setMaximum(30000000)
        self.SPI_Channel_1_BaudRate_spinBox.setValue(32000)
        self.SPI_Channel_1_BaudRate_spinBox.setDisplayIntegerBase(10)
        self.SPI_Channel_1_BaudRateRange_lineEdit = QLineEdit(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_BaudRateRange_lineEdit.setObjectName(u"SPI_Channel_1_BaudRateRange_lineEdit")
        self.SPI_Channel_1_BaudRateRange_lineEdit.setGeometry(QRect(120, 56, 121, 20))
        font66 = QFont()
        font66.setFamily(u"Segoe UI")
        font66.setPixelSize(11)
        self.SPI_Channel_1_BaudRateRange_lineEdit.setFont(font66)
        self.SPI_Channel_1_BaudRateRange_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background: lightblue;\n"
"}\n"
"")
        self.SPI_Channel_1_BaudRateRange_lineEdit.setReadOnly(True)
        self.SPI_Channel_1_SendData_pushButton = QPushButton(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_SendData_pushButton.setObjectName(u"SPI_Channel_1_SendData_pushButton")
        self.SPI_Channel_1_SendData_pushButton.setGeometry(QRect(77, 150, 101, 21))
        sizePolicy.setHeightForWidth(self.SPI_Channel_1_SendData_pushButton.sizePolicy().hasHeightForWidth())
        self.SPI_Channel_1_SendData_pushButton.setSizePolicy(sizePolicy)
        self.SPI_Channel_1_SendData_pushButton.setMinimumSize(QSize(0, 0))
        self.SPI_Channel_1_SendData_pushButton.setFont(font4)
        self.SPI_Channel_1_SendData_pushButton.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"	background-color: #05B8CC;\n"
"	border: 2px solid grey;\n"
"    border-width: 0px;\n"
"    border-radius: 10px;    \n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border-style: inset;\n"
"}")
        self.SPI_Channel_2_groupBox = QGroupBox(self.BasicCommunication_tab)
        self.SPI_Channel_2_groupBox.setObjectName(u"SPI_Channel_2_groupBox")
        self.SPI_Channel_2_groupBox.setGeometry(QRect(584, 31, 251, 301))
        self.SPI_Channel_2_groupBox.setFont(font1)
        self.SPI_Channel_2_Enable_label = QLabel(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_Enable_label.setObjectName(u"SPI_Channel_2_Enable_label")
        self.SPI_Channel_2_Enable_label.setGeometry(QRect(163, 265, 41, 16))
        self.SPI_Channel_2_Enable_label.setFont(font1)
        self.SPI_Channel_2_Disable_label = QLabel(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_Disable_label.setObjectName(u"SPI_Channel_2_Disable_label")
        self.SPI_Channel_2_Disable_label.setGeometry(QRect(67, 263, 41, 20))
        self.SPI_Channel_2_Disable_label.setFont(font1)
        self.SPI_Channel_2_horizontalSlider = QSlider(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_horizontalSlider.setObjectName(u"SPI_Channel_2_horizontalSlider")
        self.SPI_Channel_2_horizontalSlider.setEnabled(True)
        self.SPI_Channel_2_horizontalSlider.setGeometry(QRect(116, 263, 31, 22))
        self.SPI_Channel_2_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.SPI_Channel_2_horizontalSlider.setMaximum(1)
        self.SPI_Channel_2_horizontalSlider.setValue(0)
        self.SPI_Channel_2_horizontalSlider.setTracking(True)
        self.SPI_Channel_2_horizontalSlider.setOrientation(Qt.Horizontal)
        self.SPI_Channel_2_BaudRate_label = QLabel(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_BaudRate_label.setObjectName(u"SPI_Channel_2_BaudRate_label")
        self.SPI_Channel_2_BaudRate_label.setGeometry(QRect(16, 31, 101, 16))
        self.SPI_Channel_2_BaudRate_label.setFont(font1)
        self.SPI_Channel_2_DataSend_label = QLabel(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_DataSend_label.setObjectName(u"SPI_Channel_2_DataSend_label")
        self.SPI_Channel_2_DataSend_label.setGeometry(QRect(16, 82, 111, 21))
        self.SPI_Channel_2_DataSend_label.setFont(font1)
        self.SPI_Channel_2_DataReceived_label = QLabel(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_DataReceived_label.setObjectName(u"SPI_Channel_2_DataReceived_label")
        self.SPI_Channel_2_DataReceived_label.setGeometry(QRect(20, 190, 111, 21))
        self.SPI_Channel_2_DataReceived_label.setFont(font1)
        self.SPI_Channel_2_DataSend_lineEdit = QLineEdit(self.SPI_Channel_2_groupBox)
        '''
        Changes added from .py
        '''
        validator = QRegExpValidator("[0-9A-Fa-f]+")
        self.SPI_Channel_2_DataSend_lineEdit.setValidator(validator)
        # End of Changes
        self.SPI_Channel_2_DataSend_lineEdit.setObjectName(u"SPI_Channel_2_DataSend_lineEdit")
        self.SPI_Channel_2_DataSend_lineEdit.setEnabled(True)
        self.SPI_Channel_2_DataSend_lineEdit.setGeometry(QRect(13, 107, 221, 31))
        self.SPI_Channel_2_DataSend_lineEdit.setFont(font2)
        self.SPI_Channel_2_DataSend_lineEdit.setAutoFillBackground(False)
        self.SPI_Channel_2_DataSend_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.SPI_Channel_2_DataSend_lineEdit.setFrame(True)
        self.SPI_Channel_2_DataSend_lineEdit.setReadOnly(False)
        self.SPI_Channel_2_DataSend_lineEdit.setClearButtonEnabled(True)
        self.SPI_Channel_2_DataReceived_lineEdit = QLineEdit(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_DataReceived_lineEdit.setObjectName(u"SPI_Channel_2_DataReceived_lineEdit")
        self.SPI_Channel_2_DataReceived_lineEdit.setEnabled(True)
        self.SPI_Channel_2_DataReceived_lineEdit.setGeometry(QRect(17, 215, 221, 31))
        self.SPI_Channel_2_DataReceived_lineEdit.setFont(font2)
        self.SPI_Channel_2_DataReceived_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"")
        self.SPI_Channel_2_DataReceived_lineEdit.setFrame(True)
        self.SPI_Channel_2_DataReceived_lineEdit.setReadOnly(True)
        self.SPI_Channel_2_DataReceived_lineEdit.setClearButtonEnabled(True)
        self.SPI_Channel_2_BaudRate_spinBox = QSpinBox(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_BaudRate_spinBox.setObjectName(u"SPI_Channel_2_BaudRate_spinBox")
        self.SPI_Channel_2_BaudRate_spinBox.setGeometry(QRect(120, 31, 121, 21))
        self.SPI_Channel_2_BaudRate_spinBox.setFont(font1)
        self.SPI_Channel_2_BaudRate_spinBox.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QSpinBox::up-button{\n"
"    width: 0\n"
"}\n"
"QSpinBox::down-button{\n"
"    width: 0\n"
"}")
        self.SPI_Channel_2_BaudRate_spinBox.setSuffix(u"")
        self.SPI_Channel_2_BaudRate_spinBox.setMinimum(32000)
        self.SPI_Channel_2_BaudRate_spinBox.setMaximum(30000000)
        self.SPI_Channel_2_BaudRate_spinBox.setValue(32000)
        self.SPI_Channel_2_BaudRate_spinBox.setDisplayIntegerBase(10)
        self.SPI_Channel_2_BaudRateRange_lineEdit = QLineEdit(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_BaudRateRange_lineEdit.setObjectName(u"SPI_Channel_2_BaudRateRange_lineEdit")
        self.SPI_Channel_2_BaudRateRange_lineEdit.setGeometry(QRect(120, 56, 121, 20))
        self.SPI_Channel_2_BaudRateRange_lineEdit.setFont(font66)
        self.SPI_Channel_2_BaudRateRange_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background: lightblue;\n"
"}\n"
"")
        self.SPI_Channel_2_BaudRateRange_lineEdit.setReadOnly(True)
        self.SPI_Channel_2_SendData_pushButton = QPushButton(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_SendData_pushButton.setObjectName(u"SPI_Channel_2_SendData_pushButton")
        self.SPI_Channel_2_SendData_pushButton.setGeometry(QRect(79, 150, 101, 21))
        sizePolicy.setHeightForWidth(self.SPI_Channel_2_SendData_pushButton.sizePolicy().hasHeightForWidth())
        self.SPI_Channel_2_SendData_pushButton.setSizePolicy(sizePolicy)
        self.SPI_Channel_2_SendData_pushButton.setMinimumSize(QSize(0, 0))
        self.SPI_Channel_2_SendData_pushButton.setFont(font4)
        self.SPI_Channel_2_SendData_pushButton.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"	background-color: #05B8CC;\n"
"	border: 2px solid grey;\n"
"    border-width: 0px;\n"
"    border-radius: 10px;    \n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border-style: inset;\n"
"}")
        self.Peripherals_tabWidget.addTab(self.BasicCommunication_tab, "")
        self.AutomotiveCommunication_tab = QWidget()
        self.AutomotiveCommunication_tab.setObjectName(u"AutomotiveCommunication_tab")
        self.UART_DataReceived_lineEdit_2 = QLineEdit(self.AutomotiveCommunication_tab)
        self.UART_DataReceived_lineEdit_2.setObjectName(u"UART_DataReceived_lineEdit_2")
        self.UART_DataReceived_lineEdit_2.setEnabled(True)
        self.UART_DataReceived_lineEdit_2.setGeometry(QRect(10, 16, 831, 341))
        self.UART_DataReceived_lineEdit_2.setFont(font2)
        self.UART_DataReceived_lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: 2px rgb(5,184,204);\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: rgb(5,184,204,20%);\n"
"    selection-background-color: darkgray;\n"
"}")
        self.UART_DataReceived_lineEdit_2.setFrame(True)
        self.UART_DataReceived_lineEdit_2.setReadOnly(True)
        self.UART_DataReceived_lineEdit_2.setClearButtonEnabled(True)
        self.label = QLabel(self.AutomotiveCommunication_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 94, 641, 91))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(43)
        font5.setBold(True)
        font5.setWeight(75);
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: white")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.AutomotiveCommunication_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 226, 371, 51))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(18)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: white")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.Peripherals_tabWidget.addTab(self.AutomotiveCommunication_tab, "")
        self.BenchMode_tabWidget.addTab(self.DirectMode_tab, "")
        self.HIL_Mode_Tab = QWidget()
        self.HIL_Mode_Tab.setObjectName(u"HIL_Mode_Tab")
        self.HILModeFeatures_groupBox = QGroupBox(self.HIL_Mode_Tab)
        self.HILModeFeatures_groupBox.setObjectName(u"HILModeFeatures_groupBox")
        self.HILModeFeatures_groupBox.setGeometry(QRect(4, 12, 871, 411))
        self.HILModeFeatures_groupBox.setFont(font1)
        self.HILModeFeatures_groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color:  rgb(115,115,115);\n"
"	 color: white;\n"
"}")
        self.Run_pushButton = QPushButton(self.HILModeFeatures_groupBox)
        self.Run_pushButton.setObjectName(u"Run_pushButton")
        self.Run_pushButton.setGeometry(QRect(654, 350, 178, 41))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50);
        self.Run_pushButton.setFont(font7)
        self.Run_pushButton.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"	background-color: #05B8CC;\n"
"	border: 2px solid grey;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;    \n"
"     \n"
"	min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border-style: inset;\n"
"}")
        self.GenerateMode_groupBox = QGroupBox(self.HILModeFeatures_groupBox)
        self.GenerateMode_groupBox.setObjectName(u"GenerateMode_groupBox")
        self.GenerateMode_groupBox.setGeometry(QRect(27, 112, 821, 91))
        self.GenerateMode_groupBox.setFont(font1)
        self.GenerateMode_groupBox.setCheckable(False)
        self.GenerateMode_groupBox.setChecked(False)
        self.GenerateMode_Path_lineEdit = QLineEdit(self.GenerateMode_groupBox)
        self.GenerateMode_Path_lineEdit.setObjectName(u"GenerateMode_Path_lineEdit")
        self.GenerateMode_Path_lineEdit.setEnabled(True)
        self.GenerateMode_Path_lineEdit.setGeometry(QRect(20, 42, 331, 31))
        self.GenerateMode_Path_lineEdit.setFont(font2)
        self.GenerateMode_Path_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"")
        self.GenerateMode_Path_lineEdit.setFrame(True)
        self.GenerateMode_Path_lineEdit.setReadOnly(True)
        self.GenerateMode_Path_lineEdit.setClearButtonEnabled(True)
        self.GenerateTestCase_comboBox = QComboBox(self.GenerateMode_groupBox)
        self.GenerateTestCase_comboBox.addItem("")
        self.GenerateTestCase_comboBox.addItem("")
        self.GenerateTestCase_comboBox.setObjectName(u"GenerateTestCase_comboBox")
        self.GenerateTestCase_comboBox.setGeometry(QRect(370, 42, 211, 31))
        self.GenerateTestCase_comboBox.setFont(font1)
        self.GenerateTestCase_comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"   width: 15px;\n"
"   border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(Down-Arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}")
        self.GeneratePath_label = QLabel(self.GenerateMode_groupBox)
        self.GeneratePath_label.setObjectName(u"GeneratePath_label")
        self.GeneratePath_label.setGeometry(QRect(27, 16, 24, 16))
        self.GeneratePath_label.setFont(font1)
        self.Generate_pushButton = QPushButton(self.GenerateMode_groupBox)
        self.Generate_pushButton.setObjectName(u"Generate_pushButton")
        self.Generate_pushButton.setGeometry(QRect(618, 32, 178, 41))
        self.Generate_pushButton.setFont(font7)
        self.Generate_pushButton.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"	background-color: darkgray;\n"
"	border: 2px solid grey;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;    \n"
"     \n"
"	min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border-style: inset;\n"
"}")
        self.LoadMode_groupBox = QGroupBox(self.HILModeFeatures_groupBox)
        self.LoadMode_groupBox.setObjectName(u"LoadMode_groupBox")
        self.LoadMode_groupBox.setEnabled(False)
        self.LoadMode_groupBox.setGeometry(QRect(28, 227, 821, 91))
        self.LoadMode_groupBox.setFont(font1)
        self.LoadMode_groupBox.setFlat(False)
        self.LoadMode_groupBox.setCheckable(False)
        self.LoadMode_groupBox.setChecked(False)
        self.LoadMode_Path_lineEdit = QLineEdit(self.LoadMode_groupBox)
        self.LoadMode_Path_lineEdit.setObjectName(u"LoadMode_Path_lineEdit")
        self.LoadMode_Path_lineEdit.setEnabled(True)
        self.LoadMode_Path_lineEdit.setGeometry(QRect(20, 43, 561, 31))
        self.LoadMode_Path_lineEdit.setFont(font2)
        self.LoadMode_Path_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"")
        self.LoadMode_Path_lineEdit.setFrame(True)
        self.LoadMode_Path_lineEdit.setReadOnly(True)
        self.LoadMode_Path_lineEdit.setClearButtonEnabled(True)
        self.LoadPath_label = QLabel(self.LoadMode_groupBox)
        self.LoadPath_label.setObjectName(u"LoadPath_label")
        self.LoadPath_label.setGeometry(QRect(27, 17, 24, 16))
        
        self.LoadPath_label.setFont(font1)
        self.Note_label = QLabel(self.HILModeFeatures_groupBox)
        self.Note_label.setObjectName(u"Note_label")
        self.Note_label.setGeometry(QRect(50, 360, 450, 16))
        self.Note_label.setFont(font1)
        self.Note_label.setStyleSheet(u"QLabel {\n"
"    color: grey;\n"
"}\n"
"")
        self.Note_label.setVisible(False)

        self.Load_pushButton = QPushButton(self.LoadMode_groupBox)
        self.Load_pushButton.setObjectName(u"Load_pushButton")
        self.Load_pushButton.setGeometry(QRect(620, 33, 178, 41))
        self.Load_pushButton.setFont(font7)
        self.Load_pushButton.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"	background-color: darkgray;\n"
"	border: 2px solid grey;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;    \n"
"     \n"
"	min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border-style: inset;\n"
"}")
        self.ModeSelect_groupBox = QGroupBox(self.HILModeFeatures_groupBox)
        self.ModeSelect_groupBox.setObjectName(u"ModeSelect_groupBox")
        self.ModeSelect_groupBox.setGeometry(QRect(270, 32, 341, 61))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ModeSelect_groupBox.sizePolicy().hasHeightForWidth())
        self.ModeSelect_groupBox.setSizePolicy(sizePolicy3)
        self.ModeSelect_groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.ModeSelect_groupBox.setFont(font1)
        self.label_21 = QLabel(self.ModeSelect_groupBox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(16, 24, 117, 16))
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setFont(font1)
        self.ModeSelect_horizontalSlider = QSlider(self.ModeSelect_groupBox)
        self.ModeSelect_horizontalSlider.setObjectName(u"ModeSelect_horizontalSlider")
        self.ModeSelect_horizontalSlider.setEnabled(True)
        self.ModeSelect_horizontalSlider.setGeometry(QRect(155, 22, 31, 22))
        sizePolicy.setHeightForWidth(self.ModeSelect_horizontalSlider.sizePolicy().hasHeightForWidth())
        self.ModeSelect_horizontalSlider.setSizePolicy(sizePolicy)
        self.ModeSelect_horizontalSlider.setMaximumSize(QSize(31, 16777215))
        self.ModeSelect_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(215,215,215) ;\n"
"	border: 0px solid #424242; \n"
"	height: 10px; \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: #05B8CC; \n"
"	border: 2px solid #05B8CC; \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}r")
        self.ModeSelect_horizontalSlider.setMaximum(1)
        self.ModeSelect_horizontalSlider.setOrientation(Qt.Horizontal)
        self.label_22 = QLabel(self.ModeSelect_groupBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(206, 24, 112, 16))
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setFont(font1)
        self.BenchMode_tabWidget.addTab(self.HIL_Mode_Tab, "")
        self.Info_Tab = QWidget()
        self.Info_Tab.setObjectName(u"Info_Tab")
        self.BenchMode_tabWidget.addTab(self.Info_Tab, "")
        self.Conncetion_groupBox = QGroupBox(BugZ)
        self.Conncetion_groupBox.setObjectName(u"Conncetion_groupBox")
        self.Conncetion_groupBox.setGeometry(QRect(115, 10, 681, 151))
        self.Conncetion_groupBox.setFont(font2)
        self.Conncetion_groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color:  rgb(115,115,115);\n"
"	 color: white;\n"
"}")
        self.Server_Configurations_groupBox = QGroupBox(self.Conncetion_groupBox)
        self.Server_Configurations_groupBox.setObjectName(u"Server_Configurations_groupBox")
        self.Server_Configurations_groupBox.setGeometry(QRect(15, 23, 191, 111))
        self.Server_Configurations_groupBox.setFont(font2)
        self.Server_Configurations_groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color:  rgb(115,115,115);\n"
"	 color: white;\n"
"}")
        self.Server_Number_comboBox = QComboBox(self.Server_Configurations_groupBox)
        self.Server_Number_comboBox.addItem("")
        self.Server_Number_comboBox.addItem("")
        self.Server_Number_comboBox.addItem("")
        self.Server_Number_comboBox.setObjectName(u"Server_Number_comboBox")
        self.Server_Number_comboBox.setGeometry(QRect(80, 28, 101, 22))
        font77 = QFont()
        font77.setFamily(u"Segoe UI")
        font77.setPixelSize(12)        
        self.Server_Number_comboBox.setFont(font77)
        self.Server_Number_comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 6px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"   width: 15px;\n"
"   border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(Down-Arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}")
        self.Server_Number_label = QLabel(self.Server_Configurations_groupBox)
        self.Server_Number_label.setObjectName(u"Server_Number_label")
        self.Server_Number_label.setGeometry(QRect(10, 31, 61, 16))
        self.Server_Number_label.setFont(font1)
        self.Server_IP_label = QLabel(self.Server_Configurations_groupBox)
        self.Server_IP_label.setObjectName(u"Server_IP_label")
        self.Server_IP_label.setGeometry(QRect(10, 59, 61, 16))
        self.Server_IP_label.setFont(font1)
        self.Server_IP_lineEdit = QLineEdit(self.Server_Configurations_groupBox)
        self.Server_IP_lineEdit.setObjectName(u"Server_IP_lineEdit")
        self.Server_IP_lineEdit.setEnabled(True)
        self.Server_IP_lineEdit.setGeometry(QRect(81, 57, 101, 20))
        self.Server_IP_lineEdit.setFont(font1)
        self.Server_IP_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background: lightblue;\n"
"}\n"
"")
        self.Server_IP_lineEdit.setReadOnly(True)
        self.Server_Port_lineEdit = QLineEdit(self.Server_Configurations_groupBox)
        self.Server_Port_lineEdit.setObjectName(u"Server_Port_lineEdit")
        self.Server_Port_lineEdit.setEnabled(True)
        self.Server_Port_lineEdit.setGeometry(QRect(81, 83, 101, 20))
        self.Server_Port_lineEdit.setFont(font1)
        self.Server_Port_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background: lightblue;\n"
"}\n"
"")
        self.Server_Port_lineEdit.setReadOnly(True)
        self.Server_Port_label = QLabel(self.Server_Configurations_groupBox)
        self.Server_Port_label.setObjectName(u"Server_Port_label")
        self.Server_Port_label.setGeometry(QRect(10, 85, 61, 16))
        self.Server_Port_label.setFont(font1)
        self.Conncetion_Access_groupBox = QGroupBox(self.Conncetion_groupBox)
        self.Conncetion_Access_groupBox.setObjectName(u"Conncetion_Access_groupBox")
        self.Conncetion_Access_groupBox.setGeometry(QRect(224, 23, 441, 111))
        self.Conncetion_Access_groupBox.setFont(font2)
        self.Conncetion_Access_groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color:  rgb(115,115,115);\n"
"	 color: white;\n"
"}")
        self.Disconnect_pushButton = QPushButton(self.Conncetion_Access_groupBox)
        self.Disconnect_pushButton.setObjectName(u"Disconnect_pushButton")
        self.Disconnect_pushButton.setGeometry(QRect(237, 23, 176, 41))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(12)
        self.Disconnect_pushButton.setFont(font8)
        self.Disconnect_pushButton.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"	background-color: rgb(175,175,175);\n"
"	border: 2px solid grey;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;    \n"
"	min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border-style: inset;\n"
"}")
        self.Conncection_progressBar = QProgressBar(self.Conncetion_Access_groupBox)
        self.Conncection_progressBar.setObjectName(u"Conncection_progressBar")
        self.Conncection_progressBar.setGeometry(QRect(31, 77, 381, 23))
        self.Conncection_progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;	\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
        self.Conncection_progressBar.setValue(0)
        self.Conncection_progressBar.setTextVisible(True)
        self.Connect_pushButton = QPushButton(self.Conncetion_Access_groupBox)
        self.Connect_pushButton.setObjectName(u"Connect_pushButton")
        self.Connect_pushButton.setGeometry(QRect(30, 23, 178, 41))
        self.Connect_pushButton.setFont(font7)
        self.Connect_pushButton.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"	background-color: #05B8CC;\n"
"	border: 2px solid grey;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;    \n"
"     \n"
"	min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border-style: inset;\n"
"}")

        self.retranslateUi(BugZ)
        self.Channel9_horizontalSlider.valueChanged.connect(self.Channel9_lcdNumber.display)
        self.Channel10_horizontalSlider.valueChanged.connect(self.Channel10_lcdNumber.display)

        self.BenchMode_tabWidget.setCurrentIndex(0)
        self.Peripherals_tabWidget.setCurrentIndex(0)
        self.UART_BaudRate_comboBox.setCurrentIndex(12)


        QMetaObject.connectSlotsByName(BugZ)
        
        # Connect pushButton
        self.Connect_pushButton.clicked.connect(self.Connect_Func)
        
        # Disconnect pushButton
        self.Disconnect_pushButton.clicked.connect(self.Disconnect_Func)
    
        # UART horizontalSlider
        self.UART_horizontalSlider.valueChanged.connect(self.UART_horizontalSlider_Func)
        
        # SPI Channel_1 horizontalSlider
        self.SPI_Channel_1_horizontalSlider.valueChanged.connect(self.SPI_Channel_1_horizontalSlider_Func)
        
        # SPI Channel_2 horizontalSlider
        self.SPI_Channel_2_horizontalSlider.valueChanged.connect(self.SPI_Channel_2_horizontalSlider_Func)
        
        # ModeSelect_horizontalSlider (at HIL mode)
        self.ModeSelect_horizontalSlider.valueChanged.connect(self.ModeSelect_horizontalSlider_Func)
        
        # Generate pushButton
        self.Generate_pushButton.clicked.connect(self.GenerateTestCase_Func)
        
        # Load pushButton
        self.Load_pushButton.clicked.connect(self.LoadTestCase_Func)
        
        # Run pushButton
        self.Run_pushButton.clicked.connect(self.RunTestCase_Func)
        
        # UART send Button
        self.UART_SendData_pushButton.clicked.connect(self.UART_Tx)

        # SPI_CH1 send Button
        self.SPI_Channel_1_SendData_pushButton.clicked.connect(self.SPI_CH1_Tx)

        # SPI_CH2 send Button
        self.SPI_Channel_2_SendData_pushButton.clicked.connect(self.SPI_CH2_Tx)
        
        self.BenchMode_tabWidget.currentChanged.connect(self.SwitchModes_Func)

    '''
    to be changed as per user demand  
    '''
    so_file = "./client.so"
    global my_functions 
    global ProgramStatus
    global path 
    global runFlag
    runFlag = 1
    global Tx_UART_Flag
    global Tx_SPI_CH1_Flag
    global Tx_SPI_CH2_Flag
    Tx_UART_Flag = 0
    Tx_SPI_CH1_Flag = 0
    Tx_SPI_CH2_Flag = 0
    
    path = "."
    my_functions = CDLL(so_file)
    status = 0

    def SwitchModes_Func(self):
      if (self.BenchMode_tabWidget.currentIndex() == 0):
        print(self.BenchMode_tabWidget.currentIndex())
        # self.Conncetion_Access_groupBox.setEnabled(True)
        self.Disconnect_pushButton.setEnabled(True)
        self.Connect_pushButton.setEnabled(True)
        self.Connect_pushButton.setStyleSheet(u"QPushButton {\n"
        "    color: white;\n"
        "	background-color: #05B8CC;\n"
        "	border: 2px solid grey;\n"
        "    border-width: 2px;\n"
        "    border-radius: 10px;    \n"
        "     \n"
        "	min-width: 10em;\n"
        "    padding: 6px;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: grey;\n"
        "    border-style: inset;\n"
        "}")
        self.Disconnect_pushButton.setStyleSheet(u"QPushButton {\n"
        "    color: white;\n"
        "	background-color: rgb(175,175,175);\n"
        "	border: 2px solid grey;\n"
        "    border-width: 2px;\n"
        "    border-radius: 10px;    \n"
        "	min-width: 10em;\n"
        "    padding: 6px;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: grey;\n"
        "    border-style: inset;\n"
        "}")
        self.Conncection_progressBar.setStyleSheet(u"QProgressBar {\n"
        "    border: 2px solid grey;\n"
        "    border-radius: 5px;	\n"
        "}\n"
        "\n"
        "QProgressBar::chunk {\n"
        "    background-color: #05B8CC;\n"
        "    width: 20px;\n"
        "}\n"
        "\n"
        "QProgressBar {\n"
        "    border: 2px solid grey;\n"
        "    border-radius: 5px;\n"
        "    text-align: center;\n"
        "}")
        # self.Conncetion_Access_groupBox.setVisible(True)
      else:
        print(self.BenchMode_tabWidget.currentIndex())
        # self.Conncetion_Access_groupBox.setEnabled(False)
        self.Disconnect_pushButton.setEnabled(False)
        self.Connect_pushButton.setEnabled(False)
        self.Connect_pushButton.setStyleSheet(u"QPushButton {\n"
        "    color: white;\n"
        "	background-color: rgb(175,175,175,30%);\n"
        "	border: 2px solid grey;\n"
        "    border-width: 2px;\n"
        "    border-radius: 10px;    \n"
        "     \n"
        "	min-width: 10em;\n"
        "    padding: 6px;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: grey;\n"
        "    border-style: inset;\n"
        "}")
        self.Disconnect_pushButton.setStyleSheet(u"QPushButton {\n"
        "    color: white;\n"
        "	background-color: rgb(175,175,175,30%);\n"
        "	border: 2px solid grey;\n"
        "    border-width: 2px;\n"
        "    border-radius: 10px;    \n"
        "	min-width: 10em;\n"
        "    padding: 6px;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: grey;\n"
        "    border-style: inset;\n"
        "}")
        self.Conncection_progressBar.setStyleSheet(u"QProgressBar {\n"
        "    border: 2px solid grey;\n"
        "    border-radius: 5px;	\n"
        "}\n"
        "\n"
        "QProgressBar::chunk {\n"
        "    background-color: rgb(175,175,175,30%);\n"
        "    width: 20px;\n"
        "}\n"
        "\n"
        "QProgressBar {\n"
        "    border: 2px solid grey;\n"
        "    border-radius: 5px;\n"
        "    text-align: center;\n"
        "}")
        # self.Conncetion_Access_groupBox.setVisible(False)
    
    

    #########################################################
    # Function Called By Connect_pushButton
    # Responsible for Starting the Test and 
    # and begin sending frames
    #########################################################
    def TEST_Func(self):
      
      global Tx_UART_Flag
      global Tx_SPI_CH1_Flag
      global Tx_SPI_CH2_Flag

      #Message Definitions
      MESSAGE_ACK				      = 0
      MESSAGE_NACK			      = 1
      MESSAGE_HEADER_FRAME	  = 2
      MESSAGE_DATA_FRAME		  = 3
      MESSAGE_CONNECTION_KEY	= 4
      MESSAGE_UART			      = 5
      MESSAGE_SPI_CH1			    = 6
      MESSAGE_SPI_CH2			    = 7
      MESSAGE_SERIAL_SIZE     = 8
 
      #Status Definitions
      CONNECTION_OK					          = 0
      CONNECTION_WINSOCK_INIT_ERROR	  = 1
      CONNECTION_SOCKET_ERROR			    = 2
      CONENCTION_REQUEST_TIMEOUT		  = 3
      HEADER_VALID		                = 0
      HEADER_INVALID		              = 1
      
      #Serial Index
      SERIAL_UART				  = 0
      SERIAL_SPI_CH1			= 1
      SERIAL_SPI_CH2			= 2
      
      PERIPH_ID_SIZE			= 4
      
      DATA_FRAME				  = 0
      SERIAL_FRAME			  = 1
      SERIAL_RETURN_FRAME	= 2
      READINGS_FRAME			= 3
      
      
      DIO_array = [int(self.Channel1_horizontalSlider.value()),
      int(self.Channel2_horizontalSlider.value()),
      int(self.Channel3_horizontalSlider.value()),
      int(self.Channel4_horizontalSlider.value())]
      
      DIO_DATA = (c_int8 * len(DIO_array))(*DIO_array)
      
      ##PWM DATA
      PWM_mappingValue = 10000
      PWM_array = [c_int32(self.Channel9_Frequency_spinBox.value()), 
                    c_int32(self.Channel9_horizontalSlider.value() * PWM_mappingValue), 
                    c_int32(self.Channel10_Frequency_spinBox.value()), 
                    c_int32(self.Channel10_horizontalSlider.value() * PWM_mappingValue)]
      
      PWM_DATA = (c_int32 * len(PWM_array))(*PWM_array)
      
      UART_Status = 0
      SPI_CH1_Status = 0
      SPI_CH2_Status = 0
      
      ##UART CONFIG
      if (self.UART_horizontalSlider.value()):
        UART_Status = 1
        
      if (Tx_UART_Flag):
        UART_Status = 2
        
      if((self.UART_horizontalSlider.value()) and (Tx_UART_Flag)):
        UART_Status = 3
      
      UART_config = [c_int32(UART_Status), 
                    c_int32(int(self.UART_BaudRate_comboBox.currentText()))]
                    
      if(Tx_UART_Flag):      
        UART_config.append(c_int32(len(self.UART_DataSend_lineEdit.displayText()) + PERIPH_ID_SIZE))
      else:
        UART_config.append(PERIPH_ID_SIZE)
      
      UART_CONFIG = (c_int32 * len(UART_config))(*UART_config)
      
      ##UART DATA
      UART_dataArray = [int(i, 16) for i in (self.UART_DataSend_lineEdit.displayText())]  
      UART_DATA = (c_int8 * len(UART_dataArray))(*UART_dataArray)
      
      ##########################################CHANGES HERE############################33
      ##SPI_CH1 CONFIG
      if((self.SPI_Channel_1_horizontalSlider.value())):
        SPI_CH1_Status = 1
        
      if((self.SPI_Channel_1_horizontalSlider.value()) and (Tx_SPI_CH1_Flag)):
        SPI_CH1_Status = 2
        
      SPI_CH1_config = [ c_int32(SPI_CH1_Status), 
                        c_int32(int(self.SPI_Channel_1_BaudRate_spinBox.value()))]
 
      if(Tx_SPI_CH1_Flag):      
        SPI_CH1_config.append(c_int32(len(self.SPI_Channel_1_DataSend_lineEdit.displayText()) + PERIPH_ID_SIZE))
      else:
        SPI_CH1_config.append(PERIPH_ID_SIZE)
      
      SPI_CH1_CONFIG = (c_int32 * len(SPI_CH1_config))(*SPI_CH1_config)
      
      ##SPI_CH1 DATA
      SPI_CH1_dataArray = [int(i, 16) for i in (self.SPI_Channel_1_DataSend_lineEdit.displayText())]  
      SPI_CH1_DATA = (c_int8 * len(SPI_CH1_dataArray))(*SPI_CH1_dataArray)
      
      
      ##SPI_CH2 CONFIG
      if((self.SPI_Channel_2_horizontalSlider.value())):
        SPI_CH2_Status = 1
        
      if((self.SPI_Channel_2_horizontalSlider.value()) and (Tx_SPI_CH2_Flag)):
        SPI_CH2_Status = 2
      
      SPI_CH2_config = [ c_int32(SPI_CH2_Status), 
                        c_int32(int(self.SPI_Channel_2_BaudRate_spinBox.value()))]
 
      if(Tx_SPI_CH2_Flag):      
        SPI_CH2_config.append(c_int32(len(self.SPI_Channel_2_DataSend_lineEdit.displayText()) + PERIPH_ID_SIZE))
      else:
        SPI_CH2_config.append(PERIPH_ID_SIZE)
      
      SPI_CH2_CONFIG = (c_int32 * len(SPI_CH2_config))(*SPI_CH2_config)
      
      ##SPI_CH2 DATA
      SPI_CH2_dataArray = [int(i, 16) for i in (self.SPI_Channel_2_DataSend_lineEdit.displayText())]  
      SPI_CH2_DATA = (c_int8 * len(SPI_CH2_dataArray))(*SPI_CH2_dataArray)
      
      #Sending Data to generate the client frame
      my_functions.FRAME_GenerateDataFrame(DIO_DATA, PWM_DATA, UART_CONFIG, SPI_CH1_CONFIG, SPI_CH2_CONFIG)

      my_functions.FRAME_Print()
      
      ##RECIVING DATA FROM PC
      #Sending Tx-Header
      Time1 = time.time()
      #print("TIME BEFORE HEADER: " + str(int(Time1 * 1000000)))
      my_functions.UDP_ClientSend(MESSAGE_HEADER_FRAME)
      #Receiving ACK on Tx Header
      ReceiveStatus = my_functions.UDP_ClientReceive(MESSAGE_ACK)  
      #Tx State
      if(ReceiveStatus == 0): #ACK received
        #print("ACK Received")
        #Sending Data Frame
        my_functions.UDP_ClientSend(MESSAGE_DATA_FRAME)
        my_functions.FRAME_FreeBuffer(DATA_FRAME)
        
      elif (ReceiveStatus == 1): #NACK received
        print("NACK Received")
      
      ##RECIVING DATA FROM RASPBERRY PI
      #Receiving Rx-Header 
      ReceiveStatus = my_functions.UDP_ClientReceive(MESSAGE_HEADER_FRAME)
      
      if(ReceiveStatus == 0): #Header Valid
        #print("HEADER FRAME VALID")
        #Sending ACK on FrameHeader
        my_functions.UDP_ClientSend(MESSAGE_ACK)
        #Receive Rx-Data
        my_functions.UDP_ClientReceive(MESSAGE_DATA_FRAME)
        
        my_functions.FRAME_ReadingsFrame.restype = POINTER(c_uint32)
        FRAME_return = my_functions.FRAME_ReadingsFrame()
        
        Time2 = time.time()
        #print("TIME AFTER READINGS: " + str(int(Time2 * 1000000)))
      
        #print("TIME DIFFERENCE: " + str(int((Time2-Time1) * 1000000)))
        #Displaying DIO Readings
        print(FRAME_return[0])
        print(FRAME_return[1])
        print(FRAME_return[2])
        print(FRAME_return[3])
        print(FRAME_return[4])
        print(FRAME_return[5])
        print(FRAME_return[6])
        print(FRAME_return[7])
        
        
        self.Channel5_lcdNumber.display(FRAME_return[0])
        self.Channel6_lcdNumber.display(FRAME_return[1])
        self.Channel7_lcdNumber.display(FRAME_return[2])
        self.Channel8_lcdNumber.display(FRAME_return[3])
        
        #Dipslaying PWM Readings
        self.Channel11_DutyCycle_lcdNumber.display(FRAME_return[4])
        self.Channel11_Frequency_lcdNumber.display(FRAME_return[5])
        
        self.Channel12_DutyCycle_lcdNumber.display(FRAME_return[6])
        self.Channel12_Frequency_lcdNumber.display(FRAME_return[7])
        
        if(Tx_UART_Flag == 1):
          ##Sending the serial frames
          #Generate UART Frame     
          my_functions.FRAME_GenerateSerialFrame(UART_DATA, UART_config[2], SERIAL_UART)
          
          #Sending UART Frame
          my_functions.UDP_ClientSend(MESSAGE_UART)
          #MessageSent_dialog()
          Tx_UART_Flag = 0
        
        if(self.UART_horizontalSlider.value() == 1): 
          ##Receiving the UART serial frames
          if(my_functions.UDP_ClientReceive(MESSAGE_SERIAL_SIZE) != MESSAGE_NACK):
            my_functions.UDP_ClientReceive(MESSAGE_UART)
            
            my_functions.FRAME_SerialReturnFrame.restype = c_char_p
            UART_ReadingArray = my_functions.FRAME_SerialReturnFrame()
            
            #Displaying the received frame frm PC
            tempUART_ReadingArray = str(UART_ReadingArray)
            NewUartReading = tempUART_ReadingArray[6:len(tempUART_ReadingArray)-1]
            
            print("UART READING: " + str(NewUartReading))
            
            self.UART_DataReceived_lineEdit.setText(tempUART_ReadingArray[6:len(tempUART_ReadingArray)-1])
            my_functions.FRAME_FreeBuffer(SERIAL_RETURN_FRAME)
   
          #else:
            #print("UART_SIZE_ERROR\n")
        
        #if(Tx_SPI_CH1_Flag == 1):
        if(SPI_CH1_Status == 2):
          ##Sending the SPI_CH1 serial frame
          #Generate SPI_CH1 Frame     
          my_functions.FRAME_GenerateSerialFrame(SPI_CH1_DATA, SPI_CH1_config[2], SERIAL_SPI_CH1)
          
          #Sending SPI_CH1 Frame
          my_functions.UDP_ClientSend(MESSAGE_SPI_CH1)
          #MessageSent_dialog()
          Tx_SPI_CH1_Flag = 0
        
        if(self.SPI_Channel_1_horizontalSlider.value() == 1):
          print("SPI_CH1 IS ENABLED")
          ###################################
          ##Receiving the SPI_CH1 serial frames
          if(my_functions.UDP_ClientReceive(MESSAGE_SERIAL_SIZE) != MESSAGE_NACK):
            print("REACHED HERE")
            my_functions.UDP_ClientReceive(MESSAGE_SPI_CH1)
            print("BUT NOT HERE")
            my_functions.FRAME_SerialReturnFrame.restype = c_char_p
            SPI_CH1_ReadingArray = my_functions.FRAME_SerialReturnFrame()
          
            #Displaying the received frame frm PC
            tempSPI_CH1_ReadingArray = str(SPI_CH1_ReadingArray)
            NewSPI_CH1_Reading = tempSPI_CH1_ReadingArray[6:len(tempSPI_CH1_ReadingArray)-1]
            print("SPI_CH1 READING: " + str(NewSPI_CH1_Reading))
            
            self.SPI_Channel_1_DataReceived_lineEdit.setText(tempSPI_CH1_ReadingArray[6:len(tempSPI_CH1_ReadingArray)-1])
            my_functions.FRAME_FreeBuffer(SERIAL_RETURN_FRAME)
            
    
          ###################################
        
        if(SPI_CH2_Status == 2):
          ##Sending the SPI_CH2 serial frame
          #Generate SPI_CH2 Frame     
          my_functions.FRAME_GenerateSerialFrame(SPI_CH2_DATA, SPI_CH2_config[2], SERIAL_SPI_CH2)
          
          #Sending SPI_CH2 Frame
          my_functions.UDP_ClientSend(MESSAGE_SPI_CH2)
          #MessageSent_dialog()
          Tx_SPI_CH2_Flag = 0
          
        if(self.SPI_Channel_2_horizontalSlider.value() == 1):
        
          ##Receiving the SPI_CH2 serial frames
          if(my_functions.UDP_ClientReceive(MESSAGE_SERIAL_SIZE) != MESSAGE_NACK):
            my_functions.UDP_ClientReceive(MESSAGE_SPI_CH2)
            
            my_functions.FRAME_SerialReturnFrame.restype = c_char_p
            SPI_CH2_ReadingArray = my_functions.FRAME_SerialReturnFrame()
          
            #Displaying the received frame frm PC
            tempSPI_CH2_ReadingArray = str(SPI_CH2_ReadingArray)
            NewSPI_CH2_Reading = tempSPI_CH2_ReadingArray[6:len(tempSPI_CH2_ReadingArray)-1]
            print("SPI_CH2 READING: " + str(NewSPI_CH2_Reading))
            
            self.SPI_Channel_2_DataReceived_lineEdit.setText(tempSPI_CH2_ReadingArray[6:len(tempSPI_CH2_ReadingArray)-1])
            my_functions.FRAME_FreeBuffer(SERIAL_RETURN_FRAME)

      elif(ReceiveStatus == 1): #Header Invalid
        print("HEADER FRAME INVALID")
    # TEST_Func    
    
    
    #########################################################
    # Function Called By Connect_pushButton
    # Responsible for Establishing a connection 
    # between Server and client
    #########################################################
    def Connect_Func(self):
      global ProgramStatus
      global Tx_UART_Flag
      global Connection_Flag
      
      status = my_functions.UDP_ClientConnect(b"192.168.5.10", 8080)
      if(status == 0):
        for i in range(0, 101, 5):
          self.Conncection_progressBar.setValue(i)
          time.sleep(0.01)
      
        #Clearing flags
        Tx_UART_Flag = 0
      
        print("CONNECTION_OK\n")
        ProgramStatus = 1
        Connection_Flag = 1
        COUNTER = 0
        while(ProgramStatus):
          COUNTER += 1
          print("PROGRAM COUNTER: " + str(COUNTER))
          self.TEST_Func()
          QCoreApplication.processEvents()
      
      elif(status == 1):
        self.Conncection_progressBar.setValue(0)
        print("CONNECTION_WINSOCK_INIT_ERROR\n")
        ProgramStatus = 0
        Connection_Flag = 0
      elif(status == 2):
        self.Conncection_progressBar.setValue(0)
        print("CONNECTION_SOCKET_ERROR\n")
        ProgramStatus = 0
        Connection_Flag = 0
      elif(status == 3):
        self.Conncection_progressBar.setValue(0)
        print("CONENCTION_REQUEST_TIMEOUT\n")
        ProgramStatus = 0     
        Connection_Flag = 0
    # Connect_Func      
  
    def UART_Tx(self):
      global Tx_UART_Flag
      
      if(len(self.UART_DataSend_lineEdit.displayText()) > 0):
        Tx_UART_Flag = 1
   
    def SPI_CH1_Tx(self):
      global Tx_SPI_CH1_Flag
      
      if(len(self.SPI_Channel_1_DataSend_lineEdit.displayText()) > 0):
        Tx_SPI_CH1_Flag = 1
  
    def SPI_CH2_Tx(self):
      global Tx_SPI_CH2_Flag
      
      if(len(self.SPI_Channel_2_DataSend_lineEdit.displayText()) > 0):
        Tx_SPI_CH2_Flag = 1
    
    #########################################################
    # Function Called By Disconnect_pushButton
    # Responsible for Closing/Finishing the connection 
    # between Server and client
    #########################################################
    def Disconnect_Func(self):
      global ProgramStatus
      global Connection_Flag
      
      ProgramStatus = 0
      Connection_Flag = 0
      self.Conncection_progressBar.setValue(0)
      my_functions.UDP_ClientDisconnect()
      self.Note_label.setVisible(False)

      print("DISCONNECTED FROM SERVER CONNECTION_OK\n")
    # Disconnect_Func
    
    
    #########################################################
    # Function Called By SPI_Channel_1_horizontalSlider
    # Responsible for Disabling and enabling  
    # the Configurations of SPI (ensure that configurations
    # are done only when SPI is disabled)
    #########################################################
    def SPI_Channel_1_horizontalSlider_Func(self):
      if int(self.SPI_Channel_1_horizontalSlider.value()) == 0:
        self.SPI_Channel_1_BaudRate_spinBox.setEnabled(True)
      else:
        self.SPI_Channel_1_BaudRate_spinBox.setEnabled(False)
    # SPI_Channel_1_horizontalSlider_Func     
    
    
    #########################################################
    # Function Called By SPI_Channel_2_horizontalSlider
    # Responsible for Disabling and enabling  
    # the Configurations of SPI (ensure that configurations
    # are done only when SPI is disabled)
    #########################################################
    def SPI_Channel_2_horizontalSlider_Func(self):
      if int(self.SPI_Channel_2_horizontalSlider.value()) == 0:
        self.SPI_Channel_2_BaudRate_spinBox.setEnabled(True)
      else:
        self.SPI_Channel_2_BaudRate_spinBox.setEnabled(False)
    # SPI_Channel_2_horizontalSlider_Func     
    
    
    #########################################################
    # Function Called By UART_horizontalSlider
    # Responsible for Disabling and enabling  
    # the Configurations of UART (ensure that configurations
    # are done only when UART is disabled)
    #########################################################
    def UART_horizontalSlider_Func(self):
      if int(self.UART_horizontalSlider.value()) == 0:
        self.UART_BaudRate_comboBox.setEnabled(True)
      else:
        self.UART_BaudRate_comboBox.setEnabled(False)
    # UART_horizontalSlider_Func
    
    
    #########################################################
    # Function Called By UART_horizontalSlider
    # Responsible for Disabling and enabling  
    # the Configurations of UART (ensure that configurations
    # are done only when UART is disabled)
    #########################################################
    def ModeSelect_horizontalSlider_Func(self):
      global runFlag
      if int(self.ModeSelect_horizontalSlider.value()) == 0:
        self.GenerateMode_groupBox.setEnabled(True)
        self.LoadMode_groupBox.setEnabled(False)
        runFlag = 1
      else:
        self.GenerateMode_groupBox.setEnabled(False)
        self.LoadMode_groupBox.setEnabled(True)
        runFlag = 2
    # ModeSelect_horizontalSlider_Func     
    
    
    #########################################################
    # Function Called By Generate_pushButton
    # Responsible for Generating a new test case  
    #########################################################
    def GenerateTestCase_Func(self):
      global folder_path 
      global runFlag
      runFlag = 1
      folder_explorer()
      self.GenerateMode_Path_lineEdit.setText(str(folder_path))
      # Empty test case
      if (self.GenerateTestCase_comboBox.currentIndex() == 0):
        #Generating the file
        GenerationPath = '"..\RPC\File_Generation\GenerateTestScript.py" 1 '+ '"' +str(folder_path) + '"'
        os.system('"'+GenerationPath+'"')        
      # blinky
      else:
        GenerationPath = '"..\RPC\File_Generation\GenerateTestScript.py" 2 '+ '"' +str(folder_path) + '"'
        os.system('"'+GenerationPath+'"')
      
      DestinationPath = folder_path
      SourcePath = "..\RPC\GRPC_client\GPIO_write_client.py"
      copy(SourcePath, DestinationPath)
      
      SourcePath = "..\RPC\GRPC_client\GPIO_macros.py"
      copy(SourcePath, DestinationPath)
      
      SourcePath = "..\RPC\GRPC_client\GPIO_write_pb2.py"
      copy(SourcePath, DestinationPath)
      
      SourcePath = "..\RPC\GRPC_client\GPIO_write_pb2_grpc.py"
      copy(SourcePath, DestinationPath)
    # GenerateTestCase_Func     
    
    #########################################################
    # Function Called By Load_pushButton
    # Responsible for loading a pre-existing test case  
    #########################################################
    def LoadTestCase_Func(self):
      file_explorer()
      global folder_path
      global runFlag
      global file_path
      runFlag = 2   
      # load test case and save the path
      self.LoadMode_Path_lineEdit.setText(str(file_path))
      
      before_trunc = file_path.split('/')
      DestinationPath = '/'.join(before_trunc[0:len(before_trunc)-1])
      
      SourcePath = "..\RPC\GRPC_client\GPIO_write_client.py"
      copy(SourcePath, DestinationPath)
      
      SourcePath = "..\RPC\GRPC_client\GPIO_macros.py"
      copy(SourcePath, DestinationPath)
      
      SourcePath = "..\RPC\GRPC_client\GPIO_write_pb2.py"
      copy(SourcePath, DestinationPath)
      
      SourcePath = "..\RPC\GRPC_client\GPIO_write_pb2_grpc.py"
      copy(SourcePath, DestinationPath)
      
      
      # LoadTestCase_Func     
    
    
    #########################################################
    # Function Called Run_pushButton
    # Responsible for Running the loaded test case  
    #########################################################
    def RunTestCase_Func(self):
      global runFlag
      global file_path
      global folder_path
      global Connection_Flag
      
      before_trunc = file_path.split('/')
      DestinationPath = '/'.join(before_trunc[0:len(before_trunc)-1])
      
      if Connection_Flag == 1:
        ###########TO BE CHANGED : ADD A WARNING TO USER 
        #DisconnectFirst_dialog()
        self.Note_label.setVisible(True)

      elif Connection_Flag == 0:
        showdialog()
        if (runFlag == 1): 
          #os.system('"'+str(folder_path) + "\TestCase.py"+'"')
          #subprocess.call('"'+str(folder_path) + "\TestCase.py"+'"', shell=True)
          #myoutput = open(folder_path + '\TestCase.log', 'w+')
          #the_other_process = subprocess.Popen(['python', str(folder_path) + "\TestCase.py"], stdout=myoutput)
          
          os.system(  "start cmd.exe /c "+ ('"' +str(folder_path) + "\TestCase.py" + '"') )
      
        elif(runFlag == 2):
          #temp = 'START /B cmd /c'+ " "+ '"' +'"' +str(file_path) + '"' + ' > ' + '"' + str(DestinationPath) +'/TestCase.log'+ '"' + '"'
          #os.system('"' + temp + '"')
          
          #os.system("START /B cmd /c"+ '"' + str(file_path) + '"' + " > " + '"' + DestinationPath +'/TestCase.log'+ '"')
          #subprocess.call('"'+str(file_path)+'"', shell=True)
          
          #myoutput = open(DestinationPath + '\TestCase.log', 'w+')
          #the_other_process = subprocess.Popen(['python', str(file_path)] , stdout=myoutput)
          
          os.system(  "start cmd.exe /c "+ ('"'+str(file_path)+'"') )
  
          #+ " 1> " + ('"'+DestinationPath +'/TestCase.log'+'"')
   
    def retranslateUi(self, BugZ):
        BugZ.setWindowTitle(QCoreApplication.translate("BugZ", u"Bug-Z", None))
        self.Peripherals_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Direct Mode Features", None))
        self.DigitalOutPins_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Digital O/P PINS", None))
        self.Channel1_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 1", None))
        self.label_15.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_16.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.Channel2_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 2", None))
        self.label_17.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_18.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.Channel3_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 3", None))
        self.label_13.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_14.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.Channel4_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 4", None))
        self.label_19.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_20.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.DigitalInPins_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Digital I/P PINS", None))
        self.Channel5_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 5", None))
        self.Channel6_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 6", None))
        self.Channel7_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 7", None))
        self.Channel8_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 8", None))
        self.PWMInPins_groupBox.setTitle(QCoreApplication.translate("BugZ", u"PWM I/P PINS", None))
        self.Channel11_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 11", None))
        self.Channel11_Frequency_label.setText(QCoreApplication.translate("BugZ", u"Frequency (Hz)", None))
        self.Channel11_DutyCycle_label.setText(QCoreApplication.translate("BugZ", u"Duty Cycle (%)", None))
        self.Channel12_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 12", None))
        self.Channel12_Frequency_label.setText(QCoreApplication.translate("BugZ", u"Frequency (Hz)", None))
        self.Channel12_DutyCycle_label.setText(QCoreApplication.translate("BugZ", u"Duty Cycle (%)", None))
        self.PWMOutPins_groupBox.setTitle(QCoreApplication.translate("BugZ", u"PWM O/P PINS", None))
        self.Channel10_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 10", None))
        self.Channel10_Frequency_label.setText(QCoreApplication.translate("BugZ", u"Frequency (Hz)", None))
        self.Channel10_DutyCycle_label.setText(QCoreApplication.translate("BugZ", u"Duty Cycle (%)", None))
        self.Channel10_FrequencyRange_lineEdit.setText(QCoreApplication.translate("BugZ", u"   Range: 0 -> 30,000,000", None))
        self.Channel9_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 9", None))
        self.Channel9_Frequency_label.setText(QCoreApplication.translate("BugZ", u"Frequency (Hz)", None))
        self.Channel9_DutyCycle_label.setText(QCoreApplication.translate("BugZ", u"Duty Cycle (%)", None))
        self.Channel9_FrequencyRange_lineEdit.setText(QCoreApplication.translate("BugZ", u"   Range: 0 -> 30,000,000", None))
        self.Peripherals_tabWidget.setTabText(self.Peripherals_tabWidget.indexOf(self.MainFeatures_tab), QCoreApplication.translate("BugZ", u"Main Features", None))
        self.UART_groupBox.setTitle(QCoreApplication.translate("BugZ", u"UART", None))
        self.UART_Enable_label.setText(QCoreApplication.translate("BugZ", u"Enable", None))
        self.UART_Disable_label.setText(QCoreApplication.translate("BugZ", u"Disable", None))
        self.UART_BaudRate_comboBox.setItemText(0, QCoreApplication.translate("BugZ", u"50", None))
        self.UART_BaudRate_comboBox.setItemText(1, QCoreApplication.translate("BugZ", u"75", None))
        self.UART_BaudRate_comboBox.setItemText(2, QCoreApplication.translate("BugZ", u"110", None))
        self.UART_BaudRate_comboBox.setItemText(3, QCoreApplication.translate("BugZ", u"134", None))
        self.UART_BaudRate_comboBox.setItemText(4, QCoreApplication.translate("BugZ", u"150", None))
        self.UART_BaudRate_comboBox.setItemText(5, QCoreApplication.translate("BugZ", u"200", None))
        self.UART_BaudRate_comboBox.setItemText(6, QCoreApplication.translate("BugZ", u"300", None))
        self.UART_BaudRate_comboBox.setItemText(7, QCoreApplication.translate("BugZ", u"600", None))
        self.UART_BaudRate_comboBox.setItemText(8, QCoreApplication.translate("BugZ", u"1200", None))
        self.UART_BaudRate_comboBox.setItemText(9, QCoreApplication.translate("BugZ", u"1800", None))
        self.UART_BaudRate_comboBox.setItemText(10, QCoreApplication.translate("BugZ", u"2400", None))
        self.UART_BaudRate_comboBox.setItemText(11, QCoreApplication.translate("BugZ", u"4800", None))
        self.UART_BaudRate_comboBox.setItemText(12, QCoreApplication.translate("BugZ", u"9600", None))
        self.UART_BaudRate_comboBox.setItemText(13, QCoreApplication.translate("BugZ", u"19200", None))
        self.UART_BaudRate_comboBox.setItemText(14, QCoreApplication.translate("BugZ", u"38400", None))
        self.UART_BaudRate_comboBox.setItemText(15, QCoreApplication.translate("BugZ", u"57600", None))
        self.UART_BaudRate_comboBox.setItemText(16, QCoreApplication.translate("BugZ", u"115200", None))
        self.UART_BaudRate_comboBox.setItemText(17, QCoreApplication.translate("BugZ", u"230400", None))

        self.UART_BaudRate_label.setText(QCoreApplication.translate("BugZ", u"Baud Rate (bit/sec)", None))
        self.UART_DataSend_label.setText(QCoreApplication.translate("BugZ", u"Data to be sent (HEX)", None))
        self.UART_DataReceived_label.setText(QCoreApplication.translate("BugZ", u"Data Received (HEX)", None))
        self.UART_DataSend_lineEdit.setText("")
        self.UART_DataSend_lineEdit.setPlaceholderText(QCoreApplication.translate("BugZ", u"ex: AB12CD34", None))
        self.UART_DataReceived_lineEdit.setText("")
        self.UART_DataReceived_lineEdit.setPlaceholderText("")
        self.UART_SendData_pushButton.setText(QCoreApplication.translate("BugZ", u"Send", None))
        self.SPI_Channel_1_groupBox.setTitle(QCoreApplication.translate("BugZ", u"SPI Channel 1", None))
        self.SPI_Channel_1_Enable_label.setText(QCoreApplication.translate("BugZ", u"Enable", None))
        self.SPI_Channel_1_Disable_label.setText(QCoreApplication.translate("BugZ", u"Disable", None))
        self.SPI_Channel_1_BaudRate_label.setText(QCoreApplication.translate("BugZ", u"Baud Rate (bit/sec)", None))
        self.SPI_Channel_1_DataSend_label.setText(QCoreApplication.translate("BugZ", u"Data to be sent (HEX)", None))
        self.SPI_Channel_1_DataReceived_label.setText(QCoreApplication.translate("BugZ", u"Data Received (HEX)", None))
        self.SPI_Channel_1_DataSend_lineEdit.setText("")
        self.SPI_Channel_1_DataSend_lineEdit.setPlaceholderText(QCoreApplication.translate("BugZ", u"ex: AB12CD34", None))
        self.SPI_Channel_1_DataReceived_lineEdit.setText("")
        self.SPI_Channel_1_DataReceived_lineEdit.setPlaceholderText("")
        self.SPI_Channel_1_BaudRate_spinBox.setSpecialValueText("")
        self.SPI_Channel_1_BaudRateRange_lineEdit.setText(QCoreApplication.translate("BugZ", u"   Range: 32K -> 30M", None))
        self.SPI_Channel_1_SendData_pushButton.setText(QCoreApplication.translate("BugZ", u"Send", None))
        self.SPI_Channel_2_groupBox.setTitle(QCoreApplication.translate("BugZ", u"SPI Channel 2", None))
        self.SPI_Channel_2_Enable_label.setText(QCoreApplication.translate("BugZ", u"Enable", None))
        self.SPI_Channel_2_Disable_label.setText(QCoreApplication.translate("BugZ", u"Disable", None))
        self.SPI_Channel_2_BaudRate_label.setText(QCoreApplication.translate("BugZ", u"Baud Rate (bit/sec)", None))
        self.SPI_Channel_2_DataSend_label.setText(QCoreApplication.translate("BugZ", u"Data to be sent (HEX)", None))
        self.SPI_Channel_2_DataReceived_label.setText(QCoreApplication.translate("BugZ", u"Data Received (HEX)", None))
        self.SPI_Channel_2_DataSend_lineEdit.setText("")
        self.SPI_Channel_2_DataSend_lineEdit.setPlaceholderText(QCoreApplication.translate("BugZ", u"ex: AB12CD34", None))
        self.SPI_Channel_2_DataReceived_lineEdit.setText("")
        self.SPI_Channel_2_DataReceived_lineEdit.setPlaceholderText("")
        self.SPI_Channel_2_BaudRateRange_lineEdit.setText(QCoreApplication.translate("BugZ", u"   Range: 32K -> 30M", None))
        self.SPI_Channel_2_SendData_pushButton.setText(QCoreApplication.translate("BugZ", u"Send", None))
        self.Peripherals_tabWidget.setTabText(self.Peripherals_tabWidget.indexOf(self.BasicCommunication_tab), QCoreApplication.translate("BugZ", u"Basic Communication", None))
        self.UART_DataReceived_lineEdit_2.setText("")
        self.UART_DataReceived_lineEdit_2.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("BugZ", u"COMING SOON...", None))
        self.label_2.setText(QCoreApplication.translate("BugZ", u"NEW FEATURES", None))
        self.Peripherals_tabWidget.setTabText(self.Peripherals_tabWidget.indexOf(self.AutomotiveCommunication_tab), QCoreApplication.translate("BugZ", u"Automotive Communication", None))
        self.BenchMode_tabWidget.setTabText(self.BenchMode_tabWidget.indexOf(self.DirectMode_tab), QCoreApplication.translate("BugZ", u"Direct", None))
        self.HILModeFeatures_groupBox.setTitle(QCoreApplication.translate("BugZ", u"HIL Mode Features", None))
        self.Run_pushButton.setText(QCoreApplication.translate("BugZ", u"Run", None))
        self.GenerateMode_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Generate a New Test File", None))
        self.GenerateMode_Path_lineEdit.setText("")
        self.GenerateMode_Path_lineEdit.setPlaceholderText(QCoreApplication.translate("BugZ", u"Path of the generated test file is displayed here", None))
        self.GenerateTestCase_comboBox.setItemText(0, QCoreApplication.translate("BugZ", u"Empty (add your own content)", None))
        self.GenerateTestCase_comboBox.setItemText(1, QCoreApplication.translate("BugZ", u"Blinky (blink a LED)", None))

        self.GeneratePath_label.setText(QCoreApplication.translate("BugZ", u"Path:", None))
        self.Generate_pushButton.setText(QCoreApplication.translate("BugZ", u"Generate", None))
        self.LoadMode_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Load an Existing Test File", None))
        self.LoadMode_Path_lineEdit.setText("")
        self.LoadMode_Path_lineEdit.setPlaceholderText(QCoreApplication.translate("BugZ", u"Path of the loaded test file is displayed here", None))
        self.LoadPath_label.setText(QCoreApplication.translate("BugZ", u"Path:", None))
        self.Note_label.setText(QCoreApplication.translate("BugZ", u"Note: Disconnect from the Direct Mode before Pressing Run ...", None))
        self.Load_pushButton.setText(QCoreApplication.translate("BugZ", u"Load", None))
        self.ModeSelect_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Mode Select", None))
        self.label_21.setText(QCoreApplication.translate("BugZ", u"Generate a New Test", None))
        self.label_22.setText(QCoreApplication.translate("BugZ", u"Load an Existing Test", None))
        self.BenchMode_tabWidget.setTabText(self.BenchMode_tabWidget.indexOf(self.HIL_Mode_Tab), QCoreApplication.translate("BugZ", u"HIL", None))
        self.BenchMode_tabWidget.setTabText(self.BenchMode_tabWidget.indexOf(self.Info_Tab), QCoreApplication.translate("BugZ", u"System Information", None))
        self.Conncetion_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Connection", None))
        self.Server_Configurations_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Server Configurations", None))
        self.Server_Number_comboBox.setItemText(0, QCoreApplication.translate("BugZ", u"Test Bench #1", None))
        self.Server_Number_comboBox.setItemText(1, QCoreApplication.translate("BugZ", u"Test Bench #2", None))
        self.Server_Number_comboBox.setItemText(2, QCoreApplication.translate("BugZ", u"Test Bench #3", None))

        self.Server_Number_label.setText(QCoreApplication.translate("BugZ", u"Sever Num.", None))
        self.Server_IP_label.setText(QCoreApplication.translate("BugZ", u"Sever IP", None))
        self.Server_IP_lineEdit.setText(QCoreApplication.translate("BugZ", u"192.168.0.1", None))
        self.Server_Port_lineEdit.setText(QCoreApplication.translate("BugZ", u"8080", None))
        self.Server_Port_label.setText(QCoreApplication.translate("BugZ", u"Sever Port", None))
        self.Conncetion_Access_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Connection Access", None))
        self.Disconnect_pushButton.setText(QCoreApplication.translate("BugZ", u"Disconnect", None))
        self.Connect_pushButton.setText(QCoreApplication.translate("BugZ", u"Connect", None))
    # retranslateUi



def main():
  global runFlag 
  runFlag = 0
  global Connection_Flag
  Connection_Flag = 0
  # Create the Qt Application
  app = QApplication(sys.argv)
  # Changing the window icon of the app.
  app.setWindowIcon(QIcon('Bug-Z_icon.png'))

  # Create the Qt Widget that will hold the Form/s
  widget = QWidget()
  #widget.setWindowFlags(widget.windowFlags() & ~Qt.WindowMaximizeButtonHint)
  
  # Create and show the form
  form = Ui_BugZ()
  form.setupUi(widget)
  # Show what's inside the widget
  widget.show()
  # Run the main Qt loop
  # Run the Application or execute it
  app.exec_()  
  sys.exit()


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
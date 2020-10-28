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
    QRadialGradient, QValidator, QRegExpValidator)   
    
from PySide2.QtWidgets import *
from ctypes import *

import sys
import time
import os
os.system('cls')

class Ui_BugZ(object):
    def setupUi(self, BugZ):
        if BugZ.objectName():
            BugZ.setObjectName(u"BugZ")
        BugZ.resize(837, 541)
        font = QFont()
        font.setBold(False)
        font.setWeight(50);
        BugZ.setFont(font)

        self.BenchMode_tabWidget = QTabWidget(BugZ)
        self.BenchMode_tabWidget.setObjectName(u"BenchMode_tabWidget")
        self.BenchMode_tabWidget.setGeometry(QRect(9, 169, 821, 361))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.BenchMode_tabWidget.setFont(font1)
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
        self.Peripherals_groupBox.setGeometry(QRect(4, 12, 811, 321))
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
        self.Peripherals_tabWidget.setGeometry(QRect(11, 20, 791, 291))
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
        self.DigitalOutPins_groupBox.setGeometry(QRect(10, 20, 131, 231))
        self.DigitalOutPins_groupBox.setFont(font1)
        self.Channel3_groupBox = QGroupBox(self.DigitalOutPins_groupBox)
        self.Channel3_groupBox.setObjectName(u"Channel3_groupBox")
        self.Channel3_groupBox.setGeometry(QRect(20, 161, 91, 51))
        self.Channel3_groupBox.setFont(font1)
        self.Channel3_horizontalSlider = QSlider(self.Channel3_groupBox)
        self.Channel3_horizontalSlider.setObjectName(u"Channel3_horizontalSlider")
        self.Channel3_horizontalSlider.setEnabled(True)
        self.Channel3_horizontalSlider.setGeometry(QRect(29, 18, 31, 22))
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
        self.label_13 = QLabel(self.Channel3_groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(9, 20, 16, 16))
        self.label_13.setFont(font1)
        self.label_14 = QLabel(self.Channel3_groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 20, 16, 16))
        self.label_14.setFont(font1)
        self.Channel1_groupBox = QGroupBox(self.DigitalOutPins_groupBox)
        self.Channel1_groupBox.setObjectName(u"Channel1_groupBox")
        self.Channel1_groupBox.setGeometry(QRect(20, 28, 91, 51))
        self.Channel1_groupBox.setFont(font1)
        self.Channel1_horizontalSlider = QSlider(self.Channel1_groupBox)
        self.Channel1_horizontalSlider.setObjectName(u"Channel1_horizontalSlider")
        self.Channel1_horizontalSlider.setEnabled(True)
        self.Channel1_horizontalSlider.setGeometry(QRect(29, 18, 31, 22))
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
        self.label_15 = QLabel(self.Channel1_groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(9, 20, 16, 16))
        self.label_15.setFont(font1)
        self.label_16 = QLabel(self.Channel1_groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(70, 20, 16, 16))
        self.label_16.setFont(font1)
        self.Channel2_groupBox = QGroupBox(self.DigitalOutPins_groupBox)
        self.Channel2_groupBox.setObjectName(u"Channel2_groupBox")
        self.Channel2_groupBox.setGeometry(QRect(20, 94, 91, 51))
        self.Channel2_groupBox.setFont(font1)
        self.Channel2_horizontalSlider = QSlider(self.Channel2_groupBox)
        self.Channel2_horizontalSlider.setObjectName(u"Channel2_horizontalSlider")
        self.Channel2_horizontalSlider.setEnabled(True)
        self.Channel2_horizontalSlider.setGeometry(QRect(29, 18, 31, 22))
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
        self.label_17 = QLabel(self.Channel2_groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(9, 20, 16, 16))
        self.label_17.setFont(font1)
        self.label_18 = QLabel(self.Channel2_groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(70, 20, 16, 16))
        self.label_18.setFont(font1)
        self.DigitalInPins_groupBox = QGroupBox(self.MainFeatures_tab)
        self.DigitalInPins_groupBox.setObjectName(u"DigitalInPins_groupBox")
        self.DigitalInPins_groupBox.setGeometry(QRect(178, 20, 131, 231))
        self.DigitalInPins_groupBox.setFont(font1)
        self.Channel4_groupBox = QGroupBox(self.DigitalInPins_groupBox)
        self.Channel4_groupBox.setObjectName(u"Channel4_groupBox")
        self.Channel4_groupBox.setGeometry(QRect(20, 28, 91, 51))
        self.Channel4_groupBox.setFont(font1)
        self.Channel4_lcdNumber = QLCDNumber(self.Channel4_groupBox)
        self.Channel4_lcdNumber.setObjectName(u"Channel4_lcdNumber")
        self.Channel4_lcdNumber.setGeometry(QRect(15, 20, 64, 23))
        font3 = QFont()
        font3.setPointSize(9)
        self.Channel4_lcdNumber.setFont(font3)
        self.Channel4_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel4_lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.Channel5_groupBox = QGroupBox(self.DigitalInPins_groupBox)
        self.Channel5_groupBox.setObjectName(u"Channel5_groupBox")
        self.Channel5_groupBox.setGeometry(QRect(20, 94, 91, 51))
        self.Channel5_groupBox.setFont(font1)
        self.Channel5_lcdNumber = QLCDNumber(self.Channel5_groupBox)
        self.Channel5_lcdNumber.setObjectName(u"Channel5_lcdNumber")
        self.Channel5_lcdNumber.setGeometry(QRect(16, 20, 64, 23))
        self.Channel5_lcdNumber.setFont(font3)
        self.Channel5_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel5_lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.Channel6_groupBox = QGroupBox(self.DigitalInPins_groupBox)
        self.Channel6_groupBox.setObjectName(u"Channel6_groupBox")
        self.Channel6_groupBox.setGeometry(QRect(20, 161, 91, 51))
        self.Channel6_groupBox.setFont(font1)
        self.Channel6_lcdNumber = QLCDNumber(self.Channel6_groupBox)
        self.Channel6_lcdNumber.setObjectName(u"Channel6_lcdNumber")
        self.Channel6_lcdNumber.setGeometry(QRect(15, 20, 64, 23))
        self.Channel6_lcdNumber.setFont(font3)
        self.Channel6_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel6_lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.PWMOutPins_groupBox = QGroupBox(self.MainFeatures_tab)
        self.PWMOutPins_groupBox.setObjectName(u"PWMOutPins_groupBox")
        self.PWMOutPins_groupBox.setGeometry(QRect(344, 20, 431, 231))
        self.PWMOutPins_groupBox.setFont(font1)
        self.PWMOutPins_groupBox.setStyleSheet(u"")
        self.Channel7_groupBox = QGroupBox(self.PWMOutPins_groupBox)
        self.Channel7_groupBox.setObjectName(u"Channel7_groupBox")
        self.Channel7_groupBox.setGeometry(QRect(16, 24, 401, 91))
        self.Channel7_groupBox.setFont(font1)
        self.Channel7_Frequency_label = QLabel(self.Channel7_groupBox)
        self.Channel7_Frequency_label.setObjectName(u"Channel7_Frequency_label")
        self.Channel7_Frequency_label.setGeometry(QRect(8, 23, 91, 16))
        self.Channel7_Frequency_label.setFont(font1)
        self.Channel7_lcdNumber = QLCDNumber(self.Channel7_groupBox)
        self.Channel7_lcdNumber.setObjectName(u"Channel7_lcdNumber")
        self.Channel7_lcdNumber.setGeometry(QRect(329, 54, 64, 23))
        self.Channel7_lcdNumber.setFont(font3)
        self.Channel7_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel7_lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.Channel7_horizontalSlider = QSlider(self.Channel7_groupBox)
        self.Channel7_horizontalSlider.setObjectName(u"Channel7_horizontalSlider")
        self.Channel7_horizontalSlider.setEnabled(True)
        self.Channel7_horizontalSlider.setGeometry(QRect(100, 54, 221, 22))
        self.Channel7_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
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
        self.Channel7_horizontalSlider.setMaximum(100)
        self.Channel7_horizontalSlider.setValue(0)
        self.Channel7_horizontalSlider.setTracking(True)
        self.Channel7_horizontalSlider.setOrientation(Qt.Horizontal)
        self.Channel7_DutyCycle_label = QLabel(self.Channel7_groupBox)
        self.Channel7_DutyCycle_label.setObjectName(u"Channel7_DutyCycle_label")
        self.Channel7_DutyCycle_label.setGeometry(QRect(10, 55, 81, 16))
        self.Channel7_DutyCycle_label.setFont(font1)
        self.Channel7_FrequencyRange_lineEdit = QLineEdit(self.Channel7_groupBox)
        self.Channel7_FrequencyRange_lineEdit.setObjectName(u"Channel7_FrequencyRange_lineEdit")
        self.Channel7_FrequencyRange_lineEdit.setGeometry(QRect(252, 22, 141, 20))
        self.Channel7_FrequencyRange_lineEdit.setFont(font1)
        self.Channel7_FrequencyRange_lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.Channel7_FrequencyRange_lineEdit.setReadOnly(True)
        self.Channel7_Frequency_spinBox = QSpinBox(self.Channel7_groupBox)
        self.Channel7_Frequency_spinBox.setObjectName(u"Channel7_Frequency_spinBox")
        self.Channel7_Frequency_spinBox.setGeometry(QRect(101, 22, 81, 21))
        self.Channel7_Frequency_spinBox.setFont(font1)
        self.Channel7_Frequency_spinBox.setStyleSheet(u"QSpinBox {\n"
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
        self.Channel7_Frequency_spinBox.setSuffix(u"")
        self.Channel7_Frequency_spinBox.setMaximum(30000000)
        self.Channel7_Frequency_spinBox.setDisplayIntegerBase(10)
        self.Channel8_groupBox = QGroupBox(self.PWMOutPins_groupBox)
        self.Channel8_groupBox.setObjectName(u"Channel8_groupBox")
        self.Channel8_groupBox.setGeometry(QRect(16, 125, 401, 91))
        self.Channel8_groupBox.setFont(font1)
        self.Channel8_Frequency_label = QLabel(self.Channel8_groupBox)
        self.Channel8_Frequency_label.setObjectName(u"Channel8_Frequency_label")
        self.Channel8_Frequency_label.setGeometry(QRect(8, 21, 91, 16))
        self.Channel8_Frequency_label.setFont(font1)
        self.Channel8_lcdNumber = QLCDNumber(self.Channel8_groupBox)
        self.Channel8_lcdNumber.setObjectName(u"Channel8_lcdNumber")
        self.Channel8_lcdNumber.setGeometry(QRect(329, 54, 64, 23))
        self.Channel8_lcdNumber.setFont(font3)
        self.Channel8_lcdNumber.setStyleSheet(u"QLCDNumber {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(50, 50, 50);\n"
"}")
        self.Channel8_lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.Channel8_horizontalSlider = QSlider(self.Channel8_groupBox)
        self.Channel8_horizontalSlider.setObjectName(u"Channel8_horizontalSlider")
        self.Channel8_horizontalSlider.setEnabled(True)
        self.Channel8_horizontalSlider.setGeometry(QRect(100, 54, 221, 22))
        self.Channel8_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
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
        self.Channel8_horizontalSlider.setMaximum(100)
        self.Channel8_horizontalSlider.setValue(0)
        self.Channel8_horizontalSlider.setTracking(True)
        self.Channel8_horizontalSlider.setOrientation(Qt.Horizontal)
        self.Channel8_DutyCycle_label = QLabel(self.Channel8_groupBox)
        self.Channel8_DutyCycle_label.setObjectName(u"Channel8_DutyCycle_label")
        self.Channel8_DutyCycle_label.setGeometry(QRect(10, 55, 81, 16))
        self.Channel8_DutyCycle_label.setFont(font1)
        self.Channel8_FrequencyRange_lineEdit = QLineEdit(self.Channel8_groupBox)
        self.Channel8_FrequencyRange_lineEdit.setObjectName(u"Channel8_FrequencyRange_lineEdit")
        self.Channel8_FrequencyRange_lineEdit.setGeometry(QRect(252, 23, 141, 20))
        self.Channel8_FrequencyRange_lineEdit.setFont(font1)
        self.Channel8_FrequencyRange_lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.Channel8_FrequencyRange_lineEdit.setReadOnly(True)
        self.Channel8_Frequency_spinBox = QSpinBox(self.Channel8_groupBox)
        self.Channel8_Frequency_spinBox.setObjectName(u"Channel8_Frequency_spinBox")
        self.Channel8_Frequency_spinBox.setGeometry(QRect(103, 22, 81, 21))
        self.Channel8_Frequency_spinBox.setFont(font1)
        self.Channel8_Frequency_spinBox.setStyleSheet(u"QSpinBox {\n"
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
        self.Channel8_Frequency_spinBox.setMaximum(30000000)
        self.Peripherals_tabWidget.addTab(self.MainFeatures_tab, "Main Features")
        self.BasicCommunication_tab = QWidget()
        self.BasicCommunication_tab.setObjectName(u"BasicCommunication_tab")
        self.UART_groupBox = QGroupBox(self.BasicCommunication_tab)
        self.UART_groupBox.setObjectName(u"UART_groupBox")
        self.UART_groupBox.setGeometry(QRect(5, 12, 251, 251))
        self.UART_groupBox.setFont(font1)
        self.UART_Enable_label = QLabel(self.UART_groupBox)
        self.UART_Enable_label.setObjectName(u"UART_Enable_label")
        self.UART_Enable_label.setGeometry(QRect(157, 220, 41, 16))
        self.UART_Enable_label.setFont(font1)
        self.UART_Disable_label = QLabel(self.UART_groupBox)
        self.UART_Disable_label.setObjectName(u"UART_Disable_label")
        self.UART_Disable_label.setGeometry(QRect(61, 218, 41, 20))
        self.UART_Disable_label.setFont(font1)
        self.UART_horizontalSlider = QSlider(self.UART_groupBox)
        self.UART_horizontalSlider.setObjectName(u"UART_horizontalSlider")
        self.UART_horizontalSlider.setEnabled(True)
        self.UART_horizontalSlider.setGeometry(QRect(110, 218, 31, 22))
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
"	 border: 1px solid gray;\n"
"	 border-radius: 8px;\n"
"	 background-color: darkgray;\n"
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
        self.UART_DataReceived_label.setGeometry(QRect(16, 145, 101, 21))
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
        self.UART_DataReceived_lineEdit.setGeometry(QRect(13, 170, 221, 31))
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
        self.SPI_Channel_1_groupBox = QGroupBox(self.BasicCommunication_tab)
        self.SPI_Channel_1_groupBox.setObjectName(u"SPI_Channel_1_groupBox")
        self.SPI_Channel_1_groupBox.setGeometry(QRect(270, 12, 251, 251))
        self.SPI_Channel_1_groupBox.setFont(font1)
        self.SPI_Channel_1_Enable_label = QLabel(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_Enable_label.setObjectName(u"SPI_Channel_1_Enable_label")
        self.SPI_Channel_1_Enable_label.setGeometry(QRect(159, 220, 41, 16))
        self.SPI_Channel_1_Enable_label.setFont(font1)
        self.SPI_Channel_1_Disable_label = QLabel(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_Disable_label.setObjectName(u"SPI_Channel_1_Disable_label")
        self.SPI_Channel_1_Disable_label.setGeometry(QRect(63, 218, 41, 20))
        self.SPI_Channel_1_Disable_label.setFont(font1)
        self.SPI_Channel_1_horizontalSlider = QSlider(self.SPI_Channel_1_groupBox)
        self.SPI_Channel_1_horizontalSlider.setObjectName(u"SPI_Channel_1_horizontalSlider")
        self.SPI_Channel_1_horizontalSlider.setEnabled(True)
        self.SPI_Channel_1_horizontalSlider.setGeometry(QRect(112, 218, 31, 22))
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
        self.SPI_Channel_1_DataReceived_label.setGeometry(QRect(16, 145, 101, 21))
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
        self.SPI_Channel_1_DataReceived_lineEdit.setGeometry(QRect(13, 170, 221, 31))
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
        self.SPI_Channel_1_BaudRateRange_lineEdit.setFont(font1)
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
        self.SPI_Channel_2_groupBox = QGroupBox(self.BasicCommunication_tab)
        self.SPI_Channel_2_groupBox.setObjectName(u"SPI_Channel_2_groupBox")
        self.SPI_Channel_2_groupBox.setGeometry(QRect(535, 12, 251, 251))
        self.SPI_Channel_2_groupBox.setFont(font1)
        self.SPI_Channel_2_Enable_label = QLabel(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_Enable_label.setObjectName(u"SPI_Channel_2_Enable_label")
        self.SPI_Channel_2_Enable_label.setGeometry(QRect(159, 220, 41, 16))
        self.SPI_Channel_2_Enable_label.setFont(font1)
        self.SPI_Channel_2_Disable_label = QLabel(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_Disable_label.setObjectName(u"SPI_Channel_2_Disable_label")
        self.SPI_Channel_2_Disable_label.setGeometry(QRect(63, 218, 41, 20))
        self.SPI_Channel_2_Disable_label.setFont(font1)
        self.SPI_Channel_2_horizontalSlider = QSlider(self.SPI_Channel_2_groupBox)
        self.SPI_Channel_2_horizontalSlider.setObjectName(u"SPI_Channel_2_horizontalSlider")
        self.SPI_Channel_2_horizontalSlider.setEnabled(True)
        self.SPI_Channel_2_horizontalSlider.setGeometry(QRect(112, 218, 31, 22))
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
        self.SPI_Channel_2_DataReceived_label.setGeometry(QRect(16, 145, 101, 21))
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
        self.SPI_Channel_2_DataReceived_lineEdit.setGeometry(QRect(13, 170, 221, 31))
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
        self.SPI_Channel_2_BaudRateRange_lineEdit.setFont(font1)
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
        self.Peripherals_tabWidget.addTab(self.BasicCommunication_tab, "")
        self.AutomotiveCommunication_tab = QWidget()
        self.AutomotiveCommunication_tab.setObjectName(u"AutomotiveCommunication_tab")
        self.UART_DataReceived_lineEdit_2 = QLineEdit(self.AutomotiveCommunication_tab)
        self.UART_DataReceived_lineEdit_2.setObjectName(u"UART_DataReceived_lineEdit_2")
        self.UART_DataReceived_lineEdit_2.setEnabled(True)
        self.UART_DataReceived_lineEdit_2.setGeometry(QRect(10, 16, 771, 251))
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
        self.label.setGeometry(QRect(80, 62, 641, 91))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(43)
        font4.setBold(True)
        font4.setWeight(75);
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: white")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.AutomotiveCommunication_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 194, 371, 51))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(18)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: white")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.Peripherals_tabWidget.addTab(self.AutomotiveCommunication_tab, "")
        self.BenchMode_tabWidget.addTab(self.DirectMode_tab, "")
        self.HIL_Mode_Tab = QWidget()
        self.HIL_Mode_Tab.setObjectName(u"HIL_Mode_Tab")
        self.TEST_pushButton = QPushButton(self.HIL_Mode_Tab)
        self.TEST_pushButton.setObjectName(u"TEST_pushButton")
        self.TEST_pushButton.setGeometry(QRect(654, 184, 120, 120))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(25)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setWeight(50);
        font6.setStrikeOut(False)
        font6.setKerning(False)
        self.TEST_pushButton.setFont(font6)
        self.TEST_pushButton.setAutoFillBackground(False)
        self.TEST_pushButton.setStyleSheet(u"QPushButton::pressed {background-color: grey}\n"
"QPushButton{border-radius : 60; border : 1px solid grey  ; background-color: rgb(227,34,39); color: white;}")
        self.TEST_pushButton.setCheckable(True)
        self.TEST_pushButton.setChecked(False)
        self.TEST_pushButton.setAutoDefault(False)
        self.TEST_pushButton.setFlat(False)
        self.BenchMode_tabWidget.addTab(self.HIL_Mode_Tab, "")
        self.Info_Tab = QWidget()
        self.Info_Tab.setObjectName(u"Info_Tab")
        self.BenchMode_tabWidget.addTab(self.Info_Tab, "")
        self.Conncetion_groupBox = QGroupBox(BugZ)
        self.Conncetion_groupBox.setObjectName(u"Conncetion_groupBox")
        self.Conncetion_groupBox.setGeometry(QRect(81, 10, 681, 151))
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
        self.Server_Number_comboBox.setFont(font1)
        self.Server_Number_comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	 border: 1px solid gray;\n"
"	 border-radius: 8px;\n"
"	 background-color: darkgray;\n"
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
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        self.Disconnect_pushButton.setFont(font7)
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
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50);
        self.Connect_pushButton.setFont(font8)
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
        
        # Signals
        
        self.retranslateUi(BugZ)
        '''
        Signals done from GUI
        '''
        self.Channel8_horizontalSlider.valueChanged.connect(self.Channel8_lcdNumber.display)
        self.Channel7_horizontalSlider.valueChanged.connect(self.Channel7_lcdNumber.display)

        # Signals
        self.BenchMode_tabWidget.setCurrentIndex(0)
        self.Peripherals_tabWidget.setCurrentIndex(0)
        self.TEST_pushButton.setDefault(False)

        QMetaObject.connectSlotsByName(BugZ)
         
        # Connect pushButton
        self.Connect_pushButton.clicked.connect(self.Connect_Func)
        
        # Disconnect pushButton
        self.Disconnect_pushButton.clicked.connect(self.Disconnect_Func)
        
        # Test pushButton
        self.TEST_pushButton.clicked.connect(self.TEST_Func)
    
        # UART horizontalSlider
        self.UART_horizontalSlider.valueChanged.connect(self.UART_horizontalSlider_Func)
        
        # SPI Channel_1 horizontalSlider
        self.SPI_Channel_1_horizontalSlider.valueChanged.connect(self.SPI_Channel_1_horizontalSlider_Func)
        
        # SPI Channel_2 horizontalSlider
        self.SPI_Channel_2_horizontalSlider.valueChanged.connect(self.SPI_Channel_2_horizontalSlider_Func)
        
    '''
    to be changed as per user demand  
    '''
    so_file = "./client.so"
    global my_functions 
    global ProgramStatus
    
    my_functions = CDLL(so_file)
    status = 0
    
    #########################################################
    # Function Called By Connect_pushButton
    # Responsible for Starting the Test and 
    # and begin sending frames
    #########################################################
    def TEST_Func(self):
      
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
      
      DIO_array = [int(self.Channel1_horizontalSlider.value()),
      int(self.Channel2_horizontalSlider.value()),
      int(self.Channel3_horizontalSlider.value())]
      
      DIO_DATA = (c_int8 * len(DIO_array))(*DIO_array)
      
      ##PWM DATA
      PWM_mappingValue = 10000
      PWM_array = [c_int32(self.Channel7_Frequency_spinBox.value()), 
                    c_int32(self.Channel7_horizontalSlider.value() * PWM_mappingValue), 
                    c_int32(self.Channel8_Frequency_spinBox.value()), 
                    c_int32(self.Channel8_horizontalSlider.value() * PWM_mappingValue)]
      
      PWM_DATA = (c_int32 * len(PWM_array))(*PWM_array)
      
    
      
      ##UART CONFIG
      UART_config = [c_int32(self.UART_horizontalSlider.value()), 
                    c_int32(int(self.UART_BaudRate_comboBox.currentText())),
                    c_int32(len(self.UART_DataSend_lineEdit.displayText()) + PERIPH_ID_SIZE)]
      
      UART_CONFIG = (c_int32 * len(UART_config))(*UART_config)
      
      ##UART DATA
      UART_dataArray = [int(i, 16) for i in (self.UART_DataSend_lineEdit.displayText())]  
      UART_DATA = (c_int8 * len(UART_dataArray))(*UART_dataArray)
      
      ##SPI_CH1 CONFIG
      SPI_CH1_array = [ c_int32(self.SPI_Channel_1_horizontalSlider.value()), 
                        c_int32(self.SPI_Channel_1_BaudRate_spinBox.value())]
      
      SPI_CH1_CONFIG = (c_int32 * len(SPI_CH1_array))(*SPI_CH1_array)
      
      ##SPI_CH2 CONFIG
      SPI_CH2_array = [ c_int32(self.SPI_Channel_2_horizontalSlider.value()), 
                        c_int32(self.SPI_Channel_2_BaudRate_spinBox.value())]
      
      SPI_CH2_CONFIG = (c_int32 * len(SPI_CH2_array))(*SPI_CH2_array)
      
      #Sending Data to generate the client frame
      my_functions.FRAME_GenerateDataFrame(DIO_DATA, PWM_DATA, UART_CONFIG, SPI_CH1_CONFIG, SPI_CH2_CONFIG)
      my_functions.FRAME_Print()
      
      ##RECIVING DATA FROM PC
      #Sending Tx-Header
      my_functions.UDP_ClientSend(MESSAGE_HEADER_FRAME)
      #Receiving ACK on Tx Header
      ReceiveStatus = my_functions.UDP_ClientReceive(MESSAGE_ACK)  
      #Tx State
      if(ReceiveStatus == 0): #ACK received
        print("ACK Received")
        #Sending Data Frame
        my_functions.UDP_ClientSend(MESSAGE_DATA_FRAME)
        my_functions.FRAME_FreeData()      
      elif (ReceiveStatus == 1): #NACK received
        print("NACK Received")
      

      ##RECIVING DATA FROM RASPBERRY PI
      #Receiving Rx-Header 
      ReceiveStatus = my_functions.UDP_ClientReceive(MESSAGE_HEADER_FRAME)
      
      if(ReceiveStatus == 0): #Header Valid
        print("HEADER FRAME VALID")
        #Sending ACK on FrameHeader
        my_functions.UDP_ClientSend(MESSAGE_ACK)
        #Receive Rx-Data
        my_functions.UDP_ClientReceive(MESSAGE_DATA_FRAME)
        
        FRAME_return = my_functions.FRAME_ParsingDataFrame()
        
        DIO_Readings = [int(d) for d in str(bin(FRAME_return))[2:]]
        [DIO_Readings.insert(0,0) for i in range(3-len(str(bin(FRAME_return))[2:]))]

        self.Channel4_lcdNumber.display(DIO_Readings[2])
        self.Channel5_lcdNumber.display(DIO_Readings[1])
        self.Channel6_lcdNumber.display(DIO_Readings[0])
        
        if(self.UART_horizontalSlider.value() == 1):
          ##Sending the serial frames
          #Generate UART Frame     
          my_functions.FRAME_SerialFrameGenerate(UART_DATA, UART_config[2], SERIAL_UART)
          
          #Sending UART Frame
          my_functions.UDP_ClientSend(MESSAGE_UART) 
          
          ##Receiving the serial frames
          if(my_functions.UDP_ClientReceive(MESSAGE_SERIAL_SIZE) != MESSAGE_NACK):
            my_functions.UDP_ClientReceive(MESSAGE_UART)
            
            my_functions.FRAME_ReturnSerial.restype = c_char_p
            UART_ReadingArray = my_functions.FRAME_ReturnSerial()
            
            #Displaying the received frame frm PC
            tempUART_ReadingArray = str(UART_ReadingArray)
            NewUartReading = tempUART_ReadingArray[6:len(tempUART_ReadingArray)-1]
            self.UART_DataReceived_lineEdit.setText(tempUART_ReadingArray[6:len(tempUART_ReadingArray)-1])
            my_functions.FRAME_ReturnSerialFree()
   
          else:
            print("UART_SIZE_ERROR\n")
            
        if(self.SPI_Channel_1_horizontalSlider.value() == 1):
          print("SPI_CH1 IS ENABLED")
        
        if(self.SPI_Channel_2_horizontalSlider.value() == 1):
          print("SPI_CH2 IS ENABLED")

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
      
      status = my_functions.UDP_ClientConnect(b"192.168.5.10", 8080)
      if(status == 0):
        for i in range(0, 101, 5):
          self.Conncection_progressBar.setValue(i)
          time.sleep(0.01)
        
        print("CONNECTION_OK\n")
        ProgramStatus = 1
        
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
        
      elif(status == 2):
        self.Conncection_progressBar.setValue(0)
        print("CONNECTION_SOCKET_ERROR\n")
        ProgramStatus = 0
        
      elif(status == 3):
        self.Conncection_progressBar.setValue(0)
        print("CONENCTION_REQUEST_TIMEOUT\n")
        ProgramStatus = 0     
        
    # Connect_Func      
  
    
    #########################################################
    # Function Called By Disconnect_pushButton
    # Responsible for Closing/Finishing the connection 
    # between Server and client
    #########################################################
    def Disconnect_Func(self):
      global ProgramStatus
      ProgramStatus = 0
      self.Conncection_progressBar.setValue(0)
      my_functions.UDP_ClientDisconnect()
      
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
        self.SPI_Channel_1_DataSend_lineEdit.setReadOnly(False)
        self.SPI_Channel_1_BaudRate_spinBox.setEnabled(True)
      else:
        self.SPI_Channel_1_DataSend_lineEdit.setReadOnly(True)
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
        self.SPI_Channel_2_DataSend_lineEdit.setReadOnly(False)
        self.SPI_Channel_2_BaudRate_spinBox.setEnabled(True)
      else:
        self.SPI_Channel_2_DataSend_lineEdit.setReadOnly(True)
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
        self.UART_DataSend_lineEdit.setReadOnly(False)
        self.UART_BaudRate_comboBox.setEnabled(True)
      else:
        self.UART_DataSend_lineEdit.setReadOnly(True)
        self.UART_BaudRate_comboBox.setEnabled(False)
    # UART_horizontalSlider_Func 
    
    # setupUi

    def retranslateUi(self, BugZ):
        BugZ.setWindowTitle(QCoreApplication.translate("BugZ", u"Bug-Z", None))
        self.Peripherals_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Direct Mode Features", None))
        self.DigitalOutPins_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Digital O/P PINS", None))
        self.Channel3_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 3", None))
        self.label_13.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_14.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.Channel1_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 1", None))
        self.label_15.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_16.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.Channel2_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 2", None))
        self.label_17.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_18.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.DigitalInPins_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Digital I/P PINS", None))
        self.Channel4_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 4", None))
        self.Channel5_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 5", None))
        self.Channel6_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 6", None))
        self.PWMOutPins_groupBox.setTitle(QCoreApplication.translate("BugZ", u"PWM O/P PINS", None))
        self.Channel7_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 7", None))
        self.Channel7_Frequency_label.setText(QCoreApplication.translate("BugZ", u"Frequency (Hz)", None))
        self.Channel7_DutyCycle_label.setText(QCoreApplication.translate("BugZ", u"Duty Cycle (%)", None))
        self.Channel7_FrequencyRange_lineEdit.setText(QCoreApplication.translate("BugZ", u"   Range: 0 -> 30,000,000", None))
        self.Channel8_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel 8", None))
        self.Channel8_Frequency_label.setText(QCoreApplication.translate("BugZ", u"Frequency (Hz)", None))
        self.Channel8_DutyCycle_label.setText(QCoreApplication.translate("BugZ", u"Duty Cycle (%)", None))
        self.Channel8_FrequencyRange_lineEdit.setText(QCoreApplication.translate("BugZ", u"   Range: 0 -> 30,000,000", None))
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
        self.Peripherals_tabWidget.setTabText(self.Peripherals_tabWidget.indexOf(self.BasicCommunication_tab), QCoreApplication.translate("BugZ", u"Basic Communication", None))
        self.UART_DataReceived_lineEdit_2.setText("")
        self.UART_DataReceived_lineEdit_2.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("BugZ", u"COMING SOON...", None))
        self.label_2.setText(QCoreApplication.translate("BugZ", u"NEW FEATURES", None))
        self.Peripherals_tabWidget.setTabText(self.Peripherals_tabWidget.indexOf(self.AutomotiveCommunication_tab), QCoreApplication.translate("BugZ", u"Automotive Communication", None))
        self.BenchMode_tabWidget.setTabText(self.BenchMode_tabWidget.indexOf(self.DirectMode_tab), QCoreApplication.translate("BugZ", u"Direct", None))
        self.TEST_pushButton.setText(QCoreApplication.translate("BugZ", u"Test", None))
        self.BenchMode_tabWidget.setTabText(self.BenchMode_tabWidget.indexOf(self.HIL_Mode_Tab), QCoreApplication.translate("BugZ", u"HIL", None))
        self.BenchMode_tabWidget.setTabText(self.BenchMode_tabWidget.indexOf(self.Info_Tab), QCoreApplication.translate("BugZ", u"System Information", None))
        self.Conncetion_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Connection", None))
        self.Server_Configurations_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Server Configurations", None))
        self.Server_Number_comboBox.setItemText(0, QCoreApplication.translate("BugZ", u"Server #1", None))
        self.Server_Number_comboBox.setItemText(1, QCoreApplication.translate("BugZ", u"Server #2", None))
        self.Server_Number_comboBox.setItemText(2, QCoreApplication.translate("BugZ", u"Server #3", None))

        self.Server_Number_label.setText(QCoreApplication.translate("BugZ", u"Sever Num.", None))
        self.Server_IP_label.setText(QCoreApplication.translate("BugZ", u"Sever IP", None))
        self.Server_IP_lineEdit.setText(QCoreApplication.translate("BugZ", u"192.168.0.1", None))
        self.Server_Port_lineEdit.setText(QCoreApplication.translate("BugZ", u"8080", None))
        self.Server_Port_label.setText(QCoreApplication.translate("BugZ", u"Sever Port", None))
        self.Conncetion_Access_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Connection Access", None))
        self.Disconnect_pushButton.setText(QCoreApplication.translate("BugZ", u"Disconnect", None))
        self.Connect_pushButton.setText(QCoreApplication.translate("BugZ", u"Connect", None))
    # retranslateUi



# Main Function
def main():
 
  # Create the Qt Application
  app = QApplication(sys.argv)
  # Changing the window icon of the app.
  app.setWindowIcon(QIcon('Bug-Z_icon.png'))
  # Create the Qt Widget that will hold the Form/s
  widget = QWidget()
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

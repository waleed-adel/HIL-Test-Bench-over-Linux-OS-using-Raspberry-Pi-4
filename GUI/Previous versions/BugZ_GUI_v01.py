# gcc -fPIC -shared -o func.so func.c
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
    QRadialGradient)
from PySide2.QtWidgets import *
from ctypes import *

import sys
import time

class Ui_BugZ(object):
    def setupUi(self, BugZ):
        if BugZ.objectName():
            BugZ.setObjectName(u"BugZ")
        BugZ.resize(791, 566)
        font = QFont()
        font.setBold(False)
        font.setWeight(50);
        BugZ.setFont(font)
        self.Conncetion_groupBox = QGroupBox(BugZ)
        self.Conncetion_groupBox.setObjectName(u"Conncetion_groupBox")
        self.Conncetion_groupBox.setGeometry(QRect(177, 10, 441, 111))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(8)
        self.Conncetion_groupBox.setFont(font1)
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
        self.Connect_pushButton = QPushButton(self.Conncetion_groupBox)
        self.Connect_pushButton.setObjectName(u"Connect_pushButton")
        self.Connect_pushButton.setGeometry(QRect(29, 22, 178, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50);
        self.Connect_pushButton.setFont(font2)
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
        self.Disconnect_pushButton = QPushButton(self.Conncetion_groupBox)
        self.Disconnect_pushButton.setObjectName(u"Disconnect_pushButton")
        self.Disconnect_pushButton.setGeometry(QRect(236, 22, 176, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.Disconnect_pushButton.setFont(font3)
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
        self.Conncection_progressBar = QProgressBar(self.Conncetion_groupBox)
        self.Conncection_progressBar.setObjectName(u"Conncection_progressBar")
        self.Conncection_progressBar.setGeometry(QRect(30, 75, 381, 23))
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
        self.Peripherals_groupBox = QGroupBox(BugZ)
        self.Peripherals_groupBox.setObjectName(u"Peripherals_groupBox")
        self.Peripherals_groupBox.setGeometry(QRect(19, 130, 751, 281))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        self.Peripherals_groupBox.setFont(font4)
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
        self.Peripherals_tabWidget.setGeometry(QRect(10, 20, 731, 251))
        self.Peripherals_tabWidget.setFont(font4)
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
        self.DIO_tab = QWidget()
        self.DIO_tab.setObjectName(u"DIO_tab")
        self.OutPins_groupBox = QGroupBox(self.DIO_tab)
        self.OutPins_groupBox.setObjectName(u"OutPins_groupBox")
        self.OutPins_groupBox.setGeometry(QRect(164, 10, 121, 221))
        self.OutPins_groupBox.setFont(font4)
        self.OUT_Channel_10_checkBox = QCheckBox(self.OutPins_groupBox)
        self.OUT_Channel_10_checkBox.setObjectName(u"OUT_Channel_10_checkBox")
        self.OUT_Channel_10_checkBox.setGeometry(QRect(19, 30, 81, 18))
        self.OUT_Channel_10_checkBox.setFont(font4)
        self.OUT_Channel_11_checkBox = QCheckBox(self.OutPins_groupBox)
        self.OUT_Channel_11_checkBox.setObjectName(u"OUT_Channel_11_checkBox")
        self.OUT_Channel_11_checkBox.setGeometry(QRect(19, 69, 81, 18))
        self.OUT_Channel_11_checkBox.setFont(font4)
        self.OUT_Channel_12_checkBox = QCheckBox(self.OutPins_groupBox)
        self.OUT_Channel_12_checkBox.setObjectName(u"OUT_Channel_12_checkBox")
        self.OUT_Channel_12_checkBox.setGeometry(QRect(19, 109, 81, 18))
        self.OUT_Channel_12_checkBox.setFont(font4)
        self.OUT_Channel_13_checkBox = QCheckBox(self.OutPins_groupBox)
        self.OUT_Channel_13_checkBox.setObjectName(u"OUT_Channel_13_checkBox")
        self.OUT_Channel_13_checkBox.setGeometry(QRect(20, 150, 81, 18))
        self.OUT_Channel_13_checkBox.setFont(font4)
        self.OUT_Channel_14_checkBox = QCheckBox(self.OutPins_groupBox)
        self.OUT_Channel_14_checkBox.setObjectName(u"OUT_Channel_14_checkBox")
        self.OUT_Channel_14_checkBox.setGeometry(QRect(20, 190, 81, 18))
        self.OUT_Channel_14_checkBox.setFont(font4)
        self.InPins_groupBox_2 = QGroupBox(self.DIO_tab)
        self.InPins_groupBox_2.setObjectName(u"InPins_groupBox_2")
        self.InPins_groupBox_2.setGeometry(QRect(409, 10, 181, 221))
        self.InPins_groupBox_2.setFont(font4)
        self.Channel_20_groupBox = QGroupBox(self.InPins_groupBox_2)
        self.Channel_20_groupBox.setObjectName(u"Channel_20_groupBox")
        self.Channel_20_groupBox.setGeometry(QRect(10, 28, 161, 51))
        self.Channel_20_groupBox.setFont(font4)
        self.IN_Channel_20_checkBox = QCheckBox(self.Channel_20_groupBox)
        self.IN_Channel_20_checkBox.setObjectName(u"IN_Channel_20_checkBox")
        self.IN_Channel_20_checkBox.setGeometry(QRect(10, 20, 51, 18))
        self.IN_Channel_20_checkBox.setFont(font4)
        self.Channel_20_horizontalSlider = QSlider(self.Channel_20_groupBox)
        self.Channel_20_horizontalSlider.setObjectName(u"Channel_20_horizontalSlider")
        self.Channel_20_horizontalSlider.setEnabled(False)
        self.Channel_20_horizontalSlider.setGeometry(QRect(100, 18, 31, 22))
        self.Channel_20_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
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
        self.Channel_20_horizontalSlider.setMaximum(1)
        self.Channel_20_horizontalSlider.setValue(0)
        self.Channel_20_horizontalSlider.setTracking(True)
        self.Channel_20_horizontalSlider.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.Channel_20_groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 16, 16))
        self.label.setFont(font4)
        self.label_2 = QLabel(self.Channel_20_groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(141, 20, 16, 16))
        self.label_2.setFont(font4)
        self.Channel_21_groupBox = QGroupBox(self.InPins_groupBox_2)
        self.Channel_21_groupBox.setObjectName(u"Channel_21_groupBox")
        self.Channel_21_groupBox.setGeometry(QRect(10, 93, 161, 51))
        self.Channel_21_groupBox.setFont(font4)
        self.IN_Channel_21_checkBox = QCheckBox(self.Channel_21_groupBox)
        self.IN_Channel_21_checkBox.setObjectName(u"IN_Channel_21_checkBox")
        self.IN_Channel_21_checkBox.setGeometry(QRect(10, 20, 51, 18))
        self.IN_Channel_21_checkBox.setFont(font4)
        self.Channel_21_horizontalSlider = QSlider(self.Channel_21_groupBox)
        self.Channel_21_horizontalSlider.setObjectName(u"Channel_21_horizontalSlider")
        self.Channel_21_horizontalSlider.setEnabled(False)
        self.Channel_21_horizontalSlider.setGeometry(QRect(100, 18, 31, 22))
        self.Channel_21_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
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
        self.Channel_21_horizontalSlider.setMaximum(1)
        self.Channel_21_horizontalSlider.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.Channel_21_groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 20, 16, 16))
        self.label_3.setFont(font4)
        self.label_4 = QLabel(self.Channel_21_groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(141, 20, 16, 16))
        self.label_4.setFont(font4)
        self.Channel_22_groupBox = QGroupBox(self.InPins_groupBox_2)
        self.Channel_22_groupBox.setObjectName(u"Channel_22_groupBox")
        self.Channel_22_groupBox.setGeometry(QRect(10, 157, 161, 51))
        self.Channel_22_groupBox.setFont(font4)
        self.IN_Channel_22_checkBox = QCheckBox(self.Channel_22_groupBox)
        self.IN_Channel_22_checkBox.setObjectName(u"IN_Channel_22_checkBox")
        self.IN_Channel_22_checkBox.setGeometry(QRect(10, 20, 51, 18))
        self.IN_Channel_22_checkBox.setFont(font4)
        self.Channel_22_horizontalSlider = QSlider(self.Channel_22_groupBox)
        self.Channel_22_horizontalSlider.setObjectName(u"Channel_22_horizontalSlider")
        self.Channel_22_horizontalSlider.setEnabled(False)
        self.Channel_22_horizontalSlider.setGeometry(QRect(100, 18, 31, 22))
        self.Channel_22_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
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
        self.Channel_22_horizontalSlider.setMaximum(1)
        self.Channel_22_horizontalSlider.setOrientation(Qt.Horizontal)
        self.label_5 = QLabel(self.Channel_22_groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 20, 16, 16))
        self.label_5.setFont(font4)
        self.label_6 = QLabel(self.Channel_22_groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(141, 20, 16, 16))
        self.label_6.setFont(font4)
        self.Peripherals_tabWidget.addTab(self.DIO_tab, "DIO_tab")
        self.ADC_tab = QWidget()
        self.ADC_tab.setObjectName(u"ADC_tab")
        self.Peripherals_tabWidget.addTab(self.ADC_tab, "ADC_tab")
        self.UART = QWidget()
        self.UART.setObjectName(u"UART")
        self.Peripherals_tabWidget.addTab(self.UART, "UART_tab")
        self.TEST_pushButton = QPushButton(BugZ)
        self.TEST_pushButton.setObjectName(u"TEST_pushButton")
        self.TEST_pushButton.setGeometry(QRect(640, 429, 120, 120))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(25)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(50);
        font5.setStrikeOut(False)
        font5.setKerning(False)
        self.TEST_pushButton.setFont(font5)
        self.TEST_pushButton.setAutoFillBackground(False)
        self.TEST_pushButton.setStyleSheet(u"QPushButton::pressed {background-color: grey}\n"
"QPushButton{border-radius : 60; border : 1px solid grey  ; background-color: rgb(227,34,39); color: white;}")
        self.TEST_pushButton.setCheckable(True)
        self.TEST_pushButton.setChecked(False)
        self.TEST_pushButton.setAutoDefault(False)
        self.TEST_pushButton.setFlat(False)

        self.retranslateUi(BugZ)

        self.Peripherals_tabWidget.setCurrentIndex(0)
        self.TEST_pushButton.setDefault(False)

        QMetaObject.connectSlotsByName(BugZ)
        
        # Connect pushButton
        self.Connect_pushButton.clicked.connect(self.Connect_Func)
        
        # Disconnect pushButton
        self.Disconnect_pushButton.clicked.connect(self.Disconnect_Func)
        
        # Test pushButton
        self.TEST_pushButton.clicked.connect(self.TEST_Func)
    
    '''
    to be changed as per user demand  
    '''
    so_file = "./client.so"
    global my_functions 
    my_functions = CDLL(so_file)
    status = 0
    #########################################################
    # Function Called By Connect_pushButton
    # Responsible for Establishing a connection 
    # between Server and client
    #########################################################
    def Connect_Func(self):
    
      status = my_functions.UDP_ClientConnect(b"192.168.5.10", 8888)
      if(status == 0):
        for i in range(0, 101, 5):
          self.Conncection_progressBar.setValue(i)
          time.sleep(0.1)
          
        print("CONNECTION_OK\n")
        
      elif(status == 1):
        self.Conncection_progressBar.setValue(0)
        print("CONNECTION_WINSOCK_INIT_ERROR\n")
      elif(status == 2):
        self.Conncection_progressBar.setValue(0)
        print("CONNECTION_SOCKET_ERROR\n")
      # Connect_Func      
  
    
    #########################################################
    # Function Called By Disconnect_pushButton
    # Responsible for Closing/Finishing the connection 
    # between Server and client
    #########################################################
    def Disconnect_Func(self):
      my_functions.UDP_ClientDisconnect()
      self.Conncection_progressBar.setValue(0)
      print("DISCONNECTED FROM SERVER CONNECTION_OK\n")
      # Disconnect_Func
    
    
    #########################################################
    # Function Called By Connect_pushButton
    # Responsible for Starting the Test and 
    # and begin sending frames
    #########################################################
    def TEST_Func(self):
      # print(my_functions.falla7_3(10))
      #self.Conncection_progressBar.setValue(50)
      #self.Channel_20_horizontalSlider.setValue(1)
      #self.Channel_22_horizontalSlider.setValue(1)
      
      output = [int(self.OUT_Channel_10_checkBox.isChecked()),int(self.OUT_Channel_11_checkBox.isChecked()),
      int(self.OUT_Channel_12_checkBox.isChecked()),int(self.OUT_Channel_13_checkBox.isChecked()),
      int(self.OUT_Channel_14_checkBox.isChecked())]
      
      array_type = (c_int8 * len(output))(*output)
      
      arr = [1,2,3,4]
      array_type2 = (c_int8 * len(arr))(*arr)
      
      #my_functions.PrintString(array_type(*arr),4)
      
      my_functions.FRAME_GenerateDataFrame(array_type, len(output), array_type2, len(arr))
      my_functions.FRAME_Print()
      
      ##RECIVING DATA FROM PC
      #Sending Tx-Header
      my_functions.UDP_ClientSend(2)
      #Receiving ACK on Tx Header
      ReceiveStatus = my_functions.UDP_ClientReceive(0)  
      #Tx State
      if(ReceiveStatus == 0): #ACK received
        print("ACK Received")
        #Sending Data Frame
        my_functions.UDP_ClientSend(3)     
      elif (ReceiveStatus == 1): #NACK received
        print("NACK Received")
      
      
      
      ##RECIVING DATA FROM RASPBERRY PI
      #Receiving Rx-Header 
      ReceiveStatus = my_functions.UDP_ClientReceive(2)
      
      if(ReceiveStatus == 0): #Header Valid
        print("HEADER FRAME VALID")
        #Sending ACK on FrameHeader
        my_functions.UDP_ClientSend(0)
        #Receive Rx-Data
        my_functions.UDP_ClientReceive(3)
        my_functions.FRAME_ParsingDataFrame()
      elif(ReceiveStatus == 1): #Header Invalid
        print("HEADER FRAME INVALID")
        
      
      
    # TEST_Func    
    
    # setupUi

    def retranslateUi(self, BugZ):
        BugZ.setWindowTitle(QCoreApplication.translate("BugZ", u"Form", None))
        self.Conncetion_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Connection", None))
        self.Connect_pushButton.setText(QCoreApplication.translate("BugZ", u"Connect", None))
        self.Disconnect_pushButton.setText(QCoreApplication.translate("BugZ", u"Disconnect", None))
        self.Peripherals_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Peripherals", None))
        self.OutPins_groupBox.setTitle(QCoreApplication.translate("BugZ", u"O/P PINS", None))
        self.OUT_Channel_10_checkBox.setText(QCoreApplication.translate("BugZ", u"Channel_10", None))
        self.OUT_Channel_11_checkBox.setText(QCoreApplication.translate("BugZ", u"Channel_11", None))
        self.OUT_Channel_12_checkBox.setText(QCoreApplication.translate("BugZ", u"Channel_12", None))
        self.OUT_Channel_13_checkBox.setText(QCoreApplication.translate("BugZ", u"Channel_13", None))
        self.OUT_Channel_14_checkBox.setText(QCoreApplication.translate("BugZ", u"Channel_14", None))
        self.InPins_groupBox_2.setTitle(QCoreApplication.translate("BugZ", u"I/P PINS", None))
        self.Channel_20_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel_20", None))
        self.IN_Channel_20_checkBox.setText(QCoreApplication.translate("BugZ", u"Read", None))
        self.label.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_2.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.Channel_21_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel_21", None))
        self.IN_Channel_21_checkBox.setText(QCoreApplication.translate("BugZ", u"Read", None))
        self.label_3.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_4.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.Channel_22_groupBox.setTitle(QCoreApplication.translate("BugZ", u"Channel_22", None))
        self.IN_Channel_22_checkBox.setText(QCoreApplication.translate("BugZ", u"Read", None))
        self.label_5.setText(QCoreApplication.translate("BugZ", u"0", None))
        self.label_6.setText(QCoreApplication.translate("BugZ", u"1", None))
        self.Peripherals_tabWidget.setTabText(self.Peripherals_tabWidget.indexOf(self.DIO_tab), QCoreApplication.translate("BugZ", u"DIO", None))
        self.Peripherals_tabWidget.setTabText(self.Peripherals_tabWidget.indexOf(self.ADC_tab), QCoreApplication.translate("BugZ", u"ADC", None))
        self.Peripherals_tabWidget.setTabText(self.Peripherals_tabWidget.indexOf(self.UART), QCoreApplication.translate("BugZ", u"UART", None))
        self.TEST_pushButton.setText(QCoreApplication.translate("BugZ", u"Test", None))
    # retranslateUi


def main():
 
  # Create the Qt Application
  app = QApplication(sys.argv)
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
  
  
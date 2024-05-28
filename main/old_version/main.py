# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:00:50 2024

@author: Microsoft
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import function_hidden_trouble as ft

#引用项目文件


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        #初始化变量
        self.list_zrry,self.list_zrglry,self.list_zrglbm= [],[],[]
        self.kf_list_zrry,self.kf_list_zrglry,self.kf_list_zrglbm = [],[],[]
    
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1344, 903)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.yinhuan_picture = QAction(MainWindow)
        self.yinhuan_picture.setObjectName(u"yinhuan_picture")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_yhtx = QGroupBox(self.centralwidget)
        self.groupBox_yhtx.setObjectName(u"groupBox_yhtx")
        self.groupBox_yhtx.setGeometry(QRect(10, 520, 1281, 331))
        self.plainTextEdit_yhnr = QPlainTextEdit(self.groupBox_yhtx)
        self.plainTextEdit_yhnr.setObjectName(u"plainTextEdit_yhnr")
        self.plainTextEdit_yhnr.setGeometry(QRect(10, 20, 221, 71))
        self.plainTextEdit_yhnr.setReadOnly(False)
        self.plainTextEdit_yhzgyq = QPlainTextEdit(self.groupBox_yhtx)
        self.plainTextEdit_yhzgyq.setObjectName(u"plainTextEdit_yhzgyq")
        self.plainTextEdit_yhzgyq.setGeometry(QRect(240, 20, 221, 71))
        self.plainTextEdit_yhzgyq.setReadOnly(False)
        self.groupBox_jcsj = QGroupBox(self.groupBox_yhtx)
        self.groupBox_jcsj.setObjectName(u"groupBox_jcsj")
        self.groupBox_jcsj.setGeometry(QRect(710, 160, 121, 101))
        self.verticalLayoutWidget = QWidget(self.groupBox_jcsj)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 101, 71))
        self.verticalLayout_jcsj = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_jcsj.setObjectName(u"verticalLayout_jcsj")
        self.verticalLayout_jcsj.setContentsMargins(0, 0, 0, 0)
        self.radioButton_jcsj_jt = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_jcsj_jt.setObjectName(u"radioButton_jcsj_jt")
        self.radioButton_jcsj_jt.setChecked(True)

        self.verticalLayout_jcsj.addWidget(self.radioButton_jcsj_jt)

        self.radioButton_xzrq = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_xzrq.setObjectName(u"radioButton_xzrq")
        self.radioButton_xzrq.setChecked(False)

        self.verticalLayout_jcsj.addWidget(self.radioButton_xzrq)

        self.dateEdit_xzrq = QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_xzrq.setObjectName(u"dateEdit_xzrq")
        self.dateEdit_xzrq.setEnabled(False)
        self.dateEdit_xzrq.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))

        self.verticalLayout_jcsj.addWidget(self.dateEdit_xzrq)

        self.groupBox_zrrjkf = QGroupBox(self.groupBox_yhtx)
        self.groupBox_zrrjkf.setObjectName(u"groupBox_zrrjkf")
        self.groupBox_zrrjkf.setGeometry(QRect(0, 100, 691, 211))
        self.groupBox_6 = QGroupBox(self.groupBox_zrrjkf)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(110, 60, 571, 141))
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setChecked(False)
        self.groupBox_zrry = QGroupBox(self.groupBox_6)
        self.groupBox_zrry.setObjectName(u"groupBox_zrry")
        self.groupBox_zrry.setGeometry(QRect(0, 10, 181, 131))
        self.groupBox_zrry.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_zrry.setCheckable(False)
        self.groupBox_zrry.setChecked(False)
        self.horizontalLayoutWidget_4 = QWidget(self.groupBox_zrry)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 60, 171, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_zrry = QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_zrry.setObjectName(u"lineEdit_zrry")
        self.lineEdit_zrry.setEnabled(True)
        self.lineEdit_zrry.setStyleSheet(u"font: 9pt \"\u6977\u4f53\";")
        self.lineEdit_zrry.setFrame(True)
        self.lineEdit_zrry.setDragEnabled(False)
        self.lineEdit_zrry.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_zrry)

        self.label_9 = QLabel(self.horizontalLayoutWidget_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.lineEdit_zrry_kf = QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_zrry_kf.setObjectName(u"lineEdit_zrry_kf")
        self.lineEdit_zrry_kf.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_zrry_kf)

        self.label_10 = QLabel(self.horizontalLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.textBrowser_2 = QTextBrowser(self.groupBox_zrry)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(0, 20, 171, 31))
        self.textBrowser_2.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.pushButton_3 = QPushButton(self.groupBox_zrry)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(100, 100, 41, 23))
        self.pushButton_4 = QPushButton(self.groupBox_zrry)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 100, 41, 23))
        self.groupBox_zrglry = QGroupBox(self.groupBox_6)
        self.groupBox_zrglry.setObjectName(u"groupBox_zrglry")
        self.groupBox_zrglry.setGeometry(QRect(190, 10, 181, 131))
        self.horizontalLayoutWidget_5 = QWidget(self.groupBox_zrglry)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 60, 171, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_zrglry = QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_zrglry.setObjectName(u"lineEdit_zrglry")
        self.lineEdit_zrglry.setEnabled(True)
        self.lineEdit_zrglry.setStyleSheet(u"font: 9pt \"\u6977\u4f53_GB2312\";")

        self.horizontalLayout_5.addWidget(self.lineEdit_zrglry)

        self.label_11 = QLabel(self.horizontalLayoutWidget_5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.lineEdit_zrglry_kf = QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_zrglry_kf.setObjectName(u"lineEdit_zrglry_kf")
        self.lineEdit_zrglry_kf.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_zrglry_kf)

        self.label_12 = QLabel(self.horizontalLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.textBrowser_3 = QTextBrowser(self.groupBox_zrglry)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(0, 20, 171, 31))
        self.pushButton_5 = QPushButton(self.groupBox_zrglry)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 100, 41, 23))
        self.pushButton_6 = QPushButton(self.groupBox_zrglry)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(100, 100, 41, 23))
        self.groupBox_zrbm = QGroupBox(self.groupBox_6)
        self.groupBox_zrbm.setObjectName(u"groupBox_zrbm")
        self.groupBox_zrbm.setGeometry(QRect(380, 10, 191, 131))
        self.horizontalLayoutWidget_6 = QWidget(self.groupBox_zrbm)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 60, 171, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit__zrglbm = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit__zrglbm.setObjectName(u"lineEdit__zrglbm")
        self.lineEdit__zrglbm.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.lineEdit__zrglbm)

        self.label_13 = QLabel(self.horizontalLayoutWidget_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.lineEdit_zrglbm_kf = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_zrglbm_kf.setObjectName(u"lineEdit_zrglbm_kf")
        self.lineEdit_zrglbm_kf.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_zrglbm_kf)

        self.label_14 = QLabel(self.horizontalLayoutWidget_6)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_6.addWidget(self.label_14)

        self.textBrowser_zrglbm = QTextBrowser(self.groupBox_zrbm)
        self.textBrowser_zrglbm.setObjectName(u"textBrowser_zrglbm")
        self.textBrowser_zrglbm.setGeometry(QRect(0, 20, 171, 31))
        self.pushButton_7 = QPushButton(self.groupBox_zrbm)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(100, 100, 41, 23))
        self.pushButton_8 = QPushButton(self.groupBox_zrbm)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 100, 41, 23))
        self.horizontalLayoutWidget = QWidget(self.groupBox_zrrjkf)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 671, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_2 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.comboBox_zrdw = QComboBox(self.horizontalLayoutWidget)
        self.comboBox_zrdw.addItem("")
        self.comboBox_zrdw.addItem("")
        self.comboBox_zrdw.addItem("")
        self.comboBox_zrdw.addItem("")
        self.comboBox_zrdw.addItem("")
        self.comboBox_zrdw.addItem("")
        self.comboBox_zrdw.setObjectName(u"comboBox_zrdw")
        self.comboBox_zrdw.setEnabled(False)
        self.comboBox_zrdw.setAutoFillBackground(False)
        self.comboBox_zrdw.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.comboBox_zrdw.setInputMethodHints(Qt.ImhNone)
        self.comboBox_zrdw.setEditable(True)
        self.comboBox_zrdw.setDuplicatesEnabled(False)
        self.comboBox_zrdw.setFrame(True)

        self.horizontalLayout.addWidget(self.comboBox_zrdw)

        self.lineEdit_qtdw = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_qtdw.setObjectName(u"lineEdit_qtdw")
        self.lineEdit_qtdw.setEnabled(True)
        self.lineEdit_qtdw.setStyleSheet(u"font: 9pt \"\u6977\u4f53_GB2312\";")

        self.horizontalLayout.addWidget(self.lineEdit_qtdw)

        self.radioButton = QRadioButton(self.groupBox_zrrjkf)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 100, 51, 16))
        self.radioButton.setChecked(True)
        self.plainTextEdit_jcry = QPlainTextEdit(self.groupBox_yhtx)
        self.plainTextEdit_jcry.setObjectName(u"plainTextEdit_jcry")
        self.plainTextEdit_jcry.setGeometry(QRect(470, 20, 221, 71))
        self.plainTextEdit_jcry.setReadOnly(False)
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_yhtx)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(930, 10, 334, 128))
        self.verticalLayout_yhlx = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_yhlx.setObjectName(u"verticalLayout_yhlx")
        self.verticalLayout_yhlx.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_yhlx.setContentsMargins(0, 0, 0, 0)
        self.label_yhlx = QLabel(self.verticalLayoutWidget_3)
        self.label_yhlx.setObjectName(u"label_yhlx")
        self.label_yhlx.setFocusPolicy(Qt.NoFocus)
        self.label_yhlx.setLayoutDirection(Qt.LeftToRight)
        self.label_yhlx.setTextFormat(Qt.AutoText)
        self.label_yhlx.setAlignment(Qt.AlignCenter)

        self.verticalLayout_yhlx.addWidget(self.label_yhlx)

        self.comboBox_yhlx = QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.addItem("")
        self.comboBox_yhlx.setObjectName(u"comboBox_yhlx")
        self.comboBox_yhlx.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_yhlx.addWidget(self.comboBox_yhlx)

        self.label_yhjb = QLabel(self.verticalLayoutWidget_3)
        self.label_yhjb.setObjectName(u"label_yhjb")
        self.label_yhjb.setFocusPolicy(Qt.NoFocus)
        self.label_yhjb.setLayoutDirection(Qt.LeftToRight)
        self.label_yhjb.setTextFormat(Qt.AutoText)
        self.label_yhjb.setAlignment(Qt.AlignCenter)

        self.verticalLayout_yhlx.addWidget(self.label_yhjb)

        self.comboBox_yhjb = QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_yhjb.addItem("")
        self.comboBox_yhjb.addItem("")
        self.comboBox_yhjb.addItem("")
        self.comboBox_yhjb.setObjectName(u"comboBox_yhjb")
        self.comboBox_yhjb.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_yhjb.setAutoFillBackground(False)

        self.verticalLayout_yhlx.addWidget(self.comboBox_yhjb)

        self.label_bjcdw = QLabel(self.verticalLayoutWidget_3)
        self.label_bjcdw.setObjectName(u"label_bjcdw")
        self.label_bjcdw.setFocusPolicy(Qt.NoFocus)
        self.label_bjcdw.setLayoutDirection(Qt.LeftToRight)
        self.label_bjcdw.setTextFormat(Qt.AutoText)
        self.label_bjcdw.setAlignment(Qt.AlignCenter)

        self.verticalLayout_yhlx.addWidget(self.label_bjcdw)

        self.comboBox_bjcdw = QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.addItem("")
        self.comboBox_bjcdw.setObjectName(u"comboBox_bjcdw")
        self.comboBox_bjcdw.setInputMethodHints(Qt.ImhNone)
        self.comboBox_bjcdw.setDuplicatesEnabled(False)

        self.verticalLayout_yhlx.addWidget(self.comboBox_bjcdw)

        self.groupBox_lfjcdw = QGroupBox(self.groupBox_yhtx)
        self.groupBox_lfjcdw.setObjectName(u"groupBox_lfjcdw")
        self.groupBox_lfjcdw.setGeometry(QRect(840, 160, 120, 101))
        self.comboBox_lfjcdw = QComboBox(self.groupBox_lfjcdw)
        self.comboBox_lfjcdw.addItem("")
        self.comboBox_lfjcdw.addItem("")
        self.comboBox_lfjcdw.addItem("")
        self.comboBox_lfjcdw.addItem("")
        self.comboBox_lfjcdw.setObjectName(u"comboBox_lfjcdw")
        self.comboBox_lfjcdw.setGeometry(QRect(10, 40, 81, 22))
        self.comboBox_lfjcdw.setEditable(True)
        self.plainTextEdit_qtzgyq = QPlainTextEdit(self.groupBox_yhtx)
        self.plainTextEdit_qtzgyq.setObjectName(u"plainTextEdit_qtzgyq")
        self.plainTextEdit_qtzgyq.setGeometry(QRect(700, 20, 221, 71))
        self.plainTextEdit_qtzgyq.setReadOnly(False)
        self.groupBox_yhztz = QGroupBox(self.centralwidget)
        self.groupBox_yhztz.setObjectName(u"groupBox_yhztz")
        self.groupBox_yhztz.setGeometry(QRect(0, 10, 1031, 321))
        self.tableWidget_yhztz = QTableWidget(self.groupBox_yhztz)
        if (self.tableWidget_yhztz.columnCount() < 32):
            self.tableWidget_yhztz.setColumnCount(32)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(26, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(27, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(28, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(29, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(30, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_yhztz.setHorizontalHeaderItem(31, __qtablewidgetitem31)
        if (self.tableWidget_yhztz.rowCount() < 5):
            self.tableWidget_yhztz.setRowCount(5)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_yhztz.setVerticalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_yhztz.setVerticalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_yhztz.setVerticalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_yhztz.setVerticalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_yhztz.setVerticalHeaderItem(4, __qtablewidgetitem36)
        self.tableWidget_yhztz.setObjectName(u"tableWidget_yhztz")
        self.tableWidget_yhztz.setGeometry(QRect(10, 20, 1011, 291))
        self.groupBox_yhsryl = QGroupBox(self.centralwidget)
        self.groupBox_yhsryl.setObjectName(u"groupBox_yhsryl")
        self.groupBox_yhsryl.setGeometry(QRect(10, 330, 1021, 181))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_yhsryl)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 911, 141))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_xsyhnr = QTextBrowser(self.horizontalLayoutWidget_2)
        self.textBrowser_xsyhnr.setObjectName(u"textBrowser_xsyhnr")

        self.horizontalLayout_2.addWidget(self.textBrowser_xsyhnr)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.groupBox_sc = QGroupBox(self.centralwidget)
        self.groupBox_sc.setObjectName(u"groupBox_sc")
        self.groupBox_sc.setGeometry(QRect(1040, 10, 120, 161))
        self.pushButton_sc = QPushButton(self.groupBox_sc)
        self.pushButton_sc.setObjectName(u"pushButton_sc")
        self.pushButton_sc.setGeometry(QRect(10, 20, 61, 23))
        self.checkBox_zgtzs = QCheckBox(self.groupBox_sc)
        self.checkBox_zgtzs.setObjectName(u"checkBox_zgtzs")
        self.checkBox_zgtzs.setGeometry(QRect(10, 50, 81, 16))
        self.checkBox_zgtzs.setChecked(True)
        self.checkBox_zgqrd = QCheckBox(self.groupBox_sc)
        self.checkBox_zgqrd.setObjectName(u"checkBox_zgqrd")
        self.checkBox_zgqrd.setGeometry(QRect(10, 70, 81, 16))
        self.checkBox_zgqrd.setChecked(True)
        self.checkBox_tb = QCheckBox(self.groupBox_sc)
        self.checkBox_tb.setObjectName(u"checkBox_tb")
        self.checkBox_tb.setGeometry(QRect(10, 90, 71, 16))
        self.checkBox_tb.setChecked(True)
        self.checkBox_jcqktjb = QCheckBox(self.groupBox_sc)
        self.checkBox_jcqktjb.setObjectName(u"checkBox_jcqktjb")
        self.checkBox_jcqktjb.setGeometry(QRect(10, 110, 111, 16))
        self.checkBox_jcqktjb.setChecked(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1140, 460, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1344, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.radioButton.toggled.connect(self.lineEdit_zrry.setEnabled)
        self.radioButton_2.clicked.connect(self.radioButton.toggle)
        self.radioButton.toggled.connect(self.lineEdit_zrry_kf.setEnabled)
        self.radioButton.toggled.connect(self.lineEdit_zrglry.setEnabled)
        self.radioButton.toggled.connect(self.lineEdit_zrglry_kf.setEnabled)
        self.radioButton.toggled.connect(self.lineEdit__zrglbm.setEnabled)
        self.radioButton.toggled.connect(self.lineEdit__zrglbm.setEnabled)
        self.radioButton.toggled.connect(self.lineEdit_zrglbm_kf.setEnabled)
        self.radioButton_2.toggled.connect(self.comboBox_zrdw.setEnabled)
        self.radioButton_xzrq.clicked.connect(self.dateEdit_xzrq.setEnabled)
        self.radioButton_jcsj_jt.clicked.connect(self.dateEdit_xzrq.setDisabled)
        self.pushButton_2.clicked.connect(self.textBrowser_xsyhnr.clear)
        self.radioButton.toggled.connect(self.pushButton_4.setEnabled)
        self.radioButton.toggled.connect(self.pushButton_3.setEnabled)
        self.radioButton.toggled.connect(self.pushButton_6.setEnabled)
        self.radioButton.toggled.connect(self.pushButton_5.setEnabled)
        self.radioButton.toggled.connect(self.pushButton_8.setEnabled)
        self.radioButton.toggled.connect(self.pushButton_7.setEnabled)

        
        #输入隐患内容信号槽
        self.plainTextEdit_yhnr.textChanged.connect(self.show_textbrowser)
        #输入隐患整改措施信号槽
        self.plainTextEdit_yhzgyq.textChanged.connect(self.show_textbrowser)
        #输入检查单位信号槽
        self.plainTextEdit_jcry.textChanged.connect(self.show_textbrowser)
        #输入其他整改要求信号槽
        self.plainTextEdit_qtzgyq.textChanged.connect(self.show_textbrowser)
        #隐患类型
        self.comboBox_yhlx.activated.connect(self.show_textbrowser)
        #隐患级别
        self.comboBox_yhjb.activated.connect(self.show_textbrowser)
        #被检查单位
        self.comboBox_bjcdw.activated.connect(self.show_textbrowser)
        
        ##责任人及扣分
        #快速选择
        self.radioButton_2.toggled.connect(self.show_textbrowser) 
        self.comboBox_zrdw.activated.connect(self.show_textbrowser)
        #自填
        self.radioButton.toggled.connect(self.show_textbrowser)


        self.pushButton_3.released.connect(self.pushButton_3click)
        self.pushButton_3.clicked.connect(self.show_textbrowser)
        
        self.pushButton_6.released.connect(self.pushButton_6click)
        self.pushButton_6.clicked.connect(self.show_textbrowser)

        
        
        #其他不在ui内信号槽链接

        QMetaObject.connectSlotsByName(MainWindow)
        
        
    
        
        
        
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5a01\u5a01\u5a01", None))
        self.yinhuan_picture.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u5165\u9690\u60a3\u56fe\u7247", None))
        self.groupBox_yhtx.setTitle(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u586b\u5199", None))
        self.plainTextEdit_yhnr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u9690\u60a3\u5185\u5bb9", None))
        self.plainTextEdit_yhzgyq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6574\u6539\u63aa\u65bd", None))
        self.groupBox_jcsj.setTitle(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u65f6\u95f4", None))
        self.radioButton_jcsj_jt.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u5929", None))
        self.radioButton_xzrq.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u65e5\u671f", None))
        self.groupBox_zrrjkf.setTitle(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u4eba\u53ca\u6263\u5206", None))
        self.groupBox_6.setTitle("")
        self.groupBox_zrry.setTitle(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u4eba\u5458", None))
        self.lineEdit_zrry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u586b\u5199", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6263", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5206", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u884c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.groupBox_zrglry.setTitle(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u7ba1\u7406\u4eba\u5458", None))
        self.lineEdit_zrglry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u586b\u5199", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6263", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5206", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u884c", None))
        self.groupBox_zrbm.setTitle(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u7ba1\u7406\u90e8\u95e8", None))
        self.lineEdit__zrglbm.setText("")
        self.lineEdit__zrglbm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u586b\u5199", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6263", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5206", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u884c", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u9009\u62e9", None))
        self.comboBox_zrdw.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6df1\u5733\u5e02\u6c83\u5c14\u5954\u8fbe\u65b0\u80fd\u6e90\u80a1\u4efd\u6709\u9650\u516c\u53f8", None))
        self.comboBox_zrdw.setItemText(1, QCoreApplication.translate("MainWindow", u"\u676d\u5dde\u695a\u73af\u79d1\u6280\u80a1\u4efd\u6709\u9650\u516c\u53f8", None))
        self.comboBox_zrdw.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5e7f\u4e1c\u5efa\u5b89\u660c\u76db\u63a7\u80a1\u96c6\u56e2\u6709\u9650\u516c\u53f8", None))
        self.comboBox_zrdw.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5e7f\u4e1c\u5b8f\u5fb7\u79d1\u6280\u7269\u4e1a\u6709\u9650\u516c\u53f8", None))
        self.comboBox_zrdw.setItemText(4, QCoreApplication.translate("MainWindow", u"\u73e0\u6d77\u5b8f\u7965\u8fd0\u8f93\u6709\u9650\u516c\u53f8", None))
        self.comboBox_zrdw.setItemText(5, QCoreApplication.translate("MainWindow", u"\u81ea\u586b", None))

        self.lineEdit_qtdw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u5355\u4f4d", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u586b", None))
        self.plainTextEdit_jcry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u4eba\u5458\u6216\u5355\u4f4d\uff0c\u4f7f\u7528\u4e2d\u6587\u9017\u53f7\u201c\uff0c\u201d\u6216\u7a7a\u683c\u9694\u5f00", None))
        self.label_yhlx.setText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u7c7b\u578b", None))
        self.comboBox_yhlx.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u8bbe\u65bd\u7684\u4e0d\u5b89\u5168\u72b6\u6001", None))
        self.comboBox_yhlx.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4eba\u5458\u8fdd\u53cd\u5b89\u5168\u7ba1\u7406\u89c4\u5b9a\u884c\u4e3a", None))
        self.comboBox_yhlx.setItemText(2, QCoreApplication.translate("MainWindow", u"\u8f66\u8f86\u5b89\u5168\u9690\u60a3", None))
        self.comboBox_yhlx.setItemText(3, QCoreApplication.translate("MainWindow", u"\u706b\u707e\u5b89\u5168\u9690\u60a3", None))
        self.comboBox_yhlx.setItemText(4, QCoreApplication.translate("MainWindow", u"\u7535\u6c14\u5b89\u5168\u9690\u60a3", None))
        self.comboBox_yhlx.setItemText(5, QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u7f3a\u5931", None))
        self.comboBox_yhlx.setItemText(6, QCoreApplication.translate("MainWindow", u"\u5e94\u6025\u7ba1\u7406\u9690\u60a3", None))
        self.comboBox_yhlx.setItemText(7, QCoreApplication.translate("MainWindow", u"\u5371\u9669\u5316\u5b66\u54c1\u5b89\u5168\u9690\u60a3", None))
        self.comboBox_yhlx.setItemText(8, QCoreApplication.translate("MainWindow", u"\u98df\u54c1\u5b89\u5168\u9690\u60a3", None))
        self.comboBox_yhlx.setItemText(9, QCoreApplication.translate("MainWindow", u"\u73af\u4fdd\u9690\u60a3", None))
        self.comboBox_yhlx.setItemText(10, QCoreApplication.translate("MainWindow", u"\u95e8\u5c97\u7ba1\u7406\u9690\u60a3", None))
        self.comboBox_yhlx.setItemText(11, QCoreApplication.translate("MainWindow", u"\u516b\u5927\u5371\u9669\u4f5c\u4e1a\u7ba1\u7406\u9690\u60a3", None))

        self.label_yhjb.setText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u7ea7\u522b", None))
        self.comboBox_yhjb.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e00\u822c\u9690\u60a3\uff08\u73ed\u7ec4\u7ea7\uff09", None))
        self.comboBox_yhjb.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e00\u822c\u9690\u60a3\uff08\u5382\u7ea7\uff09", None))
        self.comboBox_yhjb.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e00\u822c\u9690\u60a3\uff08\u516c\u53f8\u7ea7\uff09", None))

        self.label_bjcdw.setText(QCoreApplication.translate("MainWindow", u"\u88ab\u68c0\u67e5\u5355\u4f4d", None))
        self.comboBox_bjcdw.setItemText(0, QCoreApplication.translate("MainWindow", u"\u73e0\u6d77\u5e02\u6d77\u5b9c\u6d01\u6e90\u9910\u53a8\u5783\u573e\u5904\u7f6e\u6709\u9650\u516c\u53f8", None))
        self.comboBox_bjcdw.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6cb3\u5357\u827e\u5c14\u65fa\u65b0\u80fd\u6e90\u73af\u5883\u6709\u9650\u516c\u53f8 \uff08\u8bbe\u5907\u5382\u5bb6\uff09", None))
        self.comboBox_bjcdw.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5e7f\u4e1c\u5efa\u5b89\u660c\u76db\u63a7\u80a1\u96c6\u56e2\u6709\u9650\u516c\u53f8\uff08\u571f\u5efa\u5355\u4f4d\uff09", None))
        self.comboBox_bjcdw.setItemText(3, QCoreApplication.translate("MainWindow", u"\u676d\u5dde\u80fd\u6e90\u73af\u5883\u5de5\u7a0b\u6709\u9650\u516c\u53f8\uff08\u8bbe\u5907\u5382\u5bb6\uff09", None))
        self.comboBox_bjcdw.setItemText(4, QCoreApplication.translate("MainWindow", u"\u7ef4\u5c14\u5229\u73af\u4fdd\u79d1\u6280\u96c6\u56e2\u80a1\u4efd\u6709\u9650\u516c\u53f8\uff08\u65bd\u5de5\u5355\u4f4d\uff09", None))
        self.comboBox_bjcdw.setItemText(5, QCoreApplication.translate("MainWindow", u"\u6df1\u5733\u5e02\u6c83\u5c14\u5954\u8fbe\u65b0\u80fd\u6e90\u80a1\u4efd\u6709\u9650\u516c\u53f8\uff08\u8bbe\u5907\u5382\u5bb6\uff09", None))
        self.comboBox_bjcdw.setItemText(6, QCoreApplication.translate("MainWindow", u"\u676d\u5dde\u695a\u73af\u79d1\u6280\u80a1\u4efd\u6709\u9650\u516c\u53f8\uff08\u8bbe\u5907\u5382\u5bb6\uff09", None))
        self.comboBox_bjcdw.setItemText(7, QCoreApplication.translate("MainWindow", u"\u73e0\u6d77\u5e02\u57ce\u5e02\u5f00\u53d1\u76d1\u7406\u6709\u9650\u516c\u53f8\uff08\u76d1\u7406\u5355\u4f4d\uff09", None))
        self.comboBox_bjcdw.setItemText(8, QCoreApplication.translate("MainWindow", u"\u4e0a\u6d77\u5e02\u653f\u5de5\u7a0b\u8bbe\u8ba1\u7814\u7a76\u603b\u9662\uff08\u96c6\u56e2\uff09\u6709\u9650\u516c\u53f8\uff08\u8bbe\u8ba1\u5355\u4f4d\uff09", None))
        self.comboBox_bjcdw.setItemText(9, QCoreApplication.translate("MainWindow", u"\u73e0\u6d77\u591a\u7279\u81ea\u52a8\u5316\u5de5\u7a0b\u6709\u9650\u516c\u53f8\uff08\u81ea\u63a7\u5355\u4f4d\uff09", None))
        self.comboBox_bjcdw.setItemText(10, QCoreApplication.translate("MainWindow", u"\u6709\u610f\u9910\u996e\u7ba1\u7406\u516c\u53f8\uff08\u98df\u5802\u627f\u5305\u5355\u4f4d\uff09", None))

        self.groupBox_lfjcdw.setTitle(QCoreApplication.translate("MainWindow", u"\u6765\u8bbf\u68c0\u67e5\u5355\u4f4d", None))
        self.comboBox_lfjcdw.setItemText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u67e5", None))
        self.comboBox_lfjcdw.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6d77\u5b9c\u67e5", None))
        self.comboBox_lfjcdw.setItemText(2, QCoreApplication.translate("MainWindow", u"\u653f\u5e9c\u90e8\u95e8\u67e5", None))
        self.comboBox_lfjcdw.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5b89\u4fdd\u90e8\u67e5", None))

        self.plainTextEdit_qtzgyq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u6574\u6539\u8981\u6c42\uff0c\u9ed8\u8ba4\u4e0d\u586b\uff0c\u586b1\u4e3a\u201c\u6574\u6539\u5b8c\u6210\u540e\u4e66\u9762\u56de\u590d\u6211\u516c\u53f8\u201d", None))
        self.groupBox_yhztz.setTitle(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u603b\u53f0\u8d26", None))
        ___qtablewidgetitem = self.tableWidget_yhztz.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem1 = self.tableWidget_yhztz.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem2 = self.tableWidget_yhztz.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem3 = self.tableWidget_yhztz.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem4 = self.tableWidget_yhztz.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem5 = self.tableWidget_yhztz.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem6 = self.tableWidget_yhztz.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem7 = self.tableWidget_yhztz.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem8 = self.tableWidget_yhztz.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem9 = self.tableWidget_yhztz.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem10 = self.tableWidget_yhztz.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem11 = self.tableWidget_yhztz.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem12 = self.tableWidget_yhztz.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem13 = self.tableWidget_yhztz.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem14 = self.tableWidget_yhztz.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem15 = self.tableWidget_yhztz.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem16 = self.tableWidget_yhztz.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem17 = self.tableWidget_yhztz.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem18 = self.tableWidget_yhztz.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem19 = self.tableWidget_yhztz.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem20 = self.tableWidget_yhztz.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem21 = self.tableWidget_yhztz.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem22 = self.tableWidget_yhztz.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem23 = self.tableWidget_yhztz.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem24 = self.tableWidget_yhztz.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem25 = self.tableWidget_yhztz.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem26 = self.tableWidget_yhztz.horizontalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem27 = self.tableWidget_yhztz.horizontalHeaderItem(27)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem28 = self.tableWidget_yhztz.horizontalHeaderItem(28)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem29 = self.tableWidget_yhztz.horizontalHeaderItem(29)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem30 = self.tableWidget_yhztz.horizontalHeaderItem(30)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem31 = self.tableWidget_yhztz.horizontalHeaderItem(31)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem32 = self.tableWidget_yhztz.verticalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem33 = self.tableWidget_yhztz.verticalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem34 = self.tableWidget_yhztz.verticalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem35 = self.tableWidget_yhztz.verticalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem36 = self.tableWidget_yhztz.verticalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        self.groupBox_yhsryl.setTitle(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u8f93\u5165\u9884\u89c8", None))
        self.textBrowser_xsyhnr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u9884\u89c8", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5220", None))
        self.groupBox_sc.setTitle(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.pushButton_sc.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.checkBox_zgtzs.setText(QCoreApplication.translate("MainWindow", u"\u6574\u6539\u901a\u77e5\u4e66", None))
        self.checkBox_zgqrd.setText(QCoreApplication.translate("MainWindow", u"\u6574\u6539\u786e\u8ba4\u5355", None))
        self.checkBox_tb.setText(QCoreApplication.translate("MainWindow", u"\u901a\u62a5", None))
        self.checkBox_jcqktjb.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u60c5\u51b5\u7edf\u8ba1\u8868", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u8868\u5355", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u597d", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u548c\u548c", None))
    # retranslateUi

    def pushButton_3click(self):
        return 1
    
    def pushButton_6click(self):
        
        return 2
        
#隐患输入预览信号槽
    def show_textbrowser(self):
        
        get_yhnr = self.plainTextEdit_yhnr.toPlainText() #获取输入的隐患内容
        get_yhzgcs = self.plainTextEdit_yhzgyq.toPlainText()  #获取输入的隐患整改措施
        get_djcry = self.plainTextEdit_jcry.toPlainText()  #获取输入的检查人员或单位
        if self.plainTextEdit_qtzgyq.toPlainText() == "1":
            get_qtzgyq = '整改完成后书面回复我公司'
        else:
            get_qtzgyq = self.plainTextEdit_qtzgyq.toPlainText() # 获取输入的其他整改要求
        #隐患类型
        get_yhlx = self.comboBox_yhlx.currentText()
        #隐患级别
        get_yhjb = self.comboBox_yhjb.currentText()
        #被检查单位
        get_bjcdw = self.comboBox_bjcdw.currentText()
        #快速选择
        
        if self.radioButton_2.isChecked() == True:
            get_ksxz = self.comboBox_zrdw.currentText() #获取下拉菜单文本
        elif self.radioButton.isCheckable() == True:
            if self.pushButton_3click() == 1:
                self.list_zrry.append(self.lineEdit_zrry.text())
                self.kf_list_zrry.append(self.lineEdit_zrry_kf.text())
                self.textBrowser_2.setText('责任人员{}\n扣分{}'.format(self.list_zrry,self.kf_list_zrry))
                
            elif self.pushButton_6click() == 2:
                self.list_zrglry.append(self.lineEdit_zrglry.text())
                self.kf_list_zrglry.append(self.lineEdit_zrglry_kf.text())
                self.textBrowser_3.setText('责任人员{}\n扣分{}'.format(self.list_zrglry,self.kf_list_zrglry))
            else:
                pass
                
        # get_zrry   = {'责任人员'    :list_zrry,"扣分"  :kf_list_zrry}
        # get_zrglry = {'责任管理人员':list_zrglry,"扣分":kf_list_zrglry}
        # get_zrglbm = {'责任管理部门':list_zrglbm,"扣分":kf_list_zrglbm}
        
        self.textBrowser_xsyhnr.setText('【隐患内容】：{a}\n【整改措施】：{b}\n【检查人/单位】：{c}\n【其他整改要求】：{d}\n【隐患类型】：{e}\n【隐患级别】：{f}\n【被检查单位】：{g}\n'
                                .format(a = get_yhnr,b = get_yhzgcs,c=get_djcry,d=get_qtzgyq,e = get_yhlx,f =get_yhjb,g = get_bjcdw))

   
      
        

if __name__ == '__main__':
    app = QApplication([sys.argv])#ui主程序入口
    window = Ui_MainWindow() #创建主窗体对象并实例化
    window_yh = QMainWindow() #实例化QMainWindow
    window.setupUi(window_yh) #主窗体设置
    window_yh.show() 
    sys.exit(app.exec()) #循环中等待退出
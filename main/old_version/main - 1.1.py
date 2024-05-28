# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:00:50 2024

@author: Microsoft
"""
"""
bug统计

1.删除行后未更新行号排序
2.1.2版本中使用tableview重写，本项目到此截至
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QMessageBox, QTextEdit,QLabel
from PyQt5.QtCore import Qt, QRegularExpression, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QCheckBox
from PyQt5 import QtSql
from PyQt5.QtSql import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore
import sqlite3




# -*- coding: utf-8 -*-

#%% 继承重写
#继承QTextEdit并重写，作用：
class CustomTextEdit(QTextEdit):
    def __init__(self, parent=None):
        parent = parent.tableWidget_yhztz
        super().__init__(parent)
    def focusOutEvent(self, event):
        super().focusOutEvent(event)  # 确保其他焦点事件正常处理
        Ui_MainWindow().check_input_format(self)
    #####################################
    
class CustomTextEdit_one(QTextEdit):
    def __init__(self, parent=None):
        parent = parent.tableWidget_yhztz
        super().__init__(parent)
    def focusOutEvent(self, event):
        super().focusOutEvent(event)  # 确保其他焦点事件正常处理
        Ui_MainWindow().get_QTextEdit_data(self)
    #####################################

#%% 主UI结构
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1922, 1021)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.yinhuan_picture = QAction(MainWindow)
        self.yinhuan_picture.setObjectName(u"yinhuan_picture")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_yhztz = QGroupBox(self.centralwidget)
        self.groupBox_yhztz.setObjectName(u"groupBox_yhztz")
        self.groupBox_yhztz.setGeometry(QRect(0, 10, 1621, 961))
        self.tableWidget_yhztz = QTableWidget(self.groupBox_yhztz)
        if (self.tableWidget_yhztz.columnCount() < 14):
            self.tableWidget_yhztz.setColumnCount(14)
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
        self.tableWidget_yhztz.setObjectName(u"tableWidget_yhztz")
        self.tableWidget_yhztz.setGeometry(QRect(10, 20, 1601, 931))
        self.tableWidget_yhztz.setTabletTracking(False)
        self.groupBox_sc = QGroupBox(self.centralwidget)
        self.groupBox_sc.setObjectName(u"groupBox_sc")
        self.groupBox_sc.setGeometry(QRect(1730, 30, 120, 211))
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
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(1630, 30, 81, 211))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 20, 81, 23))
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 180, 81, 23))
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 60, 81, 23))
        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 100, 81, 23))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(1630, 260, 271, 291))
        self.verticalLayoutWidget = QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 261, 261))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1922, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)

        
#%%信号槽
        self.pushButton_3.clicked.connect(self.add_row)
        
        self.pushButton_4.clicked.connect(self.delete_selected_rows)
       
        
#%%数据库初始化
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.connect_db('./洁源隐患数据库2024.db') #连接数据库

    # 连接SQLite数据库
    def connect_db(self, database_name):
        self.db.setDatabaseName(database_name)
        self.sql_model = QSqlTableModel()           # 实例化QSqlTableModel
                                       
        self.sql_model.setTable('hidden')      #关联hidden表
        self.sql_model.setEditStrategy(QSqlTableModel.OnFieldChange)# 通过setEditStrategy()方法可以设置模型的编辑策略（即数据库是如何更新的）
        self.data_list = ['id' ,'检查时间',' 检查类型',' 隐患内容', '隐患图片', '隐患类型', '隐患级别', '被检查单位', '责任人及扣分', '责任管理人员及扣分',' 责任管理部门及扣分',' 隐患整改措施',' 隐患整改期限']
        for i in range(len(self.data_list)):
            self.sql_model.setHeaderData(i, QtCore.Qt.Horizontal,self.data_list[i])

        self.sql_model.select() #从关联表获取数据
        
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)
        
        #self.tableWidget_yhztz
        
       ##############
        # 连接到SQLite数据库
        
        # self.conn = sqlite3.connect('洁源隐患数据库2024.db')
        # self.cur = self.conn.cursor()
        


        # 查询数据库中的数据
        # self.cur.execute("SELECT * FROM hidden")
        # rows = self.cur.fetchall()

        # 设置QTableWidget的列数和表头标签
        # self.tableWidget_yhztz.setColumnCount(len(rows[0]))
        # self.tableWidget_yhztz.setHorizontalHeaderLabels(['检查时间', '检查类型', '隐患内容', '隐患图片','隐患类型','隐患级别','被检查单位','责任人及扣分','责任管理人员及扣分','责任管理部门及扣分','责任管理部门及扣分','隐患整改措施','隐患整改图片','隐患整改期限','勾选'])
        # #设置列宽
        # col_ = [0,1,2,3,4,5,6,7,8,9,10,11,12,13] #列
        # col_width = [100,80,220,200,170,130,130,140,140,140,220,200,100,40]#列宽
        # for col in range(len(col_)):
        #     self.tableWidget_yhztz.setColumnWidth(col_[col], col_width[col])
            
        # # 设置QTableWidget的行数
        # self.tableWidget_yhztz.setRowCount(len(rows))

        # # 将查询结果添加到QTableWidget中
        # for row_num, row_data in enumerate(rows, start= 0):
            
        #     for col_num, col_data in enumerate(row_data, start = 1):
        #         item = QTableWidgetItem(str(col_data))
        #         self.tableWidget_yhztz.setItem(row_num, col_num, item)


    # setupUi 列表表头
    def retranslateUi(self, MainWindow):
    
       
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5a01\u5a01\u5a01", None))
        self.yinhuan_picture.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u5165\u9690\u60a3\u56fe\u7247", None))
        self.groupBox_yhztz.setTitle(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u603b\u53f0\u8d26", None))
        ___qtablewidgetitem = self.tableWidget_yhztz.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u65f6\u95f4", None));
        ___qtablewidgetitem1 = self.tableWidget_yhztz.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u7c7b\u578b", None));
        ___qtablewidgetitem2 = self.tableWidget_yhztz.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u5185\u5bb9", None));
        ___qtablewidgetitem3 = self.tableWidget_yhztz.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u56fe\u7247", None));
        ___qtablewidgetitem4 = self.tableWidget_yhztz.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u7c7b\u578b", None));
        ___qtablewidgetitem5 = self.tableWidget_yhztz.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u7ea7\u522b", None));
        ___qtablewidgetitem6 = self.tableWidget_yhztz.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u88ab\u68c0\u67e5\u5355\u4f4d", None));
        ___qtablewidgetitem7 = self.tableWidget_yhztz.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u4eba\u53ca\u6263\u5206", None));
        ___qtablewidgetitem8 = self.tableWidget_yhztz.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u7ba1\u7406\u4eba\u5458\u53ca\u6263\u5206", None));
        ___qtablewidgetitem9 = self.tableWidget_yhztz.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u7ba1\u7406\u90e8\u95e8\u53ca\u6263\u5206", None));
        ___qtablewidgetitem10 = self.tableWidget_yhztz.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u6574\u6539\u63aa\u65bd", None));
        ___qtablewidgetitem11 = self.tableWidget_yhztz.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u6574\u6539\u56fe\u7247", None));
        ___qtablewidgetitem12 = self.tableWidget_yhztz.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u6574\u6539\u671f\u9650", None));
        ___qtablewidgetitem13 = self.tableWidget_yhztz.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u52fe\u9009", None));
        self.groupBox_sc.setTitle(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.pushButton_sc.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.checkBox_zgtzs.setText(QCoreApplication.translate("MainWindow", u"\u6574\u6539\u901a\u77e5\u4e66", None))
        self.checkBox_zgqrd.setText(QCoreApplication.translate("MainWindow", u"\u6574\u6539\u786e\u8ba4\u5355", None))
        self.checkBox_tb.setText(QCoreApplication.translate("MainWindow", u"\u901a\u62a5", None))
        self.checkBox_jcqktjb.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u60c5\u51b5\u7edf\u8ba1\u8868", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8868\u683c\u64cd\u4f5c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u4e0b\u62c9\u83dc\u5355", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u4e00\u884c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u526a\u5207\u677f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u88ab\u68c0\u67e5\u5355\u4f4d", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u73e0\u6d77\u5e02\u6d77\u5b9c\u6d01\u6e90\u9910\u53a8\u5783\u573e\u5904\u7f6e\u6709\u9650\u516c\u53f8\n"#第一行
                                                                                   "\u6cb3\u5357\u827e\u5c14\u65fa\u65b0\u80fd\u6e90\u73af\u5883\u6709\u9650\u516c\u53f8\uff08\u8bbe\u5907\u5382\u5bb6\uff09\n"#第二行
                                                                                   "\u5e7f\u4e1c\u5efa\u5b89\u660c\u76db\u63a7\u80a1\u96c6\u56e2\u6709\u9650\u516c\u53f8\uff08\u571f\u5efa\u5355\u4f4d\uff09\n"#第三行
                                                                                   "\u676d\u5dde\u80fd\u6e90\u73af\u5883\u5de5\u7a0b\u6709\u9650\u516c\u53f8\uff08\u8bbe\u5907\u5382\u5bb6\uff09\n"#第四行
                                                                                   "\u7ef4\u5c14\u5229\u73af\u4fdd\u79d1\u6280\u96c6\u56e2\u80a1\u4efd\u6709\u9650\u516c\u53f8\uff08\u65bd\u5de5\u5355\u4f4d\uff09\n"#第五行
                                                                                   "\u6df1\u5733\u5e02\u6c83\u5c14\u5954\u8fbe\u65b0\u80fd\u6e90\u80a1\u4efd\u6709\u9650\u516c\u53f8\uff08\u8bbe\u5907\u5382\u5bb6\uff09\n"#第六行
                                                                                   "\u676d\u5dde\u695a\u73af\u79d1\u6280\u80a1\u4efd\u6709\u9650\u516c\u53f8\uff08\u8bbe\u5907\u5382\u5bb6\uff09\n"
                                                                                   "\u73e0\u6d77\u5e02\u57ce\u5e02\u5f00\u53d1\u76d1\u7406\u6709\u9650\u516c\u53f8\uff08\u76d1\u7406\u5355\u4f4d\uff09\n"
                                                                                   "\u4e0a\u6d77\u5e02\u653f\u5de5\u7a0b\u8bbe\u8ba1\u7814\u7a76\u603b"
                                                                                   "\u9662\uff08\u96c6\u56e2\uff09\u6709\u9650\u516c\u53f8\uff08\u8bbe\u8ba1\u5355\u4f4d\uff09\n"
                                                                                   "\u73e0\u6d77\u591a\u7279\u81ea\u52a8\u5316\u5de5\u7a0b\u6709\u9650\u516c\u53f8\uff08\u81ea\u63a7\u5355\u4f4d\uff09\n"
                                                                                   "\u6709\u610f\u9910\u996e\u7ba1\u7406\u516c\u53f8\uff08\u98df\u5802\u627f\u5305\u5355\u4f4d\uff09\n"
                                                                                   "\u5e7f\u4e1c\u5b8f\u5fb7\u79d1\u6280\u7269\u4e1a\u6709\u9650\u516c\u53f8\uff08\u7269\u4e1a\u5355\u4f4d\uff09", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u597d", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u548c\u548c", None))
    # retranslateUi
    
    
    #添加行
    def add_row(self):
        row_position = self.tableWidget_yhztz.rowCount()
        self.tableWidget_yhztz.insertRow(row_position)

        for col in range(self.tableWidget_yhztz.columnCount() - 1):
            
            item = QTableWidgetItem(f"Data {row_position},{col}")
            self.tableWidget_yhztz.setItem(row_position, col, item)

            ## 设置行高
            self.tableWidget_yhztz.setRowHeight(row_position,100)

        ## 检查时间
        date_edit = QDateEdit()  # 使用 QDateEdit 作为编辑器，并设置为当日日期
        date_edit.setDate(QDate.currentDate())  # 设置为当日日期
        self.tableWidget_yhztz.setCellWidget(row_position, 0, date_edit)
        ## 隐患整改期限
        date_edit_qx = QDateEdit()  # 使用 QDateEdit 作为编辑器，并设置为当日日期
        date_edit_qx.setDate(QDate.currentDate())  # 设置为当日日期
        self.tableWidget_yhztz.setCellWidget(row_position, 12, date_edit_qx)
        ## 在每行末尾添加复选框
        checkbox = QCheckBox()
        checkbox.setChecked(False)  # 设置复选框默认选中
        checkbox.setStyleSheet("margin-left:10%; margin-right:10%;")  # 设置复选框居中
        self.tableWidget_yhztz.setCellWidget(row_position, self.tableWidget_yhztz.columnCount() - 1, checkbox)
        
        #########添加下拉列表#######
        ## 检查类型
        combobox_jclx = QComboBox()
        combobox_jclx.addItems(["自查", "海宜查", "政府部门查", "安保部查"])
        self.tableWidget_yhztz.setCellWidget(row_position,1, combobox_jclx)
        ## 隐患类型
        combobox_yhlx = QComboBox()
        combobox_yhlx.addItems(["设备设施的不安全状态", "电气安全隐患", "管理缺失", "火灾安全隐患", "人员违反安全管理规定行为",  "应急管理隐患", "车辆安全隐患",  "食品安全隐患", "门岗管理隐患","环保隐患", "危险化学品安全隐患","八大危险作业管理隐患"])
        self.tableWidget_yhztz.setCellWidget(row_position,4, combobox_yhlx)

        ## 隐患类别
        combobox_yhjb = QComboBox()
        combobox_yhjb.addItems(["一般隐患（班组级）","一般隐患（厂级）","一般隐患（公司级）"])
        self.tableWidget_yhztz.setCellWidget(row_position,5, combobox_yhjb)
        
        #########添加输入框#######
        ##责任人及扣分
        line_edit_tt = CustomTextEdit(self) # 添加文本输入框
        self.tableWidget_yhztz.setCellWidget(row_position, 7, line_edit_tt)
        # line_editt.returnPressed.connect(lambda line_edit=line_editt: self.check_input_format(line_edit))  # 按下 Enter 键时检查输入格式
        # line_editt.editingFinished.connect(lambda line_edit=line_editt: self.check_input_format(line_edit_t))  # 失去焦点时检查输入格式

        ##责任管理人员及扣分
        line_edit_t = CustomTextEdit(self) # 添加文本输入框
        self.tableWidget_yhztz.setCellWidget(row_position, 8, line_edit_t)

        ##责任管理部门及扣分
        line_edit_ty = CustomTextEdit(self) # 添加文本输入框
        self.tableWidget_yhztz.setCellWidget(row_position, 9, line_edit_ty)

        ##隐患内容
        yinhuanneirong_line = CustomTextEdit_one(self)
        self.tableWidget_yhztz.setCellWidget(row_position, 2, yinhuanneirong_line)

        ##隐患整改措施
        yinhuanzhenggai_line = CustomTextEdit_one(self)
        self.tableWidget_yhztz.setCellWidget(row_position, 10, yinhuanzhenggai_line)

        ##被检查单位
        checkebale_line = CustomTextEdit_one(self)
        self.tableWidget_yhztz.setCellWidget(row_position, 6, checkebale_line)
        
        #########添加图片#######
        ##隐患图片
        button = QPushButton('先复制图片\n再点此')
        self.tableWidget_yhztz.setCellWidget(row_position, 3, button)
        
        button.clicked.connect(lambda _, row = row_position ,colunm = 3: self.get_clipboard_image(row,colunm))

        ##隐患图片
        buttonn = QPushButton('先复制图片\n再点此')
        self.tableWidget_yhztz.setCellWidget(row_position, 11, buttonn)
        buttonn.clicked.connect(lambda _, row = self.tableWidget_yhztz.rowCount() ,colunm = 11: self.get_clipboard_image(row,colunm))

        #设置列宽
        col_ = [0,1,2,3,4,5,6,7,8,9,10,11,12,13] #列
        col_width = [100,80,220,200,170,130,130,140,140,140,220,200,100,40]#列宽
        for col in range(len(col_)):
            self.tableWidget_yhztz.setColumnWidth(col_[col], col_width[col])

    def delete_selected_rows(self):
        selected_rows = []

        for row in range(self.tableWidget_yhztz.rowCount()):
            checkbox_item = self.tableWidget_yhztz.cellWidget(row, self.tableWidget_yhztz.columnCount() - 1)
            
            if isinstance(checkbox_item, QCheckBox) and checkbox_item.isChecked(): #用于检查一个对象是否是指定类或类型的实例
                selected_rows.append(row)

        # 逆序删除选中的行，避免删除后索引错乱
        for row in reversed(selected_rows):
            self.tableWidget_yhztz.removeRow(row)
            
       # 重新设置垂直表头标签
        row_count = self.tableWidget_yhztz.rowCount()
        colunm1 = 3
        colunm2 = 11
        # 重新设置行号
        for row in range(row_count):
            button = self.table.cellWidget(row, 3)
            button.clicked.disconnect()  # 断开之前的连接
            button.clicked.connect(lambda _, row = row_position ,colunm = 3: self.get_clipboard_image(row,colunm))
                            
    # 检查输入格式
    def check_input_format(self,line_edit):
        #text = line_edit.text()
        text = line_edit.toPlainText()
        print(text)
        # 使用正则表达式验证输入格式
        regex = QRegularExpression('^[^\d]+-\d+(\.\d+)?([,，][^\d]+-\d+(\.\d+)?)*$') 
        if not regex.match(text).hasMatch():
            self.show_warning_message()  # 显示警告信息
            #line_edit.clear()  # 清空输入内容

    #显示错误提示信息
    def show_warning_message(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("{}".format("输入格式错误，请重新输入！\n格式要求：姓名-分数，姓名-分数　\n如：口含明珠-1，进退自如-1\n如：汪自如-1"))
        message_box.setWindowTitle("警告")
        message_box.exec_()

    #获取qtextedit数据
    def get_QTextEdit_data(self, data ):
        text = data.toPlainText()
        print(text)

    #从剪切板获取复制的图片地址
    def get_clipboard_image(self, row,colunm):
        # Get the image from the clipboard
        clipboard = QApplication.clipboard()
        image = clipboard.image()

        if not image.isNull():
            # 建立一个lable用于展示图片
            label = QLabel()
            label.setPixmap(QPixmap.fromImage(image).scaled(192,108))
            label.setAlignment(Qt.AlignCenter)
            # Set the label as the cell widget in the first column of the specified row
            self.tableWidget_yhztz.setCellWidget(row, colunm, label)
        else:
            self.show_image_warning_message()
    
    #显示图片的错误提示信息
    def show_image_warning_message(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("剪切板中不包含图片，请重新复制 ")
        message_box.setWindowTitle("警告")
        message_box.exec_()

    def connect_hiddenbase(self):

        self.connect_db()


        # 添加一行数据行
    def add_row_data(self):
        # 如果存在实例化的数据模型对象
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.create_db()
    
    # 删除一行数据
    def del_row_data(self):
        if self.model:
            self.model.removeRow(self.table_widget.currentIndex().row())
        else:
            self.create_db()
            
        
#     def pushButton_3click(self):
#         return 1
    
#     def pushButton_6click(self):
        
#         return 2
        
# #隐患输入预览信号槽
#     def show_textbrowser(self):
        
#         get_yhnr = self.plainTextEdit_yhnr.toPlainText() #获取输入的隐患内容
#         get_yhzgcs = self.plainTextEdit_yhzgyq.toPlainText()  #获取输入的隐患整改措施
#         get_djcry = self.plainTextEdit_jcry.toPlainText()  #获取输入的检查人员或单位
#         if self.plainTextEdit_qtzgyq.toPlainText() == "1":
#             get_qtzgyq = '整改完成后书面回复我公司'
#         else:
#             get_qtzgyq = self.plainTextEdit_qtzgyq.toPlainText() # 获取输入的其他整改要求
#         #隐患类型
#         get_yhlx = self.comboBox_yhlx.currentText()
#         #隐患级别
#         get_yhjb = self.comboBox_yhjb.currentText()
#         #被检查单位
#         get_bjcdw = self.comboBox_bjcdw.currentText()
#         #快速选择
        
#         if self.radioButton_2.isChecked() == True:
#             get_ksxz = self.comboBox_zrdw.currentText() #获取下拉菜单文本
#         elif self.radioButton.isCheckable() == True:
#             if self.pushButton_3click() == 1:
#                 self.list_zrry.append(self.lineEdit_zrry.text())
#                 self.kf_list_zrry.append(self.lineEdit_zrry_kf.text())
#                 self.textBrowser_2.setText('责任人员{}\n扣分{}'.format(self.list_zrry,self.kf_list_zrry))
                
#             elif self.pushButton_6click() == 2:
#                 self.list_zrglry.append(self.lineEdit_zrglry.text())
#                 self.kf_list_zrglry.append(self.lineEdit_zrglry_kf.text())
#                 self.textBrowser_3.setText('责任人员{}\n扣分{}'.format(self.list_zrglry,self.kf_list_zrglry))
#             else:
#                 pass
                
#         # get_zrry   = {'责任人员'    :list_zrry,"扣分"  :kf_list_zrry}
#         # get_zrglry = {'责任管理人员':list_zrglry,"扣分":kf_list_zrglry}
#         # get_zrglbm = {'责任管理部门':list_zrglbm,"扣分":kf_list_zrglbm}
        
#         self.textBrowser_xsyhnr.setText('【隐患内容】：{a}\n【整改措施】：{b}\n【检查人/单位】：{c}\n【其他整改要求】：{d}\n【隐患类型】：{e}\n【隐患级别】：{f}\n【被检查单位】：{g}\n'
#                                 .format(a = get_yhnr,b = get_yhzgcs,c=get_djcry,d=get_qtzgyq,e = get_yhlx,f =get_yhjb,g = get_bjcdw))

#%%新建数据库
#设置
database_path ='洁源隐患数据库'
#%%%通过QSqlDatabase建立sqlite数据库
#from set_datebase1 import set_database
#set_database('洁源隐患数据库2024.db')

#%%%新建数据库 通过sqlite3创建
#from set_hidden_database import set_hidden_database
#set_hidden_database('洁源隐患数据库2024.db')

#%%主程序入口
if __name__ == '__main__':
    app = QApplication([sys.argv])#ui主程序入口
    window = Ui_MainWindow() #创建主窗体对象并实例化
    window_yh = QMainWindow() #实例化QMainWindow
    window.setupUi(window_yh) #主窗体设置
    window_yh.show() 
    sys.exit(app.exec()) #循环中等待退出
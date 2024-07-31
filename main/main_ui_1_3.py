
"""
Created on Wed Jan  3 15:00:50 2024

@author: Microsoft
"""
import os
import sys
import time
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import( QApplication, QMainWindow, QVBoxLayout, QWidget   , QPushButton , QMessageBox    ,
                             QTextEdit   , QLabel     , QAction    , QGroupBox , QTextBrowser, QPlainTextEdit ,
                             QStatusBar  , QMenuBar   , QMenu      , QStyle    , QDateEdit   , QFileDialog    , 
                             QRadioButton, QCheckBox  ,QTableView  , QComboBox  )

from PyQt5.QtCore    import Qt, QRegularExpression, pyqtSignal, QRect, QCoreApplication, QMetaObject, QDate, QTimer,QSettings,QVariant
from PyQt5.QtSql     import QSqlQuery,QSqlDatabase
from PyQt5.QtGui     import QStandardItemModel, QStandardItem,QPixmap
from collections     import defaultdict
# TODO餐厨垃圾收运有两个即时整改

# 引入本地项目代码
from Notice_of_Rectification             import Write_notice_of_retification
from retification_confirmation_sheet     import write_retification_confirmation
from notification_of_checktion           import Write_inspect_the_situation
from Monthly_inspection_statistics_table import Write_inspect_the_situation_sheet
from Overall_Hidden                      import overall_hidden_sheet
from safety_checklist                    import Write_safety_checklist

from setPrinter                          import MainApp



# -*- coding: utf-8 -*-

#%% 触发器
class ToggleState:
    def __init__(self,state):
        self.state = state

    def toggle(self):
        if self.state:
            self.state = False
        else:
            self.state = True
        return self.state

#%% 继承重写
    
#获取数据框数据，作用：当失去焦点时，获取输入数据
class CustomTextEdit_one(QTextEdit):
    def __init__(self, parent=None):
        parent = parent.hidden
        super().__init__(parent)
    def focusOutEvent(self, event):
        super().focusOutEvent(event)  # 确保其他焦点事件正常处理
        Ui_MainWindow().get_QTextEdit_data(self)
    #####################################

class MyTextEdit(QTextEdit):
    editingFinished = pyqtSignal()
    def __init__(self, parent=None):
        super(MyTextEdit, self).__init__(parent)
        self.textChanged.connect(self.on_text_changed)  # 连接 textChanged 信号到文本变化槽函数
        self.timer = QTimer(self)    # 创建定时器
        self.timer.setInterval(1000)  # 设置定时器超时时间（毫秒）
        self.timer.timeout.connect(self.on_timer_timeout) # 连接定时器到定时器超时槽函数
        self.text_changed_flag = False   # 初始化文本变化标志

    def on_text_changed(self):
        # 设置文本变化标志为 True
        self.text_changed_flag = True
        # 启动定时器
        self.timer.start()

    def on_timer_timeout(self):
        # 检查文本是否变化
        if self.text_changed_flag:
            # 停止定时器
            self.timer.stop()
            # 发出 editingFinished 信号
            self.editingFinished.emit()
            
#继承并重写，作用：当QTextEdit失去焦点时，检查输入格式
class CustomTextEdit(MyTextEdit):
    def __init__(self, parent=None):
        parent = parent.hidden
        super().__init__(parent)
    def focusOutEvent(self, event):
        super().focusOutEvent(event)  # 确保其他焦点事件正常处理
        Ui_MainWindow().check_input_format(self)


#%% 主UI结构
# -*- coding: utf-8 -*-

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
        self.hidden = QTableView(self.groupBox_yhztz)
        self.hidden.setObjectName(u"hidden")
        self.hidden.setGeometry(QRect(10, 20, 1601, 931))

        # 生成
        self.groupBox_sc = QGroupBox(self.centralwidget)
        self.groupBox_sc.setObjectName(u"groupBox_sc")
        self.groupBox_sc.setGeometry(QRect(1730, 30, 175, 211))

        self.pushButton_sc = QPushButton(self.groupBox_sc)  # 生成按钮
        self.pushButton_sc.setObjectName(u"pushButton_sc")
        self.pushButton_sc.setGeometry(QRect(10, 20, 61, 23))

        self.checkBox_zgtzs = QCheckBox(self.groupBox_sc)   # 整改通知书复选框
        self.checkBox_zgtzs.setObjectName(u"checkBox_zgtzs")
        self.checkBox_zgtzs.setGeometry(QRect(10, 50, 81, 16))


        self.checkBox_zgqrd = QCheckBox(self.groupBox_sc)  # 整改确认单复选框
        self.checkBox_zgqrd.setObjectName(u"checkBox_zgqrd")
        self.checkBox_zgqrd.setGeometry(QRect(10, 70, 81, 16))
        #self.checkBox_zgqrd.setChecked(True)

        self.checkBox_tb = QCheckBox(self.groupBox_sc)     # 通报复选框
        self.checkBox_tb.setObjectName(u"checkBox_tb")
        self.checkBox_tb.setGeometry(QRect(10, 90, 71, 16))


        self.checkBox_jcqktjb = QCheckBox(self.groupBox_sc) # 检查情况统计表复选框
        self.checkBox_jcqktjb.setObjectName(u"checkBox_jcqktjb")
        self.checkBox_jcqktjb.setGeometry(QRect(10, 110, 111, 16))

        self.checkBox_yhztz = QCheckBox(self.groupBox_sc)   # 隐患总台账复选框
        self.checkBox_yhztz.setObjectName(u"checkBox_yhztz")
        self.checkBox_yhztz.setGeometry(QRect(10, 130, 111, 16))
        
        self.checkBox_jcb = QCheckBox(self.groupBox_sc)     # 检查表复选框
        self.checkBox_jcb.setObjectName(u"checkBox_jcb")
        self.checkBox_jcb.setGeometry(QRect(10, 150, 111, 16))
        
        
        self.checkBox_lxd = QCheckBox(self.groupBox_sc)     # 工程维修联系单复选框
        self.checkBox_lxd.setObjectName(u"checkBox_lxd")
        self.checkBox_lxd.setGeometry(QRect(90, 50, 81, 16))
        

        self.enable_radio_printer = QRadioButton(u"生成后自动打印", self.groupBox_sc) # 生成后自动打印
        self.enable_radio_printer.setObjectName(u"enable_radio_printer")
        self.enable_radio_printer.setGeometry(QRect(9, 165, 120, 30))

        self.pushButton_dy = QPushButton(self.groupBox_sc)  # 打印机设置
        self.pushButton_dy.setObjectName(u"pushButton_sc")
        self.pushButton_dy.setGeometry(QRect(32, 190, 70, 23))
        self.pushButton_dy.setEnabled(False)

        self.groupBox = QGroupBox(self.centralwidget)  # 框
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(1630, 30, 81, 211))

        self.pushButton = QPushButton(self.groupBox)   # 刷新
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 20, 81, 23))

        self.pushButton_3 = QPushButton(self.groupBox) # 加一行
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 50, 81, 23))

        self.pushButton_4 = QPushButton(self.groupBox)  
        self.pushButton_4.setObjectName(u"pushButton_4")# 删除
        self.pushButton_4.setGeometry(QRect(0, 80, 81, 23))

        self.pushButton_6 = QPushButton(self.groupBox)  # 全选
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(0, 110, 81, 23))
        
        self.pushButton_7 = QPushButton(self.groupBox)  # 快选
        self.pushButton_7.setObjectName(u"pushButton_6")
        self.pushButton_7.setGeometry(QRect(48, 140, 32, 23))
        self.pushButton_7.setEnabled(False)

        self.enable_button_radio = QRadioButton(u"开启", self.groupBox)
        self.enable_button_radio.setObjectName(u"enable_button_radio")
        self.enable_button_radio.setGeometry(QRect(3, 137, 50, 30))

        self.textBrowser = QTextBrowser(self.centralwidget)    
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(1630, 570, 256, 71)) 

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

        MainWindow.setStatusBar(self.statusbar) # 状态栏


        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"导入数据")
        self.groupBox_3.setGeometry(QRect(1630, 660, 181, 291))

        self.pushButton_from_zc = QPushButton(self.groupBox_3)  # 从自查统计表
        self.pushButton_from_zc.setObjectName(u"pushButton_from_zc")
        self.pushButton_from_zc.setGeometry(QRect(0, 20, 81, 30))
        
        self.pushButton_from_zcqu = QPushButton(self.groupBox_3)  # 从自查统计表确认保存
        self.pushButton_from_zcqu.setObjectName(u"pushButton_from_zcqu")
        self.pushButton_from_zcqu.setGeometry(QRect(90, 20, 61, 30))


        ######### 初始化隐患配置面板 ##########
        self.HiddenConfigPaddld()

        ########## 菜单栏 ###########
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1922, 23))

        self.menu = QMenu(self.menubar)         # 文件
        self.menu.setObjectName(u"menu")

        self.menu_2 = QMenu(self.menubar)       # 设置
        self.menu_2.setObjectName(u"menu_2")

        self.menu_3 = QMenu(self.menubar)       # 帮助
        self.menu_3.setObjectName(u"menu_3")


        ########## 菜单栏动作 ##########
        style = QApplication.style()

        # ==== 文件操作部分 ==== #
        #新建文件
        self.aFileNew = QAction(MainWindow)
        self.aFileNew.setObjectName(u"actionhao")
        self.aFileNew.setIcon(style.standardIcon(QStyle.SP_FileIcon)) # 添加一个图标
        self.aFileNew.setShortcut(Qt.CTRL + Qt.Key_N)                 # 添加快捷键
        self.aFileNew.triggered.connect(self.onFileNew)
        
        #打开文件
        self.aFileOpen = QAction(MainWindow)
        self.aFileOpen.setObjectName(u"actionhao_2")
        self.aFileOpen.setIcon(style.standardIcon(QStyle.SP_DialogOpenButton))
        self.aFileOpen.setShortcut(Qt.CTRL + Qt.Key_O)
        self.aFileOpen.triggered.connect(self.onFileOpen)

        # ==== 设置部分 ==== #
        self.hidden_setconfig = QAction(MainWindow)
        self.hidden_setconfig.setObjectName(u"actionhao_3")
        self.hidden_setconfig.setIcon(style.standardIcon(QStyle.SP_ComputerIcon))
        self.hidden_setconfig.triggered.connect(self.ohidden_setconfig)

        # ==== 帮助部分 ==== #
        self.aHelpAbout = QAction(MainWindow)
        self.aHelpAbout.triggered.connect(self.onHelpAbout)

        ###############################
        # 添加到菜单栏
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        # 为菜单栏添加动作
        self.menu.addAction(self.aFileNew)
        self.menu.addAction(self.aFileOpen)

        self.menu_2.addAction(self.hidden_setconfig)

        self.menu_3.addAction(self.aHelpAbout)


        MainWindow.setMenuBar(self.menubar) # 菜单栏
        ###############################
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # 创建 QStandardItemModel
        self.model = QStandardItemModel()
        
        # 触发器
        self.select_allcheckbox = ToggleState(True)  # checkbox触发器

        # 初始化勾选框id值
        self.get_check_data        = []        # 用于 self.line_get_check() 函数
        self.get_check_data_output = []        # 用于获取生成中的checkbox状态   [1,2,3,4]：对应-> [整改通知书，整改确认单，通报，检查情况统计表]

        self.dataline = [  'id' ,'check_time', 'check_type','hidden_content', 'hidden_image','hidden_type', 'hidden_level', 'unit_to_be_inspected', 'inspector', 'check_the_location','responsible_punish', 'responsible_manager_punish','responsible_department_punish','corrective_measures','corrective_deadline','correactive_situastion','retification_complete_time','retification_number','retification_confirmation_number']
#%%信号槽
        #按钮
        self.pushButton_3 .clicked.connect(self.add_unit_to_columns)   # ‘添加’按钮
        self.pushButton   .clicked.connect(self.refresh)               # ‘刷新’按钮
        self.pushButton_6 .clicked.connect(self.selec_checkbox_AllorNo)# ‘全选’按钮 
        self.pushButton_4 .clicked.connect(self.delete_selected_rows)  # ‘删除’按钮
        self.pushButton_sc.clicked.connect(self.output_pushbutton)     # ‘生成’按钮
        self.enable_button_radio.toggled.connect(lambda checked: self.pushButton_7.setEnabled(checked))   # 开启快选
        self.enable_radio_printer.toggled.connect(lambda checked: self.pushButton_dy.setEnabled(checked)) # 开启打印机设置按钮
        

        self.pushButton_7.clicked.connect(self.run_calender)           # ‘快选’按钮
        self.pushButton_dy.clicked.connect(self.printer)
        

        # 连接itemChanged信号到槽函数 
        self.model.itemChanged.connect(self.onItemChanged)             # 单元格变动信号

        ##### 生成 #####
        self.checkBox_zgtzs.stateChanged.connect(  lambda data = self.checkBox_zgtzs   , number = 1: self.get_output_checkbox(data,number))  # 整改通知书
        self.checkBox_zgqrd.stateChanged.connect(  lambda data = self.checkBox_zgqrd   , number = 2: self.get_output_checkbox(data,number))  # 整改确认单
        self.checkBox_tb   .stateChanged.connect(  lambda data = self.checkBox_tb      , number = 3: self.get_output_checkbox(data,number))  # 通报
        self.checkBox_jcqktjb.stateChanged.connect(lambda data = self.checkBox_jcqktjb , number = 4: self.get_output_checkbox(data,number))  # 检查情况统计表
        self.checkBox_yhztz.stateChanged.connect(  lambda data = self.checkBox_jcqktjb , number = 5: self.get_output_checkbox(data,number))  # 隐患总台账
        self.checkBox_jcb  .stateChanged.connect(  lambda data = self.checkBox_jcqktjb , number = 6: self.get_output_checkbox(data,number))  # 检查表
        self.checkBox_lxd  .stateChanged.connect(  lambda data = self.checkBox_jcqktjb , number = 7: self.get_output_checkbox(data,number))  # 工程维修联系单
        
        ##### 导入 #####
        self.pushButton_from_zc.clicked  .connect(self.load_from_selfcheck)   # 从自查统计表导入
        self.pushButton_from_zcqu.clicked.connect(self.save_zicha_data)       # 从自查统计表导入 确认保存


#%% 初始化tableview
        self.set_database_and_biuldtable()                                       # 建立表格设置表头及连接数据库
        self.hidden.setModel(self.load_data_to_model())                          # 放入standermodel
        self.hidden.setContextMenuPolicy(Qt.CustomContextMenu)                   # 在单元格中显示插入行
        self.hidden.customContextMenuRequested.connect(self.show_context_menu)
        self.set_row_column()                                                    # 设置列宽列高
        self.set_checkbox_in_lie(False)                                          # 在每行末尾添加复选框
#%% 初始化其他数据
        self.zicha_data =  {'A': [None, None, None], 'B': [None, None, None]}

#%% 菜单栏动作槽
    def msgCritical(self, strInfo):
        dlg = QMessageBox(self)
        dlg.setIcon(QMessageBox.Critical)
        dlg.setText(strInfo)
        dlg.show()

    def onFileNew(self):      # 新建数据库
        # current_directory = os.getcwd() 获取当前运行目录
        self.show_warning_message('请自行复制，谢谢')

    def onFileOpen(self):     # 打开文件
        path, _ = QFileDialog.getOpenFileName(window_yh, '打开文件', '')
        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()
            except Exception as e:
                self.msgCritical(str(e))
            else:
                self.path = path
                self.txtEditor.setPlainText(text)

    def ohidden_setconfig(self):
        from hidden_setconfig_paddle import HiddenSetConfigWindow
        self.m = HiddenSetConfigWindow('settings.ini')              # 实例化tiaozhuan.py中的Ui_MainWindow类
        self.m.show()                                               # show()方法显示窗口

    def onHelpAbout(self):
        QMessageBox.information(window_yh, '斗战胜佛', '威威哥激情版')

#%% 快选日期范围
    def run_calender(self):
        self.set_checkbox_in_lie(False)               # 重新在每行末尾设置复选框
        from select_calender import DateRangePicker
        self.n = DateRangePicker()                    # 实例化tiaozhuan.py中的Ui_MainWindow类
        self.n.show()                                 # show()方法显示窗口
        self.n.date_range_confirmed.connect(lambda: self.fast_checkbox())
        self.n.date_range_confirmed.connect(lambda: self.enable_button_radio.setChecked(False))

    # 按日历范围快速选择勾选框
    def fast_checkbox(self):
        self.get_check_data = []
        from datetime import datetime, timedelta
        self.select_calender = self.n.confirm_dates()              # 获取选择的日期范围，类型是 tuple
        start_date_str ,end_date_str, select = self.select_calender# 解包成开始日期和结束日期
        print(select)
        # 将字符串转换为datetime对象
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date   = datetime.strptime(end_date_str, "%Y-%m-%d")

        date_range = []

        # 生成日期范围
        current_date = start_date
        while current_date <= end_date:
            date_range.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)
        #print(date_range)

        # 从数据库读取日期数据并生成序列字典
        query = QSqlQuery("SELECT check_time,check_type,id  FROM hidden ")                     # WHERE Id = {}
        while query.next():
            database_date = datetime.strptime(query.value(0), "%Y-%m-%d").strftime('%Y-%m-%d') # 二次转换，避免2024-05-01 和2024-05-1格式错误
            if database_date in date_range:
                if select == query.value(1):
                    row_aim = query.value(2)
                    self.set_checkbox(True,row_aim)                                            # 勾选目标复选框
                    self.get_check_data.append(row_aim)
        #print(self.get_check_data)

#%% 打印机设置
    def printer(self):
        MainApp().print_window()

#%% 调用打印机
    def run_printer(self,file_path):
        if self.enable_radio_printer.isChecked() == True:
            MainApp()
            MainApp().run_printer(file_path)

#%% ####### 功能函数 ########

#%%建立表格设置表头及连接数据库 
    def set_database_and_biuldtable(self):

        self.list = [
                     'id'               ,
                     '检查时间'          ,
                     '检查类型'          ,
                     '隐患内容'          ,
                     '隐患图片'          , 
                     '隐患类型'          , 
                     '隐患级别'          , 
                     '被检查单位'        ,
                     '检查人员'          ,
                     '检查地点'          ,
                     '责任人及扣分'      ,
                     '责任管理人员及扣分',
                     '责任管理部门及扣分',
                     '隐患整改措施'     ,
                     '隐患整改期限'     ,
                     '整改完成情况'     ,
                     '整改完成时间'     ,
                     '整改通知书编号'   ,
                     '整改确认单编号'   ,
                     '勾选'
                     ]
        self.model.setHorizontalHeaderLabels(self.list)
        # 连接SQLite数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('{}'.format( self.settings.value("数据库地址"     , QVariant(""))))
        if not self.db.open():
            QMessageBox.critical(None, "Error", "Database Error: %s" % self.db.lastError().text())


#%% 设置列宽列高
    def set_row_column(self):
        # 设置列宽
        _header = self.hidden.horizontalHeader()                # 获取水平表头对象
        #_header.setMinimumHeight(30)

        # 设置列宽度     [0, 1, 2 ,  3,  4 , 5 , 6 , 7 , 8 , 9 ,10 , 11, 12,13 ,14 ,15 ,16 ,17 ]
        _column_wight = [28,100,85,200,170,170,130,140,140,140,130,130,130,200,100,100,100,100,100]
        for i in  range(len(_column_wight)):
            _header.resizeSection(i,_column_wight[i] )          # 设置列宽度

        # 设置所有tableview默认行高
        self.hidden.verticalHeader().setDefaultSectionSize(100)

#%%在每行末尾添加复选框
    def set_checkbox_in_lie(self,select = False):
        for row in range(self.model.rowCount()):
            self.set_checkbox(select, row)
#%% 设置复选框
    def set_checkbox(self,select,row):
        checkbox = QCheckBox()
        checkbox.setChecked(select)                                    # 设置复选框默认不选中
        checkbox.setStyleSheet("margin-left:10%; margin-right:10%;")   # 设置复选框居中
        checkbox.stateChanged.connect(lambda date = checkbox , row = row , column_last = self.model.columnCount() - 1 : self.line_get_check(date,row , column_last))
        self.hidden.setIndexWidget(self.model.index(row, self.model.columnCount() - 1), checkbox)

#%% 从数据库加载数据 
    def load_data_to_model(self):

        # 从数据库中查询数据并添加到模型中
        query = QSqlQuery("SELECT * FROM hidden")
        while query.next():
            items = [QStandardItem(str(query.value(i))) for i in range(len(self.list)-1)]
            self.model.appendRow(items)

        return self.model
#%% 插入行

    def show_context_menu(self, pos):
        menu = QMenu(window_yh)
        insert_row_action = QAction("插入行", window_yh)
        insert_row_action.triggered.connect(self.insert_row)
        menu.addAction(insert_row_action)
        menu.exec_(self.hidden.viewport().mapToGlobal(pos))

    def insert_row(self):
        row = self.hidden.currentIndex().row() 
        self.model.insertRow(row)
        query = QSqlQuery("SELECT id FROM hidden")
        hidden_count = []
        
        while query.next():
            hidden_count.append(query.value(0))
        
        hidden_count.sort(reverse=True) # 将列表逆序，避免插入错误
        
        if not query.exec_():
            print("保存插入行错:", query.lastError().text())
            
        
        t = time.time()
        query = QSqlQuery()
        query.prepare("UPDATE hidden SET id=? WHERE id =?")
        
        # update_query = f' UPDATE hidden SET {column_name}=? WHERE id =? '
        # query.exec_(str(update_query))
        # query.addBindValue(data)
        # query.addBindValue(row)
        
        new_id = [ old_id+1 for old_id in hidden_count   if old_id >= row]
        
        query.addBindValue(new_id)
        
        old_id = [ old_id for old_id in hidden_count   if old_id >= row]
        query.addBindValue(old_id)
        
        if not query.execBatch():
            print(query.lastError())
        e = time.time()-t
        print(hidden_count,new_id)
        # lll = [QSqlQuery(f"UPDATE hidden SET id={old_id+1} WHERE id ={old_id}")  for old_id in hidden_count   if old_id >= row]
        
        
        print('耗时：',e)
        self.row_control(row)

#%% 刷新按钮 
    def refresh(self):
        
        # 刷新隐患设置面板
        self.HiddenConfigPaddld()
        
        # 刷新id
        self.refresh_id()
        
        # 断开模型与表格视图的连接
        self.hidden.setModel(None)
    
        # 清空表格视图
        self.hidden.clearSpans()

        # 将表格视图与新的模型连接
        self.hidden.setModel(self.model)

        # 清空表格视图
        self.model.removeRows(0, self.model.rowCount())

        # 重新加载数据到模型
        self.load_data_to_model()

        # 重新设置列宽列高
        self.set_row_column()

        # 重新在每行末尾设置复选框
        self.set_checkbox_in_lie(False)

        # 重置勾选框
        self.get_check_data = []

        # 清理状态显示框
        self.textBrowser.clear()

#%% 检测单元格变化并保存
    def onItemChanged(self, item):
        index = self.model.indexFromItem(item)
        if index.isValid():
            row    = int(index.row())
            column = index.column()
            data   = item.text()
            #print("Cell at row {}, column {} changed to: {}".format(row, column, data))
            print('发生变化的单元格：data,row，column：',data,row,column)
            self.save_new_cell(data,row,column)
            
#%% 对数据库插入列
    def insert_database(self,column_name_onebyone):
        data = 'ALTER TABLE hidden ADD COLUMN {} TEXT'.format(column_name_onebyone)
        print(data)
        query = QSqlQuery(data)

#%%保存单个单元格数据     
    def save_new_cell(self,data,row,column):

        column_name = self.dataline[column]
        query = QSqlQuery()
        # 构造更新语句并执行  
        update_query = f' UPDATE hidden SET {column_name}=? WHERE id =? '
        query.exec_(str(update_query))
        query.addBindValue(data)
        query.addBindValue(row)
        #print(保存的单元格data,row,column,column_name)
        if not query.exec():
            raise Exception(query.lastError().text())

#%% 保存 
    def save_data_to_database(self):
        # 遍历 QStandardItemModel 中的数据，并将更改保存到数据库
        query = QSqlQuery()
        query.prepare(
            """
            INSERT OR REPLACE INTO hidden (id ,check_time, check_type,hidden_content, hidden_image,hidden_type, hidden_level, unit_to_be_inspected, inspector, check_the_location,responsible_punish, responsible_manager_punish,responsible_department_punish,corrective_measures,corrective_deadline,correactive_situastion,retification_complete_time,retification_number)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ? ,?,?,?,?,?)
            """
        )

        for row in( range(self.model.rowCount())):
            for column in (range(len(self.list)-1)):
                query.addBindValue(self.model.item(row, column).text())
    
            if not query.exec_():
                print("Error saving data:", query.lastError().text())


#%% 刷新id
    def refresh_id(self):
        query = QSqlQuery()
        query.exec_("SELECT id FROM hidden")

        hidden_count = [] 
        while query.next():   # 检查是否有结果，并获取计数值
            hidden_count.append(query.value(0))
        for new_id, old_id in enumerate(hidden_count):
            # print("new_id:",new_id,"old_id:",old_id)
            # 已优化：如果旧id不按，不必从头，可用异步处理
            if new_id != old_id:
                query.exec_(f"UPDATE hidden SET id={new_id} WHERE id ={old_id}")
                
                # self.save_new_cell(new_id, old_id, 0)

#%% 弹簧器
    def selec_checkbox_AllorNo(self):
        self.set_checkbox_in_lie(self.select_allcheckbox.state)                     # 勾选全部 tableview 勾选框
        self.select_all_checkbox(self.select_allcheckbox.state)
        self.select_allcheckbox.toggle()

#%% 全选复选框
    def select_all_checkbox(self,select):
        if select == True:
            self.get_check_data = [i for i in range(self.model.rowCount())]#.append(b)

#%%新增一行并添加组件
    def add_unit_to_columns(self):
        row = self.model.rowCount()
        its = QStandardItem(f"{row}")
        self.model.appendRow(its)
        self.row_control(row)
    def row_control(self,row):
        
        hidden_class = self.settings.value('隐患类型下拉列表', QVariant("")).split(',') # ["一般隐患（班组级）","一般隐患（厂级）","一般隐患（公司级）"]  
        categories   = self.settings.value('检查类型下拉列表', QVariant("")).split(',') # ["自查", "查收运","查行政与应急","海宜查", "政府部门查", "安保部查"]
        fuck_hidden  = self.settings.value('隐患级别下拉列表', QVariant("")).split(',') # ["设备设施的不安全状态", "电气安全隐患", "管理缺失", "火灾安全隐患", "人员违反安全管理规定行为",  "应急管理隐患", "车辆安全隐患",  "食品安全隐患", "门岗管理隐患","环保隐患", "危险化学品安全隐患","八大危险作业管理隐患"]

        #######下拉列表#######
        quantity_combobox = QComboBox()    # 隐患级别
        quantity_combobox.addItems(hidden_class)
        quantity_combobox.currentIndexChanged.connect(lambda index, combo_box=quantity_combobox: self.on_combo_box_changed(combo_box))
        self.hidden.setIndexWidget(self.model.index(row, 6), quantity_combobox)

        category_combobox = QComboBox()    # 隐患类型
        category_combobox.addItems(categories)
        category_combobox.currentIndexChanged.connect(lambda index, combo_box=category_combobox: self.on_combo_box_changed(combo_box))
        self.hidden.setIndexWidget(self.model.index(row, 2), category_combobox)

        fuck_hidden_combobox = QComboBox() # 自查
        fuck_hidden_combobox.addItems(fuck_hidden)
        fuck_hidden_combobox.currentIndexChanged.connect(lambda index, combo_box=fuck_hidden_combobox: self.on_combo_box_changed(combo_box))
        self.hidden.setIndexWidget(self.model.index(row, 5), fuck_hidden_combobox)

        ######### 在每行末尾添加复选框######
        checkbox = QCheckBox()
        checkbox.setChecked(False)                                    # 设置复选框, 默认选中
        checkbox.setStyleSheet("margin-left:10%; margin-right:10%;")  # 设置复选框居中
        checkbox.stateChanged.connect(lambda date = checkbox , row = row , column_last = self.model.columnCount() - 1: self.line_get_check(date,row , column_last))
        self.hidden.setIndexWidget(self.model.index(row, self.model.columnCount() - 1), checkbox)
        
        ############ 日期 ###########

        ## 检查日期
        date_edit = QDateEdit()                    # 使用 QDateEdit 作为编辑器，并设置为当日日期
        date_edit.setDate(QDate.currentDate())     # 设置为当日日期
        date_edit.dateChanged.connect(lambda x = date_edit , row = row , column = 1 : self.onDateChanged(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 1), date_edit)

        ## 隐患整改期限
        date_edit_qx = QDateEdit()                 # 使用 QDateEdit 作为编辑器，并设置为当日日期
        date_edit_qx.setDate(QDate.currentDate())  # 设置为当日日期
        date_edit_qx.dateChanged.connect(lambda x = date_edit_qx  , row = row ,column = 14 : self.onDateChanged(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 14), date_edit_qx)

        #########添加图片#######
        ##隐患图片
        button = QPushButton('先复制图片\n再点此')
        self.hidden.setIndexWidget(self.model.index(row, 4), button)
        button.clicked.connect(lambda _, row = row ,colunm = 4: self.get_clipboard_image(row,colunm))

        #########添加输入框#######
        ##责任人及扣分
        line_edit_tt = CustomTextEdit(self) # 添加文本输入框
        line_edit_tt.editingFinished.connect(lambda x = line_edit_tt , row = row ,column = 10 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 10), line_edit_tt)

        ##责任管理人员及扣分
        line_edit_t = CustomTextEdit(self) # 添加文本输入框
        line_edit_t.editingFinished.connect(lambda x = line_edit_t , row = row ,column = 11 : self.get_text_frome_QTextEdit(x, row,column))
        #line_edit_t.setStyleSheet("background-color:cyan;")
        self.hidden.setIndexWidget(self.model.index(row, 11), line_edit_t)

        ##责任管理部门及扣分
        line_edit_ty = CustomTextEdit(self) # 添加文本输入框
        line_edit_ty.editingFinished.connect(lambda x = line_edit_ty , row = row ,column = 12 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 12), line_edit_ty)

        ##隐患内容
        yinhuanneirong_line = MyTextEdit()
        yinhuanneirong_line.editingFinished.connect(lambda x = yinhuanneirong_line , row = row ,column = 3 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 3), yinhuanneirong_line)

        ##隐患整改措施
        yinhuanzhenggai_line = MyTextEdit()
        yinhuanzhenggai_line.editingFinished.connect(lambda x = yinhuanzhenggai_line , row = row ,column = 13 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 13), yinhuanzhenggai_line)

        ##被检查单位 
        checkebale_line = MyTextEdit(self.settings.value("被检查单位预置内容"     , QVariant("")))# "海宜洁源餐厨垃圾处置有限公司" 
        checkebale_line.editingFinished.connect(lambda x = checkebale_line , row = row ,column = 7 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 7), checkebale_line)

        ##检查人员  
        yinhuanneirong_line = MyTextEdit(self.settings.value("检查人员预置内容"     , QVariant("")))
        yinhuanneirong_line.editingFinished.connect(lambda x = yinhuanneirong_line , row = row ,column = 8 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 8), yinhuanneirong_line)

        ##检查地点  
        yinhuanneirong_line = MyTextEdit(self.settings.value("检查地点预置内容"     , QVariant("")))# "洁源公司餐厨项目现场"
        yinhuanneirong_line.editingFinished.connect(lambda x = yinhuanneirong_line , row = row ,column = 9 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 9), yinhuanneirong_line)

        ##整改完成情况
        yinhuanneirong_line = MyTextEdit()
        yinhuanneirong_line.editingFinished.connect(lambda x = yinhuanneirong_line , row = row ,column = 15 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 15), yinhuanneirong_line)

        ##整改完成时间
        yinhuanneirong_line = MyTextEdit()
        yinhuanneirong_line.editingFinished.connect(lambda x = yinhuanneirong_line , row = row ,column = 16 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 16), yinhuanneirong_line)

        ##整改确认单
        yinhuanneirong_line = MyTextEdit()
        yinhuanneirong_line.editingFinished.connect(lambda x = yinhuanneirong_line , row = row ,column = 17 : self.get_text_frome_QTextEdit(x, row,column))
        self.hidden.setIndexWidget(self.model.index(row, 17), yinhuanneirong_line)

        ## 获取当日日期
        last_day = time.strftime('%Y-%m-%d', time.gmtime())

        ## 在database新建空行（预设行的初始值）
        query = QSqlQuery()
        query.exec_(
            """
            INSERT INTO hidden (id,check_time, check_type, hidden_type, hidden_level,unit_to_be_inspected,inspector,check_the_location)
            VALUES (?,?,?,?,?,?,?,?)
            """
        )

        list_in_line = [row,last_day,'自查','设备设施的不安全状态','一般隐患（班组级）',self.settings.value("被检查单位预置内容"     , QVariant("")),self.settings.value("检查人员预置内容"     , QVariant("")),self.settings.value("检查地点预置内容"     , QVariant(""))]
        
        for i in (range(len(list_in_line))):  
            query.addBindValue("{}".format(list_in_line[i])) # 此因python 版本原因，不能使用f'{str}'语法兼容
        if not query.exec_():
            print("Error saving data:", query.lastError().text())

#%% 获取tableview中和新加行中的选中的复选框
    def line_get_check(self,date ,row,column_last):
        if date == 2:
            self.get_check_data.append(row)
        elif date == 0:
            self.get_check_data.remove(row)
        print("当前选中了：",self.get_check_data)

#%% 获取日期数据并储存
    def onDateChanged(self, date ,row ,column):
        get_date = date.toString('yyyy-MM-dd')
        print("更新的文本内容为:",get_date,row,column)
        self.save_new_cell(get_date,row,column)        # 连接数据库并存储单元格数据

#%% 从自定义QTextEdit中获取数据并储存
    def get_text_frome_QTextEdit(self, x ,row,column):  
        new_text = x.toPlainText()
        print("更新的文本内容为:", new_text,row,column)
        self.save_new_cell(new_text,row,column)        # 连接数据库并存储单元格数据

# =============================================================================
#%% 当combobox变更时，获取发生变更的combobox的行列数，并返回变更后的名称 
    def on_combo_box_changed(self, combo_box):
        current_text = combo_box.currentText()         # 获取当前QComboBox的文本值
        index = self.hidden.indexAt(combo_box.pos())   # 获取QComboBox所在的模型索引
        row = index.row()                              # 获取QComboBox所在的行
        column = index.column()                        # 获取QComboBox所在的列
        print("ComboBox value changed to:", current_text)
        print("Row:", row, "Column:", column)

        #连接数据库并存储单元格数据
        self.save_new_cell(current_text,row,column)

#%%######### setupUi 配置及标题 ###### 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5a01\u5a01\u5a01", None))                   # 威威威
        self.yinhuan_picture.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u5165\u9690\u60a3\u56fe\u7247", None)) # 插入隐患图片
        
        self.groupBox_yhztz .setTitle(QCoreApplication.translate("MainWindow", u"\u9690\u60a3\u603b\u53f0\u8d26", None))   # 隐患总台账"
        self.groupBox_sc    .setTitle(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))                     # 生成（外框）
        self.pushButton_sc  .setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))                      # 生成（按钮）
        self.checkBox_zgtzs .setText(QCoreApplication.translate("MainWindow", u"\u6574\u6539\u901a\u77e5\u4e66", None))    # 整改通知书
        self.checkBox_zgqrd .setText(QCoreApplication.translate("MainWindow", u"\u6574\u6539\u786e\u8ba4\u5355", None))    # 整改确认单
        self.checkBox_tb    .setText(QCoreApplication.translate("MainWindow", u"\u901a\u62a5", None))                      # 通报
        self.checkBox_jcqktjb.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u60c5\u51b5\u7edf\u8ba1\u8868", None)) # 检查情况统计表
        self.checkBox_yhztz .setText(QCoreApplication.translate("MainWindow", u"隐患总台账", None))                         # 隐患总台账
        self.checkBox_jcb   .setText(QCoreApplication.translate("MainWindow", u"检查表", None))                             # 检查表
        self.checkBox_lxd   .setText(QCoreApplication.translate("MainWindow", u"维修联系单", None))                             # 工程维修联系单
        self.pushButton_dy .setText(QCoreApplication.translate("MainWindow" , u"打印机设置", None))                         # 打印机设置

        self.groupBox       .setTitle(QCoreApplication.translate("MainWindow", u"\u8868\u683c\u64cd\u4f5c", None))         # 表格操作
        self.pushButton     .setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))                      # 刷新

        self.pushButton_3   .setText(QCoreApplication.translate("MainWindow", u"\u52a0\u4e00\u884c", None))                # 加一行
        self.pushButton_4   .setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))                      # 删除
        self.pushButton_6   .setText(QCoreApplication.translate("MainWindow", u"全选", None))                              # 全选
        self.pushButton_7   .setText(QCoreApplication.translate("MainWindow", u"快选", None))                              # 选月
        self.groupBox_2     .setTitle(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u526a\u5207\u677f", None))   # 快速剪切板
        self.label          .setText(QCoreApplication.translate("MainWindow", u"\u88ab\u68c0\u67e5\u5355\u4f4d", None))    # 被检查单位

        self.groupBox_3     .setTitle(QCoreApplication.translate("MainWindow", u"导入数据", None))   
        self.pushButton_from_zc   .setText(QCoreApplication.translate("MainWindow", u"从自查统计表", None)) 
        self.pushButton_from_zcqu.setText(QCoreApplication.translate("MainWindow", u"确认保存", None)) 
                      
        # 快速剪切板
        self.plainTextEdit  .setPlainText(QCoreApplication.translate("MainWindow",  self.settings.value("快速剪切板预置内容"     , QVariant("")), None))

        '''菜单栏title'''        
        self.menu  .setTitle(QCoreApplication.translate("MainWindow", u"文件(&F)", None))   # 
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"设置(&S)", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"帮助(&H)", None))
        
        '''菜单栏动作'''
        self.aFileNew  .setText(QCoreApplication.translate("MainWindow", u"新建数据库(&N)", None))
        self.aFileOpen .setText(QCoreApplication.translate("MainWindow", u"打开(&O)..."   , None))
        self.aHelpAbout.setText(QCoreApplication.translate("MainWindow", u"关于(&A)..."   , None))
        self.hidden_setconfig.setText(QCoreApplication.translate("MainWindow", u"隐患面板设置"   , None))
    # retranslateUi


#%% 删除功能
    def delete_selected_rows(self):
        query = QSqlQuery()
        
        count_checkbox = len(self.get_check_data)
        for i in range(count_checkbox):
            row_id = self.get_check_data[i]
            print(f'删除第：{row_id}行')
            comform = '''DELETE FROM hidden WHERE id = {} ''' .format(row_id)
            query.exec_(comform)
            if not query.exec_():
                print("删除错误:", query.lastError().text())
                
        # self.refresh()
                            
#%%   检查输入格式并显示警告信息
    def check_input_format(self,line_edit):
        #text = line_edit.text()
        text = line_edit.toPlainText()
        # print(text)
        # 使用正则表达式验证输入格式
        regex = QRegularExpression('^[^\d]+-\d+(\.\d+)?([,，][^\d]+-\d+(\.\d+)?)*$') 
        if not regex.match(text).hasMatch():
            self.show_warning_message("输入格式错误，请重新输入！\n格式要求：姓名-分数，姓名-分数　\n如：口含明珠-1，进退自如-1\n如：汪自如-1")  # 显示警告信息
            #line_edit.clear()           # 清空输入内容

#%%    显示错误提示信息
    def show_warning_message(self,show_error_str):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("{}".format(show_error_str))
        message_box.setWindowTitle("警告")
        message_box.exec_()

#%%    从剪切板获取复制的图片地址
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
            self.hidden.setIndexWidget(self.model.index(row, colunm), label)
        else:
            self.show_warning_message("剪切板中不包含图片，请重新复制 ")

#%% 初始化隐患设置
    def HiddenConfigPaddld(self):
        if not os.path.exists('settings.ini'):
            # 创建默认配置文件
            settings = QSettings('settings.ini', QSettings.IniFormat)
            settings.setValue("text_box", "default text")
            
        self.settings = QSettings('settings.ini', QSettings.IniFormat)


#%%生成 
    # 获取生成中的checkbox
    def get_output_checkbox(self, data, number):
        get_shengcheng_name = ['整改通知书','整改确认单','通报','检查情况统计表','隐患总台账','检查表','工程维修联系单']
        if data == 2:
            self.get_check_data_output.append(number)
            get_name = ';  '.join([get_shengcheng_name[i-1] for i in self.get_check_data_output])
        elif data == 0:
            self.get_check_data_output.remove(number)
            get_name = '当前没选'
        print("生成框中当前选中了：",get_name) 


    # 生成按钮信号槽 
    def output_pushbutton(self):
        if 1 in self.get_check_data_output  :  # 整改通知书
            self.checktime_same_or_not()

        if 2 in self.get_check_data_output:    # 整改确认单
            self.same_or_not_checktype()

        if 3 in self.get_check_data_output:    # 通报
            self.Notification()

        if 4 in self.get_check_data_output:    # 检查情况统计表
            self.statistical()

        if 5 in self.get_check_data_output:    # 隐患总台账
            self.total()
            
        if 6 in self.get_check_data_output:    # 检查表
            self.checklist()
            
        if 7 in self.get_check_data_output:    # 工程维修联系单
            self.engineering_repair_sheet()
        get_shengcheng_name = ['整改通知书','整改确认单','通报','检查情况统计表','隐患总台账','检查表','工程维修联系单']
        get_name = ';  '.join([get_shengcheng_name[i-1] for i in self.get_check_data_output])
        
        print( '当前生成按钮下勾选了：',self.get_check_data_output, get_name) # int(self.get_check_data_output+1)


#%% 控制整改通知书  
    def rectification(self):  
        # 整改通知书模板地址 
        path_retification   = "{}".format(self.settings.value("隐患整改通知书模板"     , QVariant("")))
        # 输出文件地址
        output_dir          = "{}".format(self.settings.value("隐患整改通知书生成地址"     , QVariant("")))
        # 实例化
        output_retification = Write_notice_of_retification(path_retification, output_dir, self.get_check_data)
        # 输出编号
        retification_number = output_retification.connect_jieyuan_database() 
        # 显示
        self.textBrowser.append('{}号整改通知书生成完毕！'.format(retification_number))
        # 将生成的整改通知书编号放入数据库
        for i in range(len (self.get_check_data)):
            self.save_new_cell(retification_number,self.get_check_data[i],17)

        # 打印 
        self.run_printer(output_retification.output_file_path())

#%% 整改确认单
    def confirm(self):
        path_retification_confirmation   =  "{}".format(self.settings.value("隐患整改确认单模板"     , QVariant("")))

        output_dir                       =  "{}".format(self.settings.value("隐患整改确认单生成地址"     , QVariant("")))

        output_retification_confirmation = write_retification_confirmation(path_retification_confirmation,output_dir,self.get_check_data)

        retification_confirmation_number = output_retification_confirmation.connect_jieyuan_database() 

        self.textBrowser.append('{}号整改确认单生成完毕！'.format(retification_confirmation_number))

        # 将生成的整改通知书编号放入数据库
        for i in range(len (self.get_check_data)):

            self.save_new_cell(retification_confirmation_number,self.get_check_data[i],18)

        # 打印 
        self.run_printer(output_retification_confirmation.output_file_path())

#%% 通报  
    def Notification(self):
        path_retification_confirmation   = "{}".format(self.settings.value("每月通报模板"     , QVariant("")))

        output_dir                       = "{}".format(self.settings.value("每月通报生成地址"     , QVariant("")))

        output = Write_inspect_the_situation(path_retification_confirmation,output_dir,self.get_check_data)

        retification_confirmation_number = output.connect_jieyuan_database() 

        self.textBrowser.append('{}'.format(retification_confirmation_number))
        # 打印 
        self.run_printer(output.output_file_path())


#%% 检查情况统计表  
    def statistical(self):
        output_dir ="{}".format(self.settings.value("检查情况统计表生成地址"     , QVariant("")))

        output = Write_inspect_the_situation_sheet(output_dir,self.get_check_data)

        output.function()

        now4 = time.strftime("%Y年%m月"  ,time.localtime(time.time())).replace('年0','年')

        self.textBrowser.append('%s检查情况统计表生成完毕'%now4)

        # 打印 
        self.run_printer(output.output_file_path())

#%% 隐患总台账
    def total(self):

        output_dir = "{}".format(self.settings.value("隐患总台账生成地址"     , QVariant("")))

        output = overall_hidden_sheet(output_dir,self.get_check_data)

        output.function()

        now5 = time.strftime("%Y年%m月%d日"  ,time.localtime(time.time())).replace('年0','年').replace('月0','月')

        self.textBrowser.append('%s隐患台账生成完毕'%now5)

        # 打印 
        self.run_printer(output.output_file_path())

#%% 检查表
    def checklist(self):
        
        model_path  = "{}".format(self.settings.value("检查表模板"            , QVariant("")))

        output_dir  = "{}".format(self.settings.value("安全检查表生成地址"     , QVariant("")))

        output = Write_safety_checklist(model_path,output_dir,self.get_check_data)

        retification_confirmation_number = output.connect_jieyuan_database() 

        self.textBrowser.append('{}通报生成完毕！'.format(retification_confirmation_number))
        
        # 打印 
        self.run_printer(output.output_file_path())
#%% 工程维修联系单
    def engineering_repair_sheet(self): # TODO 待增加设置中工程维修联系单
        from engin_repair_sheet import Write_engineering_repair_sheet
        
        output_dir  = "{}".format(self.settings.value("工程维修联系单生成地址" , QVariant("")))
        
        output = Write_engineering_repair_sheet(output_dir,self.get_check_data)
        
        output.function()
        
        now5 = time.strftime("%Y年%m月%d日"  ,time.localtime(time.time())).replace('年0','年').replace('月0','月')
        
        self.textBrowser.append('%s工程维修联系单生成完毕'%now5)
        
        # 打印 
        self.run_printer(output.output_file_path())

#%% '生成'按钮  其他附属功能

# 检查时间是否同天,是否包含不同被检查单位
    def checktime_same_or_not(self):
        select_column = 'unit_to_be_inspected, check_time ,check_the_location'

        if len(self.get_check_data) == 1:
            self.rectification()

        if len(self.get_check_data)>=2:
            select_row    = tuple(self.get_check_data)
            execc         = "SELECT {} FROM hidden WHERE Id IN {} ".format(select_column,select_row) 
            #print(exec_)
            query         = QSqlQuery(execc)
            str_unit_to_be_inspected,str_check_time,check_the_location = [],[],[]               # 初始化为空列表
            cache         = [str_unit_to_be_inspected,str_check_time,check_the_location]     # 缓存

            while query.next():
                [cache[x].append(query.value(x)) for x in range(len(cache))]

            #对比列表中的不同项
            for i in range(len(str_unit_to_be_inspected)-1):
                if str_unit_to_be_inspected[i] != str_unit_to_be_inspected[i+1]:
                    self.show_warning_message("勾选中含有不同的被检查单位，请重新勾选！")  # 显示警告信息
                    break
                elif str_check_time[i]         != str_check_time[i+1]:
                    self.show_warning_message("勾选中含有不同的检查时间，请重新勾选！  ")  # 显示警告信息
                    break
                elif check_the_location[i]     != check_the_location[i+1]:
                    self.show_warning_message("勾选中含有不同的检查地点，请重新勾选！  ")  # 显示警告信息
                    break

                else:                                                                   # 调用检查通知书
                    self.rectification()
                    break

# 检查是否包含不同检查类型
    def same_or_not_checktype(self):
        select_column = 'check_type'
        if len(self.get_check_data) == 1:
            self.confirm()

        if len(self.get_check_data)>=2:

            select_row    = tuple(self.get_check_data)
            execc         = "SELECT {} FROM hidden WHERE Id IN {} ".format(select_column,select_row) 
            # print(exec_)
            query         = QSqlQuery(execc)
            check_type    = []               # 初始化为空列表

            while query.next():
                [check_type.append(query.value(0))]
            # print(check_type)
            c = []
# ==================待删除=====================================================
#             set1 = {1, 2, 3, 4, 5}
#             set2 = {1, 2}
#             print(set2.issubset(set1))    # 子集
#             print(set1.issuperset(set2))  # 超集
# =============================================================================
            classified_dates_dict  = defaultdict(list)     # 创建一个默认字典来存储日期分类及对应的序号列表
            for index, data in enumerate(check_type):      # 遍历日期列表，将日期及其对应的序号存入字典中
                classified_dates_dict[data].append(index)
            for name, data in classified_dates_dict.items():
                c.append(name)

            a = set(["自查","查收运","查行政与应急"])
            b = set(["海宜查", "政府部门查", "安保部查"])
            c = set(c)

            if a.intersection(c)and b.intersection(c):
                self.show_warning_message("勾选中含有不同的检查类型，请重新勾选！")  # 显示警告信息
            else:                                                                 # 调用整改确认单
                self.confirm()
    
#%% 从自查统计表导入
    def load_from_selfcheck(self):     # 打开文件
        path, _ = QFileDialog.getOpenFileName(window_yh, '打开文件', '')
        if path:
            try:
                global data  # TODO待取消全局变量
                data= pd.read_excel(path,sheet_name=0,header=1)  # 读取自查统计表的excel   文档参考 https://gairuo.com/p/pandas-read-excel
                data['检查时间'] = data['检查时间'].dt.strftime('%Y-%m-%d')   # 将时间戳转换为年月日
                data['检查时间'] = data['检查时间'].fillna(method='pad')      # 把当前值广播到后边的缺失值'
                data['序号'] = data['序号'] .astype(str)
                data['序号'] = data['序号'].replace(regex=[r'\d+','nan'], value=np.nan) #regex=True
                data['序号'] = data['序号'].fillna(method='pad')              # 把当前值广播到后边的缺失值'
                data.pop('图片')                                              # 删除
                data= data.drop(0,axis=0)                                     # 删除第一行
                data.dropna(axis=0,inplace=True,thresh=3)                     # 删除小于3个nan的非空行
                data = data.reset_index(drop=True)                            # 重置索引
                data.rename(columns={'内部扣分情况':'责任人'}, inplace=True )  # 重命名列名
                data.rename(columns={'Unnamed: 7':'责任管理人员'}, inplace=True ) 
                data.rename(columns={'Unnamed: 8':'责任部门'}, inplace=True ) 
                data['序号'] = data['序号'].str.replace('生产安全隐患问题','自查')
                data['序号'] = data['序号'].str.replace('收运安全隐患问题','查收运')
                data['序号'] = data['序号'].str.replace('综合、应急隐患问题','查行政与应急')
                
                global data_split_zzhenggai
                data_split_zzhenggai = data['整改要求'].str.split("（整改期限：",n=-1,expand=True)

                global data_split_zzhengga
                data_split_zzhengga  = data_split_zzhenggai[1].str.split("）",expand=True)
                data_split_zzhenggai.columns = ['整改要求','整改期限']

                if data_split_zzhengga[0].isnull().values.any():
                    self.show_warning_message('整改要求中存在数据未填写整改期限，请检查')
                else:
                    # data_split_zzhenggai['整改期限'] = data_split_zzhengga[0]
                    data['整改要求'] = data_split_zzhenggai['整改要求']
                    data['整改期限'] = data_split_zzhengga[0]
                    self.zicha_data = data 
                    # 在standaritem中显示 
                    row = self.model.rowCount()
                    for i, j in data.iterrows(): # i是int,j是series

                        its =[ QStandardItem(f"{row}"),
                               QStandardItem("{}".format(j['检查时间'])),
                               QStandardItem("{}".format(j['序号'])),
                               QStandardItem("{}".format(j['存在问题'])),
                               QStandardItem("{}".format(None)),
                               QStandardItem("{}".format(None)),
                               QStandardItem("{}".format(None)),
                               QStandardItem("{}".format(self.settings.value("被检查单位预置内容" , QVariant("")))),
                               QStandardItem("{}".format(self.settings.value("检查人员预置内容" , QVariant("")))),
                               QStandardItem("{}".format(self.settings.value("检查地点预置内容" , QVariant("")))),
                               QStandardItem("{}".format(j['责任人/责任单位'])),
                               QStandardItem("{}".format(j['责任管理人员'])), # TODO 考虑是否将责任人和扣分单独拆分
                               QStandardItem("{}".format(j['责任部门'])),
                               QStandardItem("{}".format(j['整改要求'])),
                               QStandardItem("{}".format(j['整改期限'])),
                               ]

                        self.model.appendRow(its)
                        row +=1

                # 批量导入数据库
            except Exception as e:
                self.show_warning_message(str(e))
                print(str(e))

    def save_zicha_data(self):
        
        if self.zicha_data.isnull().all().all():
            self.show_warning_message('未导入自查数据，请导入')
        else:
            query = QSqlQuery()
            # 获取最新插入的记录的id
            query.exec_("SELECT MAX(id) FROM hidden")
            if query.next():
                row =query.value(0)
    
            ## 在database新建空行（预设行的初始值）
            for i, j in self.zicha_data.iterrows(): # i是int,j是series
                query = QSqlQuery()

                query.exec_(
                    """
                    INSERT INTO hidden (id,check_time, check_type,hidden_content, hidden_type, hidden_level,unit_to_be_inspected,inspector,check_the_location,'responsible_punish', 'responsible_manager_punish','responsible_department_punish','corrective_measures','corrective_deadline')
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """
                ) 
                print(f'{row}')
                list_in_line = [row,j['检查时间'],j['序号'],j['存在问题'],None,None,self.settings.value("被检查单位预置内容" , QVariant("")),self.settings.value("检查人员预置内容" , QVariant("")),self.settings.value("检查地点预置内容", QVariant("")),j['责任人/责任单位'],j['责任管理人员'],j['责任部门'],j['整改要求'],j['整改期限']]
                
                for i in (range(len(list_in_line))):  
                    query.addBindValue("{}".format(list_in_line[i])) # 此因python 版本原因，不能使用f'{str}'语法兼容
                row +=1
                
                if not query.exec_():
                    print("存储数据错误:", query.lastError().text())


#%%主程序入口
if __name__ == '__main__':
    # 新建数据库
    # 通过QSqlDatabase建立sqlite数据库
    # Ui_MainWindow().insert_database('retification_confirmation_number') # 为数据添加列

    app = QApplication(sys.argv)# ui主程序入口
    window = Ui_MainWindow()      # 创建主窗体对象并实例化
    window_yh = QMainWindow()     # 实例化QMainWindow
    window.setupUi(window_yh)     # 主窗体设置
    window_yh.show() 

    sys.exit(app.exec())          # 循环中等待退出

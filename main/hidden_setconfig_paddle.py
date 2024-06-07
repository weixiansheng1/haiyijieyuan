# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:14:09 2024

@author: Microsoft
"""

# -*- coding: utf-8 -*-

from PyQt5.QtCore    import Qt,QRect       ,QCoreApplication ,QSettings  , QVariant
from PyQt5.QtWidgets import QWidget, QPushButton,QLabel           ,QFormLayout,QLineEdit,QDialog,QFileDialog,QTextEdit



################################################################################
## Form generated from reading UI file 'hidden_setconfig_paddleiAmgKx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

class HiddenSetConfigWindow(QDialog):

    def __init__(self,settings_file):
        super().__init__()
        self.setWindowTitle("隐患面板设置")
        self.resize(1350, 650)
        self.setWindowModality(Qt.ApplicationModal) # 设置窗口模态
        
        self.settings_file =settings_file 

        
# =============================================================================
#         # 初始化配置数据库 ini
# =============================================================================

        self.formLayoutWidget = QWidget(self)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")

        self.formLayout = QFormLayout(self)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setContentsMargins(20, 20, 60, 20)
        
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 520, 151, 23))
        self.pushButton.setText('新建今年数据库')


# =============================================================================
#         #数据库地址
# =============================================================================
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('数据库地址') # 

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)
        
        # 选择
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1292, 20, 55, 20))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"选择", None))# 保存

# =============================================================================
#         # 隐患整改通知书生成地址
# =============================================================================
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u6574\u6539\u901a\u77e5\u4e66\u751f\u6210\u5730\u5740", None))# 隐患整改通知书生成地址

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)
        
        # 选择
        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1292, 46, 55, 20))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"选择", None))# 保存


# =============================================================================
#         # 隐患整改确认单生成地址
# =============================================================================
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u6574\u6539\u786e\u8ba4\u5355\u751f\u6210\u5730\u5740", None))# 隐患整改确认单生成地址
        
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)
        
        # 选择
        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(1292, 72, 55, 20))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"选择", None))# 保存

# =============================================================================
#         # 每月通报生成地址
# =============================================================================
        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6bcf\u6708\u901a\u62a5\u751f\u6210\u5730\u5740", None))# 每月通报生成地址

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)
        
        # 选择
        self.pushButton_6 = QPushButton(self)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1292, 97, 55, 20))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"选择", None))# 保存
        
# =============================================================================
#         # 检查情况统计表生成地址
# =============================================================================
        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u60c5\u51b5\u7edf\u8ba1\u8868\u751f\u6210\u5730\u5740", None))# 检查情况统计表生成地址

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")


        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_5)

        # 选择
        self.pushButton_7 = QPushButton(self)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(1292, 124, 55, 20))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"选择", None))# 保存

# =============================================================================
#         # 隐患总台账生成地址
# =============================================================================
        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u603b\u53f0\u8d26\u751f\u6210\u5730\u5740", None))# 隐患总台账生成地址
        
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_6 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_6)

        # 选择
        self.pushButton_8 = QPushButton(self)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(1292, 149, 55, 20))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"选择", None))# 保存
        
# =============================================================================
#         # 检查表生成地址
# =============================================================================
        self.label_cl = QLabel(self.formLayoutWidget)
        self.label_cl.setObjectName(u"label_cl")
        self.label_cl.setText(QCoreApplication.translate("Form", u"检查表生成地址", None))# 隐患总台账生成地址
        
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_cl)

        self.lineEdit_cl = QLineEdit(self.formLayoutWidget)
        self.lineEdit_cl.setObjectName(u"lineEdit_cl")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_cl)

        # 选择
        self.pushButton_cl = QPushButton(self)
        self.pushButton_cl.setObjectName(u"pushButton_cl")
        self.pushButton_cl.setGeometry(QRect(1292, 175, 55, 20))
        self.pushButton_cl.setText(QCoreApplication.translate("Form", u"选择", None))# 保存
        

# =============================================================================
#         # 隐患整改通知书模板
# =============================================================================
        self.label_13 = QLabel(self.formLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u6574\u6539\u901a\u77e5\u4e66\u6a21\u677f", None))
        
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_13 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_13)

        # 选择
        self.pushButton_9 = QPushButton(self)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(1292, 202, 55, 20))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"选择", None))# 保存
# =============================================================================
#         # 隐患整改确认单模板
# =============================================================================
        self.label_14 = QLabel(self.formLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u6574\u6539\u786e\u8ba4\u5355\u6a21\u677f", None))
        
        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_14 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")


        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_14)
        
        # 选择
        self.pushButton_10 = QPushButton(self)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(1292, 227, 55, 20))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"选择", None))# 保存
        
# =============================================================================
#         # 每月通报模板
# =============================================================================
        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setText(QCoreApplication.translate("Form", u"\u6bcf\u6708\u901a\u62a5\u6a21\u677f", None))
        
        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_16 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit_16)

        # 选择
        self.pushButton_11 = QPushButton(self)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(1292, 253, 55, 20))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"选择", None))# 保存
        
# =============================================================================
#         # 检查表模板
# =============================================================================
        self.label_clm = QLabel(self.formLayoutWidget)
        self.label_clm.setObjectName(u"label_clm")
        self.label_clm.setText(QCoreApplication.translate("Form", u"检查表模板", None))
        
        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_clm)

        self.lineEdit_clm = QLineEdit(self.formLayoutWidget)
        self.lineEdit_clm.setObjectName(u"lineEdit_clm")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_clm)

        # 选择
        self.pushButton_clm = QPushButton(self)
        self.pushButton_clm.setObjectName(u"pushButton_clm")
        self.pushButton_clm.setGeometry(QRect(1292, 280, 55, 20))
        self.pushButton_clm.setText(QCoreApplication.translate("Form", u"选择", None))# 保存

# =============================================================================
#         # 保存
# =============================================================================
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(830, 520, 75, 23))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))# 保存
        
        
###############################################################################
        self.formLayoutWidget_2 = QWidget(self)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 320, 1299, 240))
        
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_2.setContentsMargins(10, 20, 20, 40)
        
# =============================================================================
#         # 检查类型下拉列表
# =============================================================================
        self.label_7 = QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u7c7b\u578b\u4e0b\u62c9\u5217\u8868", None))# 检查类型下拉列表
        
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_7 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_7)

        
# =============================================================================
#         # 隐患类型下拉列表
# =============================================================================
        self.label_8 = QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u7c7b\u578b\u4e0b\u62c9\u5217\u8868", None))# 隐患类型下拉列表
        
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_8 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_8)  
        

        
# =============================================================================
#         # 隐患级别下拉列表
# =============================================================================
        self.label_9 = QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u7ea7\u522b\u4e0b\u62c9\u5217\u8868", None))# 隐患级别下拉列表

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_9 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")


        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_9)


        
        
# =============================================================================
#         # 被检查单位预置内容
# =============================================================================
        self.label_10 = QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setText(QCoreApplication.translate("Form", u"\u88ab\u68c0\u67e5\u5355\u4f4d\u9884\u7f6e\u5185\u5bb9", None))# 被检查单位预置内容

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_10 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_10)
        
# =============================================================================
#         # 检查人员预置内容
# =============================================================================
        self.label_11 = QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u4eba\u5458\u9884\u7f6e\u5185\u5bb9", None))# 检查人员预置内容

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_11 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_11)

# =============================================================================
#         # 检查地点预置内容
# =============================================================================
        self.label_12 = QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u5730\u70b9\u9884\u7f6e\u5185\u5bb9", None))# 检查地点预置内容
        
        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_12 = QLineEdit(self.formLayoutWidget_2) 
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lineEdit_12)

# =============================================================================
#      # 快速剪切板预置内容
# =============================================================================
        self.label_13 = QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setText(QCoreApplication.translate("Form", u"快速剪切板预置内容", None))# 检查地点预置内容
        
        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_13)
        self.text_edit = QTextEdit(self.formLayoutWidget_2)
        self.text_edit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.text_edit.setFixedSize(1155, 60)
        self.text_edit.setObjectName(u"lineEdit_17")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.text_edit)

        # 加载配置
        self.load_settings()

        #### 信号槽 ####
        # lineEdit
        self.lineEdit   .textChanged.connect(lambda data ,menu = '数据库地址'           : self.save_settings(menu, data))
        self.lineEdit_2 .textChanged.connect(lambda data ,menu = '隐患整改通知书生成地址': self.save_settings(menu, data))
        self.lineEdit_3 .textChanged.connect(lambda data ,menu = '隐患整改确认单生成地址': self.save_settings(menu, data))
        self.lineEdit_4 .textChanged.connect(lambda data ,menu = '每月通报生成地址'      : self.save_settings(menu, data))
        self.lineEdit_5 .textChanged.connect(lambda data ,menu = '检查情况统计表生成地址': self.save_settings(menu, data))
        self.lineEdit_6 .textChanged.connect(lambda data ,menu = '隐患总台账生成地址'    : self.save_settings(menu, data))
        self.lineEdit_cl.textChanged.connect(lambda data, menu = "安全检查表生成地址"    : self.save_settings(menu, data))
      
        self.lineEdit_13.textChanged.connect(lambda data ,menu = '隐患整改通知书模板'    : self.save_settings(menu, data))
        self.lineEdit_14.textChanged.connect(lambda data ,menu = '隐患整改确认单模板'    : self.save_settings(menu, data))
        self.lineEdit_16.textChanged.connect(lambda data ,menu = '每月通报模板'          : self.save_settings(menu, data))
        self.lineEdit_clm.textChanged.connect(lambda data ,menu= '检查表模板'            : self.save_settings(menu, data))
        
        self.lineEdit_7 .textChanged.connect(lambda data ,menu = '检查类型下拉列表'      : self.save_settings(menu, data))
        self.lineEdit_8 .textChanged.connect(lambda data ,menu = '隐患类型下拉列表'      : self.save_settings(menu, data))
        self.lineEdit_9 .textChanged.connect(lambda data ,menu = '隐患级别下拉列表'      : self.save_settings(menu, data))
        self.lineEdit_10.textChanged.connect(lambda data ,menu = '被检查单位预置内容'    : self.save_settings(menu, data))
        self.lineEdit_11.textChanged.connect(lambda data ,menu = '检查人员预置内容'      : self.save_settings(menu, data))
        self.lineEdit_12.textChanged.connect(lambda data ,menu = '检查地点预置内容'      : self.save_settings(menu, data))
        self.text_edit  .textChanged.connect(lambda menu       = '快速剪切板预置内容'    : self.onTextChanged(menu) )
        
        # ‘保存’
        self.pushButton_2.clicked.connect(self.SaveChange)
        self.pushButton_3.clicked.connect(lambda  _,dataline = "数据库地址"           ,linename =self.lineEdit   :self.openfile_and_select(dataline,linename))
        self.pushButton_4.clicked.connect(lambda  _,dataline = "隐患整改通知书生成地址",linename =self.lineEdit_2 :self.select_folder(dataline,linename))
        self.pushButton_5.clicked.connect(lambda  _,dataline = "隐患整改确认单生成地址",linename =self.lineEdit_3 :self.select_folder(dataline,linename))
        self.pushButton_6.clicked.connect(lambda  _,dataline = "每月通报生成地址"      ,linename =self.lineEdit_4 :self.select_folder(dataline,linename))
        self.pushButton_7.clicked.connect(lambda  _,dataline = "检查情况统计表生成地址",linename =self.lineEdit_5 :self.select_folder(dataline,linename))
        self.pushButton_8.clicked.connect(lambda  _,dataline = "隐患总台账生成地址"    ,linename =self.lineEdit_6 :self.select_folder(dataline,linename))
        self.pushButton_cl.clicked.connect(lambda _,dataline = "安全检查表生成地址"    ,linename =self.lineEdit_cl:self.select_folder(dataline,linename))
       
        self.pushButton_9.clicked.connect(lambda  _,dataline = "隐患整改通知书模板"    ,linename =self.lineEdit_13:self.openfile_and_select(dataline,linename))
        self.pushButton_10.clicked.connect(lambda _,dataline = "隐患整改确认单模板"    ,linename =self.lineEdit_14:self.openfile_and_select(dataline,linename))
        self.pushButton_11.clicked.connect(lambda _,dataline = "每月通报模板"          ,linename =self.lineEdit_16:self.openfile_and_select(dataline,linename))
        self.pushButton_clm.clicked.connect(lambda _,dataline = "检查表模板"           ,linename =self.lineEdit_clm:self.openfile_and_select(dataline,linename))
        

# {'数据库地址': './洁源隐患数据库2024.db', '隐患整改通知书生成地址': '../main', '隐患整改确认单生成地址': '../main', '每月通报生成地址': '../main', '检查情况统计表生成地址': '../main', '隐患总台账生成地址': '../main', '隐患整改通知书模板': '../Template_resource/隐患台账类模板/海宜洁源公司安全检查整改通知书.docx', '隐患整改确认单模板': '../Template_resource/隐患台账类模板/洁源公司整改确认单.docx', '每月通报模板': '../Template_resource/隐患台账类模板/安全生产专项工作检查情况的通报.docx', '隐患类型下拉列表': '一般隐患（班组级）,一般隐患（厂级）,一般隐患（公司级）', '检查类型下拉列表': '自查,查收运,查行政与应急,海宜查,政府部门查,安保部查', '隐患级别下拉列表': '设备设施的不安全状态,电气安全隐患,管理缺失,火灾安全隐患,人员违反安全管理规定行为,应急管理隐患,车辆安全隐患,食品安全隐患,门岗管理隐患,环保隐患,危险化学品安全隐患,八大危险作业管理隐患', '被检查单位预置内容': '海宜洁源餐厨垃圾处置有限公司', '检查人员预置内容': '张健新、关智远、廖振威', '检查地点预置内容': '洁源公司餐厨项目现场', '快速剪切板预置内容': '珠海市海宜洁源餐厨垃圾处置有限公司\n河南艾尔旺新能源环境有限公司（设备厂家）\n广东建安昌盛控股集团有限公司（土建单位）\n杭州能源环境工程有限公司（设备厂家）\n维尔利环保科技集团股份有限公司（施工单位）\n深圳市沃尔奔达新能源股份有限公司（设备厂家）\n杭州楚环科技股份有限公司（设备厂家）\n珠海市城市开发监理有限公司（监理单位）\n上海市政工程设计研究总院（集团）有限公司（设计单位）\n珠海多特自动化工程有限公司（自控单位）\n有意餐饮管理公司（食堂承包单位）\n广东宏德科技物业有限公司（物业单位）\n'}

    # 选择文件地址
    def openfile_and_select(self,dataline,linename):
        options1 = QFileDialog.Options()
        settings = QSettings(self.settings_file, QSettings.IniFormat)
        file, _  = QFileDialog.getOpenFileName(self, "选择文件", "", "所有文件 (*)", options = options1)
        if file:
            print("File selected:", file)
            self.save_settings(dataline, file)
            self.display_lineEdit(linename, settings.value(dataline , QVariant("")))

    # 打开文件夹并选择文件夹
    def select_folder(self,dataline,linename):
        settings = QSettings(self.settings_file, QSettings.IniFormat)
        m = QFileDialog.getExistingDirectory(None,"选取文件夹","")  # 起始路径
        if m:
            self.save_settings(dataline, m)
            self.display_lineEdit(linename, settings.value(dataline , QVariant("")))

    # 获取textline改变后的数据
    def onTextChanged(self,menu):
        text = self.text_edit.toPlainText()
        self.save_settings(menu, text)

    # 保存按钮
    def SaveChange(self):
        ...
        
    # qlineEdit显示
    def display_lineEdit(self,line,display):
        return line.setText(display)
    
    # 从qline保存设置到配置文件中
    def save_settings(self,menu,data):
        #print(data)
        settings = QSettings(self.settings_file, QSettings.IniFormat)
        settings.setValue(menu, QVariant(data))

    # 从配置文件中加载设置
    def load_settings(self):
        settings = QSettings(self.settings_file, QSettings.IniFormat)

        self.lineEdit   .setText(settings.value("数据库地址"           , QVariant("")))
        self.lineEdit_2 .setText(settings.value("隐患整改通知书生成地址", QVariant("")))
        self.lineEdit_3 .setText(settings.value("隐患整改确认单生成地址", QVariant(""))) 
        self.lineEdit_4 .setText(settings.value("每月通报生成地址"      , QVariant(""))) 
        self.lineEdit_5 .setText(settings.value("检查情况统计表生成地址", QVariant("")))  
        self.lineEdit_6 .setText(settings.value("隐患总台账生成地址"    , QVariant("")))    
        self.lineEdit_cl .setText(settings.value("安全检查表生成地址"   , QVariant("")))    
        
        self.lineEdit_13.setText(settings.value("隐患整改通知书模板"    , QVariant("")))    
        self.lineEdit_14.setText(settings.value("隐患整改确认单模板"    , QVariant("")))    
        self.lineEdit_16.setText(settings.value("每月通报模板"          , QVariant("")))    
        self.lineEdit_clm.setText(settings.value("检查表模板"           , QVariant("")))    
        
        self.lineEdit_7 .setText(settings.value("检查类型下拉列表"     , QVariant("")))    
        self.lineEdit_8 .setText(settings.value("隐患类型下拉列表"     , QVariant("")))     
        self.lineEdit_9 .setText(settings.value("隐患级别下拉列表"     , QVariant("")))   
        self.lineEdit_10.setText(settings.value("被检查单位预置内容"   , QVariant("")))   
        self.lineEdit_11.setText(settings.value("检查人员预置内容"     , QVariant("")))    
        self.lineEdit_12.setText(settings.value("检查地点预置内容"     , QVariant("")))   
        self.text_edit  .setText(settings.value("快速剪切板预置内容"   , QVariant("")))   


# # #%%主程序入口
# if __name__ == '__main__':

#     app = QApplication([sys.argv])# ui主程序入口

#     window_yh = HiddenSetConfigWindow('settings.ini')     # 实例化QMainWindow
    
#     window_yh.show() 

#     sys.exit(app.exec())          # 循环中等待退出


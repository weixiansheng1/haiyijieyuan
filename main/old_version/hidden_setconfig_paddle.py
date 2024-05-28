# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:14:09 2024

@author: Microsoft
"""

# -*- coding: utf-8 -*-
import sys
import os          
from PyQt5.QtWidgets import QWidget, QPushButton,QLabel,QFormLayout,QLineEdit,QDialog
from PyQt5.QtCore    import Qt,QRect,QCoreApplication
from PyQt5.QtCore    import QSettings, QPoint, QSize, QVariant
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QLineEdit, QSpinBox, QWidget, QPushButton,QApplication

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
        
        self.settings_file = settings_file
        if not os.path.exists(self.settings_file):
            # 创建默认配置文件
            settings = QSettings(self.settings_file, QSettings.IniFormat)
            settings.setValue("text_box", "default text")
        
# =============================================================================
#         # 初始化配置数据库(txt)
# =============================================================================
        #self.file_path = file_path
        # with open(file_path,'r',encoding='utf-8') as f:
        #     #逐行读取文件内容
        #     lines = f.read()
        #     self.hidden_config = eval(lines)
        #     f.close()

        self.formLayoutWidget = QWidget(self)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")

        self.formLayout = QFormLayout(self)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setContentsMargins(10, 20, 20, 20)
        
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 460, 151, 23))
        self.pushButton.setText('新建今年数据库')

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('数据库地址') # 

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        # 隐患整改通知书生成地址
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u6574\u6539\u901a\u77e5\u4e66\u751f\u6210\u5730\u5740", None))# 隐患整改通知书生成地址

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)
        
        # 隐患整改确认单生成地址
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u6574\u6539\u786e\u8ba4\u5355\u751f\u6210\u5730\u5740", None))# 隐患整改确认单生成地址
        
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setText(self.hidden_config['隐患整改确认单生成地址'])
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)
        
        # 每月通报生成地址
        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6bcf\u6708\u901a\u62a5\u751f\u6210\u5730\u5740", None))# 每月通报生成地址

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setText(self.hidden_config['每月通报生成地址'])
        
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)
        
        # 检查情况统计表生成地址
        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u60c5\u51b5\u7edf\u8ba1\u8868\u751f\u6210\u5730\u5740", None))# 检查情况统计表生成地址

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setText(self.hidden_config['检查情况统计表生成地址'])

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_5)
        
        # 隐患总台账生成地址
        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u603b\u53f0\u8d26\u751f\u6210\u5730\u5740", None))# 隐患总台账生成地址
        
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_6 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setText(self.hidden_config['隐患总台账生成地址'])

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_6)
        
        # 隐患整改通知书模板
        self.label_13 = QLabel(self.formLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u6574\u6539\u901a\u77e5\u4e66\u6a21\u677f", None))
        
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_13 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setText(self.hidden_config['隐患整改通知书模板'])

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_13)

        # 隐患整改确认单模板
        self.label_14 = QLabel(self.formLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u6574\u6539\u786e\u8ba4\u5355\u6a21\u677f", None))
        
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_14 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setText(self.hidden_config['隐患整改确认单模板'])

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_14)
        
        # 每月通报模板
        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setText(QCoreApplication.translate("Form", u"\u6bcf\u6708\u901a\u62a5\u6a21\u677f", None))
        
        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_16 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setText(self.hidden_config['每月通报模板'])

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_16)



        # 保存
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(830, 460, 75, 23))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))# 保存
        
        self.formLayoutWidget_2 = QWidget(self)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 260, 1341, 171))
        
        
        
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_2.setContentsMargins(10, 20, 20, 20)
        
        # 检查类型下拉列表
        self.label_7 = QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u7c7b\u578b\u4e0b\u62c9\u5217\u8868", None))# 检查类型下拉列表
        
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_7 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setText(self.hidden_config['检查类型下拉列表'])

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_7)
        
        # 隐患类型下拉列表
        self.label_8 = QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u7c7b\u578b\u4e0b\u62c9\u5217\u8868", None))# 隐患类型下拉列表
        
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_8 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setText(self.hidden_config['隐患类型下拉列表'])

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_8)  
        
        # 隐患级别下拉列表
        self.label_9 = QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u9690\u60a3\u7ea7\u522b\u4e0b\u62c9\u5217\u8868", None))# 隐患级别下拉列表

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_9 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setText(self.hidden_config['隐患级别下拉列表'])

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_9)

        # 被检查单位预置内容
        self.label_10 = QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setText(QCoreApplication.translate("Form", u"\u88ab\u68c0\u67e5\u5355\u4f4d\u9884\u7f6e\u5185\u5bb9", None))# 被检查单位预置内容

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_10 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setText(self.hidden_config['被检查单位预置内容'])

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_10)

        # 检查人员预置内容
        self.label_11 = QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u4eba\u5458\u9884\u7f6e\u5185\u5bb9", None))# 检查人员预置内容

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_11 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setText(self.hidden_config['检查人员预置内容'])

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_11)

        # 检查地点预置内容
        self.label_12 = QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u5730\u70b9\u9884\u7f6e\u5185\u5bb9", None))# 检查地点预置内容
        
        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_12 = QLineEdit(self.formLayoutWidget_2) 
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setText(self.hidden_config['检查地点预置内容'])

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lineEdit_12)

        # 加载配置
        self.load_settings()

        #### 信号槽 ####
        # lineEdit
        self.lineEdit   .textChanged.connect(lambda data ,menu = '数据库地址':            self.ChangeClassDate(menu, data))
        self.lineEdit_2 .textChanged.connect(lambda data ,menu = '隐患整改通知书生成地址': self.ChangeClassDate(menu, data))
        self.lineEdit_3 .textChanged.connect(lambda data ,menu = '隐患整改确认单生成地址': self.ChangeClassDate(menu, data))
        self.lineEdit_4 .textChanged.connect(lambda data ,menu = '每月通报生成地址': self.ChangeClassDate(menu, data))
        self.lineEdit_5 .textChanged.connect(lambda data ,menu = '检查情况统计表生成地址': self.ChangeClassDate(menu, data))
        self.lineEdit_6 .textChanged.connect(lambda data ,menu = '隐患总台账生成地址': self.ChangeClassDate(menu, data))
        self.lineEdit_13.textChanged.connect(lambda data ,menu = '隐患整改通知书模板': self.ChangeClassDate(menu, data))
        self.lineEdit_14.textChanged.connect(lambda data ,menu = '隐患整改确认单模板': self.ChangeClassDate(menu, data))
        self.lineEdit_16.textChanged.connect(lambda data ,menu = '每月通报模板': self.ChangeClassDate(menu, data))
        self.lineEdit_7 .textChanged.connect(lambda data ,menu = '检查类型下拉列表': self.ChangeClassDate(menu, data))
        self.lineEdit_8 .textChanged.connect(lambda data ,menu = '隐患类型下拉列表': self.ChangeClassDate(menu, data))
        self.lineEdit_9 .textChanged.connect(lambda data ,menu = '隐患级别下拉列表': self.ChangeClassDate(menu, data))
        self.lineEdit_10.textChanged.connect(lambda data ,menu = '被检查单位预置内容': self.ChangeClassDate(menu, data))
        self.lineEdit_11.textChanged.connect(lambda data ,menu = '检查人员预置内容': self.ChangeClassDate(menu, data))
        self.lineEdit_12.textChanged.connect(lambda data ,menu = '检查地点预置内容': self.ChangeClassDate(menu, data))

        # ‘保存’
        self.pushButton_2.clicked.connect(self.SaveChangeTXT)
        


        # 加载设置
        self.load_settings()


    def ChangeClassDate(self, menu,data):
        self.hidden_config[menu] = data
# {'数据库地址': './洁源隐患数据库2024.db', '隐患整改通知书生成地址': '../main', '隐患整改确认单生成地址': '../main', '每月通报生成地址': '../main', '检查情况统计表生成地址': '../main', '隐患总台账生成地址': '../main', '隐患整改通知书模板': '../Template_resource/隐患台账类模板/海宜洁源公司安全检查整改通知书.docx', '隐患整改确认单模板': '../Template_resource/隐患台账类模板/洁源公司整改确认单.docx', '每月通报模板': '../Template_resource/隐患台账类模板/安全生产专项工作检查情况的通报.docx', '隐患类型下拉列表': '一般隐患（班组级）,一般隐患（厂级）,一般隐患（公司级）', '检查类型下拉列表': '自查,查收运,查行政与应急,海宜查,政府部门查,安保部查', '隐患级别下拉列表': '设备设施的不安全状态,电气安全隐患,管理缺失,火灾安全隐患,人员违反安全管理规定行为,应急管理隐患,车辆安全隐患,食品安全隐患,门岗管理隐患,环保隐患,危险化学品安全隐患,八大危险作业管理隐患', '被检查单位预置内容': '海宜洁源餐厨垃圾处置有限公司', '检查人员预置内容': '张健新、关智远、廖振威', '检查地点预置内容': '洁源公司餐厨项目现场', '快速剪切板预置内容': '珠海市海宜洁源餐厨垃圾处置有限公司\n河南艾尔旺新能源环境有限公司（设备厂家）\n广东建安昌盛控股集团有限公司（土建单位）\n杭州能源环境工程有限公司（设备厂家）\n维尔利环保科技集团股份有限公司（施工单位）\n深圳市沃尔奔达新能源股份有限公司（设备厂家）\n杭州楚环科技股份有限公司（设备厂家）\n珠海市城市开发监理有限公司（监理单位）\n上海市政工程设计研究总院（集团）有限公司（设计单位）\n珠海多特自动化工程有限公司（自控单位）\n有意餐饮管理公司（食堂承包单位）\n广东宏德科技物业有限公司（物业单位）\n'}

    def SaveChangeTXT(self):
        # 转换为字符串并手动添加大括号
        import json
        dictionary_str = '{' + json.dumps(self.hidden_config, ensure_ascii=False)[1:-1] + '}'

        # # 将字符串保存到txt文件
        # with open(self.file_path, 'w', encoding='utf-8') as file:
        #     file.write(dictionary_str)



    # 保存设置到配置文件中
    def save_settings(self):
        settings = QSettings(self.settings_file, QSettings.IniFormat)
        settings.setValue("数据库地址", QVariant(self.lineEdit.text()))
        settings.setValue("text_box2", "default text")


    # 从配置文件中加载设置
    def load_settings(self):
        settings = QSettings(self.settings_file, QSettings.IniFormat)

        text1 = settings.value("数据库地址", QVariant(""))
        self.lineEdit.setText(text1)
        text2 = settings.value("隐患整改通知书生成地址", QVariant(""))
        self.lineEdit_2.setText(text2)






# #%%主程序入口
if __name__ == '__main__':

    app = QApplication([sys.argv])# ui主程序入口
    settings_file ='settings.ini'
    window_yh = HiddenSetConfigWindow(settings_file)     # 实例化QMainWindow
    
    window_yh.show() 

    sys.exit(app.exec())          # 循环中等待退出


# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:56:25 2024

@author: Microsoft
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5 import QtCore 



class Window(QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.connect_db()

        self.sql_model = QSqlTableModel()           # 实例化一个QSqlTableModel对象，
                                       
        self.sql_model.setTable('hidden')      #调用setTable()方法设置数据表   #
        self.sql_model.setEditStrategy(QSqlTableModel.OnFieldChange)# 通过setEditStrategy()方法可以设置模型的编辑策略（即数据库是如何更新的）
        self.data_list = ['id' ,'检查时间',' 检查类型',' 隐患内容', '隐患图片', '隐患类型', '隐患级别', '被检查单位', '责任人及扣分', '责任管理人员及扣分',' 责任管理部门及扣分',' 隐患整改措施',' 隐患整改期限']

        for i in range(len(self.data_list)):
            self.sql_model.setHeaderData(i, QtCore.Qt.Horizontal,self.data_list[i])

        
        self.table_view = QTableView()
        self.table_view.setModel(self.sql_model)

        self.select_btn = QPushButton('select')
        self.insert_btn = QPushButton('insert')
        self.delete_btn = QPushButton('delete')
        self.select_btn.clicked.connect(self.select_data)
        self.insert_btn.clicked.connect(self.insert_data)
        self.delete_btn.clicked.connect(self.delete_data)
        
        btn_h_layout = QHBoxLayout()
        window_v_layout = QVBoxLayout()
        btn_h_layout.addWidget(self.select_btn)
        btn_h_layout.addWidget(self.insert_btn)
        btn_h_layout.addWidget(self.delete_btn)
        window_v_layout.addWidget(self.table_view)
        window_v_layout.addLayout(btn_h_layout)
        self.setLayout(window_v_layout)

    def connect_db(self):
        self.db.setDatabaseName('./洁源隐患数据库2024.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def closeEvent(self, event):
        self.db.close()
        event.accept()
    def select_data(self):                   
        self.sql_model.setFilter('score > 95') # setFilter()方法设置过滤器，传入的参数就是WHERE语句中的条件
        self.sql_model.select() #select()方法将表中的数据映射到模型中

    def insert_data(self):   #3 传入索引值来确定数据的插入位置，传入0表示在第一行插入。setData()方法可以用来插入或更新值，需要两个参数，第一个是QModelIndex对象，第二个是插入的数据。
        self.sql_model.insertRow(0)
        self.sql_model.setData(self.sql_model.index(0, 0), 3)
        self.sql_model.setData(self.sql_model.index(0, 1), '0101')
        self.sql_model.setData(self.sql_model.index(0, 2), 'Jack')
        self.sql_model.setData(self.sql_model.index(0, 3), 85)
        self.sql_model.submit() #提交更改

    def delete_data(self):   #4 在delete_data()函数中，我们只需要往removeRow()方法中传入索引值来删除相应行即可。
        self.sql_model.removeRow(0)
        self.sql_model.submit()
        


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
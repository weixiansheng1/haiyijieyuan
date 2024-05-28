
"""
数据库初始化

先在最下方取消掉#号，方可运行本函数模块
"""
import sqlite3

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImageReader, QPixmap
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice

from PyQt5.QtSql import QSqlQuery
from PyQt5.QtSql import *
from PyQt5 import QtCore


def set_database(base_name: str):
    
    db = QSqlDatabase.addDatabase('QSQLITE')
    #建立数据库
    db.setDatabaseName('{}'.format(base_name))
    
    if not db.open():
        error = db.lastError().text()
        QMessageBox.critical('数据库连接错误：', error)
        
    
    query =  QSqlQuery()      # 实例化QSqlTableModel对象
    
    query.exec_('''CREATE TABLE hidden (
                id INTEGER ,
               检查时间 TEXT,
               检查类型 TEXT,
               隐患内容 TEXT,
               隐患图片 BLOB,
               隐患类型 TEXT,
               隐患级别 TEXT,
               被检查单位 TEXT,
               责任人及扣分 TEXT,
               责任管理人员及扣分 TEXT,
               责任管理部门及扣分 TEXT,
               隐患整改措施 TEXT,
               隐患整改期限 TEXT
               )''' )

def read_data():    
    # 从数据库中查询数据并添加到模型中
    query =  QSqlQuery() 
    query.exec_("SELECT * FROM hidden")
    
        
def save_data_to_database(item):
    query = QSqlQuery()
    query.prepare(
        """
        INSERT OR REPLACE INTO hidden (id ,检查时间, 检查类型,隐患内容, 隐患图片,隐患类型, 隐患级别, 被检查单位, 责任人及扣分, 责任管理人员及扣分,责任管理部门及扣分, 隐患整改措施,隐患整改期限)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ? ,?)
        """
    )
    for i in range(len(item)):
        query.addBindValue(item[i])
    
# 将图片数据转换为字节流
def image_to_bytes(image_path):
    image = QImageReader(image_path).read()  # 从文件读取图片
    byte_array = QByteArray()
    buffer = QBuffer(byte_array)
    buffer.open(QIODevice.WriteOnly)
    image.save(buffer, "jpg")  # 这里假设存储为PNG格式，您可以根据需要调整
    image_data = bytes(byte_array.data())
    
    return  sqlite3.Binary(image_data)

image_path=" E:/海宜洁源安全共享文件/jieyuan_safety_application/main/d9c3.jpg"                                                                                                                                    
                
##%%通过QSqlDatabase建立sqlite数据库
database_path = './洁源隐患数据库2024.db'
set_database(database_path)

item = [1,"2024.2.29", "自查" ,  "丁琳琳开车违规使用手机", image_to_bytes(image_path), "人的不安全行为", "一般（班组级）", "洁源公司", "关智远-1",  "关智远-1",  "安环部-1", "罚站", "2024.2.29" ]

save_data_to_database(item)

read_data()
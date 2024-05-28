# -*- coding: utf-8 -*-
"""
先去set_datebase.py建立数据库
"""

import sqlite3

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImageReader, QPixmap
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice

from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery

# 连接到 洁源隐患数据库2024 数据库，如果不存在则会自动创建

conn = sqlite3.connect('洁源隐患数据库2024.db')

# 创建一个游标对象来执行 SQL 语句
cur = conn.cursor()

# 将数据存储到数据库
def save_data(idkey,
              check_time, 
              check_type, 
              hazard_content, 
              hazard_image, 
              hazard_type,
              hazard_class ,
              units_tobe_inspected, 
              responsible_person , 
              resposible_management_person, 
              resposible_management, 
              corrective_measure ,
              corrective_deadline):
    cur.execute("INSERT INTO hidden ( id ,检查时间, 检查类型, 隐患内容, 隐患图片, 隐患类型, 隐患级别, 被检查单位, 责任人及扣分, 责任管理人员及扣分, 责任管理部门及扣分, 隐患整改措施, 隐患整改期限) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ? ,?)", 
                (idkey,check_time, check_type, hazard_content, hazard_image, hazard_type, hazard_class ,units_tobe_inspected, responsible_person , resposible_management_person, resposible_management, corrective_measure ,corrective_deadline))
    conn.commit()

# 从洁源隐患数据库2024中读取数据
def read_data():    
    cur.execute("SELECT * FROM hidden")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        #print("隐患:", row[1])
        #print("内容:", row[2])


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
# 保存数据
save_data( 1,"2024.2.29", "自查" ,  "丁琳琳开车违规使用手机", image_to_bytes(image_path), "人的不安全行为", "一般（班组级）", "洁源公司", "关智远-1",  "关智远-1",  "安环部-1", "罚站", "2024.2.29" )



# 测试读取数据
read_data()

# 关闭游标和数据库连接
cur.close()
conn.close()




'''周一 完成图片数据存储'''

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImageReader, QPixmap
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice

# 连接到 SQLite 数据库，如果不存在则会自动创建
conn = sqlite3.connect('洁源隐患数据库2024.db')
cur = conn.cursor()

# 读取图片并存储到数据库
def save_image_to_database(image_path):
    image = QImageReader(image_path).read()  # 从文件读取图片
    image_data = image_to_bytes(image)  # 将图片转换为字节流
    cur.execute("INSERT INTO images (image) VALUES (?)", (sqlite3.Binary(image_data),))
    conn.commit()

# 将图片数据转换为字节流
def image_to_bytes(image):
    byte_array = QByteArray()
    buffer = QBuffer(byte_array)
    buffer.open(QIODevice.WriteOnly)
    image.save(buffer, "PNG")  # 这里假设存储为PNG格式，您可以根据需要调整
    return bytes(byte_array.data())

# 测试保存图片
#save_image_to_database('E:/海宜洁源安全共享文件/jieyuan_safety_application/main/d9c3.jpg')

#cur.execute("SELECT 隐患图片 FROM hidden")
#rows = cur.fetchall()
#for i in rows:
#    print(i)
# 关闭游标和数据库连接
#cur.close()
#conn.close()
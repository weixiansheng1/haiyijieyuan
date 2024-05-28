# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:00:34 2024

@author: Microsoft
"""

import sqlite3

# 连接到 SQLite 数据库，如果不存在则会自动创建
conn = sqlite3.connect('洁源隐患数据库2024.db')

cur = conn.cursor()         # 创建一个游标对象来执行 SQL 语句
def check_time(time):
    
    cur.execute("INSERT INTO users (检查时间) VALUES (?, ?)", ('{}'.format(time))) # 插入数据
    conn.commit()               # 提交事务

def check_type(type_):

    cur.execute("INSERT INTO users (检查类型) VALUES (?, ?)", ('{}'.format(type_))) # 插入数据
    conn.commit()               # 提交事务


# 从文件读取图片数据
def read_image(file_path):
    with open(file_path, 'rb') as f:
        image_data = f.read()
    return image_data

# 将图片数据存储到数据库
def save_image_to_database(image_id, image_data):
    cur.execute("INSERT INTO images (id, 隐患图片) VALUES (?, ?)", (image_id, sqlite3.Binary(image_data)))
    conn.commit()

# 从数据库中读取图片数据
def read_image_from_database(image_id):
    cur.execute("SELECT image FROM images WHERE id = ?", (image_id,))
    row = cur.fetchone()
    if row:
        image_data = row[0]
        return image_data
    else:
        return None


# 将图片数据存储到数据库
save_image_to_database(1, read_image('d9c3.jpg'))
print("Image saved to database.")

# 从数据库中读取图片数据
retrieved_image_data = read_image_from_database(1)

# 将图片数据写入文件（可选）
with open('retrieved_image.jpg', 'wb') as f:
    f.write(retrieved_image_data)
    print("Image retrieved from database and saved to file.")

# 关闭游标和数据库连接
cur.close()
conn.close()
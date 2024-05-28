
"""
先在最下方取消掉#号，方可运行本函数模块
"""


import sqlite3

def set_hidden_database(database: str):
    
    # 连接到 SQLite 数据库，如果不存在则会自动创建
    conn = sqlite3.connect(database)
    
    # 创建一个游标对象来执行 SQL 语句
    cur = conn.cursor()
    
    # 创建一个数据库
    cur.execute('''CREATE TABLE hidden (
                   id INTEGER ,
                   check_time TEXT,
                   check_type TEXT,
                   hidden_content TEXT,
                   hidden_image BLOB,
                   hidden_type TEXT,
                   hidden_level TEXT,
                   unit_to_be_inspected TEXT,
                   inspector TEXT,
                   check_the_location TEXT,
                   responsible_punish TEXT,
                   responsible_manager_punish TEXT,
                   responsible_department_punish TEXT,
                   corrective_measures TEXT,
                   corrective_deadline TEXT,
                   correactive_situastion TEXT,
                   retification_complete_time TEXT,
                   retification_number TEXT,
                   retification_confirmation_number TEXT,
                   )''')
    
    # 关闭游标和数据库连接
    cur.close()
    conn.close()
    
def set_number_database(database: str):
    
    # 连接到 SQLite 数据库，如果不存在则会自动创建
    conn = sqlite3.connect(database)
    
    # 创建一个游标对象来执行 SQL 语句
    cur = conn.cursor()
    
    # 创建一个数据库
    cur.execute('''CREATE TABLE number (
                   id_of_rectification INTEGER 
                   id_of_rectification INTEGER 
                   )''')
    
    # 关闭游标和数据库连接
    cur.close()
    conn.close()
    # # 隐患整改图片数据库
    # zg_conn = sqlite3.connect('隐患整改图片数据库2024.db')
    # curr = zg_conn.cursor()
    # curr.execute('''CREATE TABLE zgtp(
    #                 id INTEGER ,
    #                 隐患整改图片 BLOB
    #                 )''')
    # curr.close()
    # zg_conn.close()
    
    

#新建数据库 通过sqlite3创建
#set_hidden_database('洁源隐患数据库2024.db')
set_number_database('洁源隐患数据库2024.db')
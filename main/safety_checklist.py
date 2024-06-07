# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:28:40 2024

@author: Microsoft
"""

"""
# =============================================================================
#                      安全检查表
# =============================================================================
"""

import os
import time
from   docxtpl     import DocxTemplate               # pip install docxtpl
from   PyQt5.QtSql import QSqlQuery
from   dataclasses import dataclass

# 获取当前日期
now  = time.strftime("%Y-%m-%d"      ,time.localtime(time.time()))
now1 = time.strftime("%Y年 %m月 %d日",time.localtime(time.time()))
now2 = time.strftime("%Y0%m"         ,time.localtime(time.time()))
now3 = time.strftime("%Y年%m月份"    ,time.localtime(time.time()))
now4 = time.strftime("%Y年%m月"      ,time.localtime(time.time())).replace('年0','年')
now5 = time.strftime("%Y年%m月%d日"  ,time.localtime(time.time())).replace('年0','年').replace('月0','月')


@dataclass
class Write_safety_checklist:

    file_path  :str          # 模板地址
    output_dir :str          # 输出文件路径
    select_row :None

    # ======================================================================= #
    #                              功能                                    
    # ======================================================================= #

    # 删除列表中空字符
    def not_empty(self,s):
        return s and s.strip()
    # 连接数据库
    def connect_jieyuan_database(self):
                       #【       0            ,    1    ,    2          】
        select_column = 'unit_to_be_inspected,check_time,hidden_content' 
        # 读取word模板 TODO待写装饰器
        try:
            with open(self.file_path, 'r') :
                template_path = DocxTemplate(r"{}".format(self.file_path))    # 模板地址
        except FileNotFoundError:
            return("读取模板文件失败，请检查模板文件地址")

        # 读取数据
        if len(self.select_row) ==1:
            select_row_ = self.select_row[0]
            exec_ = "SELECT {} FROM hidden WHERE Id = {} ".format(select_column,select_row_) 
        elif len(self.select_row)>=1:
            select_row_ = tuple(self.select_row)
            exec_ = "SELECT {} FROM hidden WHERE Id IN {} ".format(select_column,select_row_) 


        #print(exec_) 
        query = QSqlQuery(exec_)

        # 初始输入数据字符串
        str_unit_to_be_inspected = []    # 被检查单位 TODO.冗余，备用
        str_check_time           = []    # 检查时间   TODO.冗余，备用
        str_hidden_content       = []    # 隐患内容

        cache = [str_unit_to_be_inspected,str_check_time,str_hidden_content]

        # 跟据query获取数据库的数据，并生成字符串
        while query.next():
            [cache[x].append(query.value(x)) for x in range(len(cache))]


        # 检查时间格式转换
        transf_check_time = [ (i.replace('-', '年', 1).replace('-', '月')+'日').replace('年0','年').replace('月0','月')  for i in str_check_time]

        # 其他
        self.unit_to_be_inspected = str_unit_to_be_inspected         # 被检查单位 TODO.冗余，备用
        self.check_time           = transf_check_time                # 检查时间   TODO.冗余，备用
        self.problem              = str_hidden_content               # 存在问题

        self.checklist = [{'序号': '\a%s.'%x,'存在问题': y }for x,y in enumerate(self.problem,start=1)]
        # print(self.check_time)
        # print(self.retification_requirements)
        
        
        
    # 跟据query数据写入docx      # 替换参数 
        context = { '安全检查'      :self.checklist

                    }
        template_path.render(context) # 渲染


        # 保存生成内容
        try: 
            output_dir = r"{}".format(self.output_dir)
            self.output = os.path.join(output_dir, "海宜洁源公司日常检查表安全检查{}.docx ".format(self.check_time[0]))
            template_path.save(self.output)
            self.output.join('安全检查表生成完毕:')
        except:
            self.output = '保存文件失败，请检查生成地址'
        
        return self.output




#%% 返回生成文件地址
    def output_file_path(self):
        return self.output


# =============================================================================
#           测试
# =============================================================================

# select_data = [0,1,2]


# taxt = Write_safety_checklist("../Template_resource/隐患台账类模板/日常检查表.docx","../main",select_data)
# taxt.connect_jieyuan_database()
# print(taxt)
# #tongji_d_h(zhenggai, '整改通知书')










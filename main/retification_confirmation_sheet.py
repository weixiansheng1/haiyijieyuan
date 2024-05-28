# -*- coding: utf-8 -*-
"""
# =============================================================================
#                      整改确认单
# =============================================================================
"""
import os
import time,datetime
from   docxtpl       import DocxTemplate               # pip install docxtpl
from   PyQt5.QtSql   import QSqlQuery
from   dataclasses   import dataclass


# 获取当前日期
now  = time.strftime("%Y-%m-%d"      ,time.localtime(time.time()))
now1 = time.strftime("%Y年 %m月 %d日",time.localtime(time.time()))
now2 = time.strftime("%Y0%m"         ,time.localtime(time.time()))
now3 = time.strftime("%Y年%m月份"    ,time.localtime(time.time()))
now4 = time.strftime("%Y年%m月"      ,time.localtime(time.time())).replace('年0','年')
now5 = time.strftime("%Y年%m月%d日"  ,time.localtime(time.time())).replace('年0','年').replace('月0','月')

@dataclass
class write_retification_confirmation():
    file_path    :str          # 模板地址
    output_dir   :str          # 输出文件路径
    select_row   :None
    ############## 数据处理 ##############
    
    # 删除列表中空字符
    def not_empty(self,s):
        return s and s.strip()
    # 连接数据库
    def connect_jieyuan_database(self):
                     #【       0   ,      1       ,    2              ，          3              ,                 4              】
        select_column = 'check_time,hidden_content,corrective_measures,retification_complete_time,check_type' 
        # 读取word模板
        template_path               = DocxTemplate(r"{}".format(self.file_path))    # 模板地址
        if len(self.select_row) ==1:
            select_row_ = self.select_row[0]
            exec_ = "SELECT {} FROM hidden WHERE Id = {} ".format(select_column,select_row_) 
        elif len(self.select_row)>=1:
            select_row_ = tuple(self.select_row)
            exec_ = "SELECT {} FROM hidden WHERE Id IN {} ".format(select_column,select_row_) 


        #print(exec_) 
        query = QSqlQuery(exec_)

        # 初始输入数据字符串
        str_check_time           = []    # 检查时间
        str_hidden_content       = []    # 隐患内容
        str_corrective_measures  = []    # 隐患整改措施
        complete_time            = []    # 整改完成时间
        check_type               = []    # 检查类型 ：海宜查、自查
        
        cache = [str_check_time,str_hidden_content,str_corrective_measures,complete_time,check_type]
        
        # 跟据query获取数据库的数据，并生成字符串
        while query.next():
            [cache[x].append(query.value(x)) for x in range(len(cache))]
            pass

        # 检查时间格式转换
        to_time          = [str_check_time[i].replace('-', '年', 1).replace('-', '月').replace('年0','年').replace('月0','月')+'日' for i in range(len(str_check_time)) ]
        to_complete_time = [complete_time [i].replace('-', '年', 1).replace('-', '月')+'日'  if complete_time[i] else ''  for i in range(len(complete_time)) ]

        # 最终数据
        self.complete_number = str(now2)                         # 整改确认单编号
        self.check_time      = to_time                           # 检查时间
        self.problem         = str_hidden_content                # 存在问题
        self.retification_requirements =  str_corrective_measures# 整改措施
        self.complete_time   = to_complete_time

        # # 整改通知书附件内容
        # # 参考文章https://zhuanlan.zhihu.com/p/366902690
        
        querendan_sc = [{'问题描述': self.problem[i],'序号': str(i+1),'图片':'' ,'整改措施':self.retification_requirements[i],'检查时间':self.check_time[i] ,'完成时间':self.complete_time[i] } for i in range(len(self.problem))]#ki:键  a ：值

        # 跟据query数据写入docx        # 替换参数 
        context = {'确认单编号':self.complete_number,
                   '确认单'    : querendan_sc,
                    }

        template_path.render(context) # 渲染


        # 保存生成内容
        output_dir = r"{}".format(self.output_dir)
        print(check_type)
        if check_type[0] =='自查':
            output_name = "海宜洁源公司整改确认单{}-自查.docx ".format(now4)
        elif check_type[0] == '海宜查':
            output_name = "海宜洁源公司整改确认单{}-海宜查.docx ".format(now4)
        self.output = os.path.join(output_dir,output_name )
        template_path.save(self.output)
        print('生成隐患整改确认单完毕')

        return self.complete_number
    
    def output_file_path(self):
        return self.output

        #查看某文件夹下是否存在按月份生成的文件夹，如果没有则生成
    def wenjianjia(self,wenjianjia_path):
        nowmonth = datetime.datetime.now()
        current_month = nowmonth.strftime("%Y年-%m月")
        folder_path = os.path.join(wenjianjia_path, current_month) # 构建文件夹路径
        if not os.path.exists(folder_path):                        # 判断文件夹是否存在，如果不存在则创建它
            os.makedirs(folder_path)
        return folder_path





# =============================================================================
#           测试函数
# =============================================================================

'''
        字体大小对应pt
        初号44pt
        小初36pt
        号26pt
        小一24pt
        二号22pt
        小二18pt
        三号16pt
        小三15pt
        四号14pt
        小四12pt
        五号10.5pt
        八号5
        七号5.5
        字号‘小六’对应磅值6.5
        字号‘六号’对应磅值7.5
        字号‘小五’对应磅值9
        '''
    # 统计段落数和行数
def tongji_d_h(file,name):
    num_paragraphs = len(file.paragraphs)
    num_lines = 0
    for paragraph in file.paragraphs:
        num_lines += len(paragraph.text.split('\n'))
        # 统计表格数
    num_tables = len(file.tables)
    for table in file.tables:    
        row_count = len(table.rows)
        column_count = len(table.columns)
        print(f'{name}模板的第{table}个表格中有{row_count}行，{column_count}列')
    print(f"{name}模板中有 {num_paragraphs} 个段落和 {num_lines} 行文本, {num_tables} 个表格。")



# =============================================================================
#           测试
# =============================================================================

# select_data = [0,1,3]


# taxt = write_retification_confirmation("../Template_resource/隐患台账类模板/洁源公司整改确认单.docx","../main",select_data)
# taxt.connect_jieyuan_database()
# #tongji_d_h(zhenggai, '整改通知书')
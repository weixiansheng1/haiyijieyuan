# -*- coding: utf-8 -*-
"""
# =============================================================================
#                      整改通知书
# =============================================================================
"""

import os
import time,datetime
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
class Write_notice_of_retification:

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
                     #【       0            ,      1   ,    2    ，          3       ，      4     ,           5       】
        select_column = 'unit_to_be_inspected,check_time,inspector,check_the_location,hidden_content,corrective_measures,responsible_punish,corrective_deadline' 
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
        str_unit_to_be_inspected = []    # 被检查单位 
        str_check_time           = []    # 检查时间
        str_inspector            = []    # 检查人员
        str_check_the_location   = []    # 检查地点
        str_hidden_content       = []    # 隐患内容
        str_corrective_measures  = []    # 隐患整改措施
        chache_data              = []    # 缓存
        responsible_person       = []    # 责任人员
        retification_deadline    = []    # 整改期限
        
        cache = [str_unit_to_be_inspected,str_check_time,str_inspector,str_check_the_location,str_hidden_content,str_corrective_measures,responsible_person,retification_deadline]
        
        # 跟据query获取数据库的数据，并生成字符串
        while query.next():
            [cache[x].append(query.value(x)) for x in range(len(cache))]
            pass


        # 检查时间格式转换
        to_time  = str_check_time[0].replace('-', '年', 1).replace('-', '月')+'日' 
        to_time  = to_time.replace('年0','年').replace('月0','月')
        
        # 获取确认单编号
        confirm_muber = QSqlQuery("SELECT retification_number FROM hidden")
        
        while confirm_muber.next():
            ccache  = confirm_muber.value(0)[8:]
            chache_data.append(ccache)

        # 整改通知书编号拆分
        c          = list(filter(self.not_empty,chache_data))                            # 调用迭代器并转为list
        to_int     = [int(c[x]) for x in range(len(c))]                                  # 转换为为整型
        now_number = max(to_int) + 1                                                     # 选取最大编号，+1后获得本次编号
        
        last_year_month           = str_check_time[0][:7]
        self.complete_number = str(last_year_month + '-'+ "{:0>3d}".format(now_number))  # 得到完整的编号


        # 其他
        self.check_time           = to_time                                              # 检查时间 
        self.unit_to_be_inspected = str_unit_to_be_inspected[0]                          # 被检查单位
        self.check_the_location   = str_check_the_location  [0]                          # 检查地点
        self.inspectors           = str_inspector           [0]                          # 检查人员

        self.problem,self.retification_requirements =  self.merge_str(str_hidden_content,str_corrective_measures,responsible_person,retification_deadline)       # 存在问题  # 整改要求

        # print(self.problem)
        # print(self.retification_requirements)
        
        # # 整改通知书附件内容
        # # 参考文章https://zhuanlan.zhihu.com/p/366902690
        attachments = [{'问题描述': str_hidden_content[i],'序号': str(i+1),'图片':'' } for i in range(len(str_hidden_content))]#ki:键  a ：值


    # 跟据query数据写入docx      # 替换参数 
        context = { '编号'      :'{}'.format(self.complete_number) ,
                    '检查时间'  :'{}'.format(self.check_time), 
                    '被检查单位':'{}'.format(self.unit_to_be_inspected),      # 需要使用format才能跟随文档格式！！！
                    '检查人员'  :'{}'.format(self.inspectors),
                    '检查地点'  :'{}'.format(self.check_the_location) ,
                    '其他要求'  :'{}'.format(''),
                    '存在问题'  :'{}'.format(self.problem)        ,
                    '整改要求'  :'{}'.format(self.retification_requirements),
                    '附件'      : attachments     ,               # 整改通知书附件,
                    }
        template_path.render(context) # 渲染


        # 保存生成内容
        output_dir = r"{}".format(self.output_dir)
        self.output = os.path.join(output_dir, "海宜洁源公司安全检查整改通知书（餐厨垃圾处理一期项目）{}.docx ".format(to_time))
        template_path.save(self.output)
        print('生成隐患整改通知书完毕')
        
        return self.complete_number


        # merge hidden and rectification strings 合并字符串
    def merge_str(self,list_for_merge,str_corrective_measures,responsible_person,retification_deadline):
        re,data = '',''
        re_person = ''
        for i in range(len(list_for_merge)):
            if '-' in responsible_person[i]:
                str_front = '（责任人员：'
                re_person = responsible_person[i].translate(str.maketrans('-', ' ','0123456789'))  # translate(str.maketrans: 第一个和第二个参数的长度必须匹配。在两个参数的情况下，会将第一个参数的字符，依次的映射成第二个参数的字符（o-> X，w-> Y）。第三个参数表示在映射完的结果之后，需要移除的字符。
            else:
                str_front = '（责任单位：'
            str_right_deadlint = ''
            if '即时整改' in retification_deadline[i] :
                ...

            elif retification_deadline[i] == '':
                retification_deadline[i] = '' 
            else:
                str_right_deadlint = '前整改完成'
                retification_deadline[i] = retification_deadline[i].replace('-', '年', 1).replace('-', '月')+'日' # str.replace(old, new[, max])
                
            data =  data + str(i+1) + '. ' + list_for_merge[i] + str_front + re_person    +')\n'
            re   =  re   + str(i+1) + '. ' + str_corrective_measures[i] + '（整改期限：' + retification_deadline[i] + str_right_deadlint +'）\n'
        return data , re


        #查看某文件夹下是否存在按月份生成的文件夹，如果没有则生成
    def wenjianjia(self,wenjianjia_path):
        nowmonth = datetime.datetime.now()
        current_month = nowmonth.strftime("%Y年-%m月")
        folder_path = os.path.join(wenjianjia_path, current_month) # 构建文件夹路径
        if not os.path.exists(folder_path):                        # 判断文件夹是否存在，如果不存在则创建它
            os.makedirs(folder_path)
        return folder_path

#%% 返回生成文件地址
    def output_file_path(self):
        return self.output

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

# select_data = [0,1,2]


# taxt = Write_notice_of_retification("../Template_resource/隐患台账类模板/海宜洁源公司安全检查整改通知书（餐厨垃圾处理一期项目）.docx","../main",select_data)
# taxt.connect_jieyuan_database()
# #tongji_d_h(zhenggai, '整改通知书')










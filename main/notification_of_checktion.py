# -*- coding: utf-8 -*-
"""
# =============================================================================
#                      检查通报
# =============================================================================
"""
import os
import time,datetime
import re
from   docxtpl         import DocxTemplate,RichText         # pip install docxtpl
from   PyQt5.QtSql     import QSqlQuery
from   PyQt5.QtWidgets import QMessageBox
from   dataclasses     import dataclass
from   collections     import defaultdict


# 获取当前日期
now  = time.strftime("%Y-%m-%d"      ,time.localtime(time.time()))
now1 = time.strftime("%Y年 %m月 %d日",time.localtime(time.time()))
now2 = time.strftime("%Y0%m"         ,time.localtime(time.time()))
now3 = time.strftime("%Y年%m月份"    ,time.localtime(time.time()))
now4 = time.strftime("%Y年%m月"      ,time.localtime(time.time())).replace('年0','年')
now5 = time.strftime("%Y年%m月%d日"  ,time.localtime(time.time())).replace('年0','年').replace('月0','月')

@dataclass
class Write_inspect_the_situation:
    file_path       :str          # 模板地址
    output_dir      :str          # 输出文件路径
    select_row      :None
    chinese_num = ['','一','二','三','四','五','六','七','八','九','十','百','零']
    # ======================================================================= #
    #                              功能                                    
    # ======================================================================= #

    # 连接数据库
    def connect_jieyuan_database(self):
                     #【       被检查单位     ,  检查类型, 检查时间 ,    检查地点      ，   隐患内容   ,     隐患整改措施   ,     责任人员      ,    责任管理人员           ，     责任部门               ，  整改期限        ,   隐患类型   ， 整改情况           】
        select_column = 'unit_to_be_inspected,check_type,check_time,check_the_location,hidden_content,corrective_measures,responsible_punish,responsible_manager_punish,responsible_department_punish,corrective_deadline,hidden_type,correactive_situastion'

        # 读取word模板
        template_path               = DocxTemplate(r"{}".format(self.file_path))    # 模板地址
        if len(self.select_row) ==1:
            select_row_ = self.select_row[0]
            exec_ = "SELECT {} FROM hidden WHERE Id = {} ".format(select_column,select_row_) 
        elif len(self.select_row)>=1:
            select_row_ = tuple(self.select_row)
            exec_ = "SELECT {} FROM hidden WHERE Id IN {} ".format(select_column,select_row_) 
        else:
            self.show_warning_message('请勾选内容')

        #print(exec_) 
        query = QSqlQuery(exec_)

        # 初始输入数据字符串
        str_unit_to_be_inspected   = []    # 被检查单位 
        str_check_type             = []    # 检查类型
        str_check_time             = []    # 检查时间
        str_check_the_location     = []    # 检查地点
        str_hidden_content         = []    # 隐患内容
        str_corrective_measures    = []    # 隐患整改措施
        responsible_person         = []    # 责任人员
        responsible_manager_punish = []    # 责任管理人员
        responsible_department_punish = [] # 责任部门
        retification_deadline      = []    # 整改期限
        hidden_type                = []    # 隐患类型
        str_correactive_situastion = []    # 整改情况

        cache = [str_unit_to_be_inspected,str_check_type,str_check_time,str_check_the_location,str_hidden_content,str_corrective_measures,responsible_person,responsible_manager_punish,responsible_department_punish,retification_deadline,hidden_type,str_correactive_situastion]

        # 跟据query获取数据库的数据，并生成字符串
        while query.next():
            [cache[x].append(query.value(x)) for x in range(len(cache))]
            pass

        # 检查时间格式转换
        to_time  = [str_check_time[i].replace('-', '年', 1).replace('-', '月').replace('年0','年').replace('月0','月')+'日' for i in range(len(str_check_time))]


        self.check_time           = to_time                                           # 检查时间 
        self.str_check_type       = str_check_type                                    # 检查类型
        self.unit_to_be_inspected = str_unit_to_be_inspected                          # 被检查单位
        self.check_the_location   = str_check_the_location                            # 检查地点
        self.problem              = str_hidden_content                                # 存在问题
        self.retification_requirements =  str_corrective_measures                     # 整改要求
        self.responsible_person   = responsible_person                                # 责任人员
        self.responsible_person_g = responsible_manager_punish                        # 责任管理人员
        self.responsible_person_m = responsible_department_punish                     # 责任部门
        self.retification_deadline= retification_deadline                             # 整改期限
        self.hidden_type          = hidden_type                                       # 隐患类型
        self.correactive_situastion = str_correactive_situastion                      # 整改情况

        # 数据拼接及整理
        self.uncorrected_problem  = self.uncorrected_problem()                        # 未完成整改的隐患
        self.check_haiyi_dict     = self.merge_check_str('海宜查',self.str_check_type,self.check_time)  # 检查类型:海宜查
        self.check_jieyuan_dickt  = self.merge_check_str('自查'  ,self.str_check_type,self.check_time)  # 检查类型:自查
        self.check_shouyun_dickt  = self.merge_check_str('查收运',self.str_check_type,self.check_time)  # 检查类型:查收运
        self.check_xingzheng_dickt  = self.merge_check_str('查行政与应急',self.str_check_type,self.check_time)  # 检查类型:查行政与应急


        
    # 跟据query数据写入docx      # 替换参数 
    # # 参考文章https://zhuanlan.zhihu.com/p/366902690
        context = { '年月'        : now4,
                    '未整改问题'  :'{}'.format(self.uncorrected_problem), 
                    '自查'        : self.check_jieyuan_dickt, 
                    '查收运'      : self.check_shouyun_dickt,
                    '查行政与应急':self.check_xingzheng_dickt,
                    '海宜查'     : self.check_haiyi_dict, 
                    '生成日期'   : now5
                    }
        template_path.render(context) # 渲染


        # 保存生成内容
        output_dir = r"{}".format(self.output_dir)
        self.output = os.path.join(output_dir, "关于珠海市海宜洁源餐厨垃圾处置有限公司{}安全生产专项工作检查情况的通报.docx ".format(now4))
        template_path.save(self.output)
        return now4 

    def output_file_path(self):
        return self.output

    # 跟据数字匹配中文数字
    def chinese_number(self, int_:int): # 
        '''
        用于输入数字进行匹配中文数字，输入数字必须大于零
        int_ : 输入整型
        '''
        tenss  = 0                      # 控制'十'
        contro = 0                      # 控制'百'
        zero   = 0                      # 控制'零'

        tens   = 0                      # 十位
        hundreds = 0                    # 百位
        units  = int_ % 10              # 个位
        if 10<=int_<=19:
            tenss = 10
        elif 20<= int_ <=99:
            tenss = 10
            tens   = (int_ // 10) % 10  # 十位
        if 100<=int_:
            if  (int_ // 10) % 10 ==0 and int_ % 10 != 0:  # 十位
                zero   = 12
            elif 1 <= (int_ // 10) % 10 :
                tenss = 10
            tens   = (int_ // 10) % 10  # 十位
            hundreds = (int_ // 100) % 10  # 百位
            contro = 11
        result_num =  self.chinese_num[hundreds]+ self.chinese_num[contro]+self.chinese_num[zero]+self.chinese_num[tens] +  self.chinese_num[tenss]+self.chinese_num[units]
        return  result_num


    # 未完成整改的隐患
    def uncorrected_problem(self):
        query = QSqlQuery('SELECT hidden_content, responsible_punish FROM hidden WHERE correactive_situastion IS NOT "已完成整改"  ') #  
        not_null = ''
        responsible_person =''
        i    = 1
        rt = RichText()

        while query.next():  
            if query.value(1):

                if '公司' in query.value(1):
                    str_front = '（责任单位：'
                    responsible_person = query.value(1)

                elif '部' in query.value(1):
                    str_front = '（责任部门：'
                    responsible_person = query.value(1)
                else:
                    str_front = '（责任人员：'
                    responsible_person = query.value(1).translate(str.maketrans('-', ' ','0123456789'))  # translate(str.maketrans: 第一个和第二个参数的长度必须匹配。在两个参数的情况下，会将第一个参数的字符，依次的映射成第二个参数的字符（o-> X，w-> Y）。第三个参数表示在映射完的结果之后，需要移除的字符。
                not_null = '（{}）'.format(self.chinese_number(i)) + query.value(0) + str_front  + responsible_person + ')\a'
                rt.add(not_null, size = 32, font = 'eastAsia:仿宋')  

            else:
                null = '（{}）'.format(self.chinese_number(i)) + query.value(0) 
                null1= str_front   + ')\a'
                rt.add(null , size  = 32  , font = 'eastAsia:仿宋')  
                rt.add(null1, color ='red', size = 32,font = 'eastAsia:仿宋')  # 红色，24号字体大小

            #\n, \a, \t and \f will be translated respectively into newlines, new paragraphs, tabs and page breaks
            i += 1
        return rt


    # 预分类器：用于分类输入数据 返回分类好的字典
    def Pre_sorted(self,pre):
        classified_dates_dict  = defaultdict(list)     # 创建一个默认字典来存储日期分类及对应的序号列表
        for index, data in enumerate(pre):             # 遍历日期列表，将日期及其对应的序号存入字典中
            classified_dates_dict[data].append(index)
        return classified_dates_dict
    
    # 二次分类器：输入要的类型，返回该类型所对应的日期的分类字典，字典里包含有分类好的列表
    def classify_hz(self,object_to_c:str,object_list,Sec_class_ob): # 待分类对象（str），对象的列表,二次分类对象
        cache = []
        object_newdict = {}
        sec_newdict    = {}
        date = self.Pre_sorted(object_list)
        #print(date)
        for data, index_list in date.items():
            # print(data, ":", index_list)
            if object_to_c in  data:                     # 选出对象列表
                object_newdict[object_to_c] = index_list # 字典
                
        #print('第一次分类情况：',object_newdict)
        if object_to_c in object_newdict.keys():
            # 二次分类
            data = [cache.append(Sec_class_ob[i]) for i in object_newdict[object_to_c]]
            #print('第二次预分类:',cache)
            Sec_date = self.Pre_sorted(cache)
            #print('第二次分类情况：',Sec_date )
            for data, index_list in Sec_date.items():
                sec_newdict[data] = [object_newdict[object_to_c][i]  for i in index_list ] # 将列表对应回去
                
            #print('最终分类：',sec_newdict)
            
            return sec_newdict
        else:
            return None

    # 内容合并器：将二次分类器分类好的字典映射内容
    def merge_check_str(self,object_to_c:str,object_list,Sec_class_ob):

        data = self.classify_hz(object_to_c,object_list,Sec_class_ob)
        if data:
           # print('data:',data)
            a = 1
            first_line = []
            two_line   = []
            for date, index_list in data.items():

                #print(date, ":", index_list)
                problem_in                   = [] # 隐患
                retification_requirements_in = [] # 整改要求
                responsible_person_in        = [] # 责任人员
                responsible_person_g_in      = [] # 责任管理人员
                responsible_person_m_in      = [] # 责任部门
                retification_deadline_in     = [] # 整改期限
                correactive_situastion_in    = [] # 整改情况

                for i in index_list:
                    problem_in.append(self.problem[i])
                    retification_requirements_in.append(self.retification_requirements[i])
                    responsible_person_in       .append(self.responsible_person       [i])
                    responsible_person_g_in     .append(self.responsible_person_g     [i])
                    responsible_person_m_in     .append(self.responsible_person_m     [i])
                    retification_deadline_in    .append(self.retification_deadline    [i])
                    correactive_situastion_in   .append(self.correactive_situastion   [i])

                play_checktime_problem = '%s.检查时间：%s\a存在问题：\a' %(a,date)
                problem_checktime = self.merge_str(problem_in,retification_requirements_in,responsible_person_in, responsible_person_g_in,responsible_person_m_in,retification_deadline_in,correactive_situastion_in )                                  # 检查地点的检查问题

                first_line.append(play_checktime_problem)
                two_line  .append(problem_checktime     )
                
                a+=1

            tree =[ {"检查时间":first_line[i] , "存在问题":two_line[i]} for i in range(len(first_line))]
        else:
            tree = [{"检查时间":RichText('请删除本行',color = 'red',size = 32,font = 'eastAsia:仿宋'), "存在问题":RichText('请删除本行',size = 32,color = 'red',font = 'eastAsia:仿宋')}]

        return tree

    # 合并当前检查日期字符串
    def merge_str(self,problem_for_merge,str_corrective_measures,responsible_person,responsible_manager_punish,responsible_department_punish,retification_deadline,correactive_situastion):
        merge_check = RichText()
        for i in range(len(problem_for_merge)):
            str_right_deadlint  =  ''
            finished_correction = ''
            full_stop_a = ''
            full_stop_b = ''
            full_stop_c = ''
            manager_    = ''
            department_ = ''
            person_score =''
            # 判断责任管理人员扣分
            if responsible_manager_punish[i]:
                manager_    =  re.sub(r'([\u4e00-\u9fa5]+(?:\（[^\）]+\）)?)-(\d+(?:\.\d+)?)', r'\1扣\2分', responsible_manager_punish[i])
                full_stop_a = '；'
                full_stop_b = '。'
            else:
                full_stop_a = '。'
                
            # 判断责任部门扣分
            if responsible_department_punish[i]:
                department_ =  re.sub(r'([\u4e00-\u9fa5]+(?:\（[^\）]+\）)?)-(\d+(?:\.\d+)?)', r'\1扣\2分', responsible_department_punish[i])
                full_stop_b = '；'
                full_stop_c = '。'
                
            # 判断责任人员
            if re.search(r'[\u4e00-\u9fff]', responsible_person[i]) :
                if '公司' in  responsible_person[i]:
                    str_front = '（责任单位：'
                    person    =  responsible_person[i]
                elif '部' in  responsible_person[i]:
                    str_front = '（责任部门：'
                    person    = responsible_person[i]
    
                else:
                    str_front = '（责任人员：'
                    if '-' in responsible_person[i]:
                        person_score = re.sub(r'([\u4e00-\u9fa5]+(?:\（[^\）]+\）)?)-(\d+(?:\.\d+)?)', r'\1扣\2分', responsible_person[i])+ full_stop_a + manager_ + full_stop_b + department_+full_stop_c
                    else:
                        person_score = ''
                    person = responsible_person[i].translate(str.maketrans('-', ' ','0123456789'))  # translate(str.maketrans: 第一个和第二个参数的长度必须匹配。在两个参数的情况下，会将第一个参数的字符，依次的映射成第二个参数的字符（o-> X，w-> Y）。第三个参数表示在映射完的结果之后，需要移除的字符。
                merge_1= f'''\a（{i+1}）{problem_for_merge[i]}{str_front}{person})\a整改意见：{str_corrective_measures[i]}{person_score}''' 
                merge_check.add(merge_1, size = 32, font = 'eastAsia:仿宋')  

            else:
                str_front = '（责任人员：'
                person    = '请填写责任人员'
                merge_a   = f'''\a（{i+1}）{problem_for_merge[i]}'''
                merge_check.add(merge_a, size = 32, font = 'eastAsia:仿宋')
                merge_b   = f'''{str_front}{person})'''
                merge_check.add(merge_b, size = 32, font = 'eastAsia:仿宋',color = 'red')
                merge_c   = f'''\a整改意见：{str_corrective_measures[i]}{person_score}''' 
                merge_check.add(merge_c, size = 32, font = 'eastAsia:仿宋')
                
            # 判断及时整改
            if re.search(r'[\u4e00-\u9fff\d]', retification_deadline[i]) : # 如果匹配到中文或者数字
                if '即时整改' not in retification_deadline[i] :
                    str_right_deadlint = '前整改完成'
                    retification_deadline[i] = retification_deadline[i].replace('-', '年', 1).replace('-', '月')+'日' # str.replace(old, new[, max])
                
                if '已完成' in correactive_situastion[i]:
                    finished_correction = '\a整改情况：已完成整改。'
                merge_3 = f'''（整改期限：{retification_deadline[i]}{str_right_deadlint}）{finished_correction}'''
                merge_check.add(merge_3, size = 32, font = 'eastAsia:仿宋')
                    
            else:
    
                merge_3 = f'''（整改期限：{retification_deadline[i]}{str_right_deadlint}）{finished_correction}'''
                merge_check.add(merge_3, size = 32, font = 'eastAsia:仿宋',color = 'red')

        return merge_check


    #查看某文件夹下是否存在按月份生成的文件夹，如果没有则生成
    def wenjianjia(self,wenjianjia_path):
        nowmonth = datetime.datetime.now()
        current_month = nowmonth.strftime("%Y年-%m月")
        folder_path = os.path.join(wenjianjia_path, current_month) # 构建文件夹路径
        if not os.path.exists(folder_path):                        # 判断文件夹是否存在，如果不存在则创建它
            os.makedirs(folder_path)
        return folder_path
    
    #%%    显示错误提示信息
    def show_warning_message(self,show_error_str):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("{}".format(show_error_str))
        message_box.setWindowTitle("警告")
        message_box.exec_()


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
# select_data = [0,1,2,3,4,5,6]

# taxt = Write_inspect_the_situation("../Template_resource/隐患台账类模板/安全生产专项工作检查情况的通报.docx","../main",select_data)
# taxt.connect_jieyuan_database()
# #tongji_d_h(zhenggai, '整改通知书')

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:37:49 2024

@author: Microsoft
"""


import os
import time
import pandas  as pd
import win32com.client
from   docxtpl import DocxTemplate #pip install docxtpl


#全局控制变量
year = 2024    #年
date_of_write = "2024年1月1日"    #签订时间
zerenshu_run = 'yes' #是否生成责任书'yes' 'no'
print_word = 'yes'   #是否打印'yes' 'no'
print_time_a = 5 #文件夹打印间隔时间  50
print_time_b = 3 #文件间打印间隔时间  30
sleep        = 1 #打印第二份文件间隔时间

"""
# =============================================================================
# 原始人员名单数据清洗
# =============================================================================
"""


# =============================================================================
# 模板位置
# =============================================================================
#责任书模板位置
zjlyfzjl = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource\责任书模板\2024\1-总经理与副总经理"
fzjlybm  = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource\责任书模板\2024\2-副总经理与部门"
ahb      = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource\责任书模板\2024\3-部门与员工\1-安环部"
scb      = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource\责任书模板\2024\3-部门与员工\2-生产部"
ddzx     = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource\责任书模板\2024\3-部门与员工\3-调度中心"
syb      = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource\责任书模板\2024\3-部门与员工\4-收运部"
syb_dq   = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource\责任书模板\2024\3-部门与员工\4-收运部\东区"
syb_xq   = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource\责任书模板\2024\3-部门与员工\4-收运部\西区"
zhb      = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource\责任书模板\2024\3-部门与员工\5-综合部"
#人员名单模板位置
jyrymd   = r"E:\海宜洁源安全共享文件\jieyuan_safety_application\Template_resource"
#责任书生成位置
zrs      = r'E:\海宜洁源安全共享文件\jieyuan_safety_application'




# =============================================================================
# 函数
# =============================================================================
#遍历文件夹下所有文件（不要文件夹）
def get_filelists(file_dir):
    list_directory = os.listdir(file_dir)
    filelists = []
    for directory in list_directory:
         if(os.path.isfile(directory)):
            filelists = list_directory
            filelists.append(directory)
    return filelists

    
#拼接地址
def path_dir(list_directory,path_name):
    list_ =os.listdir(list_directory)
    read_jieyuan_name_dir =  [s for s in list_ if path_name in s] # 读洁源名单文件地址
    new_dir =  list_directory + '\\' + ' '.join(read_jieyuan_name_dir)  #拼接地址
    return new_dir


# =============================================================================
# 读取excel并清洗数据
# =============================================================================


#地址
new_dir = path_dir(jyrymd, "洁源花名册")

read_name_xlsx = pd.read_excel(new_dir,sheet_name= "8月",usecols=[3,4,6])   #读取excel
read_name_xlsx_y = read_name_xlsx.dropna(axis=0, how='all',inplace=False)   #警告，dropna按行删除,不修改源数据
read_name_xlsx_y.columns = ['所在部门','姓名','岗位']                        #重命名列名
haode = read_name_xlsx_y.drop(read_name_xlsx_y.index[[0]])                  #删除全是na的行
hao = haode.loc[11:,]                                                       #从安环部往后人员名单
haoya = hao.reset_index(drop = True)                                       # 重置列索引,drop = true：不保留原来index，只是为了好看
haone = haode.loc[5:10,]                                                   # 管理层特殊人员
haone_ = haone.drop(columns = '所在部门' )                                  #删除列
haone_haoya = haone_.reset_index(drop = True)      

"""
# =============================================================================
# ================Dataframe 转换为word=========================================
# =============================================================================

"""
'''字体大小对应pt

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


# =============================================================================
# 直接读取docx模板填写数据，避免后期表格有变动后需要大改==========================
# =============================================================================


# 将dataframe转换成list
def dataframe_tolist(dataframe):
    data = dataframe.values.tolist()
    return data

# 判断地址下文件夹是否存在,若不存在则生成文件夹
def path_dir_(list_directory,path_name):
    list_ =os.listdir(list_directory)
    read_jieyuan_name_dir =  [s for s in list_ if path_name in s] # 读洁源名单文件地址
    out_dir =  list_directory + '\\' + ''.join(path_name)         # 拼接地址
    if read_jieyuan_name_dir :
        pass
    else:
        os.makedirs(out_dir)  # 新建输出文件夹
    return out_dir


#调用责任书word模板,写入并保存(部门，岗位，领导，下级，责任书模板路径，签署日期，输出的责任书地址)
def select_tamplate(post,leader,rabbish,zrs_path,year,date_of_write,makedir_):

    #读取word模板
    zrs = DocxTemplate(zrs_path)
    
    #替换函数
    context = {"年":"{}".format(year),
               "领导": "{}".format(leader),
               '屌丝':"{}".format(rabbish),
               '卖身时间': '{}'.format(date_of_write),# 需要使用format直接变成字符串才能跟随文档格式！！！
               }
    
    zrs.render(context)#渲染
    
    #保存
    #new_dir =  makedir_ + '\\' + ''.join(out_dir)  #拼接地址
    #dir_ = os.makedirs(new_dir)
    #new_dir=path_dir_(makedir_,out_dir)
    output_path = os.path.join(makedir_, "{}-{}-{}.docx ".format(post,rabbish,year))
    zrs.save(output_path)



#生成责任书文件夹,并得到责任书地址
zerenshu_path = path_dir_(zrs,'责任书')
ahb_path      = path_dir_(zerenshu_path,'1-安环部')
scb_path      = path_dir_(zerenshu_path,'2-生产部')
ddzx_path     = path_dir_(zerenshu_path,'3-调度中心')
syb_path      = path_dir_(zerenshu_path,'4-收运部')
syb_east_path = path_dir_(syb_path,'收运部东区')
syb_west_path = path_dir_(syb_path,'收运部西区')
zhb_path      = path_dir_(zerenshu_path,'5-综合部')
fzjlybm_path  = path_dir_(zerenshu_path,'0-副总经理与部门')
#不打印的
bdy_path      = path_dir_(zerenshu_path,'6-不打印')

#部门员工：将dataframe转换成list
hao_dapartment= dataframe_tolist(haoya['所在部门'])
hao_name      = dataframe_tolist(haoya['姓名'])
hao_post      = dataframe_tolist(haoya['岗位'])

#纯纯领导：将dataframe转换成list
hao_name_chun = dataframe_tolist(haone_haoya['姓名'])
hao_post_chun = dataframe_tolist(haone_haoya['岗位'])




#部门领导及岗位
leader_      = ['张健新','林祺','张振','朱汉钜','赖志杰','陈俊儒','彭爱正','郑晓培','刘听','王瑞','杨君','邓家雄'] # 12
gangweimoban = ['安环专责','生产管理专责','运行工','检修工','调度员','系统维护专责', # 6
                '东区车辆检修工','东区司机','东区押运员','西区司机','西区押运员', # 5
                '西区车辆检修工','收运专责','综合部行政办事员','综合部专责','化验员'] # 5
#副总经理与部门
leader_fuck_u = ['杨君','叶远彪',"朱子超"] 
gangweimoban_fuck_u = ['安环部安全生产责任书',
                       '调度中心安全生产责任书',
                       '生产部安全生产责任书',
                       '收运部安全生产责任书',
                       '综合部安全生产责任书'] 



def select(a,b,mban,path):
    leader_fuck = leader_[a]             #选领导
    gangweiboban_s = gangweimoban[b]    #责任书模板路径
    zrs_path = path_dir(mban,gangweiboban_s)             
    zerenshu_dad_path = path             #责任书所在文件的目录
    return leader_fuck, zrs_path, zerenshu_dad_path

def select_2(a,b,mban,path):
    leader_fuck = leader_fuck_u[a]             #选领导
    gangweiboban_s = gangweimoban_fuck_u[b]    #责任书模板路径
    zrs_path = path_dir(mban,gangweiboban_s)             
    zerenshu_dad_path = path             #责任书所在文件的目录
    return leader_fuck, zrs_path, zerenshu_dad_path


# =============================================================================
#   生成各部门责任书
# =============================================================================
if zerenshu_run == 'yes':
    for f in range(len(hao_dapartment)):
        department_ = hao_dapartment[f]
        post_ = hao_post[f]
        rabbish_ = hao_name[f]
        if department_ == '安环部':
            leader_fuck, zrs_path, zerenshu_dad_path = select(0, 0,ahb,ahb_path)    # (领导，部门，输出文件夹)
    
        elif department_ == '生产部':
            if post_ == '生产管理专责':
                leader_fuck, zrs_path, zerenshu_dad_path = select(1, 1,scb,scb_path) 
            elif post_ == '运行工':
                leader_fuck, zrs_path, zerenshu_dad_path = select(8, 2,scb,scb_path) 
            elif post_ == '检修工':
                leader_fuck, zrs_path, zerenshu_dad_path = select(11, 3,scb,scb_path) 
            elif post_ == '化验员':
                leader_fuck, zrs_path, zerenshu_dad_path = select(8, 15,scb,scb_path) 
        
        elif department_ == '收运部':
            leader_fuck, zrs_path, zerenshu_dad_path = select(6, 12,syb,syb_path) 
            
        elif department_ == '收运部东区':
            if post_ == '司机':
                leader_fuck, zrs_path, zerenshu_dad_path = select(3, 7,syb_dq,syb_east_path) 
            elif post_ == '押运员':
                leader_fuck, zrs_path, zerenshu_dad_path = select(3, 8,syb_dq,syb_east_path) 
            elif post_ == '车辆检修工':
                leader_fuck, zrs_path, zerenshu_dad_path = select(3, 6,syb_dq,syb_east_path) 
            
        elif department_ == '收运部西区':
            if post_ == '司机':
                leader_fuck, zrs_path, zerenshu_dad_path = select(4, 9,syb_xq,syb_west_path) 
            elif post_ == '押运员':
                leader_fuck, zrs_path, zerenshu_dad_path = select(4, 10,syb_xq,syb_west_path) 
            elif post_ == '车辆检修工':
                leader_fuck, zrs_path, zerenshu_dad_path = select(4, 11,syb_xq,syb_west_path) 
    
        elif department_ == '监控中心':
            if post_ == '系统维护专责':
                leader_fuck, zrs_path, zerenshu_dad_path = select(10, 5,ddzx,ddzx_path)
            elif post_ == '监控调度员':
                leader_fuck, zrs_path, zerenshu_dad_path = select(7, 4,ddzx,ddzx_path) 
                
        elif department_ == '综合部':
            if post_ == '综合专责':
                leader_fuck, zrs_path, zerenshu_dad_path = select(5, 14,zhb,zhb_path) 
            elif post_ == '行政办事员':
                leader_fuck, zrs_path, zerenshu_dad_path = select(5, 13,zhb,zhb_path) 
        else:
            print("没打出来的人名字有：{}-{}-{}".format(department_, post_,rabbish_))
    
    
        select_tamplate(post_,leader_fuck,rabbish_,zrs_path,year,date_of_write,zerenshu_dad_path)
        

# =============================================================================
#  生成管理层责任书
# =============================================================================


    for u in range(len(hao_name_chun)):
        post_ = hao_post_chun[u]
        rabbish_ = hao_name_chun[u]
        if post_ == '副总经理':
            if rabbish_ == '杨君':
                leader_fuck, zrs_path, zerenshu_dad_path = select_2(2, 1,fzjlybm,fzjlybm_path) #(领导，部门，模板，输出文件夹)
            else:
                leader_fuck, zrs_path, zerenshu_dad_path = select_2(2, 1,fzjlybm,bdy_path) 
                pass
        elif post_ == '安环部经理':
            leader_fuck, zrs_path, zerenshu_dad_path = select_2(1, 0,fzjlybm,fzjlybm_path)
        elif post_ == '调度中心副主任':
            leader_fuck, zrs_path, zerenshu_dad_path = select_2(2, 2,fzjlybm,fzjlybm_path) 
        elif post_ == '综合部经理':
            leader_fuck, zrs_path, zerenshu_dad_path = select_2(1, 4,fzjlybm,fzjlybm_path) 
        elif post_ == '收运部经理':
            leader_fuck, zrs_path, zerenshu_dad_path = select_2(0, 3,fzjlybm,fzjlybm_path)
            
        select_tamplate(post_,leader_fuck,rabbish_,zrs_path,year,date_of_write,zerenshu_dad_path)


else:
    pass

'''
# =============================================================================
#  批量打印
# =============================================================================

打印时要调整打印机默认设置，设置成双面打印
fhg
'''


# ahb_path,scb_path,syb_path,syb_west_path,zhb_path,fzjlybm_path,ddzx_path
print_path = [syb_east_path]

if print_word == 'yes':
    # 获取指定目录下所有的 Word 文档路径
    for i in range(len(print_path)):
        
        folder_path = print_path[i]
        print('打印文件：',folder_path)

        doc_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.docx')]
        #doc_paths =doc_paths[]   # 控制断点续打
        # 创建 Word 应用程序对象
        word = win32com.client.Dispatch('Word.Application')
        time.sleep(print_time_a)
        # 遍历所有的 Word 文档并打印
        for doc_path in doc_paths:
            doc = word.Documents.Open(doc_path)
            time.sleep(print_time_b)
            print('{}正在打印第一份'.format(doc_path))
            doc.PrintOut(Copies=2, PrintToFile=False, Collate=False, ManualDuplexPrint=False)  # 使用默认打印机进行打印,打2份
            time.sleep(sleep) # 10
            print('{}正在打印第二份'.format(doc_path))
            doc.PrintOut(Copies=2, PrintToFile=False, Collate=False, ManualDuplexPrint=False)
            doc.Close()
            
        word.Quit()  # 退出 Word 应用程序

else:
    pass

   

    

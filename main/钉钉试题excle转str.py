# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:52:23 2024

@author: Microsoft
"""

import pandas as pd
import sys 
sys.setrecursionlimit(sys.getrecursionlimit()*5)


# Load the Excel file
file_path = r'E:\海宜洁源安全共享文件\标准化自评\【4】法律法规与安全管理制度\4.2规章制度\2-安全生产规章制度\安全管理制度汇总\洁源公司制度汇总2024\43-珠海市海宜洁源餐厨垃圾处置有限公司相关方安全管理制度\钉钉试题-试题（珠海市海宜洁源餐厨垃圾处置有限公司相关方安全管理制度）.xlsx'
biaoqian ='43-洁源公司相关方安全管理制度'
score1 = ''
xls = pd.ExcelFile(file_path)

# Check sheet names to understand the structure of the file
sheet_names = xls.sheet_names
sheet_names

# Load the content of the first sheet
df = pd.read_excel(file_path, sheet_name='工作表 1')
df.head()

# Extract relevant columns and clean up data
df_clean = df.iloc[1:, [0, 1, 2, 5, 6, 7, 8, 9]].copy()
df_clean.columns = ['题型', '题干', '答案', '分数', '选项A', '选项B', '选项C', '选项D']
df_clean.head()

# Initialize lists to hold formatted questions
single_choice_questions = []
multiple_choice_questions = []
true_false_questions = []

# Define function to format questions
def format_question(row):
    question_type = row['题型']
    question_text = row['题干']
    correct_answer = row['答案']
    if score1 == '':
        score = score1
    else:
        score = row['分数']

    options = {
        'A': row['选项A'],
        'B': row['选项B'],
        'C': row['选项C'],
        'D': row['选项D']
    }
    
    if question_type == '单选题':
        formatted_question = f"{len(single_choice_questions)+1}.【单选题】{question_text}\n"
        for key, value in options.items():
            if pd.notna(value):
                formatted_question += f"{key}．{value}\n"
        formatted_question += f"正确答案：{correct_answer}\n答案解析：\n标签：{biaoqian}\n分值：{score}\n"
        single_choice_questions.append(formatted_question)
    
    elif question_type == '多选题':
        formatted_question = f"{len(multiple_choice_questions)+1}.【多选题】{question_text}\n"
        for key, value in options.items():
            if pd.notna(value):
                formatted_question += f"{key}．{value}\n"
        formatted_question += f"正确答案：{correct_answer}\n答案解析：\n标签：{biaoqian}\n分值：{score}\n"
        multiple_choice_questions.append(formatted_question)
    
    elif question_type == '判断题':
        formatted_question = f"{len(true_false_questions)+1}.【判断题】{question_text}\n"
        formatted_question += f"正确答案：{correct_answer}\n答案解析：\n标签：{biaoqian}\n分值：{score}\n"
        true_false_questions.append(formatted_question)
    else:
        print(question_type)

# Apply the formatting function to each row
df_clean.apply(format_question, axis=1)

# Combine all questions into a single formatted string
formatted_questions = '\n'.join(single_choice_questions + multiple_choice_questions + true_false_questions)
print(formatted_questions)
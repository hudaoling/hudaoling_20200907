# -*- coding: utf-8 -*-
import pandas as pd
import jieba
from collections import Counter
from jpype import *
import pymysql
import re
import traceback
from  pyhanlp import  *
import  numpy
import xlrd #读取excel模块

#  加载自然语言处理模块
#startJVM(getDefaultJVMPath,"-Djava.class.path=C:\Program Files\hanlp\hanlp-1.7.0.jar;C:\Program Files\hanlp","-Xms1g","-Xmx1g")
HanLP =JClass('com.hankcs.hanlp.HanLP')
NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
Segment = HanLP.newSegment().enableOrganizationRecognize(True)


#打开一个workbook
workbook = xlrd.open_workbook('filters.xlsx')
#抓取所有sheet页的名称
worksheets = workbook.sheet_names()
#print('worksheets is %s' %worksheets)
#定位到sheet-filters
worksheet1 = workbook.sheet_by_name(u'filters')

#遍历sheet-filters中所有行row
num_rows = worksheet1.nrows
for curr_row in range(num_rows):
    row = worksheet1.row_values(curr_row)
    #print('row%s is %s' %(curr_row,row))

#遍历sheet-filters中所有列col
num_cols = worksheet1.ncols
for curr_col in range(num_cols):
    col = worksheet1.col_values(curr_col)
    #print('col%s is %s' %(curr_col,col))


#遍历sheet-filters中所有单元格cell
filters=[]
for rown in range(num_rows):#num_rows
    for coln in range(num_cols):
        filters.append(worksheet1.cell_value(rown,coln))
        continue
# print(filters) #读取“过滤词表”对应的所有单元格值.#<class 'list'>
# print(filters.index("云")) #查找filters中是否有“云”字
# filters.extend(filters_learning) #list.extend()给列表filters追加一个列表filters_learning
# filters = set(filters) #set 列表的不重复元素组合

#连接数据库
db = pymysql.connect(host='172.20.5.170', port=3306, user='hudaoling_ttl', passwd='hudaoling_ttl@!#', db='azure', charset="utf8")
cursor = db.cursor() #使用cursor()方法获取操作游标
# 获取项目名称、单位名称
cursor.execute("select distinct scene from project_name where scene != '' and scene is not null;")
data = cursor.fetchall()  # 接收mysql查询的所有结果

#将scene分词后，如果在filters里面，将该分词放弃
for d in data:
    scene = d[0]
    terms = list(jieba.cut(scene))#将scene分词，以“list”形式呈现
    #print(terms)
    s_words = [word for word in terms if str.lower(word) not in filters]#过滤掉filters里面的词
    #print(type(s_words),s_words)
    s_str = "".join(s_words)
    #print("s_str",s_str,s_words) #<class 'str'>
    #print(s_str.find("云"))
#
#去掉城市、地名
    s_terms = StandardTokenizer.segment(s_str)
    s_words = []
    for terms in s_terms:
        if str(terms.nature) not in ["ns", "qt", "w"]:
            s_words.append(str(terms.word))
    s_str = "".join(s_words)
    #print("s_str",s_str) #<class 'str'>
    s_words = list(jieba.cut(s_str))
    #print(s_words,s_str)

#如果filters关键字在scene里面，则scene替换该关键字为空
    for word in filters:
        if word  in s_str:
            s_str=s_str.replace(word,"")
            #print(word,"==",s_str)
            cursor.execute("update project_name set keyword = '{sn}' where scene = '{so}';".format(sn=s_str, so=d[0]))
            #cursor.execute("update project_name set keyword = '{sn}' where scene = '{so}';".format(sn=keyword2, so=d[0]))
            db.commit()

    # for f in filters:
    #     if f in keyword:
    #         keyword = keyword.replace(f,"")
    #         #print(keyword)
    # #print(keyword)
    # if keyword in cell:
    #     keyword=re.sub('\S',"",keyword)
    # #print(keyword) #跳出上级if，可以输出keyword
    #
    #     s_terms = StandardTokenizer.segment(s_str)
    #     s_words = []
    #     # 去掉地名，时量词，标点符号
    #     for sterm in s_terms:
    #         if str(sterm.nature) not in ["ns", "qt", "w"]:
    #             s_words.append(str(sterm.word))
    #
# cursor.close()
# db.close()
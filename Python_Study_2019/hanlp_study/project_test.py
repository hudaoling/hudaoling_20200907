# -*- coding: utf-8 -*-
import pandas as pd
import jieba
from collections import Counter
from jpype import *
import pymysql
import re
import traceback
import pyhanlp
from  pyhanlp import  *



# 去掉项目名称中的 机构团体名 nt
project_name="安庆市公共安全应急指挥中心备份中心"
company_name="安庆市公共安全应急指挥中心"

NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer') #NLP分词
StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')  #标准分词

# 去掉项目名称中的 nt机构团体名
p_terms = NLPTokenizer.segment(project_name) #项目名称的词性  NLPTokenizer
print(project_name)
print(p_terms)
for pterm in p_terms:
    if str(pterm.nature) in ["nt"]: #nt机构团体名
        #project_name = re.sub(".*" + str(pterm.word), "", project_name).replace("哈哈", '')
        flag = True
        flag_db = 2
        print('pterm.nature:', pterm.nature) # .nature是“词性”
        print('pterm.word:',pterm.word) # .word是“词内容”
        print('project_name',project_name)#项目名称被清空
        break

project_name="安庆市公共安全应急指挥中心备份中心"
company_name="安庆市公共安全应急指挥中心"
print("-" * 20,"去掉公司名称中的机构后缀、地名","-" * 20)
# 去掉公司名称中的nis机构后缀、nt地名
c_terms = StandardTokenizer.segment(company_name)#公司名称的分词
print(company_name)
print(c_terms)
for cterm in c_terms:
    if str(cterm.nature) in ["nis", "ns"]:
        print("cterm.nature",cterm.nature)
        company_name = company_name.replace(str(cterm.word), "")
        print('-',company_name)


project_name="安庆市公共安全应急指挥中心备份中心"
company_name="安庆市公共安全应急指挥中心7"
print("-" * 20,"接着从机构名称中去除单位名称","-" * 20)
if company_name in project_name:
    #index = project_name.index(company_name)
   # print('index', index)
    project_name = project_name.replace(company_name, "")
print('project_name2',project_name)

#关闭JVM连接
#shutdownJVM()
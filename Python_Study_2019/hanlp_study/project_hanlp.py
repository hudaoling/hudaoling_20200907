# -*- coding: utf-8 -*-
import pandas as pd
import jieba
from collections import Counter
from jpype import *
import pymysql
import re
import traceback
from  pyhanlp import  *

#  加载自然语言处理模块
#startJVM(getDefaultJVMPath,"-Djava.class.path=C:\Program Files\hanlp\hanlp-1.7.0.jar;C:\Program Files\hanlp","-Xms1g","-Xmx1g")
NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')

# 连接数据库
db = pymysql.connect(host='172.20.5.170', port=3306, user='hudaoling', passwd='hudaoling@123', db='azure', charset="utf8")
cursor = db.cursor()

# 获取项目名称、单位名称
cursor.execute("select ProjectName, CustomerName  from project_name  where  YEAR(CreateDate)=2018;")
data = cursor.fetchall()

if __name__ == "__main__":
    i = 0
    for d in data:
        flag = False
        flag_db = 0
        project_name = d[0]
        company_name = d[1]

        # drop company name
        # project_name = re.sub("（.*）|\(.*\)", "", project_name).replace("股份", "")
        # company_name = re.sub("（.*）|\(.*\)", "", company_name).replace("股份", "")
        project_name = project_name.replace("股份", "")
        company_name = company_name.replace("股份", "")


        if company_name in project_name and company_name[-1] != "云":
            # 去除项目名称中的单位名称
            project_name = project_name.replace(company_name, "")
            flag = True
            flag_db = 1
        else:
            project_name = project_name.replace("备份", "哈哈备份").replace("文档", "哈哈文档")

            # 去掉项目名称中的 机构团体名 nt
            p_terms = NLPTokenizer.segment(project_name)
            for pterm in p_terms:
                if str(pterm.nature) in ["nt"]:
                    project_name = re.sub(".*"+str(pterm.word), "", project_name).replace("哈哈", '')
                    flag = True
                    flag_db = 2
                    break

        if flag == False:
            c_terms = StandardTokenizer.segment(company_name)
            for cterm in c_terms:
                # 去掉公司名称中的机构后缀、地名
                if str(cterm.nature) in ["nis", "ns"]:
                    company_name = company_name.replace(str(cterm.word), "")
            # 接着从机构名称中去除单位名称
            if company_name != "" and company_name[-1] != "云" and company_name in project_name:
                index = project_name.index(company_name) + len(company_name)
                print('index',index)
                if project_name[index:index+1] in ["云"]:
                    company_name = company_name[:-2]
                project_name = project_name.replace(company_name, "").replace("哈哈", "")
                p_terms = StandardTokenizer.segment(project_name)
                for pterm in p_terms:
                    if str(pterm.nature) in ["nis", "ns"]:
                        project_name = project_name.replace(str(pterm.word), "")
                # print(project_name, company_name, d[0], d[1], p_terms, c_terms)
                flag = True
                flag_db = 3


        if flag == True and flag_db != 0:
            cursor.execute("update project_name set scene='{scene}' where project_name='{pn}';".format(scene=project_name, flag=flag_db, pn=d[0]))
            db.commit()
            print(project_name, d[0])

    cursor.close()
    db.close()



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


#  加载自然语言处理模块
#startJVM(getDefaultJVMPath,"-Djava.class.path=C:\Program Files\hanlp\hanlp-1.7.0.jar;C:\Program Files\hanlp","-Xms1g","-Xmx1g")
HanLP =JClass('com.hankcs.hanlp.HanLP')
NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
Segment = HanLP.newSegment().enableOrganizationRecognize(True)


with open("C:\\Users\\hu.daoling\\Desktop\\del_words.txt", "r", encoding="utf-8") as f:
    del_words = f.read().split("\n")
    #print(del_words)
for del_word in del_words:
    jieba.add_word(del_word) #增加分词
jieba.load_userdict("C:\\Users\\hu.daoling\\Desktop\\add_words.txt")#增加用户自定义分词词典

# 过滤词库1
with open("C:\\Users\\hu.daoling\\Desktop\\stop_words.txt", "r", encoding="utf-8") as f:
    stop_words = f.read().split("\n")
    #print(stop_words)
    #print(type(stop_words)) # <class 'list'>
# 过滤词库2
with open("C:\\Users\\hu.daoling\\Desktop\\filters.txt", "r", encoding="utf-8") as f:
    filters = f.read().split("\n")
    #print(filters)
# 过滤词库2
with open("C:\\Users\\hu.daoling\\Desktop\\filters_learning.txt", "r", encoding="utf-8") as f:
    filters_learning = f.read().split("\n")
    #print(filters_learning)
#
filters.extend(filters_learning) #list.extend()给列表filters追加一个列表filters_learning
filters = set(filters) #set 列表的不重复元素组合
#
db = pymysql.connect(host='172.20.5.170', port=3306, user='hudaoling_ttl', passwd='hudaoling_ttl@!#', db='azure', charset="utf8")
cursor = db.cursor() #使用cursor()方法获取操作游标
# 获取项目名称、单位名称
cursor.execute("select distinct scene from project_name where scene != '' and scene is not null;")
data = cursor.fetchall()  # 接收mysql查询的所有结果

scene = []
for d in data:
    temp = d[0].replace(" ", "").replace("-", "").replace("---", "").replace("--", "")
    #print("d[0]:",type(d[0]))#<class 'str'>字符串
    terms = list(jieba.cut(temp))#对scene分词,分词后是列表list
    #print("terms",terms,type(terms))#列表list
    # 去掉过滤词库1
    s_words = [word for word in terms if str.lower(word) not in stop_words]
    #print(s_words)
    #print(type(s_words))#<class 'list'>
    s_str = "".join(s_words)
    #print("s_words",type(s_words)) #<class 'list'>
    #print("s_str",type(s_str)) #<class 'str'>
    s_str = re.sub("\d+", "", s_str)#去掉数字

    # 去掉地名，时量词，标点符号
    s_terms = StandardTokenizer.segment(s_str)
    s_words = []
    for sterm in s_terms:
        if str(sterm.nature) not in ["ns", "qt", "w"]:
            s_words.append(str(sterm.word))
    s_str = "".join(s_words)
    #print(s_str.find("云"))
    s_words = list(jieba.cut(s_str))

    # 去掉过滤词库2
    # for word in s_words:
    #     if word not in filters:
            #print(type(word))#<class 'str'>
            # terms_save = [word for word in s_words if word not in filters]
            # length = len("".join(word))
            # if length <= 1:
            #     break
            # print(word, d[0], s_words)
            # cursor.execute("update project_name set keyword = '{sn}' where scene = '{so}';".format(sn=word, so=d[0]))
            # db.commit()
    #         break
# print(filters)
# cursor.close()
# db.close()

















































































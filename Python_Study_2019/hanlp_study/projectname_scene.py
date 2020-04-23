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

# 连接数据库
db = pymysql.connect(host='172.20.5.170', port=3306, user='hudaoling_ttl', passwd='hudaoling_ttl@!#', db='azure', charset="utf8")
cursor = db.cursor() #使用cursor()方法获取操作游标

# 获取项目名称、单位名称
cursor.execute("select ProjectName,CustomerName from project_name  where  YEAR(CreateDate)=2018;")
data = cursor.fetchall() #接收mysql查询的所有结果
#print(data)#mysql打开是元祖
#print(len(data)) # 查看data数据总共有多少条记录

if __name__ == "__main__":
    for d in data:
        flag = False
        flag_db = 0
        project_name = d[0]#项目名称
        company_name = d[1]#公司名称
        #print(company_name,project_name)

        #项目名称中包含公司名称，去除公司名称
        if company_name != "" and company_name in project_name:
            project_name = project_name.replace(company_name, "")

            project_name = re.sub('[a-zA-Z0-9]', "", project_name)
            #filter=['集团','备份','存储','文档','需求','云盘','项目','数据','云','硬盘','扩容','年', '设备','升级','服务','硬件','一期','二期','三期','管理','中心','增购','及','容灾','','']
            project_name = project_name.replace("集团", "").replace("备份", "").replace("存储", "").replace("文档", "").replace("需求", "").replace("云盘", "").replace("项目", "").replace("管理", "")
            project_name = project_name.replace("容灾", "").replace("硬盘", "").replace("扩容", "").replace("增购", "").replace("设备", "").replace("升级", "").replace("服务", "").replace("硬件", "")
            # project_name = project_name.replace("一期", "").replace("二期", "").replace("三期", "").replace("管理", "").replace("中心", "").replace("增购", "").replace("及", "").replace("容灾", "")
            r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~《》（）＋＋——、，]+' #去除所有符号
            project_name = re.sub(r,'',project_name)

            #project_name =re.compile('\d').sub('',project_name)
            #print(type(project_name), type(d[0]))
            print(d[0],"&&&",project_name)

            #把处理后的关键字同步回mysql字段
            cursor.execute("update project_name set scene='{scene}' where  ProjectName='{pn}' and YEAR(CreateDate)=2018  ;".format(scene=project_name,pn=d[0]))
            db.commit() #提交结果到mysql


        # 去掉项目名称中的 机构团体名 nt
        # p_terms = NLPTokenizer.segment(project_name)  # 项目名称分词（分出机构名称）
        # for pterm in p_terms:
        #     if str(pterm.nature) in ["nt"]:
        #         project_name = re.sub(".*", "", project_name)#替换机构名称
        #         #print(d[0],'---',pterm) #是机构团体名nt
        #         print(d[0], "$$", project_name)
        #      continue

        # 去掉公司名称中的nis机构后缀、nt地名
        # c_terms = StandardTokenizer.segment(company_name)  # 公司名称的分词(分出机构后缀，地名等)
        # for cterm in c_terms:
        #     if str(cterm.nature) in ["nis", "ns"]:
        #         company_name = company_name.replace(str(cterm.word), "")
        #         # print(company_name,'---',cterm)
        #     continue

cursor.close() #关闭游标操作
db.close() #关闭数据连接


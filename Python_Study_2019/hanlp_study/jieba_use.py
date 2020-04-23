import  jieba
import  pymysql

#jieba模块的分词用法
s = '我想和女朋友一起去北京故宫博物院参观和闲逛。'
cut = jieba.cut(s)
print (cut)
print ('【Output】',','.join(cut))

print(list(jieba.cut(s))) #将分词转换成列表

import jieba.posseg as pseg  #获得词性表

words = pseg.cut(s) #转换词性
print("===" * 10,"词性","===" * 10)

# 返回的是生成器哦，既words是一个内存地址
print(words)  #output:<generator object cut at 0x000001FB049DF750>

# 该如何打印分词结果呢？
for word,flag in words:
    print("%s  %s"%(word, flag))

#import  collections
from  collections import Counter
c = Counter(s).most_common(20)
print(c)


import jieba

#加载用户自定义字典
#jieba.load_userdict("C:\\Users\\hu.daoling\\Desktop\\add_words.txt")

#增加、删除分词
sen="胶州市市长江大桥"
sen_list=jieba.cut(sen)
#print(",".join(sen_list)) #将分词用逗号连接起来
#print(list(sen_list)) #将分词转换为列表list
for i in sen_list:
    print(i,end=",")

jieba.add_word('江大桥',freq=20000)
sen_list=jieba.cut(sen)
for i in sen_list:
    print(i,end="。")

#分词的一些测试实例
import re
import jieba

a = 'hello Wordsss111113我是某某'
c = ['hello', 'Wordsss111113', '我是某某', 'huxiameie ']
# strinfo = re.compile('he')
# print(strinfo)
# b = re.compile('\w').sub('',a)
# b=re.sub('[a-zA-Z0-9]',"",a)
# b=re.sub('\w',"",a)
# print(b)

# r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'  # 去除所有符号
# b = re.sub(r,'',a)

b = list(jieba.cut(a))
c = list(jieba.cut(c))
print("b", b)
print("c", c)
if b in c:
    print('bbbb', b)

#jieba.add_word(del_word) #增加分词
#jieba.load_userdict #增加用户自定义分词词典


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

# filters=['ttt','yyy','aaa']
# filters_learning=['yyyyoyiu','xxx']
# filters.extend(filters_learning)
# print("filters",filters)
#
# stop_words=['ttt','bbb','zzz''arm']
# s_words = [word for word in filters if str.lower(word) not in stop_words]
# print("s_words",s_words)

test="abcde\n某某\ng\nH\n大爷]"
#print('test',test,type(test))
#file=['a','b','c','d','e','f','g','h','A','H','Z']
file="abcde我是某某fghAHZ\n你是谁呢？\n我是你大爷ma\n上海\n江西\n鹰潭市\n湖南省\n金华\n北京\n青岛\n重庆市"
#print('file',file,type(file))

file2 = list(jieba.cut(file))
#print("file2",file2,type(file2))

s_words=[i for i in file2 if str(i) not in test]
#print('s_words',s_words)

s_str = "".join(s_words)
#print('s_str',s_str,type(s_str))

length = len("".join(s_words))
#print("length",length)


#去掉列表中的地名
s_terms = StandardTokenizer.segment(s_str)
#print(s_terms)
s_words = []
for terms in s_terms:
    if str(terms.nature) not in ["ns", "qt", "w"]:
        s_words.append(str(terms.word))
        #print(s_words)
s_str = "".join(s_words)
print("s_str",type(s_str),s_str)
s_words = list(jieba.cut(s_str))
#print(s_words,type(s_words))

print(s_str.find('你是'))

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

# 启动JVM
#startJVM(getDefaultJVMPath,"-Djava.class.path=C:\Program Files\hanlp\hanlp-1.7.0.jar;C:\Program Files\hanlp","-Xms1g","-Xmx1g")

# 中文分词：HanLP
print("=" * 30 + "HanLP分词" + "=" * 30)
HanLP = JClass('com.hankcs.hanlp.HanLP')
print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
print("-" * 70)

#标准分词：StandardTokenizer
print("=" * 30 + "标准分词" + "=" * 30)
StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
print(StandardTokenizer.segment('你好，欢迎在Python中调用HanLP的API'))
print("-" * 70)

# NLP分词：NLPTokenizer会执行全部命名实体识别和词性标注
print("=" * 30 + "NLP分词" + "=" * 30)
NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
print(NLPTokenizer.segment('中国科学院计算技术研究所的宗成庆教授正在教授自然语言处理课程'))
print("-" * 70)

#索引分词
print("=" * 30 + "索引分词" + "=" * 30)
IndexTokenizer = JClass('com.hankcs.hanlp.tokenizer.IndexTokenizer')
termList = IndexTokenizer.segment("主副食品");
for term in termList:
    print(str(term) + " [" + str(term.offset) + ":" + str(term.offset + len(term.word)) + "]")
print("-" * 70)


print("=" * 30 + " N-最短路径分词" + "=" * 30)
# CRFSegment = JClass('com.hankcs.hanlp.seg.CRF.CRFSegment')
# segment=CRFSegment()
# testCase ="今天，刘志军案的关键人物,山西女商人丁书苗在市二中院出庭受审。"
# print(segment.seg("你看过穆赫兰道吗"))
print("-" * 70)

print("=" * 30 + " CRF分词" + "=" * 30)
print("-" * 70)

print("=" * 30 + " 极速词典分词" + "=" * 30)
SpeedTokenizer = JClass('com.hankcs.hanlp.tokenizer.SpeedTokenizer')
print(NLPTokenizer.segment('江西鄱阳湖干枯，中国最大淡水湖变成大草原'))
print("-" * 70)

print("=" * 30 + " 自定义分词" + "=" * 30)
CustomDictionary = JClass('com.hankcs.hanlp.dictionary.CustomDictionary')
CustomDictionary.add('攻城狮')
CustomDictionary.add('单身狗')
HanLP = JClass('com.hankcs.hanlp.HanLP')
print(HanLP.segment('攻城狮逆袭单身狗，迎娶白富美，走上人生巅峰'))
print("-" * 70)

print("=" * 20 + "命名实体识别与词性标注" + "=" * 30)
NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
print(NLPTokenizer.segment('中国科学院计算技术研究所的宗成庆教授正在教授自然语言处理课程'))
print("-" * 70)


document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
           "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
           "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
           "严格地进行水资源论证和取水许可的批准。"
print("=" * 30 + "关键词提取" + "=" * 30)
print(HanLP.extractKeyword(document, 8))
print("-" * 70)

print("=" * 30 + "自动摘要" + "=" * 30)
print(HanLP.extractSummary(document, 3))
print("-" * 70)

# print("="*30+"地名识别"+"="*30)
# HanLP = JClass('com.hankcs.hanlp.HanLP')
# segment = HanLP.newSegment().enablePlaceRecognize(true)
# testCase=["武胜县新学乡政府大楼门前锣鼓喧天",
#         "蓝翔给宁夏固原市彭阳县红河镇黑牛沟村捐赠了挖掘机"]
# for sentence in testCase :
#   print(HanLP.segment(sentence))
# print("-"*70)

# print("="*30+"依存句法分析"+"="*30)
# print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))
# print("-"*70)

#关闭JVM连接
shutdownJVM()
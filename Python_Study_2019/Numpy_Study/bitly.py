path='D:\\PythonProject\\hanlp_study\\pydata-book-2nd-edition\\datasets\\bitly_usagov\\example.txt'
#print(open(path).readline())#每次读取一行；返回的是一个字符串对象，保持当前行的内存
#print(open(path).readlines())#读取所有行然后把它们作为一个字符串列表返回
#print("openpathe",open(path)) #<_io.TextIOWrapper name>

import  json
records=[json.loads(line) for line in open(path)] #jason转换成字典
#print(type(records))#<class 'list'>
#print(records[0])
#print(records[1])
#print(records[0]['tz'])#字典选择key是：tz的内容打印

time_zones=[rec['tz'] for rec in records if 'tz' in rec]#字典中含‘tz’的关键字内容，都打印出来
#print('time_zones',time_zones)

# #分类计数
# from collections import  defaultdict
# def get_counts(sequence):
#     counts=defaultdict(int)#定义一个空字典
#     for x in sequence:
#         counts[x]+=1 #针对x分类计数
#     return  counts
# counts=get_counts(time_zones)
# print('counts',counts,'\n')#defaultdict(<class 'int'>

# #取topN排名前多少行
# from collections import  Counter
# counts=Counter(time_zones)
# print(counts.most_common(10))#取排名前10条


#DataFrame将数据表示为一个表格
from pandas import DataFrame,Series
import pandas as pd
import  numpy as np
frame=DataFrame(records) #frame将records(字典)调整为一个表格
import  matplotlib
import  pylab

# print(frame)
# print(frame['tz'])#表格中tz的关键字内容
# print(frame['tz'][:20])#取出前20条（不排序）
#tz_counts=frame['tz'].value_counts()#value_counts  对tz关键字的内容分类计数,并排序
#print(tz_counts)
#print(tz_counts[:20])#表格中取出tz的排列前20条（排序）


#--------清洗数据并用matplotlib可视化报告--------
# clean_tz=frame['tz'].fillna('Missing')#替换缺失值NA为Missing
# clean_tz[clean_tz=='']='Unkown'#替换控制为Unknow
# #print(clean_tz)
# tz_counts=clean_tz.value_counts()#清洗完成后，再用value_counts分类计数
# #print(tz_counts)

#--------plot画图 kind = ’bar‘ 图标类型为条形图，rot 为转向率，倾斜角度--------
# tz_counts[0:20].plot(kind='barh',rot=0)
# pylab.show()#图形显示
# print(frame['a'][1])
# print(frame['a'][50])


#--------用数据中的 a 数据进行切片提取第一个数据，frame.a.dropna   和 frame['a'].dropna 是一样的--------
#dropna 返回一个仅含非空数据和索引值的 Series
results=Series([x.split()][0] for x in frame.a.dropna())
#print(results[:10])

#按照a中 windows 和非windows进行分类统计
cframe = frame[frame.a.notnull()]#非空单元格
#print('Windows',cframe.a.str.contains('Windows'))#是否包含字符串‘Windows’output:True of False

#np.where(condition, x, y)；满足条件(condition)，输出x，不满足输出y。
operating_system = np.where(cframe.a.str.contains('Windows'),
                            'Windows','Not Windows')
#print(operating_system[:5])

by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
#print(agg_counts[:20])

#用于按升序排序
indexer=agg_counts.sum(1).argsort()
#print(indexer[:10])

#利用take按照顺序截取最后10行
count_subset=agg_counts.take(indexer)[-10:]
print(count_subset)
count_subset.plot(kind='barh',stacked=True)
pylab.show()#图形显示

normed_subset=count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh',stacked=True)
pylab.show() #图形显示


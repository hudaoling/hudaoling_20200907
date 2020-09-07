
import numpy as np
import pandas as pd
import  re

df=pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['utah','ohio','texas','oregon'])
# print(df)

# t=df[df['b']>0.5].index
# print(t)
"""
               b         d         e
utah   -0.667969  1.974801  0.738890
ohio   -0.896774 -0.790914  0.474183
texas   0.043476  0.890176 -0.662676
oregon  0.701109 -2.238288 -0.154442
"""

#将函数应用到由各列或行形成的一维数组上。DataFrame的apply方法可以实现此功能
# f=lambda x:x.max()-x.min()
# #默认情况下会以列为单位，分别对列应用函数
# t1=df.apply(f)
# print(t1)

# """
# b    1.597883
# d    4.213089
# e    1.401566
# dtype: float64

# #
# t2=df.apply(f,axis=1)
# print(t2)
#

# utah      2.642770
# ohio      1.370957
# texas     1.552852
# oregon    2.939397
# dtype: float64
# """
#
# #除标量外，传递给apply的函数还可以返回由多个值组成的Series
# def f(x):
#     return pd.Series([x.min(),x.max()],index=['min','max'])
# t3=df.apply(f)
# #从运行的结果可以看出，按列调用的顺序，调用函数运行的结果在右边依次追加
# print(t3)
#
# """
#             b         d         e
# min -0.896774 -2.238288 -0.662676
# max  0.701109  1.974801  0.738890
# """
#
# #元素级的python函数，将函数应用到每一个元素
# #将DataFrame中的各个浮点值保留两位小数
# f=lambda x: '%.2f'%x
# t3=df.applymap(f)
# print(t3)
# """
#             b      d      e
# utah    -0.67   1.97   0.74
# ohio    -0.90  -0.79   0.47
# texas    0.04   0.89  -0.66
# oregon   0.70  -2.24  -0.15
# """
#
# #注意，之所以这里用map,是因为Series有一个元素级函数的map方法。而dataframe只有applymap。
# t4=df['e'].map(f)
# print(t4)
#
# """
# utah     0.74
# ohio     0.47
# texas   -0.66
# oregon  -0.15
# """111.

# df2=pd.DataFrame([list('abc'),list('def'),list('hij')],columns=list('xyz'))
# print(df2)
# print(df2[df2['x']=='d'].index.tolist()[0]-1)
# print(df2.loc[0]['z'])



# df3 = pd.DataFrame({'BoolCol': [1, 2, 3, 3, 4],'attr': [22, 33, 22, 44, 66]},
#        index=[10,20,30,40,50])
# print(df3)
# # a = df3[(df3.BoolCol==3)&(df3.attr==22)].index.tolist()
# # print(df3[(df3.BoolCol==3)&(df3.attr==22)].index.tolist())
# # print(a)
# # df3['name']=df3['attr'].apply((lambda x:x*3 if x==22 else None))
# # print(df3)
#
# df3['name']=df3[['attr','BoolCol']].apply((lambda row:row.index.tolist() if row['attr']==22 else None),axis=1)
# print(df3)
#
# if [False, False, False]:
#     print('a')
#
# x='abcdefgh'
# print(x.matches)

# 多个子字符串
# key_list = ['java', 'python', 'go', 'c++']
#
# # 字符串
# str = '我爱java,python,go,php'
# str2='Ni'
#
# if any(key in str2 for key in key_list):
#     print("包含哦!")




#------------read()方法------------
# 特点是：读取整个文件，将文件内容放到一个字符串变量中。
# 劣势是：如果文件非常大，尤其是大于内存时，无法使用read()方法。
# file = open('contract.txt', 'r')  # 创建的这个文件，也是一个可迭代对象
# print(type(file))#文本文件<class '_io.TextIOWrapper'>
# try:
#     text = file.read()  # 结果为str类型
#     print(type(text))#<class 'str'>
#     print(text)
# finally:
#     file.close()

#------------readline()方法------------
# 特点：readline()方法每次读取一行；返回的是一个字符串对象，保持当前行的内存
# 缺点：比readlines慢得多
# file = open('contract.txt', 'r')
# try:
#     while True:
#         text_line = file.readline() #<class 'str'>
#         if text_line:
#             print(type(text_line), text_line)
#         else:
#             break
# finally:

#     file.close()

#------------readlines()方法------------
# 特点：一次性读取整个文件；自动将文件内容分析成一行列表list
# file = open('contract.txt', 'r')
# try:
#     text_lines = file.readlines()#<class 'list'>
#     print(type(text_lines), text_lines)
#     for line in text_lines: #line是<class 'str'>
#         print(type(line), line)
# finally:
#     file.close()

# 判断某些内容或字符串存在则打印。
# import  json
# file = open('contract.txt', 'r')
# text_lines = file.readlines()
# #print(type(text_lines),text_lines)
# reads=[read for read in text_lines if '吴迪'  in read ]#如果吴迪在read里就打印
# print(reads)

# 列表转换为字典
# list1 = ['key1','key2','key3']
# list2 = ['1','2','3']
# dict=dict(zip(list1,list2))
# print(dict)

# from collections import  defaultdict
# counts=defaultdict(int)#
# print(counts)


# #ix,loc,iloc使用方法
# import pandas as pd
# data=[[1,2,3],[4,5,6]]
# index=['a','b']#行号
# columns=['c','d','e']#列号
# df=pd.DataFrame(data,index=index,columns=columns)#生成一个数据框
# print(df)
# print(df.loc[:,'c':'d'])
# print(df.iloc[:,0:2])
# print(df.ix[:,'c':'d'])
# print(df.ix[:,0:2])


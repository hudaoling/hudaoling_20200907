
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

b=[1,2,3,3,3]
print(b.count(3))
print(b ?)
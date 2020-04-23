# Author:Winnie Hu


import time

"""时间的三种格式
格式化字符串
元组格式 time.localtime()
时间戳格式time.time() """

#程序加上一些sleep时间，等待执行
time.sleep(0.1)

#time模块的使用帮助
#print(help(time))

#时间戳Timestamp：从当前时间到1970的相差秒时间
print(time.time())

#时间戳转化成元组struct_time(tuple)，
#gmtime:结果为UTC时区（格林威治天文时间）
#localtime:结果为UTC+8时区（北京时间）
print(time.localtime())#UTC+8北京时间
print(time.gmtime())#UTC时区，不输入默认传当前时间戳
print(time.gmtime(10000000))#也可以自定义输入的时间戳

#元组转换成时间戳
x=time.localtime()#元组
y=time.time()#时间戳
print('元组换时间戳：',time.mktime(x))
print(time.localtime(y))#将时间戳转换为元组

#元组转换成“格式化字符串日期”
#时间戳不能直接转换，需要先转换成元组
print("x元组:",x)
print("y时间戳:",y)
print('strftime:',time.strftime("%Y-%m-%d %H:%M:%S",x))
print('strftime:',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(y)))

print('asctime:',time.asctime(x))#元组转换成系统默认的日期字符格式
print('ctime:',time.ctime(y))#时间戳转成默认的日期字符格式

#将格式化字符的日期反转为元组格式
print('strptime:',time.strptime('2018-06-13 14:09:35',"%Y-%m-%d %H:%M:%S"))


#如何取用时间
#定义x变量，是一个元组形式的时间格式
x=time.localtime()#可以加时间戳的参数
print(x)
print(x.tm_year)#年
print(x.tm_mon)#月
print(x.tm_mday)#日
print('this is 2018 day:',x.tm_yday)#一年的第几天

import datetime

print('now()',datetime.datetime.now()) #返回当前时间
print('时间戳',datetime.date.fromtimestamp(time.time()) ) # 当前时间戳直接转成日期格式
print('+3',datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
print('-3',datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
print('hours=3',datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print('minutes=30',datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分



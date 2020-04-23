# Author:Winnie Hu

#shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，
# 可以持久化任何pickle可支持的python数据格式
#序列化和反转序列化

import shelve,datetime
# d=shelve.open("shelve_test")#打开一个文件
# info={'age':22,'job':'it'}
# name=['Alex','rain','test']
# d['name']=name
# d['info']=info
# d['date']=datetime.datetime.now()
# d.close()


d=shelve.open("shelve_test")#打开一个文件
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))

# Author:Winnie Hu

"""用于序列化的两个模块
    json，用于字符串 和 python数据类型间进行转换
    pickle，用于python特有的类型 和 python的数据类型间进行转换
Json模块提供了四个功能：dumps、dump、loads、load
pickle模块提供了四个功能：dumps、dump、loads、load"""


#将已经序列化的字典，反序列化（解析出来）
print("----普通的办法eval反序列化------")
f=open("test.text","r")
data=eval(f.read())#eval将字符串转换成字典
f.close()
print(data['age'])

print("----json loads方法反序列化------")
#json只支持简单的列表等数据类型，不支持复杂的函数等
import json
f=open("test.text","r")
data=json.loads(f.read())
print(data['name'])

print("----pickle loads方法反序列化------")
import pickle
def sayhi(name):
   print("hello:",name)  #反序列化的程序中没有该内存地址，需要把函数拷贝过来
    #print("2222")
f=open("test2.text","rb")
data=pickle.loads(f.read())
print(data['name'])
print(data['func']("Ryan"))#相当于调用函数sayhi,然后再给sayhi传值Ryan.sayhi=data['func']
#函数反序列化的时候，只认函数名即可，函数体可以不一样

print("----pickle load方法反序列化------")
import pickle
def sayhi(name):
   print("hello:",name)  #反序列化的程序中没有该内存地址，需要把函数拷贝过来
f=open("test2.text","rb")
pickle.load(f)#==pickle.loads(f.read())
print(data['name'])
print(data['func']("Ryan"))

print("----json loads多次反序列化------")
#不能反序列多次。
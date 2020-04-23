# Author:Winnie Hu
#jason 不用开发语言之间的数据交互，取代xml
#jason默认支持简单的数据类型，复杂的需要用pickle

#序列化：将字符串写入硬盘中
print("----普通的办法序列化------")
info={'name':'alex','age':'22','job':'it'}
f=open("test.text","w")
f.write(str(info)) #info字典写入test文件

print("\n----json dumps方法序列化------")
import json
info={'name':'alex','age':'22','job':'it'}
f=open("test.text","w")#test.text新建一个文件
print(json.dumps(info))#反转结果打印出来
f.write(json.dumps(info))#反转结果写入文件test
f.close()

print("\n----pickle dumps方法序列化------")
import pickle
def sayhi(name):
    print("hello:",name)
info={'name':'alex','age':'22','job':'it','func':sayhi}
f=open("test2.text","wb")#pickle变成了二进制,所以需要用wb写入
print(sayhi)##sayhi是函数的内存地址
print(pickle.dumps(info))#pickle是将info反转，打印出来反转结果
f.write(pickle.dumps(info))#info反转结果，写入文件test
f.close()


print("\n----pickle dumps方法序列化------")
import pickle
def sayhi(name):
    print("hello:",name)
info={'name':'alex','age':'22','job':'it','func':sayhi}
f=open("test2.text","wb")#pickle变成了二进制,所以需要用wb写入
pickle.dump(info,f)#==f.write(pickle.dumps(info))
f.close()

print("\n----json dumps多次序列化，但不能反序列------")
#注意：多次反转可以，但是多次反序列不行。万一需要反转多次，那就保存为多个文件
import json
info={'name':'alex','age':'22','job':'it'}
f=open("test3.text","w")

#一次反转，存了1次info
f.write(json.dumps(info))

#二次反转，存了第2次info
info['age']=38#年龄变更
f.write(json.dumps(info))
f.close()
# Author:Winnie Hu
#用于加密相关的操作，3.x里代替了md5模块和sha模块，
# 主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

import  hashlib
m=hashlib.md5()#生成一个hash对象m
m.update(b"Hello")#m更新内容为Hello,b代表字节byte类型
print('md5值m',m)#m成为一个md5值
print('十六进制m',m.hexdigest())#十六进制加密并打印出来“m”

m.update(b"It's me")#m更新增加内容It's me
print("m1",m.hexdigest())

m2=hashlib.md5()
m2.update(b"HelloIt's me")#检验m第二次update后，是不是变成了"HelloIt's me"，可以看十六进制加密码是否一致
print("m2",m2.hexdigest())

m.update(b"It's been a long time since last time we...")
print(m.hexdigest())

print("二进制",m.digest())#二进制格式hash

#加密含字符或中文的内容
m3=hashlib.md5()#
m3.update("Hello，let me 天王盖地虎".encode(encoding="utf-8"))#需要
print('m3',m3.hexdigest())#十六进制加密并打印出来“m”



#sha加密方法，已淘汰，不建议使用
hash = hashlib.sha1()
hash.update(b'admin')
print("sha1",hash.hexdigest())

hash2 = hashlib.sha512()
hash2.update(b'admin')
print("sha512",hash2.hexdigest())

#hmack模块，创建key和内容再进行处理然后再加密
#速度快，常用于消息加密
import  hmac
h=hmac.new(b"abcde","你是我的甜心youare250".encode(encoding="utf-8"))
print("hmac",h.hexdigest())

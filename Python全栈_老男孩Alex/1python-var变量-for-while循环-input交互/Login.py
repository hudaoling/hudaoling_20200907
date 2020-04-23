# Author:Winnie Hu

# Author:Winnie Hu
import getpass
#password=getpass.getpass("password:")#密文密码的方式

#if else的用法和格式,没有循环
_username='ryan'
_password='abc456'
username=input("username:")
password=input("password:")
print(username,password)
if _username==username and _password==password:#输入的用户名和密码与变量定义的用户名密码相同时
    print("Welcom user {name} login...".format(name=username))#注意换行后强制缩进了
else: #if与else同等级
    print("Invalid username or password!")
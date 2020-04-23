# Author:Winnie Hu
#http://www.cnblogs.com/alex3714/articles/5465198.html 课程资料
#print("hello world!")
#print("name")

'''变量'''
#变量 可以改变赋值的类型
#常量π  尽量用变量名大写表示
PIE = "3.1415926..."
print(PIE)
name = "Winnie Hu" #1
name2 = name #2  name赋值给name2
print(name) #3
print("My name is" ,name,name2)#4
name="PaoChe Ge" #5 name重新赋值，写入内存改变
print(name,name2)#6 name2的赋值并没有随着name赋值而变化，因为name2已经优先写入内存中了，不会再改变了。

#变量名只能是字母、数字或下划线的任意组合；(空格不行)
# 变量名的第一个字符不能是数字；
#关键字不能声明为变量名['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
#_name，name2,_____name____ 都是正确的写法
#2name，-name,#name,$name,Name Of Ryan都是错误的写法
#约定熟成的命名方式（变量名有含义，用英文简写,不宜写拼音）
#NameOfGirl，age,Job,GirlFriendOfJack,Wife_of_Ryan，Don'tLieToMe 适合的写法


'''字符编码'''
#二进制编码 二进制是由1和0两个数字组成的，它可以表示两种状态，即开和关。所有输入电脑的任何信息最终都要转化为二进制。
#ASCII:（American Standard Code for Information Interchange，美国标准信息交换代码）是基于拉丁字母的一套电脑编码系统，主要用于显示现代英语和其他西欧语言，
# 其最多只能用 8 位来表示（一个字节），即：2**8 = 256-1，所以，ASCII码最多只能表示 255 个符号。
#GBK,GB2312:为了处理汉字，程序员设计了用于简体中文的GB2312和用于繁体中文的big5。通常我们还是用GBK指代中文Windows内码。
#Unicode:（统一码、万国码、单一码）是一种在计算机上使用的字符编码。Unicode 是为了解决传统的字符编码方案的局限而产生的，它为每种语言中的每个字符设定了统一并且唯一的二进制编码，规定虽有的字符和符号最少由 16 位来表示（2个字节），即：2 **16 = 65536，
#UTF-8:en:1byte cn:3bytes,是对Unicode编码的压缩和优化，他不再使用最少使用2个字节，而是将所有的字符和符号进行分类：ascii码中的内容用1个字节保存、欧洲的字符用2个字节保存，东亚的字符用3个字节保存...
print("你好，世界！") #python3.0 默认UTF-8格式

#单行注释
#多行注释的功能（使用3个单引号或双引号）
'''
多行注释
多行注释
多行注释
'''
#多行变量赋值，3个单引号或双引号
Reason='''
多行注释
多行注释
多行注释
'''
print(Reason)

#单行变量赋值，1个单引号或双引号
Reason='My Name is Ryan'
Reason2="My Name's Ryan"
print(Reason,Reason2)


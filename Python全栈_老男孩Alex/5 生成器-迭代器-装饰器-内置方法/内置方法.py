# Author:Winnie Hu

#all()如果所有元素都是true,则返回true，不为true则返回false
#any()任意一个元素是true,则返回true,否则返回false
print("any()",all([0,-5,3]))
print("all()",all(["a",-5,3]))
print("any()",any([0,-5,3]))
print("any()",any([]))

#ascii()转换成ascii码格式
a=ascii(["我爱北京天安门",1,2,3])
print(a,type(a))

#bin() 数字的二进制转换
print("bin()",bin(1))
print("bin()",bin(10))

#bool布尔函数，判断真假
print("bool()",bool(1))
print("bool()",bool(0))
print("bool()",bool([]))

#bytearray()二进制修改
a=bytes("abcde",encoding="utf-8")#二进制字符
b=bytearray("abcde",encoding="utf-8")#可修改二进制
print(a.capitalize(),a)#
#print(b.capitalize(),b)
print(b[0])#a的ascii位置为97
print(b[1])#b的ascii位置为98

#callable()判断对象是否可调用，带括号就可被调用
print("callable()",callable([]))#返回true or false

#chr()把数字对应的ascii出来;ord()把ascii码中字符对应的位置找出来
print(chr(98))#ascii码98位置对应的字母是b
print(ord("b"))#ascii码字符b对应的位置是98

#classmethod 类方法

#compile（）把字符串转换成可执行程序
code="1+3/2*6"
c=compile(code,'','exec')
print(c)
print(exec(code))
#complex复数
#dict字典
#delatter
#dir 显示对象可用的方法
a={}
print(dir(a))

#eval() #把字符串(数据，简单运算等)编译成字典
# exec() 执行程序

#filter()过滤出你需要的数据
def sayhi(n):
    print(n)
sayhi(3)

# lambda() 匿名函数,只能写三元运算
calc=lambda n:print(n)
calc(5)

resfilter=filter(lambda n:n>6,range(10))#过滤出合格
resmap=map(lambda n:n*n,range(10))#对输出的每个值做处理

print("\n-----filter()&map()------")
print(resfilter)#filter类型<filter object at 0x00D6BD50>
for i in resfilter:print(i)
for j in resmap:print(j)

import  functools
print("\n-----reduce()值相加或相乘------")
resreduce=functools.reduce(lambda  x,y:x+y,range(10))
resreduce1=functools.reduce(lambda  x,y:x*y,range(1,10))
print(resreduce)#依次相加
print(resreduce1)#相乘（阶乘）

#float()浮点
#format()格式化

#frozenset()不可编辑的集合
a=set([1,4,333,212,33,33,12,4])#可变
b=frozenset([1,4,333,212,33,33,12,4])#不可变

#globals()整个程序变量名（key）和变量值(values)，作为一个字典
print(globals())

#hash（）哈希，通过一系列的运算转换为固定的映射关系
print(hash(1))
print(hash('alex'))
print(hash('Alex'))
print(hash('Ryan'))
print(hash('ryan'))

#local()只打印出局部变量（作为一个字典），和globals不同
def test():
    local_var=333
    print(locals())
    print(globals().get('local_var'))#内部用global也没有
test()
print(globals())#打印全局变量，不打印局部变量，所以local_var是没有打印的
print(globals().get('local_var'))#返回none

#next取出下一个值（迭代器使用）

#class object 世间万物皆为对象，每个对象都有属性，每个对象具备某些功能

#oct 八进制
#ord
#pow（x,n）返回x的n次方
#repr()用字符串表示对象
#reversed()列表反转
#round(x,n)#保留小数的几位
#slice(2,5)切片，取一个范围下的某一段值

#sorted()排序
a={6:2,8:0,1:4,-5:6,99:11,4:22}
print(a)#无序
print(sorted(a.items()))#按列表的key排序
print(sorted(a.items(),key=lambda x:x[1]))#按列表的values排序

#type()查看数据类型

#zip()把两个数联合起来为一个迭代器
a=[1,2,3,4]
b=['a','b','c','d']
for i in zip(a,b):
    print(i)

#__import__()导入字符串形式的模块,用户自定义模块

#help（）查看帮助
#hex()转成十六进制
#id()返回内存地址
#input()输入
#int()取整形
#len()字符长度
#max() min()返回最大值最小值
#oct()转八进制
#repr()把一个对象内存地址，用字符串表示出来
#sum()求和
#super()
# tuple()方法,将列表转换成列表
#zip()将 两组数据合并起来
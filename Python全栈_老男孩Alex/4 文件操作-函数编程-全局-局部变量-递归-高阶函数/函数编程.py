# Author:Winnie Hu
#函数是指将一组语句的集合通过一个名字(函数名)封装起来，
# 要想执行这个函数，只需调用其函数名即可
"""
函数的特性:
    减少重复代码
    使程序变的可扩展
    使程序变得易维护

1、面相对象：华山派——》类——》classs
2、面相过程:少林派——》过程——》def
3、函数式编程：逍遥派——》函数——》def

def test(x):#test（）#是函数名,()是形参
    "The function definitions" #参数的含义
    x+=1 #程序处理逻辑，复杂的代码集
    return x #定义返回值

"""
"""
#函数，有return返回值
def func1():
    "testing1"
    print("in the func1")
    return 10
#过程,返回none
def func2():
    "testing2"
    print("in the func2")

x=func1()#调用函数，接收func1返回值
y=func2()#调用函数，没有返回值
print('from func1 return is %s'%x)#结果是10
print('from func2 return is %s'%y)#结果是none

#函数的使用
import  time #导入时间模块
def logger():#定义函数
    time_format='%Y-%m-%d %X'#定义时间格式
    time_current=time.strftime(time_format)#调用系统时间
    with open("yesterday",'a+') as f:
        f.write("%s end action\n"%time_current)

def test1():#定义函数
    print("in the test1")
    logger()
def test2():
    print("in the test2")
    logger()
def test3():
    print("in the test3")
    logger()
test1()#调用函数
test2()
test3()

#函数的返回值 return用于结束函数，另一方面是返回某一个值
#return可以任意指定个数和类型，输出为元组
#return既可返回值，也可返回任意的object对象，比如函数等
#为什么要有return返回值？通知下一段程序：该函数执行完成了。
def testa():
    print("in the test1")
    return 0, 'hello',['alex','wupeiqi'],{'name':'alex'}
    print("end") #return之后的语句是不会执行的
print(testa())
#返回元组 (0, 'a', ['alex', 'wupeiqi'], {'name': 'alex'})


#参数形参和实参（x,y）
def test(x,y):#x,y是形参，只是一个引用,不占内存
    print(x,y)

test(1,2)#1，2是实参，x=1,y=2 实际上使用的，真实存在内存变量中的
test(1,2)#  位置参数调用，与形参位置一一对应
test(y='a',x='b')#关键参数调用，与形参顺序无关,必须在位置参数的后面

x='aa'
y='bb'
test(y=y,x=x)
test(3,y=2)

def test2(x,y,z):
    print(x,y,z)
test2(3,6,9)
test2(3,6,z=9)
test2(3,y=6,z=9)
test2(x=3,y=6,z=9)
test2(z=9,x=3,y=6,)

#默认参数：调用函数的时候，默认参数非必须传递
#用途：设定默认值，省去了必须指定的要求
def test(x,y=2):
    print(x,y)
test(1)
test(1,100)
"""

#参数组：非固定参数，若你的函数在定义时不确定用户想传入多少个参数，就可以使用非固定参数
#定义形参的时候，实参一定不能多；但是当有默认变量时，实参可以少。

#*args代表接受的参数量是不固定的，
#把n个位置参数 转换成元组
def test(x,*args):
    print(x,args)
test(1,100,5,6,'a')#直接写参数
test(*[1,100,5,6,'a','b','b'])#*args=tuple([1,100,5,6,'a','b'])元组

#把 N 个关键字参数，转换成字典
def test2(**kwargs):#**kwargs转换成字典
    print(kwargs)
    print(kwargs['name'],kwargs['age'],kwargs['job'])
test2(name='alex',age=8,job='IT',salary=50000)#关键字参数

def test3(name,age=18,*args,**kwargs):
    print(name,age,args,kwargs)

test3('alex')#w未指定**kwargs时，默认返回空{}
test3('alex',26,sex='m',job='it')#**kwargs
test3('alex',sex='m',job='it',age=3)#**kwargs


test3('alex',6,sex='m',job='it')#*args,没有位置参数，就返回空（）
test3('alex',6,7,9,sex='m',job='it')#*args，有位置参数，就返回（7,9）

#函数嵌套函数
def test3(name,age=18,*args,**kwargs):
    print(name,age,args,kwargs)
    logger("test3")#嵌套函数

def logger(source):#logger这个函数需先定义再调用
    print("from %s"% source)

test3('alex',6,7,9,sex='m',job='it')
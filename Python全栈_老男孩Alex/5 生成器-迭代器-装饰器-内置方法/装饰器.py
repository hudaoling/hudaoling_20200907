# # Author:Winnie Hu
#
# 装饰器：
# 定义：本质就是函数（装饰其它函数）就是为其它函数添加附加功能。
# 原则：1.不能修改被装饰的函数的源代码
#       2.不能修改被装饰的函数的调用方式
# 实现装饰器的知识储备：高阶函数+嵌套函数=装饰器
# 1、函数既变量：
#    a.定义一个变量，相当于把函数的“函数体”赋值给了变量。
# 2、高阶函数：
#    a:把一个函数名当做实参传给另外一个函数（在不修改被装饰函数代码的情况下，为其添加功能）
#    b:返回值中包含函数名(不修改函数的调用方式)
# 3、嵌套函数
#   a.函数里面再定义子函数

#
# 匿名函数：没有用def定义的函数
# 匿名函数—lambda x:x*3
# 匿名函数的赋值—calc=lambda x:x*3


#高阶函数(函数名传给实参)
# import  time
# def bar():
#     time.sleep(3)
#     print('in the bar')
#
# def test1(func):
#     start_time=time.time()
#     func()  # bar传给了func,因此func=bar,func()=bar()
#     #bar()
#     stop_time=time.time()
#     print("the func run time is %s"%(stop_time-start_time))
# test1(bar)#bar是函数名，相当于变量，bar相当于门牌号，输出为内存地址
# bar()

#高阶函数（返回值包含函数名）
# import  time
# def bar():
#     time.sleep(3)
#     print('in the bar')
#
# def test1(func):
#    print(func)
#    return func
# test1(bar)#bar是函数名，相当于变量，bar相当于门牌号，输出为内存地址
# test2(bar())

#装饰器案例
import time
def timer(func):#timer(test1),func=test1
    def deco():
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the func run time is %s "%(stop_time-start_time))
    return deco

@timer #相当于test1=timer(test1)重新赋值，test1相当于deco（内存地址）
def test1():
    time.sleep(3)
    print('in the test1')
    return
@timer
def test2():
    time.sleep(3)
    print('in the test2')

test1()
test2()

# Author:Winnie Hu
#高阶函数：变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
#abs是内置函数，取绝对值

def add(x,y,f):# f被赋值为内置函数"abs"
    return  f(x)+f(y)

res = add(3,-6,abs)#abs为内置函数
print(res)


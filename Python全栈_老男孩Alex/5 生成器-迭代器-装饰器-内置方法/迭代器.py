# Author:Winnie Hu
print("我们已经知道，可以直接作用于for循环的数据类型有以下几种：\n"
"一类是集合数据类型，如list、tuple、dict、set、str等；\n"
"一类是generator，包括生成器和带yield的generator function。\n"
"这些可以直接作用于for循环的对象统称为可迭代（可循环）对象：Iterable。\n"
"可以使用isinstance()判断一个对象是否是Iterable对象：\n")

print("迭代器：可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。")

print("----Iterable----")
from collections import  Iterable
#"可迭代对象"
print(isinstance([], Iterable))#true
print(isinstance({}, Iterable))#true
print(isinstance('abc', Iterable))#true
print(isinstance((x for x in range(10)), Iterable))#true
print(isinstance(100, Iterable))#false

print("----Iterator迭代器----")
from collections import  Iterator
#"迭代器"
#生成器generators是迭代器
print(isinstance((x for x in range(10)), Iterator))#true
print(isinstance([], Iterator))#false
print(isinstance({}, Iterator))#false
print(isinstance('abc', Iterator))#false

print("----iter()函数----")
#iter()函数：
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))#true
print(isinstance(iter('abc'), Iterator))#true

#for循环的原理：实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

print("----小结----")
print("凡是可作用于for循环的对象都是Iterable类型；\n"
"凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；\n"
"集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。")
# Author:Winnie Hu
print("通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了\n。"
      "所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。\n"
      "要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：\n"
      "如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。")

#***列表，在cmd下执行 [i * 2 for i in range(10)]
# a=[]
# for i in range(10):
#     a.append(i*2)
# print(a)

#列表
# a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# for i in a:
#     b.append(i+1)
# print('a:',a,'\n','b:',b)


#***列表生成器：(i * 2 for i in range(10))，将[]列表改为（）生成器
#列表生成器generator object

#列表是生成后存于内存中，而列表生成器保存的是算法，并不占内存空间。
#只有在调用时才会生成相应的数据，调用一次返回一个，
#用for循环取值，还有一个__next__()方法，取下一个值；
#不能用列表切片的形式取值
f=(i * 2 for i in range(10))
print(f)#f代表generator生成器,输出为<generator object fib at 0x0106F330>
print(f.__next__())#取next
print(f.__next__())#取下一个next
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print("----use <f.__next__()逐个取值>-----\n")
for i in f:
    print(i)

print("----use <for i in f循环取值>-----\n")



#***裴波那契：从小到大推算数字
# def fib(max):#100
#     n,a,b=0,0,1
#     while n<max:#n<100
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return  'done'
#
# fib(100)


#带yield的函数生成器generator function，实现列表生成器，
#可以中途跳出该函数，进行一些输出等操作
def fib(max):#100
    n,a,b=0,0,1
    while n<max:#n<100
        yield b#保存了函数的中断状态，返回当前状态值（函数停在此位置）
        a,b=b,a+b
        n=n+1
    return  'done'#如果next执行超过范围时，会抛异常

f=fib(100)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

print("--------------start loop--------")
for i in f:
    print(i)#循环调用

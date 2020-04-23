#裴波那契数列
# def fib(max):#形参max
#      n,a,b=0,0,1#变量赋值
#      while n<max:#100次循环内
#          print(b)
#          a,b=b,a+b# 初次赋值是a1=1(b0初始值),b1=0（a0初始值）+1（b0初始值）=1,二次赋值a2=1（b1）,b2=(a1)+1(b1)=2
#          n=n+1
#      return 'done'
# fib(100) #这是一个函数

#函数式列表生成器，只要有yield就是一个生成器，已经不是函数了

def fib(max):#形参max
     n,a,b=0,0,1#变量赋值
     while n<max:#100次循环内
         yield b#列表生成器，生成b
         a,b=b,a+b# 初次赋值是a1=1(b0初始值),b1=0（a0初始值）+1（b0初始值）=1,二次赋值a2=1（b1）,b2=(a1)+1(b1)=2
         n=n+1
     return 'done'
f=fib(10)  #这是一个generator----生成器
print(f.__next__())#调用yield b，并返回值
print(f.__next__())
print(f.__next__())
print("--打印累了，干点别的活吧--")#函数可以随时跳出，进行别的操作
print(f.__next__())
print(f.__next__())
print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())#当next次数超过maxx=10时，抛异常：StopIteration: done
print("\n")
print("---for---")#next完成，进入到for循环，继续打印
for i in f:
    print(i)


#如果想要拿到return返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
def fib(max):#100
    n,a,b=0,0,1
    while n<max:#n<100
        yield b
        a,b=b,a+b
        n=n+1
    return  'done'#如果next执行超过范围时，会抛异常
g = fib(5)
while True:
    try:#不停的尝试
        x = next(g)
        print('g:', x)
    except StopIteration as e:#异常处理代码
        print('Generator return value:', e.value)
        break




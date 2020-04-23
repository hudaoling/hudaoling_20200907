# Author:Winnie Hu

#递归：函数内部可以调用其自己
#最大递归次数是999次
#递归必须要有个明确的结束
# 每进入一层问题规模应该有所减少
#递归效率不高，递归层次过多会导致栈溢出

#无限次递归的函数，不能使用
# def calc(n):
#     print(n)
#     return calc(n+1)
# calc(0)

def calc(n):
    print(n)
    if int(n/2)>0:
        return calc(n/2)
    print("-->",n)
calc(16)
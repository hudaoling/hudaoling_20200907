import pandas as pd
from pandas import Series,DataFrame
import  numpy as np

#Series类似于一维数组，由一组数据和与数据索引组成
obj=Series([4,7,-5,3]) #构建Series，名称为obj,将自动创建0——>N-1的整数型索引
print(obj)
print(obj.values)#查询Series-obj的值
print(obj.index)#查询Series-obj的索引
#output:RangeIndex(start=0, stop=4, step=1)

#可以通过赋值的方式就地修改,通过改变索引内容直接赋值。
obj.index=['Bob','Steve','Jeff','Ryan']  #原来索引是[1,2,3,4]
print(obj)


obj2=Series([4,7,-5,3],index=['d','b','a','c'])#手动添加index索引
print(obj2)
print(obj2.index)#查询Series-obj2的索引
#output:Index(['d', 'b', 'a', 'c'], dtype='object')

print(obj2['a'],obj2['d']) #可以通过索引的方式选取Series中的单个或一组值
obj2['d']=8  #将obj index索引为d的数值变更为8
print(obj2['d'])


#Numpy数组运算（布尔值数组过滤，标量乘法，应用数学函数等）都会保留索引和值之间的链接：
print(obj2[obj2>2])
print(obj2*2)
print(np.exp(obj2))# np.exp(B) 求e的幂次方;np.sqrt(B):求B的开方

#可以将Series看成一个定长的有序字典，因为他是索引值到数据值的一个映射。它可以用在许多原本需要字典参数的函数中
print('b' in obj2,'f' in obj2) #b是存在的索引则true，而f是不存在的索引则false,只能通过索引取值


#可以通过python字典来构建Series:
sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3=Series(sdata)
print(obj3)

state=['California','Ohio','Oregon','Texas']
obj4=Series(sdata,index=state) #在index 指定为states时，需要到sdata数组中去匹配相对应的值,注意区分大小写）
print(obj4)
#output：'California'不在sdata中，其结果为NaN(非数字not a number，缺失值missing，NA值）

#pandas中isnull和notnull函数用于简称缺失数据
print(pd.isnull(obj4))#isnull：缺失值为True，非缺失值为False
print(pd.notnull(obj4))# notnull：缺失值为False，非缺失值为True
#Series也有类似的实例方法
print(obj4.isnull())
print(obj4.notnull())

#Series最重要的一个功能：算术运算中会自动对其不同索引的数据：两个数组相加时，会根据索引相同的值相加，例如Ohio洲的两个数组值相加）
print(obj3+obj4)

#给Series数组及其index索引赋予一个名字name
obj4.name='population'
obj4.index.name='state'
print(obj4) #output:最下方Name: population
print(obj4.index) #output:最右方name='state'
print(obj4['Ohio']) #根据索引取值


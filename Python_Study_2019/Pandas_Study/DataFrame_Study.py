#DataFrame是一个表格型的数据结构，每列可以是不同的值类型（数值，字符串，布尔值等），既有行索引也有列索引，被看做由Series组成的字典（共用同一个索引），类似于Excel表格。

from pandas import Series,DataFrame
import pandas as pd
import  numpy as np

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data) #不指定列排序，则自动按data字典顺序
frame=DataFrame(data,columns=['year','state','pop']) #指定列按year,state,pop此排序
print(frame)

#类似于Series,传入的数据中找不到，就会产生NA值（output中是NaN表示)
frame2=DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five']) #显式指定列顺序和索引
print(frame2)  #debt 为NaN


#取列：可以将DataFrame的列获取为Series数组，拥有原来相同的索引且各Series的name属性也自动定义好了，例如name=state,name=year。
print(frame2['state'])
print(frame2.year)
print(frame2['year'])  #等同于print(frame2.year)
print(frame2['pop'])
#取行，用索引字段ix,可以将DataFrame的行获取为Series数组，通过位置或名称的方式进行获取
print(frame2.ix['three']) #use index

#列可以通过赋值的方式进行修改,列表或数组长度必须匹配,所有的空位都将被填上缺失值
frame2['debt']=16.5#debt=16.5
print(frame2)
frame2['debt']=np.arange(5) #长度5，整数0-4
print(frame2)
val=Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
print(frame2) #one,three自动填充为NaN

#删除列,关键字del
frame2['eastern']=frame2.state=='Ohio'
print(frame2)
del frame2['eastern']
print(frame2)

#另一种数据形式的嵌套字典（也就是字典的字典）
pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=DataFrame(pop)
print(frame3)
print(frame3.T)#行列转置

print(DataFrame(pop,index=[2001,2002,2003])) #2000索引未被指定则合并删除，2003索引新增但无值则NaN
print(frame3)

print(frame3['Ohio'][:-1])  #取Ohio列的值,倒数第一个的索引是-1
pdata={'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]}
print(DataFrame(pdata))

#给index和columns属性命名
frame3.index.name='year'
frame3.columns.name='state'
print(frame3)
print(frame3.index) #取出索引值
print(frame3.values)#取值列值
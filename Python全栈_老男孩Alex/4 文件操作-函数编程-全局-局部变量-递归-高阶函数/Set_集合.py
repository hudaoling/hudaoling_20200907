# Author:Winnie Hu
#集合{}是一个无序的，不重复的数据组合，它的主要作用如下：
#去重，把一个列表变成集合，就自动去重了
#关系测试，测试两组数据之前的交集、差集、并集等关系
#按command键，再双击可以进入函数的含义
list1=[1,4,5,7,3,6,7,9]
list1=set(list1) #将列表设置为集合{}
print(list1,type(list1))

list2=set([2,6,0,66,22,8,4])
print(list1,list2)

#交集（取出两个子集相同的部分），简单运算符 &
print("交集intersection",list1.intersection(list2))
print("交集&",list1 & list2)


#并集(两个子集合并，去重)，简单运算符 \
print("并集union",list1.union(list2))
print("并集 | ",list1 | list2)

#差集 简单运算符 -
print("1差2集difference",list1.difference(list2))
print("2差1集difference",list2.difference(list1))
print("1差2集-",list1 - list2)
print("2差1集-",list2 - list1)


#对称差集---反向差集，互相没有的取出来,简单运算符 ^
print("对称差集",list1.symmetric_difference(list2))
print("对称差集^",list1 ^ list2)

#子集和父集  简单运算符<= >=
list3=set([1,7,3]) #都包含在list1中
print("子集",list3.issubset(list1))
print("父集",list1.issuperset(list3))

print("子集<=",list3<=list1)
print("父集>=",list1>=list3)

#判断两个集合是否有交集，没有交集返回true,否则返回false
list4=set([5,6,8])
print("交集判断T",list4.isdisjoint(list3))
list5=set([5,6,7])
print("交集判断F",list5.isdisjoint(list3))

#add增加
list1.add(999)#单项添加
list1.update([777,888,999,777]) #多项添加
print("update",list1)
print("len",len(list1))#集合长度

#pop,dicard删除
list1.remove(777)
print("remove",list1) #指定元素删除，元素不存在会报错
list1.pop() #任意随机删除
print("pop",list1)
list1.discard('a') #删除指定元素，存在即删除，不存在不做操作
print("discard",list1)

#判断某个元素在不在集合里面
print(777 in list1)
print(777 not in list1)
print('a' not in list1)


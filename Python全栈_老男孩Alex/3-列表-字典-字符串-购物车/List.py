# Author:Winnie Hu

#list的使用
#按command键，再双击可以进入函数的含义
names=["ZhangYang", "GuYun" ,"XiangPeng","XuLiangChen"]
print(names)
#取单个值
print(names[0]) #ZhangYang
print(names[2]) #XiangPeng
print(names[-1])#取最后一个值XuLiangChen
print(names[-3])#取倒数第三个GuYun
#切片
#前闭后开（顾头不顾尾）的取值范围，即后面的是2位置不取
print(names[1:2]) #"['GuYun']
print(names[0:3])#0可以忽略 ['ZhangYang', 'GuYun', 'XiangPeng']
print(names[:3])#['ZhangYang', 'GuYun', 'XiangPeng']
print(names[-2:])# 如果想取最后一个，必须不能写-1，只能这么写['XiangPeng', 'XuLiangChen']
print(names[0::2])#从0开始每隔一个取值['ZhangYang', 'XiangPeng']
print(names[::3])h#和上面的一样，跳着切片，步长为3

#追加-只能单个追加
names.append("LeiHaidong")
print(names)

#insert插入-只能单个插入
names.insert(1,"ChenRonghua")
names.insert(3,"XingZhiyu")
print(names)

#修改-
names[2]="XieDi"
print(names)

#remove，del删除-
names.remove("ChenRonghua")
del names[3]#删除指定位置
names.pop(3)#删除指定位置
names.pop()#默认删除最后一个
print(names)

#index查询指定位置
print(names.index("XieDi"))
print(names[names.index("XieDi")])

#count计数
names=["ZhangYang", "ZhangYang" ,"XiangPeng","XuLiangChen"]
print(names.count("ZhangYang"))

#清空列表
#names.clear()
print(names)
#列表反转
names.reverse()
#排序
names.sort()
#扩展
#names.extend()
names2 = [1,2,3,4,5,6]
names.extend(names2)
print(names,names2)

#删除变量
del names2
print(names2)


#浅copy，只克隆第一层，第二层以后就是记录内存地址，后面直接调研
names_a=["a","b","c","d"]
print(names_a)
'''del names_a #删除变量
#print(names_a)'''

name_copy=names_a.copy() #复制变量,浅copy
print(name_copy) #name_copy
names_a[3]="e" #变更下列表，看下复制情况
print(names_a)
print(name_copy) #第一层copy的内容，不会变化

#第二层变量会随之改变
names_a=["a","b","c",["a","b","c","d"],"d"]
print(names_a)
name_copy=names_a.copy()
print(name_copy)
names_a[4]="e" #把第一层列表，元素d变成e
names_a[3][0]="e"#第二层列表，元素a变成e
print(names_a)
print(name_copy) #第一层列表的变化未被重新复制，但是第二层列表(只是记住了内存地址，取内存地址对应的值，所以是变化的）

name_copy #复制变量的二层列表改变时，会反向影响“被复制的变量”
name_copy[3][0]="z"
print(names_a)
print(name_copy)


#深深的copy,完全克隆，不受“被复制变量”的改变影响
import copy
names_a=["a","b","c",["a","b","c","d"],"d"]
name_copy=copy.deepcopy(names_a)
names_a[4]="e"
names_a[3][0]="e"
print(names_a)
print(name_copy)

#列表循环,依次逐个打印
for i in name_copy:
    print(i)

#列表长度
print(len(names))

#元组,不可变，不允许编辑
names=("ZhangYang", "ZhangYang" ,"XiangPeng","XuLiangChen")
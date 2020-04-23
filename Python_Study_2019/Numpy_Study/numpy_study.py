from numpy import  *
import  numpy as np

#ndarray是一个通用的同构数据多维容器，shape表示各维度大小，dtype说明数组类型
#----------数据类型int,float,bool等----------
# print(np.int8) #<class 'numpy.int8'>
# print(np.dtype(np.int8)) #int8
#
# dt = np.dtype([('age',np.float)])
# a = np.array([(10,),(20,),(30,)], dtype = dt)
# print(a)
#
# student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
# a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
# print(a)


# aranges随机生成整数数组;
# ndarray.ndim 用于返回数组的维数，等于秩
# a = np.arange(24)
# print("a",a)
# print (a.ndim,"--",a.shape)# a 现只有一个维度
# # 现在将a调整其维度大小
# b = a.reshape(2,4,3)  # b 现在拥有三个维度
# print("b",b)
# print (b.ndim,"--",b.shape)

#np.array将输入（列表、元祖、数组）转换成多维数组ndarray
#shape查看数组大小，reshape调整数组大小，dtype数组类型
# a = np.array([[1,2,3],[4,5,6]])
# a.shape =  (3,2)
# print ("a.shape",a)
# a.reshape(2,3)
# print("a.reshape",a)
# print(a*10,a.dtype)

#zeros,empty,arange用法
# print("np.zeros",np.zeros(6))#zeros是生成均为0值的数组
# print("np.zeros",np.zeros([2,3]))
# print("np.empty",np.empty(12))
# print("np.empty",np.empty([2,3,2]))#empty任意随机数字
# print("arange",np.arange(15))#python内置函数range数组版


#astype将数组调整数据类型
#float浮点，int整数，string_字符串，bool布尔
# arr=np.array([1,2,3,4,5])
# print(arr.dtype)
# arr=arr.astype(np.float)
# print(arr.dtype)
# print("arr*arr",arr*arr) #数组可以参与各种计算
# print("1/arr",1/arr)

# #包含数字的字符串string_也可以转换为float或int数字
# numeric_strings=np.array(['1.25','-9.6','42','4.449'],dtype=np.string_)
# print("numeric_strings",numeric_strings.dtype,numeric_strings)
# numeric_strings2=numeric_strings.astype(float)
# print("numeric_strings2",numeric_strings2.dtype,numeric_strings2)

# #基本的切片和索引
# arr=np.arange(10)
# print("arr[5]",arr[5])
# print("arr[4:8]",arr[4:8])
# arr[4:8]=12
# print("arr",arr)
#
# #对索引切片重新赋值后，修改会反应在源数组（随之会改变）
# arr_slice=arr[4:8]
# print(arr_slice)
# arr_slice[1]=12345
# print(arr,arr_slice)


#多维数组切片,以及取值方法
# arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("arr2d",arr2d)
# print(arr2d[2])#取1-3行
# print(arr2d[0][2])#取1行3列
# print("arr2d[0,2]",arr2d[0,2])#取1行3列，中间用逗号隔开（行和列）
# print("arr2d[:2,1:]",arr2d[:2,1:])#取1-2行，2-n列
# print("arr2d[1,:2]",arr2d[1,:2])#取2行，1-3列列
# print("arr2d[:2]",arr2d[:2])#取1-2行，不指定列（即所有），“：”可以代替所有行或列
#
# arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #这是2*2*3的数组
# print("arr3d",arr3d)
# print(arr3d[0])


#多维度复制，重新赋值
# old_values=arr3d[0].copy()
# arr3d[0]=42
# print("arr3d",arr3d)#arr3d[0]被重新赋值为42
# print("old_values",old_values)
# arr3d=old_values#arr3d整数据被重新赋值为old_values=arr3d[0].copy()
# print("arr3d",arr3d)

# #布尔型索引,布尔长度要和被索引长度一致，否则报错
# #IndexError: boolean index did not match indexed array along dimension 0; dimension is 6 but corresponding boolean dimension is 7
# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# data=np.random.randn(7,4)
# print(names)
# print(data)
# print(names== 'Bob')
# print(data[names=='Bob'])#names=='Bob'为True时，从数组data中取数，False 时不取数，刚好1，4为True，取了1，4行
# print(data[names!='Bob'])#names！='Bob'时，从数组data取值
# print(data[names!='Bob',2:])#切片，行=names!='Bob'，列=2到N
# data[data<0]=0#将数组data所有<0的值，归置为0
# print(data)
# data[names!='Joe']=7#将数组data所有不含‘Joe’的值，归置为0
# print(data)

# #花式索引，花式索引跟切片不一样，它总是将数据复制到新数组中
# arr=np.empty((8,4))
# print(arr)
# for i in range(8):
#     arr[i]=i #将arr数组值为i
#     print(i)
#     print(arr[i])
# print(arr)
# print("arr[[4,3,0,6]]",arr[[4,3,0,6]])
# print("arr[[-3,-5,-7]]",arr[[-3,-5,-7]])

# #数组转置和轴对换arr.T（行列转置）
# arr=np.arange(15).reshape(3,5)
# print(arr)
# print(arr.T)#行列转置
# arr=np.random.randn(6,3)#randn产生随机数的函数
# print("arr",arr)
# print("np.dot",np.dot(arr.T,arr))

# #通用的函数abs,sqrt,square,exp,sign，floor等等
# #maximum,minimum,mod,add,less,equal等等
# arr=np.arange(10).reshape(2,5)
# print(arr)
# print(np.sqrt(arr))
# x=np.random.randn(8)#随机生成8各数字
# y=np.random.randn(8)
# print("x,y",x,y)
# print("np.maximum(x,y)",np.maximum(x,y))#最大值
# print("abs",np.abs(x))

# #利用数组进行数据处理
# points=np.arange(-5,5,0.01)#-5到5，步长为0.01的数组
# xs,ys=np.meshgrid(points,points)
# z=np.sqrt(xs**2+ys**2)
# print(ys)
# print(z)
#
# import  matplotlib.pyplot as plt #可视化模块
# plt.imshow(z,cmap=plt.cm.gray);plt.colorbar() #可视化创建
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")#可视化标题
# plt.show()

# #将条件逻辑表述为数组运算,相当于x if condition else y
# arr = np.random.randn(4, 4)
# print(arr)
# print(arr>0)
# print(np.where(arr>0,2,-2))#正值替换为2，将所有负值替换为－2。若利用np.where，则会非常简单

# #数学和统计方法sum,mean,std,var,min,max
# #可以通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算。sum、mean以及标准差std等聚合计算（aggregation，通常叫做约简（reduction））
# arr=np.random.randn(4,5)#随机生成4-5之间的数字
# print("arr",arr)
# print("arr.mean",arr.mean())#平均值
# print("np.mean",np.mean(arr))#平均值
# print("arr.sum",arr.sum())#总和
# print("arr.mean(axis=1)",arr.mean(axis=1))#所有行计算
# print("arr.sum(axis=0)",arr.sum(0))#所有列计算

#排序sort
arr=np.random.randn(5)
arr.sort()
print("sort()",arr)

arr=np.random.randn(2,5)
arr.sort(1)
print("sort(1)",arr)
arr.sort(0)
print("sort(0)",arr)


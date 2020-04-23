import numpy as np
#ndarray数组，如何构建数组
arr=np.arange(10)
arr[4]=5
arr[5:7]=12
arr_slice=arr[7:9]
arr_slice[1]=12345
print("arr",arr)

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d.shape)#(3, 3)二维数据： 三行三列

print(arr2d[0][2]) #ndarray索引方法
print(arr2d[0,2]) #效果同上

arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d.shape)#(2, 2, 3)三维数据
print("arr3d[0]",arr3d[0]) #output:[[1 2 3] [4 5 6]]
print("arr3d[1,0]",arr3d[1,0]) #output:[7 8 9]

#切片索引
print(arr[1:6])


old_values=arr3d.copy()
arr3d[0]=42
print("arr3d",arr3d)
print("old_values",old_values)

import ran
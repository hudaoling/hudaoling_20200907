# Author:Winnie Hu
print('from the package package_test')

#把package_test包下的模块test1(所有的代码加载到这个位置)
from .import  test1
#相当于test1='test1.py all code'  test1是个变量
#from .是从当前目录下导入
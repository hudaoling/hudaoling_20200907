# Author:Winnie Hu

import  module_alex#导入模块名
print(module_alex.name)
module_alex.say_hello()

from  module_alex import *#导入模块的所有代码过来，相当于直接运行模块代码
def logger():
     print('in the main')
print(module_alex.name)
logger()
#当本程序有logger函数时，以本程序输出。
# 本程序无logger时，才输出module_alex的logger()输出


from module_alex import logger as logger_alex
logger()#本程序的logger
logger_alex()#module_alex.logger函数重命名后的logger_alex函数



#跨路径跨目录的导入模块和包
import sys,os
print('环境变量',sys.path)
print('main文件当前目录:\n',os.path.abspath(__file__))
print('main文件的根目录2018-6-5:\n',os.path.dirname(os.path.abspath(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('根目录2018-6-5的根目录PythonStudy_hdl:\n',BASE_DIR)
sys.path.append(BASE_DIR)
import  test
#test.fib(5) #引用test模块下的fib函数



#导入包python package，执行其目录下的_init_.py文件
print("package_test")
import  package_test
# run _init_.py--->test1='test1.py all code'--->可直接调用.test1

#导入package后，如何调用包下面的模块呢？
#以下以test1.py模块为例
package_test.test1.test()
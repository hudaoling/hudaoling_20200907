# Author:Winnie Hu
#print("""
一定义
"模块module"：用来从逻辑上组织python代码（变量，函数，类，逻辑）。
本质就是.py结尾的python文件；实现一个功能。（文件名test.py,对应的模块名是test）
也就是python程序文件。

"包python package":用来从逻辑上组织模块的；本质就是一个目录（必须带有一个_init_.py文件）

二导入方法
1、导入 import  module_name,module_name2
#使用方法 module_name.say_hello()建议使用此种方法）
#本质是 module_alex被导入成为一个变量

2、导入所有的函数 from module_name import *
#把test文件里的所有代码拿过来执行一遍，不建议用*
#使用方法logger() ,name() 这种方法直接调用函数

3、from module_name import logger
4、from module_name import logger as logger_alex
#调用后重命名函数，避免函数重名冲突
""")
#print("""
三 import本质（路径搜索和搜索路径）

"导入模块"的本质就是把python文件解释一遍
"导入包"的本质就是执行该包下的_init_.py文件

# 跨目录导入py文件
import module_name ---->module_name.py---->module_name.py的路径（找 ）
---->sys.path(当前路径)---->
#""")

三、导入优化
用from方法调用函数，相当于把代码拿过来用，避免每次调用每次去查找，
从而可以优化函数调用效率。


四、模块的分类
a.标准库（内置模块）
1.time与datetime
2.
b.开源模块
c.自定义模块

# import module_alex
# print(module_alex.name)
# module_alex.say_hello()
#
# from module_alex import *
# logger() #mfrom   odule_alex
#
# def logger():
#     print('我不在module_alex中')
# logger() # from logger
# import  package_test #导入python package

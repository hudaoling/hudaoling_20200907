# # Author:Winnie Hu
# #如何去找conf下的settings.py和main.py文件
#
# print(__file__) #返回当前程序相对路径（在cmd里面是相对路径）
#
# #动态获取到绝对路径并写入到环境变量
# import os
# import sys
# print(os.path.abspath(__file__))#返回当前程序的绝对路径
# print(os.path.dirname(os.path.abspath(__file__)))#找到了atm的父路径，返回目录名不需要文件名
#
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#找到了Atm根目录路径
# sys.path.append(BASE_DIR)#把Atm目录程序加入到环境变量
# import Conf,Core #再导入多个程序目录
#
# from Conf import settings#调用文件settings
# from Core import main#调用文件main
# main.login()


print(__file__)
import os
import sys
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import Conf,Core
from Conf import settings
from Core import main
main.login()
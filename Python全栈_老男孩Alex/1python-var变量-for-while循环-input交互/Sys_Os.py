# Author:Winnie Hu

import sys #导入sys库
#print(sys.path) #打印环境变量
#print(sys.argv) #打印该py的绝对路径
#print(sys.argv[2]) #从列表list里,接收参数


#标准库和定制库的存放位置
#os.py；sys.py也是标准库（存在以下位置）
'''
'D:\\Users\\hu.daoling\\AppData\\Local\\Programs\\Python\\Python36-32\\lib',
'D:\\Users\\hu.daoling\\AppData\\Local\\Programs\\Python\\Python36-32\\lib'\\site-packages',
'''

import os #导入os模块，跟系统交互调用等

os.system("dir")  #输出当前路径的文件列表,结果直接输出到屏幕上，输出之后就没有了。
cmd_res=os.system("dir") #os.system不会把值输出给变量，执行命令，不保存结果
print("---",cmd_res) #输出为0，代表命令执行成功，但无结果


cmd_res=os.popen("dir").read() #read把执行结果读出来，且是中文
print("---",cmd_res)

os.mkdir("new_dir") #当前目录创建一个目录



#自己写库文件（模块，其实就是写一个py文件，然后再import该库文件即可）
import login  #login是自己写的一个登陆文件

#导入时默认在当前目录找库文件，如果文件不在该目录时，会提示No module named 'login'
#这时请把该库文件放入到定制库中，或者手动添加环境变量
"""'D:\\Users\\hu.daoling\\AppData\\Local\\Programs\\Python\\Python36-32\\lib',"""






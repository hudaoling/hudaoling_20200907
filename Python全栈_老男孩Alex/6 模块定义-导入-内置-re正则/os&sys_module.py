# Author:Winnie Hu
#本文建议在cmd下完成，用于提供系统级别的操作
#os模块的作用：文件夹（路径）的查询、新建、删除、判断、环境变量
import  os

print(os.getcwd()) #获取当前工作目录，即当前python脚本工作的目录路径
print(os.chdir('D:\\Users'))  #改变当前脚本工作目录；相当于shell下cd
print(os.chdir(r'D:\Users'))#改变当前脚本工作目录；相当于shell下cd
print(os.curdir)  #返回当前目录: ('.')
print(os.pardir)  #获取当前目录的父目录字符串名：('..')
print(os.makedirs(r'Z:\A\B\C'))  #可生成多层递归目录
print(os.removedirs(r'Z:\A\B\C')) #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
print(os.mkdir(r'Z:\B')) #生成单级目录；相当于shell中mkdir dirname
print(os.rmdir(r'Z:\B'))#删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print(os.listdir(r'Z:'))   #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
#print(os.remove() )# 删除一个文件
#print(os.rename("oldname","newname")) #重命名文件/目录
#print(os.stat('path/filename'))#  获取文件/目录信息

#window目录是右斜杠\\ linux目录是左斜杠/

print(os.sep)  #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.linesep)   # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
print(os.pathsep)    #输出用于分割文件路径的字符串(环境变量)
print(os.name)    #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.system('dir'))  #运行shell命令，直接显示
print(os.environ)  #获取系统环境变量
print(os.path.abspath(r'Z:\a\b\c\a.txt')  #返回path规范化的某文件绝对路径
print(os.path.split(r'Z:\a\b\c\a.txt'))  #将path分割成目录和文件名二元组返回
print(os.path.dirname(r'Z:\a\b\c\a.txt'))  #返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename(r'Z:\a\b\c\a.txt'))  #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.exists(r'Z:\a\b\c\a.txt'))  #如果path存在，返回True；如果path不存在，返回False
print(os.path.isabs(r'Z:\a\b\c\a.txt'))  #如果path是绝对路径，返回True
print(os.path.isfile(r'Z:\a\b\c\a.txt'))  #如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir(r'Z:\a\b\c\a.txt'))  #如果path是一个存在的目录，则返回True。否则返回False
print(os.path.join(r'Z:',r'b',r'b.txt'))  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.getatime(path))  #返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime(path))  #返回path所指向的文件或者目录的最后修改时间


#sys模块的方法，用于提供对解释器相关的操作
#sys模块的作用是：返回操作系统平台名称，环境变量等
sys.argv#命令行参数List，第一个元素是程序本身路径
sys.exit(n)#退出程序，正常退出时exit(0)
sys.version #获取Python解释程序的版本信息
sys.maxint#最大的Int值
sys.path#返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform#返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
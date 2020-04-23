# Author:Winnie Hu

# Author:Winnie Hu
# r读，w写，a是追加,r+是读写（追加）,w+是写读，a+是追加读写，rb二进制读写文件

'''
data=open("yesterday",encoding="utf-8").read()#读文件
print(data)

# r 是指文件以只读模式打开
f=open("yesterday",'r',encoding="utf-8")#内存对象，文件句柄
data=f.read()#一行一行读完结束，读完一遍就结束了。
data2=f.read()#data2不会再重头读，没有读出内容。
print(data)
print('------data2------',data2)
'''

#  w 是覆盖写，旧文件将会被覆盖内容清除，慎重操作
f=open("yesterday",'w',encoding="utf-8")#内存对象，文件句柄
f.write("wo ai beijing tiananmen,\n")#写内容，是新建文件
f.write("tiananmen shang taiyang sheng")

# a 追加内容在文本最后面,追加模式也是不能读的
f=open("yesterday",'r',encoding="utf-8")#内存对象，文件句柄
f.write("lai lai lai")
f.write("zou zou zou")
f.close()#关闭文件

f=open("yesterday",'r',encoding="utf-8")

#打印前5行
print(f.readlines())#读出来为一个列表
for i in range(5):#打印前5行
    print(f.readline())

#不常用，不打印第9行，index是排序
for index,line in enumerate(f.readlines()):
    if index==9:
        print('----我是分割线-----')
        continue
    print(line.strip())#strip把空格和换行去掉

#常用方法,高效循环，一行一行读写，缓解内存压力，适合G以上大文件'''
count=0
for line in f:#f是迭代器
    if count==9:
        print('----我不需要输出，请忽略----')
        count += 1
        continue
    print(line)
#寻找光标位置tell,返回指定位置seek

#print(f.tell())#按字符计数，找到光标位置
#print(f.readline()) #readline是读行，默认第一行开始
#print(f.readline())#继续往下打印行
print(f.read(220)) #read是读字符串
print(f.tell())    #读的字符当前位置
f.seek(0)          #将光标返回0，也可以其它字符位置
print(f.tell())    #光标重置后的新位置
print(f.readline()) #打印当前位置的行内容

#其它的文件操作
print(f.encoding)#当前编码类型
print(f.fileno())#文件编号
print(f.name)#打印文件名
print(f.isatty())#打印是否终端设备
print(f.seekable())#打印，光标是否能返回
print(f.readable())#文件是否可读
print(f.writable())#文件是否可写
print(f.closed)#检查文件是否有关闭，返回true或false
f.close()#关闭文件
print(f.closed)#关闭以后，就是true


#读写的时候是先写内存（中间有个缓存时间），达到一定量（缓存满了）再往硬盘里刷
#如果你需要实时写硬盘，就需要用flush
f=open("yesterday2",'w',encoding="utf-8")
f.write("hello ryanhello ryanhello ryan\n")
print(f.flush())

#进度条的实现方法
import  sys,time
for i in range(10):
    sys.stdout.write("#")#sys.stdout屏幕输出
    sys.stdout.flush()
    time.sleep(0.1)

# truncate 将文件截取到第n个字符
f=open("yesterday2",'a',encoding="utf-8")
f.truncate(5)

# r+文件读写(打开读文件，并在后面追加写)
f=open("yesterday2",'r+',encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
f.write("hello world")#以读和追加的方式打开
print(f.readline())


# w+文件写读(写还是往后追加，没有太多用处)
f=open("yesterday2",'w+',encoding="utf-8")
f.write("---hello world---\n")#以读和追加的方式打开
f.write("---ryan---\n")
f.write("---winnie---\n")
print(f.tell())
print(f.readline())
f.seek(5)#光标移到第5个字符
print(f.tell())
f.write("---append shoud be here---")
print(f.readline())

#追加读写
#f=open("yesterday2",'a+',encoding="utf-8")#追加读写

# rb以二进制读文件,ab是追加二进制
f=open("yesterday2",'rb')#以二进制读文件，网络传输使用，读出来文件前面带一个b
print(f.readline())
print(f.readline())

# wb以二进制写文件
f=open("yesterday2",'wb')
f.write("hello ryan test\n".encode())
f.close()

# 文件修改（修改后写入新文件，用replace需求修改的内容）
f = open("yesterday", 'r', encoding="utf8")  # 源文件
f_new = open("yesterday2", 'w', encoding="utf8")  # 修改后写入到新文件
for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受", "肆意的快乐等Alex享受")
    f_new.write(line)
f.close()
f_new.close()

# with语句
为了避免打开文件后忘记关闭，可以通过管理上下文，即：
with open('log', 'r') as f:
    如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源。

    with open('log1') as obj1, open('log2') as obj2:
        pass
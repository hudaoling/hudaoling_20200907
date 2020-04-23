# Author:Winnie Hu

name="My Name is {name},She is a worker and She is {year} old"
print(name.capitalize())#首字母
print(name.count("i"))
print(name.center(50,"-")) #打印50个字符，不够用-补齐，并摆放中间
print(name.endswith("ker")) #判断是否以什么结尾
print(name.expandtabs(tabsize=30))# \  把这个键转换成多少个空格
print(name.find("is")) #取字符的索引位置，从0开始计算
print(name[name.find("is"):13])#返回索引的目的就是为了切片取字符串
print(name[name.find("is"):])#从is取数到最后
print(name.format(name='Winnie Hu',year=32))#给变量赋值
print(name.format_map({'name':'Winnie Hu','year':32}))#给变量赋值，不常用
#print(name.index())
print('ab23'.isalnum())#判断name变量，是不是阿拉伯数字
print('abcde'.isalpha())#判断是不是纯英文字母
print('2'.isdigit())#判断是不是十进制
print('100'.isdigit())#判断是不是整数
print('name_of_you'.isidentifier())#判断是不是一个合法的标识符（合法的变量名）
print('1name'.islower())#判断是不是小写
print('MY NAME '.isupper())#判断是不是大写
print('33'.isnumeric())#判断是不是一个数字
print(name.isspace())#判断是不是空格
print('My Name Is '.istitle())#判断是不是标题,单词首个字母大写是标题
print('My Name Is '.isprintable())#判断是不是能打印
print('+'.join(['1','2','3','4']))#把列表合并为字符串格式
print(name.ljust(100,'*'))#用*补全到指定的字符数量,字符串在左边
print(name.rjust(100,'-'))#用*补全到指定的字符数量，字符串在右边
print('\nWinnie Del\n'.strip())#\n代表换行，strip默认去掉两头的空格或回车
print('Winnie Del\n'.lstrip())#\n代表换行，lstrip去掉左边的空格或回车
print('Winnie Del\n'.rstrip())#\n代表换行，lstrip去掉右边的空格或回车
print('Winnie'.lower())#转换成小写
print('Winnie'.upper())#转换成大写
p = str.maketrans("abcdefli",'123$@456')#定义字符串与另一串字符串的对应关系
print("alex li".translate(p))#对alex li,根据上面的对应关系进行逐一替换,可用于密码加码等
print('alex li'.replace('l','L',1))#替换字符串
print('alex lil'.rfind('l'))#查找到从右边开始的某个字符串
print('al ex lil'.split())#按照指定的分割符拆分列,结果是list
print('al-ex-lil'.split('-'))#按照指定的分割符拆分列
print('1+2+3+4'.split('+'))#按照指定的分割符拆分列
print('1+2\n+3+4'.splitlines())#按空格或换行来拆分列
print('Alex Li'.swapcase())#大小写转换
print('alex li'.title())#变更为标题，首字母大写
print('alex li'.zfill(50))#字符串不够的时候，补0
name2='\n@qq.com' #\n代表换行






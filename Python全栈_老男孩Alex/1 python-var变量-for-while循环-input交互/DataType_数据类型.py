# Author:Winnie Hu
一、数字
2是一个整数的例子
3.23是浮点数的例子
type（） #查看数据类型

1.int（整型）
在32位机器上，整数的位数为32位，取值范围-2**31~2*31-1
在64位机器上，整数的位数为64位，取值范围-2**63~2*63-1
2.long(长整型，大一些的整数)
长度没有指定宽度，如果整数发生溢出，python会自动将整数数据转换为长整型


3.float浮点数
浮点数用来处理实数，即带有小数的数字。
52.3E-4是浮点数的例子。E标记表示10的幂。在这里，52.3E-4表示52.3 *10**4

二、布尔值
真或假  1或0

三、string字符串
"hello world"
万恶的字符串拼接：python中的字符串在C语言中体现为是一个字符数组，每次创建字符串时候需要在内存中开辟一块连续的空，并且一旦需要修改字符串的话，就需要再次开辟空间，万恶的 + 号每出现一次就会在内从中重新开辟一块空间。
字符串格式化输出
name = "alex"
print
"i am %s " % name
'i am {}'.format(name)
# 输出: i am alex

PS: 字符串是 % s;整数 % d;浮点数 % f
字符串常用功能：移除空白;分割;长度;索引;切片

四、列表list[]---中括号表示，可变
列表是我们最以后最常用的数据类型之一，通过列表可以对数据实现最方便的存储、修改等操作
names = ['Alex', "Tenglan", 'Eric']
创建列表：
name_list = ['alex', 'seven', 'eric']
或
name_list ＝ list(['alex', 'seven', 'eric'])
基本操作：索引;切片;追加;删除;长度;循环;包含

五、元组 info()-----括号表示,不可变列表
创建元组：
元组其实跟列表差不多，也是存一组数，只不是它一旦创建，便不能再修改，所以又叫只读列表
语法
names = ("alex", "jack", "eric")
ages = (11, 22, 33, 44, 55)
或
ages = tuple((11, 22, 33, 44, 55))

六、字典 info{}-----大括号标识，是无序的
字典一种key - value 的数据类型，使用就像我们上学用的字典，通过笔划、字母来查对应页的详细内容。
语法:
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
字典的特性：
dict是无序的
key必须是唯一的,so 天生去重

person = {"name": "mr.wu", 'age': 18}
或
person = dict({"name": "mr.wu", 'age': 18})
常用操作：索引;新增;删除;键、值、键值对;循环;长度

七、数据运算
http://www.runoob.com/python/python-operators.html
算数运算：比较运算：赋值运算：赋值运算：成员运算：成员运算：位运算：运算符优先级：

八、bytes类型
二进制，01
八进制，01234567
十进制，0123456789
十六进制，0123456789
ABCDEF
二进制到16进制转换
http://jingyan.baidu.com/album/47a29f24292608c0142399cb.html?picindex=1

#python里面的byte类型，与字符串类型的转换
msg="我爱北京天安门"
print(msg)
print(msg.encode(encoding="utf-8"))#字符串编码称为二进制
print(msg.encode(encoding="utf-8").decode(encoding="utf-8")) #二进制解码成字符串

九、集合set(),是一个无序的，不重复的数据组合，
它的主要作用如下：
1、去重，把一个列表变成集合，就自动去重了
2、关系测试，测试两组数据之前的交集、差集、并集等关系
s = set([3, 5, 9, 10])  # 创建一个数值集合
t = set("Hello")  # 创建一个唯一字符的集合
a = t | s  # t 和 s的并集
b = t & s  # t 和 s的交集
c = t – s  # 求差集（项在t中，但不在s中）
d = t ^ s  # 对称差集（项在t或s中，但不会同时出现在二者中）

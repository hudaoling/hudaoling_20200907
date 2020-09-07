#语法： 变量（名）=input("提示语")
content=input("你吃了吗？")
print("我们收到用户反馈:"+content)

#让用户输入a,让用户输入b,计算机计算a+b的结果
a=input("请输入a:")#input接收到的内容是str
b=input("请输入b:")#input接收到的内容是str,如果要进行数字运算，必须先int转换
c=int(a)+int(b)
d=a+b
print(c,d) #c=a+b(输入的数字相加),d=a&b（输入的数字合并）
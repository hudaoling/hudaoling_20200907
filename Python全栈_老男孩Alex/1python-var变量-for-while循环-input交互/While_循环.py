# Author:Winnie Hu
#while循环条件成立时，执行程序
'''count= 0 #count是计数器，从0开始
while True:
    print("count:",count)
    count=count+1#count+=1
    if count==1000:
        break#当执行到1000时，就跳出，执行结束（不包含1000）'''

'''count=0
while True:
    print("count:",count)
    count+=1
    if count<10:print("0-10:",count)
    elif count<20:print("10-20:",count)
    else:break'''

#while True:为true时，可以不断循环执行,if else是单次循环
#本例中，用户输入错误时，可以继续输入用户名和密码
#while True 语句中一定要有结束该循环的break语句，否则会一直循环下去的。
d = {
'tenglan wu':'stu1101',
'longze luolan':'stu1102',
'yanfei luolan':'stu1103',
'mengfei luo':'stu1104',
}

'''while True:
    name = input('请输入您的用户名：')
    if name in d:
        break
    else:
        print('您输入的用户名不存在，请重新输入')
        continue #退出if这层循环，重新进入input循环
while True:
    password = input('请输入您的密码：')
    if d[name] == password:
        print('进入系统')
        break
    else:
        print('您输入的密码不正确，请重新输入')
        continue
   '''  #用户登陆提示

while True:
    name = input('请输入您的用户名：')
    if name in d:
        break
    else:
        print('您输入的用户名不存在，请重新输入')
        continue

count = 5
while count:
    password = input('请输入您的密码：')
    if d[name] == password:
        print('进入系统')
        break
    else:
        count -= 1
        print('您输入的密码不正确，还有{%s}次输入机会'%count)
        continue
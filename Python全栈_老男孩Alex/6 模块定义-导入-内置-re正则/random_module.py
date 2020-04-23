# Author:Winnie Hu

import  random
#random的作用是随机返回一个浮点数、整数、字符等

#随机浮点数
print(random.random())#0-1直接的随机浮点数
print(random.uniform(1,10))#指定区间随机浮点数

#取某范围的随机整数（两头都可取，例子可取1-5）
print(random.randint(1,5))

#在某范围随机取值（前开后闭，5不取，例子可取1-4）
print(random.randrange(1,5))

print(random.randrange(10,20,2))#按指定步长2来取值(取偶数)

print(random.choice('HELLO'))#在字符串中随机取一个
print(random.choice([1,2,3,4,5,'a','b']))#在一个列表中随机取一个
print(random.sample('HELLO',3))#在一个字符串中随机取三个
print(random.sample([1,2,3,4,5,'a','b'],4))#在一个列表中随机去四个


#列表随机打乱顺序
items=[1,2,3,4,5,6,7]
print('有序',items)
random.shuffle(items)
print('shuffle后',items)

#随机生成验证码的例子
checkcode=''
for i in range(5):
    current=random.randrange(0,5)
    if current == i:
        tmp=chr(random.randint(60,90))
    else:
        tmp=random.randint(0,9)
    checkcode+=str(tmp)
print(checkcode)
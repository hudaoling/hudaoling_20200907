# Author:Winnie Hu

#随机生成验证码的例子
import random
checkcode1=''
#方法一：只有数字
for i in range(4):
    current=random.randint(1,9)
    checkcode1+=str(current)
print(checkcode1)

#方法二：数字字母结合
checkcode=''
for i in range(4):#四位验证码
    #i循环时（比如是0）,current在0-4之间随机猜一个值，如果猜对了继续往下走
    current=random.randrange(0,4)
    # 字母（猜对了，就取一个字母）
    if current==i:
        tmp=chr(random.randint(65,90))
    # 数字（猜对了，就取一个字母）
    else:
        tmp=random.randint(0,9)
    checkcode+=str(tmp)#增加了一个随机的字母或数字
print(checkcode)#生成4位随机验证码
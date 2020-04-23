# Author:Winnie Hu

#if...elif...else 猜年龄的小程序，猜一次就结束了,不需要用break
age_of_oldboy=56
guess_age=int(input("guess age:"))#input默认读出结果是字符串
if guess_age==age_of_oldboy :
    print("yes,you got it.")
elif guess_age > age_of_oldboy :
    print("think smaller...")
else:
    print("think bigger!")

#while True...if...else循环,猜对年龄退出，未猜对一直执行
age_of_oldboy=56
while True:
  guess_age=int(input("guess age:"))
  if guess_age==age_of_oldboy :
     print("yes,you got it.")
     break  #猜对年龄时程序退出
  elif guess_age > age_of_oldboy :
     print("think smaller...")
  else:
     print("think bigger!")


#while True...if...else循环,猜3次退出，猜对年龄也退出。
age_of_oldboy=56
count=0
while True:
  if count==3:  #计数器等于3时，退出程序
    break
  guess_age=int(input("guess age:"))
  if guess_age==age_of_oldboy :
     print("yes,you got it.")
     break  #猜对年龄时程序退出
  elif guess_age > age_of_oldboy :
     print("think smaller...")
  else:
     print("think bigger!")
  count +=1

# while...if...else(省略了true)循环,猜3次退出，猜对年龄也退出。
#3次尝试出错的时候，提示您尝试多次登录失败，请退出
age_of_oldboy = 56
count = 0
while count < 3:#省略了true写法
 guess_age = int(input("guess age:"))
 if guess_age == age_of_oldboy:
    print("yes,you got it.")
    break  # 猜对年龄时程序退出
 elif guess_age > age_of_oldboy:
    print("think smaller...")
 else:
    print("think bigger!")
    count += 1
else: #当while条件不满足，则执行else条件
  print("you have tried too many...fuck off")


#for in...if...else 循环,猜3次退出，猜对年龄也退出。
#3次尝试出错的时候，提示您尝试多次登录失败，请退出
age_of_oldboy = 56
count = 0
for i in range(3):#i循环3次，所以下面条件可执行3次，既猜3次
 guess_age = int(input("guess age:"))
 if guess_age == age_of_oldboy:
    print("yes,you got it.")
    break  # 猜对年龄时程序退出
 elif guess_age > age_of_oldboy:
    print("think smaller...")
 else:
    print("think bigger!")
else: #当for循环正常走完时，执行else条件（如果break时就不执行）
  print("you have tried too many...fuck off")
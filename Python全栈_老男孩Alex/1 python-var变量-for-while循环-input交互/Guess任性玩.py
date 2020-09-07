# Author:Winnie Hu

# while...if...else(省略了true)循环,猜3次退出，猜对年龄也退出。
#3次尝试后询问用户是否继续猜测
age_of_oldboy = 56
count = 0
while count < 3:#省略了true写法
 guess_age = int(input("guess age:"))
 if guess_age == age_of_oldboy:
    print("yes,you got it.")
    break  # 猜对年龄时程序退出
 elif guess_age > age_of_oldboy:
    print("thi1nk smaller...")
 else:
    print("think bigger!")
    count += 1
    if count== 3: # 当用户猜了3次时，询问用户是否继续玩
      continue_confirm=input("do you want to keep guessing...?")
      if continue_confirm !='n': # 当用户不选择no时，count重新0开始计数
        count =0

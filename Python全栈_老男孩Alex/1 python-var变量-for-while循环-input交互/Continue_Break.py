# Author:Winnie Hu

#continue 跳出本次循环，进入下一次循环
#break 跳出并终止循环,一般用于结束程序
for i in range(0,10):
    if i<3:
      print("loop",i)
    else:
      continue #跳出本次循环，什么也不做，进入for循环
    print("hehe...")# 这个执行时机与print("loop",i)同时进行的

#嵌套循环（大小循环）
for i in range(0,10):
    print("big-------",i)
    for j in range(10):
       print("small",j)
       if j >5:
           break #结束循环


"""跳出本次循环，进入for循环，执行看结果能明白
for i in range(10):
    if i<5:
        continue #小于5时___退出循环，进入到for循环（继续打印i,从5开始） 
    print("loop",i)
"""

"""跳出并结束循环，直接退出程序
for i in range(10):
    if i<5:
        break
    print("loop",i)
"""

"""
#break和continue的实操练习
for i in range(250):
    if i < 50:
        continue #小于50时退出该条件，i继续for循环
    elif i<100: #当i在50-100之间循环时，打印'50~100'
        print('50~100')
        continue #打印完退出该条件，i继续for循环
    elif i < 200:#当i在100-200之间循环时，打印'100~200'
        print('100~200') #继续往下走print(i)也将执行
    else:
        break #上述条件都不满足，直接退出循环，推出程序
    print(i)
"""
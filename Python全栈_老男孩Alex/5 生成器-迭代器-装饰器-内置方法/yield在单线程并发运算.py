# Author:Winnie Hu

import time
def consumer(name):#
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield#yield是列表生成器，没有返回值（暂为空）
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
c=consumer("Ryan")#c变成了一个生成器
c.__next__()#只调用yield，不传值
baozi1="韭菜馅"
c.send(baozi1)#把包子发送给c，调用yield并给它传一个值baozi1="韭菜馅"
c.__next__()#next是调用yeild,不传值


#单线程下的并行效果，是异步IO的雏形
#yield生成器
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()#调用一下yield
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")

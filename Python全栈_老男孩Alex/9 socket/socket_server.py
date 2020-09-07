# 服务器端
import os,sys

import socket
server=socket.socket()
server.bind(('localhost',6969))#绑定监听端口
server.listen(1) #开始监听,设置大于1时需要实现异步

while True:
    conn, addr = server.accept()  # 等待状态
    while True:
        print("我要开始等电话了")

        #conn就是客户端连接过来再服务得为其生成的一个连接实例
        print(conn,addr)

        print("电话来了")
        sdata=conn.recv(1024) #接收数据
        if not sdata:#判断是否接收到数据
            print("client has lost...")
            break

        print("srecv:",sdata)
        res=os.popen(sdata.decode('utf-8')).read()  #接收命令参数，并调用os执行命令
        conn.send(res.encode()) #返回命令执行结果
        #服务端一次发送字节数有限，需要循环发送sendall

        # conn.send((sdata.upper()))


server.close()
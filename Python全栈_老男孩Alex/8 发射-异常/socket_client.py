
#客户端
import socket
client=socket.socket() #声明socket类型，同时生成socket连接对象

client.connect(('localhost',6969))#连接到服务器


while True:#实现不停的send
    msg=input(">>:").strip()
    if len(msg) ==0:continue  #如果是空时，请重新输入
    # client.send(b"hello world") #发送消息
    # client.send("我打瞌睡了a".encode("utf-8"))  #中文需要先编码成utf8
    client.send(msg.encode("utf-8"))  #中文需要先编码成utf8
    #消息不能send空，会卡住

    # cdata=client.recv(1024) #接收消息
    # zdata=client.recv(1024) #接收消息
    data=client.recv(1024)
    # print("recv:",cdata)
    # print("recv:",zdata.decode()) #解码成中文
    print("recv:",data.decode())



client.close() #关闭连接



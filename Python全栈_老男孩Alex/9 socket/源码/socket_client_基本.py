#客户端
import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',9999))

while True:
    msg = input(">>:").strip()
    client.send(msg.encode("utf-8"))  # 发送指令

    if len(msg) == 0:continue  #如果接收为空时，就断开连接
    data = client.recv(10240)

    print("recv:",data.decode())

client.close()
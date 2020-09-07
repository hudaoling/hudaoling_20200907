import  socket

def server():
    server = socket.socket()
    server.bind(('localhost',6969))
    server.listen(5)

    while True:
        client_conn,addr= server.accept()
        print(client_conn)
        print(addr)
        handle_request(client_conn)
        client_conn.close() #关闭客户端本地连接

def handle_request(client_conn):
    buf=client_conn.recv(1024)
    client_conn.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    client_conn.send(bytes("hello,Flora",encoding='utf-8'))

if __name__ == '__main__':
    server()

'''
服务器，开启app和监听端口,监听并响应客户端请求
'''

import  tornado.web
import  tornado.ioloop
import  tornado.httpserver
import  config

'''配置文件，包含了端口等所有参数'''

from  application import Application
'''应用程序包含了router配置'''


if __name__ == '__main__':

    app=Application()#创建了Application一个子类
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options['port'])
    httpServer.start(1)

    tornado.ioloop.IOLoop.current().start()



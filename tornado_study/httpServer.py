import  tornado.web

import  tornado.ioloop

'''引入httpserver模块'''
import  tornado.httpserver



class IndexHandler(tornado.web.RequestHandler):

    '''处理get请求，不能处理post请求'''
    def get(self):

        '''对应http的请求，给浏览器响应信息'''
        self.write('tornado is starting')

if __name__ == '__main__':

    app=tornado.web.Application([(r"/",IndexHandler)])

    #app.listen只能在单进程中使用
    # app.listen(8000) #相当于下面两条命令1.创建服务器2.开启监听

    '''实例化一个http服务器对象'''
    httpServer = tornado.httpserver.HTTPServer(app)


    '''一、单进程启动，http默认是单进程启动执行'''
    httpServer.listen(8000)


    ''' 二、多进程启动，但由于存在一些问题，不建议使用，建议手动启动多个进程并绑定不同端口'''
    '''1.每个子进程都会从父进程中赋值一份IOLoop的实例，如果在创建子进程修改了IOLoop会影响子进程
       2.所有的进程都是由一个命令启动的，无法在不停止服务的情况下修改代码
       3.所有进程共享一个端口，想要分别监控很困难
    '''
    httpServer.bind(8000)
    httpServer.start(5)
    #开启n个进程；不填时默认开启1；当填写None或-n负数时，开启cpu对应的核数


    tornado.ioloop.IOLoop.current().start()
    #执行py文件后，服务器启动起来



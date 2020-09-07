import  tornado.web
import  tornado.ioloop
import  config


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('8081:tornado is starting')

if __name__ == '__main__':


    #使用已定义的变量值
    print("list = ",config.options['list'])
    app=tornado.web.Application([(r"/",IndexHandler)])

    app.listen(config.options['port'])

    tornado.ioloop.IOLoop.current().start()


#带参数启动，需要在命令行中，带着参数执行py文件
'''python options_study.py --port=9000 --list=tor,my,she,you'''

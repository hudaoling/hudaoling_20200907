import  tornado.web
import  tornado.ioloop


'''options进行全局参数的定义、存储和转换'''
import  tornado.options
# from tornado.options import options,define

#一、基础方法define:定义参数
'''代码原型:tornado.options.define(name,default=None,type=None,help=None,metavar=None,multiple=False,group=None,callable=None)'''


#二、获取参数的方法,并转换命令行参数
'''tornado.options.parse_command_line()''' #从终端获取
'''tornado.option.parse_config_file(path)'''#从配置文件导入参数，txt配置文件，不建议使用
'''tornado.option.parse_config_file(path)'''#py配置文件，建议最终使用

#三、基础属性options，全局的options对象，所有定义的选项变量都会作为该对象的属性
'''tornado.options.options'''



#定义两个参数
tornado.options.define('port',default=8000,type=int)
tornado.options.define('list',default=[],type=str,multiple=True)

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('tornado is starting')

if __name__ == '__main__':

    #转换命令行参数，并保存到tornado.options.options里面

    tornado.options.options.logging=None #关闭日志

    # tornado.options.parse_command_line()
    tornado.options.parse_config_file('config_parse')

    #使用已定义的变量值
    print("list = ",tornado.options.options.list)
    app=tornado.web.Application([(r"/",IndexHandler)])

    app.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()


#带参数启动，需要在命令行中，带着参数执行py文件
'''python options_study.py --port=9000 --list=tor,my,she,you'''

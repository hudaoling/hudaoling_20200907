'''
创建ornado.web.Application子类
用于存放app类和router路由的
'''

import tornado.web
from  views  import  index
import config


class Application(tornado.web.Application):
    '''继承父类，创建一个子类'''
    def __init__(self):

        handlers=[
            (r'/',index.IndexHandler),
            (r'/sunck', index.SunckHandler,{"p1":"zhang","p2":"wang"}), #路由传参

            # '''反向解析,通过reverse_url将name跳转'''
            #'''如果使用name属性，不能用元组，必须使用tornado.web.url
            tornado.web.url(r'/kaige',index.KaigeHandler,{"p3":"zhao","p4":"sun"},name='kaigeviews'),

            #获取客户端请求中的uri
            # (r'/liuyifei/(\w+)/(\w+)/(\w+)', index.LiuyidfeiHandler),
            (r'/liuyifei/(?P<p1>\w+)/(?P<p3>\w+)/(?P<p2>\w+)', index.LiuyidfeiHandler),

            #获取客户端请求中的url的参数
            (r'/zhangmanyu', index.ZhangmanyuHandler),

            (r'/postfile',index.PostFileHandler),

            #request对象
            (r'/zhuyin', index.ZhuyinHandler),

            #上传文件
            (r'/upfile', index.UpFileHandler),


            #write方法
            (r'/write', index.WriteHandler),

            # write Json
            (r'/json', index.JsonHandler),

            # 状态码
            (r'/status', index.StatusHandler),

            # 重定向
            (r'/index', index.RedirectHandler),

            # 错误处理
            #iserror？flag=2
            (r'/iserror', index.ErrorHandler),

        ]


        super(Application,self).__init__(handlers,**config.settings)


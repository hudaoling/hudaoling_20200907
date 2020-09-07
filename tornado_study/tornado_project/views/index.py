'''
首页视图，网站的首页
除了首页视图，还可以创建网站的其他页面，例如购物车，我的页面等等
'''


'''tornado.web.RequestHandler
1、利用HTTP协议向服务器传递参数：
提取uri的特定部分； 
get,post方式传递参数

2、request对象(客户端请求)
method:get/post
host:主机ip或域名，端口
uri:请求的完整资源地址
path:请求的路径部分
query:请求参数部分
version:使用的HTTP版本
headers:请求的协议头
body:请求体数据
remote_ip:客户端的IP
files:用户上传的文件，字典类型

3、tonado.httputil.HTTPFile对象
是接收到的文件对象
filename：文件名称
body：文件的数据主体
conten_type：文件的类型'''


from tornado.web import RequestHandler
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#添加环境变量：index目录上级的上级目录，tornado_project，否则config导入失败
import config
import json



class IndexHandler(RequestHandler):

    '''处理get请求，不能处理post请求'''
    def get(self,*args,**kwargs):
        '''对应http的请求，给浏览器响应信息'''
        url = self.reverse_url("kaigeviews")  #实现网页转换，通过name值跳转
        self.write("<a href='%s'>去另一个页面</a>"%(url))  #调转到其他页面设置


class SunckHandler(RequestHandler):
    def initialize(self,p1,p2):
        '''初始化路由传入的参数（并非用户传入的参数）'''
        self.p1=p1
        self.p2=p2

    def get(self,*args,**kwargs):
        print(self.p1,self.p2)
        self.write('he is a nice man')

# 网页跳转
class KaigeHandler(RequestHandler):
    def initialize(self, p3, p4):
        '''初始化路由传入的参数（并非用户传入的参数）'''
        self.p3 = p3
        self.p4 = p4

    def get(self,*args,**kwargs):
        print(self.p3,self.p4)
        self.write('kaige is a teacher')



# 获取客户端get请求中的特定uri
# '''http://127.0.0.1:8081/liuyifei/goog/nice/handsom'''
class LiuyidfeiHandler(RequestHandler):
    def get(self, p1,p2,p3,*args, **kwargs):
        print(p1,p2,p3)
        self.write('liuyifei is a beautiful')


# 获取客户端get请求中的参数值
# '''http://127.0.0.1:8081/zhangmanyu?a=1&b=2&c=3&d=2&d=8'''

class ZhangmanyuHandler(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument('a')
        b = self.get_query_argument('b')
        c = self.get_query_argument('c')

        # get_query_arguments，接收多个参数，返回的是一个列表
        d = self.get_query_arguments('d')

        print(a,'-',b,'-',c,'-',d)

        self.write('Zhangmanyu is a beautiful')



# post请求
class PostFileHandler(RequestHandler):

    #获取页面
    def get(self,*args, **kwargs):
        self.render("postfile.html")

    #获取post传入的参数
    def post(self,*args, **kwargs):
        name = self.get_body_argument("username")
        passwd =self.get_body_argument("passwd")

        # get_body_arguments，接收多个参数，返回的是一个列表
        hobbyList =self.get_body_arguments("hobby")
        print(name,passwd,hobbyList)

        self.write('%s likes %s'%(name,hobbyList))

        #可以获取get，也可以获取post请求参数,一般不建议使用
        # self.get_argument()
        # self.get_arguments()


# requet对象
# http://127.0.0.1:8081/zhuyin?a=1&b=2
class ZhuyinHandler(RequestHandler):
    def get(self,*args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)

        self.write('zhuyin is a beautiful')


#接收文件对象request.files
class UpFileHandler(RequestHandler):
    def get(self,*args, **kwargs):
        self.render('upfile.html')

    #接收上传的文件，所有文件用字典接收
    '''{'file': [{'filename': 'b.txt', 'body': b'\xe4\xbd\xa0\xe6\xb5\x8bgood', 'content_type': 'text/plain'},
              {'filename': 't1.txt', 'body':'terefdgdfhfgh'}'''

    def post(self, *args, **kwargs):
        filesdict=self.request.files
        print(filesdict)
        for inputname in filesdict:
            filearr=filesdict[inputname]
            for  fileObj in filearr:
                filepath=os.path.join(config.BASE_DIRS,'upfile/'+fileObj.filename)
                with open(filepath,'wb') as f:
                    f.write(fileObj.body)

        self.write('ok')


'''响应输出response
selt.write(chunk)将数据写到<输出缓冲区>
利用write方法写json数据
'''

class WriteHandler(RequestHandler):
    def get(self,*args, **kwargs):
        self.write("sunck is a good man")
        self.write("sunck is a good woman")
        self.write("sunck is a handsome man")

        self.finish() #刷新缓冲区,关闭档次请求通道

#json
class JsonHandler(RequestHandler):
    def get(self,*args, **kwargs):

        per={"name":"feng",
             "age":18,
             "height":175,
             "weight":70,
             }

        # jsonStr=json.dumps(per) # 将字典转换成json
        # self.write(jsonStr)     # 转json再写，content_type识别为text/html

        '''set_header:手动设置一个名为name，值为value的响应头,name:字段名称value：值'''
        self.set_header("Content-Type","application/json:charset=UTF-8")
        self.set_header("sunck","good")

        self.write(per)#write自动序列化方式,content_type属性为application/json



# '''set_default_header:在进入http响应之前调用，预先设置好通用默认的请求头'''
class DefaultHeaderHandler(RequestHandler):
    def set_default_headers(self, *args, **kwargs):
        self.set_header("Content-Type","application/json:charset=UTF-8")


# 为响应设置状态码:self.set_status(status_code,reason=None)
class StatusHandler(RequestHandler):
    def get(self,*args, **kwargs):
        code=999
        mes="i dont want go on"
        self.set_status(code,mes)
        self.write("%s-%s"%(code,mes))




# 重定向到url网址 self.redirect(url)
class RedirectHandler(RequestHandler):
    def get(self,*args, **kwargs):
        self.redirect("/")



# 抛出http错误状态，默认为500，抛出错误后tornado会调用write_error()方法进行处理
# self.send_error(status_code=500,**kwargs)，
# 用来处理send_error抛出的错误信息，并返回浏览器错误界面
# write_error(status_code,**kwargs)
class ErrorHandler(RequestHandler):
    def write_error(self, status_code: int, **kwargs):
        if status_code ==500:
            self.write("服务器内部错误")
        elif status_code == 404:
            self.write("资源不存在")
        else:
            self.write("我也不知道")
        self.set_status(status_code)

    def get(self,*args, **kwargs):

        flag=self.get_query_argument("flag")
        if flag == '0':
            self.send_error(500) #send_error

        self.write("you are right")




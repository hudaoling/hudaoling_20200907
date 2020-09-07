'''用户设置服务器的参数和配置信息'''

import os,sys
BASE_DIRS=os.path.dirname(__file__)
'''该文件所在目录'''

sys.path.append(os.path.dirname(__file__)) #添加环境变量
# print(sys.path)

#参数
options={'port':8081,
         'list':['good','nice','haha']}



#配置
settings={
    # '''设置静态文件目录'''
    "static_path":os.path.join(BASE_DIRS,"static"),

    # '''设置模板文件目录'''
    "template_path": os.path.join(BASE_DIRS, "templates"),

    "debug": True,

}

'''
debug:设置tornado是否工作在调试模式下，默认False即工作在生产环境下，autoreload=True也可设置自动重启
debug：True时的特性:
1、自动重启：监控代码变更后会自动启动，如果代码有错误需手动重启
2、取消缓存编译的模板(compiles_template_cache=False可单独设置）
3、取消缓存静态文件的hash值（static_hase_cache=False单独设置），
4、提供追踪信息，不常用（serve_traceback=True单独设置）'''


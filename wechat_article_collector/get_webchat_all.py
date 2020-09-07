# -*- coding: utf-8 -*-
import requests
import datetime,time,random,re
import json
import  pandas as pd
from bs4 import BeautifulSoup
from queue import Queue       #线程
from threading import Thread  #线程
from pyquery import PyQuery as pq


from CommonTool.API_Webchat_Login import Webchat_Login   #自定义模块，实现微信扫码自动登录（扫码是无法跳过的）
from CommonTool.API_Get_Ip import GetIp,Get_zhima        #自定义模块，实现代理IP的获取
from CommonTool.API_MongoDB import MongoAPI              #自定义模块，实现本地mongodb的增删改等
from CommonTool.API_Citys import get_citys               #自定义模块，爬取全国省市县区




"""
需要提交的data
以下个别字段是否一定需要还未验证。
注意修改yourtoken,number
number表示从第number页开始爬取，为5的倍数，从0开始。如0、5、10……
token可以使用Chrome自带的工具进行获取
fakeid是公众号独一无二的一个id，等同于后面的__biz
"""

# AS：联想网盘、亿方云;AB：英方、鼎甲、Veritas;AR：日志易、Splunk
# MjM5Mzg1MDk2Ng==	亿方云订阅号		hzyifangyun  历史消息是否需要爬取？

#所有公众号抓取（手工过滤掉不需要的），通常用于增量爬取：
gzh_str_all="""
fakeid	            nickname		alias
MjM5NjU1OTYyMA==	爱数		AISHUchina
MzUxMDU5NjQ3Mg==	联想Filez		Lenovo-Filez
MzI4NDQ2NjM5Ng==	亿方云		hzfangcloud
MzA5MjM5MDgzOA==	英方云		i2soft
MjM5OTEzNTUzOA==	英方软件		info2soft
MzIwMDUxOTExMA==	鼎甲		SCUTECH-DJ
MzA4MjUyMTQ0NA==	VERITAS中文社区		VERITAS_CHINA
MjM5MDQxNjMxMA==	日志易		rizhiyi
MzI5MDQ5ODAxMQ==	Splunk大数据		Splunk-China




"""

#指定公众号爬取，通常用于首次大批量
gzh_str="""
MzI2NDk5NzA0Mw==	36氪		wow36kr
MzI2NDk5NzA0Mw==	36氪		wow36kr   1453-200
MjM5ODI5Njc2MA==	51CTO技术栈		blog51cto
MzA3MzI4MjgzMw==	机器之心		almosthuman2014 444
MTQzMjE1NjQwMQ==	虎嗅网		huxiu_com   1353
MzU0MDY1MTQwNA==	数据观		cbdioreview   390
"""

def str_to_dict(gzh_str):
    '''
    将a_str形式的字符串转化为字典形式；
    :param a_str:
    :return:
    '''
    str_a =list( i for i in gzh_str.split('\n') if i !='' )
    str_b ={}
    for a in str_a:
        if 'fakeid' not in a:

            a1 = a.split('\t')[0]
            a2 =a.split('\t')[1]
            a3 = a.split('\t')[3]
            str_b[a3] = a1
    print(str_b)

    return str_b



#调用get_search函数，公众号的查询关键参数fakeid
def get_search(keys):
    '''keys是你需要爬取的公众号关键字，选取和关键字匹配的前5个公众号'''

    search_list = []
    for key in keys:
        data_search = {
            "action": "search_biz",
            "begin": 0,
            "count": "5", #获取关键字查找对应的公众号数量
            "query": key,
            "token": token,
            "lang": "zh_CN",
            "f": "json",
            "ajax": "1",}

        url_search='https://mp.weixin.qq.com/cgi-bin/searchbiz?'

        search_json = requests.get(url_search, timeout=30,headers=headers, params=data_search).json()
        time.sleep(random.randint(1, 3) + random.random())  # 勤劳的小蜜，休息一会吧，省的微信把你kill了

        # print(search_json)

        for item in  search_json["list"]:
            search_dic={}
            search_dic['fakeid'] = item['fakeid']
            search_dic['nickname'] = item['nickname']
            search_dic['alias'] = item['alias']
            search_list.append(search_dic)
            # print('search_list',search_list)
    return search_list



#获取文章title,url，date等
def get_articles(gzh_list,start_num):
    '''gzh_list:是获得公众号名单和查询关键字，strat_num是需要爬取的页数，一页显示5条; '''
    id = 1
    article_list = []

    for gzh,fakeid in gzh_list.items():

        for num in range(start_num):

            data = {
                "action": "list_ex",
                "begin": num*5,
                "count": "5",
                "fakeid": fakeid,
                "query": "",
                "type": "9",
                "token": token,
                "lang": "zh_CN",
                "f": "json",
                "ajax": "1",}

            # 使用get方法进行提交，返回了一个json，里面是每一页的数据
            url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
            content_json = requests.get(url, timeout=15, headers=headers,params=data,proxies=None).json()
            print(content_json)
            time.sleep(random.randint(1, 3) + random.random())#亲，休息会吧


            #从json中读取文件
            for item in content_json["app_msg_list"]:
                id +=1
                article_dict={}
                # 提取每页文章的标题及对应的url
                article_dict['id'] = fakeid +'_' + str(num)+'_'+ str(id) #添加文章编号
                article_dict['title'] = item['title']
                article_dict['digest'] = item['digest']
                article_dict['date'] = item['create_time']

                tims_zone = item['create_time']
                article_dict['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(tims_zone)))

                article_dict['from_gzh']=gzh
                article_dict['link'] = item['link']

                # 调用run方法启用15个线程执行，主要执行：get_article_content请求每篇文章网页获得文章正文内容
                # article_dic['content'] = run(item['link'],proxies)
                try:
                    article_dict['content'] = get_article_content(item['link'])
                    failed_list=None
                except Exception as e:
                    failed_list=[]
                    failed_list.append(item['link'])
                    print ("{} is failed".format(item['link'])) #解析失败的网页
                    print (e)
                    continue

                # 调用API_MongoDB,写入mongodb(如果title内容存在则不写入)
                webchat_table.insert_check(article_dict,'title')
                print('article_dic', article_dict)

                article_list.append(article_dict)

    return  article_list


def run(link,proxies):
    ''' 负责开启多线程任务，并行爬取link。'''
    start = time.time()
    # 实例化一个队列对象
    link_q = Queue()
    print('start get content...')
    # thread_list 列表保存线程
    thread_list = []
    # 把爬下来的代理地址逐个放进队列
    link_q.put(link)
    # 开启15个线程并放入thread_list
    # 最后往队列放入数量与线程一样的数字0，作为每个线程结束的标记
    for _ in range(15):
        thread_list.append(Thread(target=get_article_content, args=(link_q,proxies))) #调用get_article_content
        link_q.put(0)
    for w in thread_list:
        # 启动线程
        w.start()
    for w in thread_list:
        # 等待线程终止
        w.join()
    print('[verification] total time: %.2f s' % (time.time() - start))
    print('get content finished !')


def get_article_content(link_q):

    # proxies = random.choice(proxy_list)
    doc = pq(link_q)
    article_content= doc('.rich_media_content').text()  # 获取文章的正文内容

    time.sleep(random.randint(1,2) + random.random())  # 亲，休息会吧

    return article_content

if __name__ == '__main__':


    #1.实例化
    webchat_login = Webchat_Login()

    #1.微信公众号自动登录，获得cookie, token
    cookie, token = webchat_login.weixin_login()


    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        ]

    headers = { "User-Agent": random.choice(user_agent_list),
        'Connection': 'keep-alive',
        'Host': 'mp.weixin.qq.com',
        'Cookie': cookie
         }

    # 调用get_search函数，公众号的查询关键参数fakeid，一次性获得即可（后期不变）
    # keys = ['爱数', '联想网盘', '亿方云', '英方云', '鼎甲', 'Veritas', '日志易', 'Splunk']
    # fakeid_list = get_search(keys)
    # fakeid_list_df = pd.DataFrame(fakeid_list, columns=fakeid_list[0].keys())  # 表转换成df
    # fakeid_list_df.to_excel('html/fakeid_list.xlsx', encoding='utf-8', )  # 将df写入excel

    # 创建MongoDB连接，并调用增删改查等方法
    webchat_table = MongoAPI("localhost", 27017, "webchat_spider", "webchat_table")  # 其中有一个webchat_t1测试表 "webchat_table"


    # 取得公众号和对应查询关键参数fakeid
    gzh_list = str_to_dict(gzh_str_all)

    # 爬取西刺网址的代理IP并验证可用性
    # Ip_class = GetIp('http://www.hiyd.com/dongzuo/')  # 实例化
    # Ip_class.run()  # 调用run
    # proxy_list = Ip_class.success_list


    # 爬取芝麻代理IP（收费，每天20个免费测试用）
    # url_zhima='http://http.tiqu.alicdns.com/getip3?num=20&type=1&pro=&city=0&yys=0&port=11&pack=97959&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'
    # zhima = Get_zhima(url_zhima)
    # zhima.get_zhima_ip()
    # proxy_list = zhima.proxy_list


    # 取得公众号文章title,url,date等
    # 数字代表你需要爬取的页码数，每天增量爬取仅需第一页即可，如果需要全量爬取建议只选一个公众号并指定页码数（因为公众号爬取超过1000条会暂时封cookie）
    # 本文中增加了线程，但实际用不上，数据量很小；IP代理也用不上
    article_list = get_articles(gzh_list,1)

    # print(article_list)




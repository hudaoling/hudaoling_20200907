import requests
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
import  numpy as np
import json,re,math,random
import time,datetime

from pyquery import PyQuery as pq
import urllib3
urllib3.disable_warnings()



from CommonTool.API_Webchat_Login import Webchat_Login   #自定义模块，实现微信扫码自动登录（扫码是无法跳过的）
from CommonTool.API_Get_Ip import GetIp,Get_zhima        #自定义模块，实现代理IP的获取
from CommonTool.API_MongoDB import MongoAPI              #自定义模块，实现本地mongodb的增删改等
from CommonTool.API_Citys import get_citys               #自定义模块，爬取全国省市县区


pd.set_option('display.width',5000)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',2000)



def status_code(response):
    # 判断网页返回的状态码是否正常
    # 如果状态码是200说明可以正常访问
    if response.status_code == 200:
        print(response,':is ok')
    # 如果状态码是302，则说明IP已经被封
    if response.status_code == 302:
        print(response,':ip is invalid')
    if response.status_code == 403:
        print(response, ':ip is Forbidden')


def get_details(soup,key,page):
    # -----------解析并读取文档及内容列表-----------

    article_root = 'https://weixin.sogou.com'
    titles_all = soup.select('div[class="txt-box"]')  # 取出文章所有标签

    for title in titles_all:
        article_dict = {}
        article_dict['title'] = title.select_one('h3 a').get_text()
        tims_zone = title.select_one('div[class="s-p"]').get('t')
        article_dict['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(tims_zone)))
        article_dict['from_gzh'] = title.select_one('ul div[class="s-p"]').get_text()
        article_dict['sumary'] = title.select_one('p').get_text()
        article_dict['key_word'] = key

        article_link_temp= article_root + title.select_one('h3 a').get('href') #临时链接
        article_dict['article_link_temp'] = article_link_temp
        article_dict['page'] = page

        article_list.append(article_dict)
        print(article_dict)
        sougou_webchat.insert(article_dict) # 写入mongodb,如果存在则不写入

    return article_list




# 第一步：获得文章标题、公众号和临时链接
def get_pages(url):

    key_response = requests.get(url, timeout=20,headers=headers,proxies=None)

    if key_response.status_code == 200:
        page1_data = key_response.content.decode('utf-8')
        # with open('html/html/{}—1—{}.html'.format(key,int(time.time())), 'w', encoding='utf8') as f:
        #     f.write(page1_data)
        print(page1_data)

        page1_soup = BeautifulSoup(page1_data, 'lxml') #转换成lxml,可以用bs4解析
        #-----------取出搜索结果的总文章数article_num，再用article_num/10=页码数（无法直接获取uuuu最大页码数）-----------
        string=page1_soup.select_one('div[class="mun"]').get_text()
        pattern = re.compile(r'(?<=找到约)\d+\.?\d*')
        article_num= pattern.findall(string.replace(",",""))
        pages = math.ceil(int(article_num[0]) / 10) #向上取整
        print('pages',pages)

        time.sleep(random.randint(0, 2) + random.random())
    else:
        print(key_response.status_code)
        pages=0

    return  pages



def get_article(key_list):
    # 公众号关键字循环输入查询
    url = 'https://weixin.sogou.com/weixin?query={}&_sug_type_=&sut=4469&lkt=4%2C1587712814825%2C1587712818025&s_from=input&_sug_=y&type=2&sst0=1587712818128&page={}&ie=utf8&w=01019900&dr=1'

    for key in key_list:
        # pages=get_pages(url.format(key,1))  #获得页码数

        proxies = random.choice(proxy_list)
        # -----------取出1-pages所有页面的文章列表-----------
        for page in range(3):

            page_link='https://weixin.sogou.com/weixin?query={}&_sug_type_=&sut=4469&lkt=4%2C1587712814825%2C1587712818025&s_from=input&_sug_=y&type=2&sst0=1587712818128&page={}&ie=utf8&w=01019900&dr=1'

            page_response = requests.get(page_link.format(key, page + 1), timeout=15, headers=headers,proxies=proxies)  # 发送请求

            if page_response.status_code == 200:
                page_data= page_response.content.decode('utf-8') #读取请求文件
                print(page_data)
                soup = BeautifulSoup(page_data, 'lxml')  # 转换成lxml,可以用bs4解析
                img=soup.select_one('img[id="seccodeImage"]').get('src')

                get_details(page_data,key,page) #调用get_details函数

            else:
                print(page_response.status_code)
            time.sleep(random.randint(2,3) + random.random())



# 第二步：根据临时链接，发送网络请求，解析并取得真实得链接
def get_true_link(link):

    response_temp = requests.get(link.strip(), timeout=20, headers=headers, proxies=None)
    data_temp = response_temp.content.decode('utf-8')  # 读取请求文件
    with open('html/html/{}_temp{}.html'.format(key,int(time.time())), 'w', encoding='utf8') as f:
        f.write(data_temp)
    url_temp = re.findall('url ' + '(.+?);', data_temp.replace("+", "").replace("= ", ""))
    article_link = ''.join(url_temp).replace("'", "").replace(" ", "")  # 解析出固定网址(跳转后正确网址)
    print('article_link:',article_link)


    time.sleep(random.randint(1,2)+random.random())
    return article_link




# 第三步：根据真实网址，获得文章具体内容，分开三步操作是避免IP被屏蔽（否则会很惨）------------
def get_article_content(link):
    doc = pq(link)
    article_content = doc('.rich_media_content').text()  # 获取文章的正文内容
    time.sleep(random.randint(0,2)+random.random())

    return article_content



if __name__ == '__main__':

    # -----------创建爬虫代理-----------
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    ]

    headers = {"User-Agent": random.choice(user_agent_list),
               "Host": "weixin.sogou.com",
               "Connection": "keep-alive",
               'Cookie': 'ABTEST=0|1587519318|v1; IPLOC=CN3100; SUID=67FA9DB44018960A000000005E9F9F56; SUID=67FA9DB41810990A000000005EA15F83; weixinIndexVisited=1; SUV=00A1E9BBB49DFA675EA15F85C62A5538; ld=Hlllllllll2WooJWlllllVfuktylllllHJTfBZllll9lllllpZlll5@@@@@@@@@@; LCLKINT=6657; LSTMV=323%2C29; CXID=12FA0425CC94B8FE1AB2CB1058E78D7B; SNUID=738D67433137975A32BBAE7932520630; JSESSIONID=aaaMawyFvkXLb-y7yhSgx; ppinf=5|1589254500|1590464100|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklODElOTMlRTklODElOTN8Y3J0OjEwOjE1ODkyNTQ1MDB8cmVmbmljazoxODolRTklODElOTMlRTklODElOTN8dXNlcmlkOjQ0Om85dDJsdUZHMmg2QXA3UFoyNm92WWhENnBiSW9Ad2VpeGluLnNvaHUuY29tfA; pprdig=PijBdXyzKUjmK3CrCUxRAbEe4VyM9f8MbFlwqQEze77JZ3bP9FSLZUAFharb3kTnvGBqPkzrQm5ld1MGDe9cf9tuZzoq48oo7t7H2jCYwWyjyxOHDRGXgYhErIFTr5_-TPwr6-zc5-uu8J9d8vSYQq1l9yOtb_rbyeOCnKXnp1E; sgid=14-47630777-AV66GWSAXU84icFtC3MlGMu4; ppmdig=15892545000000004bb0803ee8d8d25bc0aecc9f552f11f5; sct=3'

               }


    # 爬取西刺网址的代理IP并验证可用性
    # Ip_class = GetIp('http://www.hiyd.com/dongzuo/')  # 实例化
    # Ip_class.run()  # 调用run
    # proxy_list = Ip_class.success_list
    # proxy_list=[None,None]

    # 爬取芝麻免费测试的IP
    url_zhima='http://http.tiqu.alicdns.com/getip3?num=20&type=1&pro=&city=0&yys=0&port=11&pack=97959&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'

    zhima = Get_zhima(url_zhima)
    zhima.get_zhima_ip()
    proxy_list=zhima.proxy_list

    # 创建MongoDB连接，并调用增删改方法
    sougou_webchat = MongoAPI("localhost", 27017, "webchat_spider", "soug_webchat_list")  # 其中有一个webchat_t1测试表

    key_list = ['splunk']  # AS：联想网盘、亿方云;AB：英方、鼎甲、Veritas;AR：日志易、Splunk

    #一、获取文章清单和临时链接并写入mongodb
    article_list = []
    key = key_list[0]

    get_article(key_list)
    # artile_list_df=pd.DataFrame(article_list,columns=article_list[0].keys())  #将文章列  表转换成df
    # artile_list_df.to_excel('html/{}_article_list.xlsx'.format(key), encoding='utf-8', )#将df写入excel


    # 二、根据临时链接获得正式链接，并解析文档正文内容
    # a_list = sougou_webchat.find({}) #从mongodb读取临时链接
    #
    # for article in a_list:
    #     link=article(['article_link_temp'])
    #     _id=article(['_id'])
    #     article['article_link']=get_true_link(link) #调用get_true_link
    #     article['article_content']=get_article_content(link)#调用get_article_content
    #
    #     sougou_webchat.update({"_id": _id},article)  #更新mongodb里面的文章信息


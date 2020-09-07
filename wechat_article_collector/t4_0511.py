import requests
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
import  numpy as np
import json,re,math,random
import time,datetime
import image

from pyquery import PyQuery as pq
import urllib3
urllib3.disable_warnings()
import wechatsogou


#get_ip是自定义py文件，目前是爬取西刺免费代理，验证并返回可用的代理IP
from API_Get_Ip import GetIp,Get_zhima
from API_MongoDB import MongoAPI  #自定义模块


pd.set_option('display.width',5000)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',2000)

# -----------创建爬虫代理-----------
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
]



headers = {"User-Agent":random.choice(user_agent_list),
          "Host": "weixin.sogou.com",
          "Connection": "keep-alive",
          # 'Cookie':'ABTEST=0|1587519318|v1; IPLOC=CN3100; SUID=67FA9DB44018960A000000005E9F9F56; SUID=67FA9DB41810990A000000005EA15F83; weixinIndexVisited=1; SUV=00A1E9BBB49DFA675EA15F85C62A5538; ld=Hlllllllll2WooJWlllllVfuktylllllHJTfBZllll9lllllpZlll5@@@@@@@@@@; LCLKINT=6657; LSTMV=323%2C29; ppinf=5|1588040686|1589250286|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklODElOTMlRTklODElOTN8Y3J0OjEwOjE1ODgwNDA2ODZ8cmVmbmljazoxODolRTklODElOTMlRTklODElOTN8dXNlcmlkOjQ0Om85dDJsdUZHMmg2QXA3UFoyNm92WWhENnBiSW9Ad2VpeGluLnNvaHUuY29tfA; pprdig=vNOPN41I3Uol9lmpTbDN3SiD6xjx50S5XrjfbUJrxWllHnYp-WAt6ikP97_TQmp9sG2oEhyYpt9uvKZmyFoA7rJoUP13JmRJwrdcuRslD8F1otqyGLHTdPVFpVGukMxb9qt5727FwoIrg1v-r1nj2Jl45A0_J3DGpO5d813Lg4c; sgid=14-47630777-AV6nkib5IlHic5v6Zs37wbkib0; CXID=12FA0425CC94B8FE1AB2CB1058E78D7B; SNUID=D32DC7E2919534C5FCF2B6AF9107EA3C; ppmdig=15891611920000002843c4a31870434845813c5f9cbaeb28; JSESSIONID=aaaCARK2ZuRs5_kPA2Rgx; sct=53',
'Cookie':'BTEST=0|1587519318|v1; IPLOC=CN3100; SUID=67FA9DB44018960A000000005E9F9F56; SUID=67FA9DB41810990A000000005EA15F83; weixinIndexVisited=1; SUV=00A1E9BBB49DFA675EA15F85C62A5538; ld=Hlllllllll2WooJWlllllVfuktylllllHJTfBZllll9lllllpZlll5@@@@@@@@@@; LCLKINT=6657; LSTMV=323%2C29; CXID=12FA0425CC94B8FE1AB2CB1058E78D7B; SNUID=738D67433137975A32BBAE7932520630; JSESSIONID=aaaMawyFvkXLb-y7yhSgx; ppinf=5|1589254500|1590464100|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklODElOTMlRTklODElOTN8Y3J0OjEwOjE1ODkyNTQ1MDB8cmVmbmljazoxODolRTklODElOTMlRTklODElOTN8dXNlcmlkOjQ0Om85dDJsdUZHMmg2QXA3UFoyNm92WWhENnBiSW9Ad2VpeGluLnNvaHUuY29tfA; pprdig=PijBdXyzKUjmK3CrCUxRAbEe4VyM9f8MbFlwqQEze77JZ3bP9FSLZUAFharb3kTnvGBqPkzrQm5ld1MGDe9cf9tuZzoq48oo7t7H2jCYwWyjyxOHDRGXgYhErIFTr5_-TPwr6-zc5-uu8J9d8vSYQq1l9yOtb_rbyeOCnKXnp1E; sgid=14-47630777-AV66GWSAXU84icFtC3MlGMu4; ppmdig=15892545000000004bb0803ee8d8d25bc0aecc9f552f11f5; sct=3'
}



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


# 第一步：获得文章标题、公众号和临时链接
def get_pages(url):

    def page():
        page1_data = key_response.content.decode('utf-8')
        page1_soup = BeautifulSoup(page1_data, 'lxml')  # 转换成lxml,可以用bs4解析
        print(page1_data)
        # -----------取出搜索结果的总文章数article_num，再用article_num/10=页码数（无法直接获取uuuu最大页码数）-----------
        string = page1_soup.select_one('div[class="mun"]').get_text()
        pattern = re.compile(r'(?<=找到约)\d+\.?\d*')
        article_num = pattern.findall(string.replace(",", ""))
        pages = math.ceil(int(article_num[0]) / 10)  # 向上取整
        time.sleep(random.randint(1, 2) + random.random())
        return  pages

    # 先从第一页取出每个公众号搜索结果的页码数
    proxies = random.choice(proxy_list)

    key_response = requests.get(url, timeout=20,headers=headers,proxies=proxies)

    if key_response.status_code==200:
        pages=page()
    else:
        proxies = random.choice(proxy_list)
        key_response = requests.get(url, timeout=20,headers=headers,proxies=proxies)
        pages=page()


    return  pages

# 根据临时链接，发送网络请求，解析并取得真实得链接
def get_true_link(article_link_temp):
    # ---------- 临时网址,发起临时链接，为了获得固定网址------------

    proxies = random.choice(proxy_list)

    try :
        response_temp = requests.get(article_link_temp.strip(), timeout=20, headers=headers, proxies=proxies)
    except Exception:
        proxies = random.choice(proxy_list)
        response_temp = requests.get(article_link_temp.strip(), timeout=20, headers=headers, proxies=proxies)

    data_temp = response_temp.content.decode('utf-8')  # 读取请求文件
    # with open('html/html/temp{}.html'.format(int(time.time())), 'w', encoding='utf8') as f:
    #     f.write(data_temp)
    url_temp = re.findall('url ' + '(.+?);', data_temp.replace("+", "").replace("= ", ""))
    article_link = ''.join(url_temp).replace("'", "").replace(" ", "")  # 解析出固定网址(跳转后正确网址)
    # print('i am herer')
    print('article_link:',article_link)

    time.sleep(random.randint(1,2)+random.random())

    return article_link


# -----------解析正确链接并读取文档及内容列表-----------
def get_details(soup,key, article_list):
    # soup = BeautifulSoup(data, 'lxml')  # 转换成lxml,可以用bs4解析
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

        article_link_temp= article_root + title.select_one('h3 a').get('href') #解析临时链接
        article_dict['article_link_temp'] = article_link_temp

        article_link = get_true_link(article_link_temp) #调用get_true_link获得真实link
        article_dict['article_link']=article_link
        try:
            doc = pq(article_link)  #pq是否会被屏蔽？
        except:
            print('dq failed')
            continue
        article_dict['article_content'] = doc('.rich_media_content').text()  # 获取文章的正文内容
        print(doc('.rich_media_content').text())

        sougou_webchat.insert_check([article_dict],{'title':article_dict['title']})  # 写入mongodb,如果存在则不写入
        article_list.append(article_dict)

        time.sleep(random.randint(1, 2) + random.random())#休息一会，别太频繁





def get_article(key_list):

    # 公众号关键字循环输入查询
    url = 'https://weixin.sogou.com/weixin?query={}&_sug_type_=&sut=4469&lkt=4%2C1587712814825%2C1587712818025&s_from=input&_sug_=y&type=2&sst0=1587712818128&page={}&ie=utf8&w=01019900&dr=1'
    article_list = []

    for key in key_list:
        print(key)
        pages=get_pages(url.format(key,1))

    # -----------取出1-pages所有页面的文章列表-----------
        proxies = random.choice(proxy_list)
        for page in range(pages):
            page_link='https://weixin.sogou.com/weixin?query={}&_sug_type_=&sut=4469&lkt=4%2C1587712814825%2C1587712818025&s_from=input&_sug_=y&type=2&sst0=1587712818128&page={}&ie=utf8&w=01019900&dr=1'
            print(page_link.format(key, page))
            page_response = requests.get(page_link.format(key, page + 1), timeout=15, headers=headers,proxies=None)  # 发送请求


            if page_response.status_code == 200:
                page_data = page_response.content.decode('utf-8')  # 读取请求文件
                soup = BeautifulSoup(page_data, 'lxml')  # 转换成lxml,可以用bs4解析

                if soup.select_one('p[class="p3"]').get_text()=="验证码：":
                    print("failed:need verify code")
                else:
                    pass


            else:
                # proxies = random.choice(proxy_list) #不返回200时，说明IP存在问题，需要更换IP
                page_response = requests.get(page_link.format(key, page + 1), timeout=15, headers=headers,proxies=None)  # 发送请求
                page_data = page_response.content.decode('utf-8')  # 读取请求文件
                soup = BeautifulSoup(page_data, 'lxml')  # 转换成lxml,可以用bs4解析

                if soup.select_one('p[class="p3"]').get_text()=="验证码：":
                    print("failed:need verify code")
                else:
                    pass



            time.sleep(random.randint(1, 2) + random.random())

            #调用解析文章具体信息函数
            # get_details(soup, key,article_list)



    return article_list




if __name__ == '__main__':

    # 爬取西刺网址的代理IP并验证可用性
    # Ip_class = GetIp('http://www.hiyd.com/dongzuo/')  # 实例化
    # Ip_class.run()  # 调用run
    # proxy_list = Ip_class.success_list

    # 爬取芝麻免费测试的IP
    # url_zhima='http://http.tiqu.alicdns.com/getip3?num=190&type=1&pro=&city=0&yys=0&port=1&pack=97654&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'
    # zhima = Get_zhima(url_zhima)
    # zhima.get_zhima_ip()
    # proxy_list=zhima.proxy_list

    # 创建MongoDB连接，并调用增删改方法
    sougou_webchat = MongoAPI("localhost", 27017, "webchat_spider", "sougou_webchat")  # 其中有一个webchat_t1测试表

    key_list = ['Splunk']  # AS：联想网盘、亿方云;AB：英方、鼎甲、Veritas;AR：日志易、Splunk

    #获得首页和总页数
    # get_article(key_list)







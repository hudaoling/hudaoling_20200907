from datetime import *
import wechatsogou
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches

import requests
import datetime,time,random,re
import json
import  pandas as pd
from bs4 import BeautifulSoup
from queue import Queue       #线程
from threading import Thread  #线程
from pyquery import PyQuery as pq
from PIL import Image

# # 特定文章爬取
# def get_articles(headline=True, original=True, timedel=1, add_account=None,url=''):
#
#     ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)
#
#     url='http://mp.weixin.qq.com/profile?src=3&timestamp=1587698474&ver=1&signature=ORCd7eeKinB3Aq1pFv-9KgIKY7*9B7BQnAN-SDDy6bm**Q*GPj4IAuIOhkouWao5xcV7GyQdocV*icyq0-ypMQ=='
#     html=ws_api.get_article_content(url, del_qqmusic=True, del_mpvoice=True, unlock_callback=None,
#                         identify_image_callback=None, hosting_callback=None, raw=True)
#
#     return html
#
#
#
# if __name__ == "__main__":
#     html = get_articles(timedel=1)
#     print(html)
#
#     with open('', 'w',encoding='utf-8') as f:
#         f.write(html)



# ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)

# # 查找公众号
# infos=ws_api.search_gzh('爱数')
# for info in infos:
#     print(info)


#获得公众号的详细介绍
# aishu_url='http://mp.weixin.qq.com/profile?src=3&timestamp=1587704655&ver=1&signature=hoaJwjf9KGoR-CD6263JqRwSaL-tmiYNs04pZWwIEZhtGgeOirTPoMY9RIkHMFIsI2HvCb6GHV53orohmpwzPQ=='
# a=['爱数','36氪']
# for c in a:
#     info=ws_api.get_gzh_info(c)
#     if '爱数' in info.values():
#         info=info
#     else: info={}
#     print(info)


#关键字搜索
# keys=ws_api.get_sugg('爱数')
# for key in keys:
#     print(key)

#搜索和“爱数”这个关键字相关的，公众号文章
# articles=ws_api.search_article('爱数')
# print(articles)
# for article in articles:
#     print(article)


#获得历史文章,搜狗已经悄悄的停用了。
# his_articles=ws_api.get_gzh_article_by_history('爱数')
# print(his_articles)
# for article in his_articles:
#     print(article)


#搜索和“爱数”这个关键字相关的，公众号文章
# articles=ws_api.get_article_content('爱数')
# print(articles)
# for article in articles:
#     print(article)
#








# class WeChat():
#     def __init__(self):
#         self.session = requests.session()
#         self.session.verify = False
#
#

class sougou_login(object):

    def __init__(self):
        self.session = requests.session()

        self.token = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Host': 'account.sogou.com',
            'Connection': 'keep-alive',
            'Referer': 'https://weixin.sogou.com/', }


##h获取二维码
    def get_code(self):
        url = 'https://open.weixin.qq.com/connect/qrconnect?appid=wx6634d697e8cc0a29&scope=snsapi_login&response_type=code&redirect_uri=https%3A%2F%2Faccount.sogou.com%2Fconnect%2Fcallback%2Fweixin'
        url_base = 'https://open.weixin.qq.com' #验证码图片

        response = self.session.get(url,headers= self.headers, verify=False)
        data = response.content.decode('utf-8')
        soup = BeautifulSoup(data, 'lxml')  # 转换成lxml,可以用bs4解析
        img_src=soup.select_one('div[class="wrp_code"] img')

        img_link=url_base+img_src.get('src')

        response = requests.session().get(img_link)  #弹出登录二维码
        with open('image.jpg', 'wb') as f:
            f.write(response.content)
        image = Image.open('image.jpg')
        image.show()
        print('请使用微信扫描二维码登录:')

    #检查登录结果，status=1代表成功
    def check_login(self):
        # while True:
        time.sleep(15)
        checkUrl = 'https://lp.open.weixin.qq.com/connect/l/qrconnect?uuid=001m42OEtFn8ga23&_=1589507541224'


        checkResponse =  self.session.get(checkUrl, headers= self.headers, verify=False)
        check = json.loads(checkResponse.text)
        print (check)
        print(check["status"])

        return check["status"]

        print('session.cookies:', self.session.cookies)
        cookieDict = response.cookies.get_dict()
        print('cookieDict:', cookieDict)
        cookie = ''
        for key, value in cookieDict.items():
            cookie += key + '=' + value + ';'
        print('cookie:',cookie)

        return  cookie

    cookie=get_code()

    print('cookie:',cookie)



login=sougou_login()
login.get_code()
print("session.cookies:", login.session.cookies, '\n')

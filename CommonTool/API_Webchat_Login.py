import _thread
import os
import random
import sys
import time

import json
import requests

from PIL import Image
import warnings
warnings.filterwarnings('ignore')

"""参考链接:'https://github.com/xla145/mp_weixin/blob/master/weixin_login.py' 
            https://www.javascriptc.com/615.html"""

class Webchat_Login(object):
    def __init__(self):

        self.session = requests.session()
        self.username='hu.daoling@aishu.cn'
        self.pwd='51ccd2e2348ed7bb2375dc702ac3e254'
        self.token=''

        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
                 'Host': 'mp.weixin.qq.com',
                 'Connection':'keep-alive',
                 'Referer': 'https://mp.weixin.qq.com/',}


    # 模拟登录，带着用户名和账号
    def weixin_login(self):
        url = "https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin"
        params= {
            'username': self.username,
            'pwd':self.pwd,
            'token':self.token,
            'imgcode': '',
            'f': 'json',
            'lang':'zh_CN',
            'ajax': 1,
            }
        response = self.session.post(url, data=params, headers= self.headers, verify=False)
        if response.status_code == 200:
            data = response.content.decode('utf-8')
            print('data:',data)

            # 1.扫码登录
            self.get_weixin_login_qrcode()

              # 2.验证登录结果
            check_status=self.check_login()

            # 3.根据登录结果取得cookie和token
            if check_status == 1:
                cookie, token=self.login()
            else:
                print ("login failed:",check_status)
                cookie=None
                token=None

            return cookie, token


    #下载二维码并扫码
    def get_weixin_login_qrcode(self):
        url = 'https://mp.weixin.qq.com/cgi-bin/loginqrcode?action=getqrcode&param=4300'   #二维码地址，rd会每次变化，&rd=646
        response =  self.session.get(url, headers= self.headers, verify=False)

        with open ('QRImg.jpg','wb') as f:
            f.write(response.content)
            f.close()

        image = Image.open('QRImg.jpg')
        print('请使用微信扫描二维码登录:')
        image.show()


    #检查登录结果，status=1代表成功
    def check_login(self):
        # while True:
        time.sleep(15)
        checkUrl = 'https://mp.weixin.qq.com/cgi-bin/loginqrcode?action=ask&token=&lang=zh_CN&f=json&ajax=1'
        checkResponse = self.session.get(checkUrl, headers= self.headers, verify=False)
        check = json.loads(checkResponse.text)
        print (check)
        print(check["status"])

        return check["status"]


    #用session发送登录请求，获得token和cookie
    def login(self):
        url = "https://mp.weixin.qq.com/cgi-bin/bizlogin?action=login"

        data = {
            'f': 'json',
            'ajax': 1,
            'random': random.random()
        }
        response = self.session.post(url, data=data, headers= self.headers, verify=False)
        # {"base_resp":{"err_msg":"ok","ret":0},"redirect_url":"/cgi-bin/home?t=home/index&lang=zh_CN&token=1502993366"}
        data = json.loads(response.text)
        print('data_login:',data)
        redirect_url = data["redirect_url"]

        token = redirect_url[redirect_url.rfind("=") + 1:len(redirect_url)]
        print('token:',token)

        print('session.cookies:', self.session.cookies)
        cookieDict = response.cookies.get_dict()
        print ('cookieDict:',cookieDict)
        cookie = ''
        for key, value in cookieDict.items():
            cookie += key + '=' + value + ';'
        print (cookie)

        return cookie,token


if __name__ == '__main__':

    # 1.实例化
    webchat_login=Webchat_Login()

    # 1.登录
    cookie, token=webchat_login.weixin_login()

    print ('last_print',cookie,token)





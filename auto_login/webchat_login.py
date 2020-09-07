import requests
import re
from PIL import Image
import urllib3
urllib3.disable_warnings()
from bs4 import  BeautifulSoup

import  json

#1.获取uuid  为扫码的链接寻找参数
#2.获取二维码
#3.扫描二维码的时候持续发送请求的链接https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=obw7uFJYPw==&tip=0&r=-527204269&_=1520945398715
#
#
class WeChat():
    def __init__(self):
        self.session=requests.session()
        self.session.verify=False

    ##获取uuid
    def getUuid(self):
        url="https://login.wx.qq.com/"
        response=self.session.get(url)
        #print(response.text)
        self.uuid=re.findall(r'uuid = "(.*?)"',response.text)
        print(self.uuid)
    ##h获取二维码
    def get_code(self):
        url="https://login.weixin.qq.com/qrcode/{}".format(self.uuid)
        response=self.session.get(url)
        print(response.content)
        with open('wxcode.png','wb') as f :
            f.write(response.content)
        image=Image.open('wxcode.png')
        image.show()

    ##扫码之后的请求，不扫码请求是401
    ##扫码之后是200
    def login(self):
        url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={}&tip=1&r=1175963284&_=1587961936038".format(self.uuid)
        while True:
            response=self.session.get(url)
            if '200' in response.text:
                self.redirect_url=re.findall('redirect_uri="(.*?)"',response.text)[0]
                break
        print(response.text)

    #手机上点击登录后，发送的请求，这个是获取下一个重要链接的请求参数
    def login_parse(self):
        response=self.session.get(self.redirect_url,allow_redirects=False)
        print(response.history)
        print(response.status_code)
        soup=BeautifulSoup(response.text,'lxml')
        self.skey=soup.find('skey').text
        self.wxsid=soup.find('wxsid').text
        self.wxuin = soup.find('wxuin').text
        self.pass_ticket = soup.find('pass_ticket').text
        self.isgrayscale = soup.find('isgrayscale').text
        print(self.skey)
        '''
        <error>
        <ret>0</ret>
        <message></message>
        <skey>@crypt_b78dd979_ba51a26273893cc5fd471e8a5bf59f44</skey>
        <wxsid>9sdRG7Oy8VMI1gEr</wxsid>
        <wxuin>2359397621</wxuin>
        <pass_ticket>CrvVhVc84VwMpTeSvUgmAkZ0TVLHqfw%2BuNvJOu3tLhXmSrG7BEM9n%2BrLeqWG9Fh0</pass_ticket>
        <isgrayscale>1</isgrayscale>
        </error>
        '''
        print(response.text)
    ##登录进去，获取微信用户的详细信息（好友、公众号等信息）
    def login_in(self):
        url="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-603124408&pass_ticket=SpeKAGlPKJl48YWyrgD18vBSMskBIt%252B5rm1rkhaciSaV1oo%252FgNIbGkWKGnrkUkbJ"
        data={"BaseRequest":{"Uin":self.wxuin,"Sid":self.wxsid,"Skey":self.skey,"DeviceID":"e547323813630142"}}
        response=self.session.post(url,data=json.dumps(data))
        response.encoding="utf8"
        print(response.status_code)
        print(response.text)


    def main(self):
        print(self.getUuid())
        self.get_code()
        self.login()
        self.login_parse()
        self.login_in()


if __name__=="__main__":
    wechat=WeChat()
    wechat.main()

import requests
from lxml import etree
import http.cookiejar


#经过验证，方案可用——flora,2020-5-8
class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/'
        self.session = requests.Session()
        self.filename = 'cookies_zhihu.txt'
        self.session.cookies = http.cookiejar.LWPCookieJar()
        # 初始化cookies

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)

        selector = etree.HTML(response.text)
        token = selector.xpath('//div/form/input/@value')
        print('token',token)
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }

        response1 = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response1.status_code == 200:
            print('first')
            self.session.cookies.save(self.filename, ignore_discard=True, ignore_expires=True)
            # 保存cookies

        response2 = self.session.get(self.logined_url, headers=self.headers)
        if response2.status_code == 200:
            # self.profile(response.text)
            # print(response2.text)
            print('second')
            with open('zhihu_save.html', 'w', encoding='utf-8') as f:
                f.write(response2.text)


if __name__ == "__main__":
    login = Login()
    login.login(email='daodao2010@qq.com', password='')
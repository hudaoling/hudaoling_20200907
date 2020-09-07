import  requests
from PIL import Image
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import time
import json


class login(object):

    def __init__(self):
        self.session = requests.session()

        self.headers = {
            'Connection': 'keep-alive',
            'Host': 'open.weixin.qq.com',
            'Referer': 'https://weixin.sogou.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Cookie': 'pgv_pvid=4604574410; tvfe_boss_uuid=e5942c0c3dce0ad7; pgv_pvi=5349365760; RK=/ULZXH3HcY; ptcz=a3cb75e43f051834570e0a399deb111d1758ad497ff4933e7a1893e8ec139101; pac_uid=0_5e5885a75f8b8; ptui_loginuin=381134568@qq.com; _ga=GA1.2.1834982270.1588740012; pgv_si=s9000305664; pgv_info=ssid=s8430539379; cert=7q9WE_MPj6FTeoPtJnmhFFaqJiXGG4Zm; ticket_id=0; ticket=7cb4b7eb2498a8b87ae8fbfbcdc5a542c85ef7d9; __CURRENT_TOKEN__='
        }

    def test(self):
        log_url='https://account.sogou.com/connect/login?provider=weixin&client_id=2017&ru=https%3A%2F%2Fweixin.sogou.com&third_appid=wx6634d697e8cc0a29&href=https%3A%2F%2Fdlweb.sogoucdn.com%2Fweixin%2Fcss%2Fweixin_join.min.css%3Fv%3D20170315'



        log_res=requests.get(log_url)

        print(log_res.content.decode())

        base_url='https://open.weixin.qq.com'

        soup = BeautifulSoup(log_res.content.decode(), 'lxml')
        u1=soup.select_one('img[class="qrcode lightBorder"]').get('src')
        qrcode_url=base_url+u1
        print(qrcode_url)

        qrcode_res=self.session.get(qrcode_url,headers=self.headers,verify=False)
        # print(qrcode_res.content)
        with open('sougou_img.jpg', 'wb') as f:
            f.write(qrcode_res.content)
        image = Image.open('sougou_img.jpg')
        print('请使用微信扫描二维码登录:')
        image.show()






    # 检查登录结果，status=1代表成功
    def check_login(self):
        # while True:
        time.sleep(20)
        # checkUrl = 'https://mp.weixin.qq.com/cgi-bin/loginqrcode?action=ask&token=&lang=zh_CN&f=json&ajax=1'

        # checkUrl='https://account.sogo.com/callbackRedirect?data=%7B%22data%22%3A%7B%22ru%22%3A%22https%3A%2F%2Fweixin.sogou.com%22%2C%22noStatus%22%3Atrue%2C%22xd%22%3A%22https%3A%2F%2Fweixin.sogou.com%22%2C%22userid%22%3A%22o9t2luFG2h6Ap7PZ26ovYhD6pbIo%40weixin.sohu.com%22%7D%2C%22status%22%3A%220%22%2C%22statusText%22%3A%22%22%7D&cookieToken=d025b14f99864f5fa7b95b8e42bcdb1e&flag=SET'
        checkUrl='https://lp.open.weixin.qq.com/connect/l/qrconnect?uuid=0811unIvbT4RRln6&_=1589536587628'
        checkResponse = self.session.get(checkUrl, headers=self.headers, verify=False)
        # print(checkResponse)
        check = json.loads(checkResponse.text)
        print(check)
        print(check["status"])

        return check["status"]


login=login()
login.test()

login.check_login()
print("session.cookies:", login.session.cookies, '\n')

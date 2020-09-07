import base64
import re
import threading
import time
import requests
import warnings
warnings.filterwarnings('ignore')
from PIL import Image


#——————————————————————————————方案经过测试验证，可用——————————————————————————————

# 1.获取二维码
def getjdQrCode():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'referer': 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
    }

    qrCodeUrl = f'https://qr.m.jd.com/show?appid=133&size=147&t={round(time.time()*10000)}'
    qrHtml = requests.get(qrCodeUrl, headers=headers)
    # print(qrHtml.content)
    cookies = qrHtml.cookies.get_dict()
    # print(cookies)
    token = cookies['wlfstk_smdl']
    cookieString = ''
    for key, value in cookies.items():
        cookieString = cookieString + str(key) + "=" + str(value) + ";"
    cookieString = r'%s' % (cookieString)
    print('cookieString',cookieString)

    with open('qrCode2.jpg', 'wb') as f:
        f.write(qrHtml.content)
    image = Image.open('qrCode2.jpg')
    image.show()
    return {'status': 1,  'cookieString': cookieString, 'token': token}

# 5.轮询二维码状态
def jdLoginStatus(cookieString, token):
    while True:
        time.sleep(0.5)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'referer': 'https://passport.shop.jd.com/nologin/login.action?ReturnUrl=http%3A%2F%2Fshop.jd.com%2F',
            'cookie': cookieString
        }
        checkUrl = f'https://qr.m.jd.com/check?callback=jQuery4643268&appid=133&token={token}&_={round(time.time()*10000)}'
        checkResponse = requests.get(checkUrl, headers=headers, verify=False)
        checkJson = eval(checkResponse.text[14:-1])
        print(checkJson)
        if checkJson['code'] == 201:
            print('二维码未扫描')
            pass
        elif checkJson['code'] == 202:
            print('手机客户端确认登录')
            pass
        elif checkJson['code'] == 257:
            print('无效的二维码')
            cookie = 2
            loginStatus = 0
            break
        elif checkJson['code'] == 203:
            print('二维码过期')
            cookie = 2
            loginStatus = 0
            break
        elif checkJson['code'] == 200:
            print('登陆成功')
            ticket = checkJson['ticket']
            loginStatus = 1
            print('ticket',ticket)
            # 5.拿着门票去获取登陆后的cookie
            cookie = getqrCodeTicketValidation(ticket)
            break
        else:
            # 不知道什么状况
            cookie = 2
            loginStatus = 0
            break
    return cookie


#带着ticket登录后，取得cookie
def getqrCodeTicketValidation(ticket):
    url = f'https://passport.jd.com/uc/qrCodeTicketValidation?t={ticket}'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'referer':'https://passport.jd.com/uc/login?ltype=logout&ReturnUrl=https://order.jd.com/center/list.action'
    }
    response =session.post(url,headers=headers,verify=False)
    cookieDict = response.cookies.get_dict()
    cookie = ''
    for key,value in cookieDict.items():
        cookie += key + '=' + value + ';'
    return cookie


def checkOrder(cookie):
    url = 'https://order.jd.com/center/list.action'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'cookie': cookie
    }

    response = requests.get(url, headers=headers)
    buy_list=response.text #加.text读出来是str,如果是response.content读出来是bytes(后面加上.decode()就转换为str)
    return  buy_list


dict_code=getjdQrCode()   #cookieString & token
cookie=jdLoginStatus(dict_code['cookieString'],dict_code['token'])  #cookie

buy_list=checkOrder(cookie) #返回购物清单网页

print('cookie',cookie)

with open('buylist2.html','w',encoding='gbk') as f:
    f.write(buy_list)
# print('\n','buy_list','\n',buy_list)





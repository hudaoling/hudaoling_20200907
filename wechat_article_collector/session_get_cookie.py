import requests
import  random
import http.cookiejar as cookielib
from API_Get_Ip import GetIp
import requests.utils, pickle


session=requests.session()
session.cookies = cookielib.LWPCookieJar('jd-cookies')

try:
    session.cookies.load(ignore_discard=True)
    print('加载成功：',session.cookies)
except:
    print('Cookie 未能加载')


def isLogin():
    url='https://home.jd.com/'
    login_page=session.get(url,headers=headers,allow_redirects=False)
    # print('login_page',login_page.text)
    # with open('buy_page.html2','w',encoding='gbk') as f:
    #     f.write(login_page.text)
    login_code=login_page.status_code
    print('login_code',login_code)
    if login_code==200:
        return True
    else:
        return False


def login(secret,account):
    post_url="https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F"

    post_data={
    'sa_token':'B68C442BE645754F33277E701208059080DD726A94A73F76DEC3053A838549C06EB7D3797CE1C5BBE7C2B2EF9CA7D467C3C76FF0A28885EE64B432120BA9B13D348C69B7D2A54084AD0AF9F604987E3FF4F05CFA833594DEAA638A1460132F8E4FC41F9984A0550F77FF3A51047D9FFA6937B2323ADE6CDB3A98776094AD46AFC0D104BE5A33FD4B2D219E65930F424CA62E9A76B0553DAFABE006ED3256B130266A76FAF5CCE3ADAB479A1B91EBE72CDE6DD023D1EE4CA826799743FE145744C3631A933932A4508DB5E03BC0CC960EAD6C79FBA9774E8082E14F6CD91339EBC68638E1E4DE90ED5EE1E313A789333EB723858939AB3DA7AFF39BF9154E601D3D7BA69EBDD3185B593AA06E61BF99E69DA97A8ED673144F99C024725C899C5A1D252CFF2A8819DB21BB5B89FBA0C94153B9FF523817611B54EFB89F3E043D78AE9CD1FF79ADD1426B0142332DD9FBBF68E7E73CBC653EADC50E8040B9EF49BAAA8A8C96FE49E6C6A03F3F40A438D55BED7B0276B7C6A0FB6DC653EB9538EEECFA08E2A91400588A52F19F648799FC79CE96FC087A832DD381E7B55C5CBF306EBFFFCA14B1678718A0204547324A8DAA119CD417A6DEEAC3DF97E96D9A725ADCBDCF54E751B0F9AE42204ECEAB0BBF837F15D96385C51F533596F377B8199411',
    'uuid':'374ad441-8b30-4c8b-b335-a4905a18f4ae',
    'eid':'JRBQEAA6CCUEXRWG4JZ5CPT635D2QNVZFP7GLSSOURRNYVVXYGQM2OUV4GJLS7NYNR77BIXONLRWLU4F6PDN5CRQOA',
    'eid':'JRBQEAA6CCUEXRWG4JZ5CPT635D2QNVZFP7GLSSOURRNYVVXYGQM2OUV4GJLS7NYNR77BIXONLRWLU4F6PDN5CRQOA',
    'fp':'f1ce38266946d08aaf272ff0f6178a4c',
    '_t':'t',
    'loginType':'c',
    'main_flag':'main_flag',
    'pubkey':'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDC7kw8r6tq43pwApYvkJ5laljaN9BZb21TAIfT/vexbobzH7Q8SUdP5uDPXEBKzOjx2L28y7Xs1d9v3tdPfKI2LR7PAzWBmDMn8riHrDDNpUpJnlAGUqJG9ooPn8j7YNpcxCa1iybOlc2kEhmJn5uwoanQq+CA6agNkqly2H4j6wIDAQAB',
    'useSlideAuthCode':'1',
    'loginname':account,
    'nloginpwd': secret,
    }
    try:
        login_page=session.post(post_url,data=post_data,headers=headers)
        # login_code=login_page.text
        print(login_page.status_code)
    except:
        pass
    session.cookies.save('jd-cookies',ignore_discard=True, ignore_expires=True)


cookie=[]
for c in session.cookies:
    print(c.name, c.value)
    cookie.append(c.name + '=' + c.value)
cookie_str = "".join(cookie)
print('cookie', cookie_str)

#发送get请求获得网站信息
def my_page(url):
    res=requests.get(url,headers=headers2,proxies=None)
    print('res.status_code',res.status_code)
    page_str=res.content.decode()
    with open('buy_page2.html','w',encoding='utf-8') as f:
        f.write(page_str)
    return page_str



if __name__ == '__main__':
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    ]

    headers = {"User-Agent": random.choice(user_agent_list),
               "Host": "passport.jd.com",
               # "origin": "https://passport.jd.com",
               # "referer": "https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F",
               }

    headers2 = {"User-Agent": random.choice(user_agent_list),
               "Host": "passport.jd.com",
               "origin": "https://passport.jd.com",
               "referer": "https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F",
               'cookie':cookie_str
               }

    # # 爬取西刺网址的代理IP并验证可用性
    # Ip_class = GetIp('http://www.hiyd.com/dongzuo/') #实例化
    # Ip_class.run()  # 调用run方法
    # proxy_list = Ip_class.success_list
    # free_proxy = random.choice(proxy_list)

    #验证登录是否成功，不成功重新登录并保存cookies
    if isLogin():
        print('您已经登录')
    else:
        login('thelivedream','daodao2012')


    # # #利用 session登陆后，可以随意访问网站内容
    buy_url='https://home.jd.com/'
    buy_page=my_page(buy_url)
    print(buy_page)


    # login('thelivedream', 'daodao2012')
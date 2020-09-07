import requests
import  random
import http.cookiejar as cookielib
from API_Get_Ip import GetIp
import requests.utils, pickle


user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
]

headers = {"User-Agent": random.choice(user_agent_list),
           "Host": "www.douban.com",
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate, br',
           'Connection': 'keep-alive',
           }





response = requests.get("http://www.douban.com",headers=headers)

print(response.status_code,'\n')
print('response.headers: ',response.headers,'\n')
print('set_cookie: ',response.headers['Set-Cookie'],'\n')
print('cookies: ',response.cookies,'\n')


cookieJar = requests.cookies.RequestsCookieJar()

# #添加请求cookir
# for cookie in response.cookies:
#     # print('cookie.name,cookie.value: ',cookie.name,cookie.value,'\n')
#     cookieJar.set(cookie.name,cookie.value)
#
print('cookieJar_old:',cookieJar,'\n')


#添加相应cookie
for cookie in response.headers['Set-Cookie'].split(";"):
    key=cookie.split('=')[0]
    value=cookie.split('=')[1]
    print(key,value)
    cookieJar.set(key,value)

print('cookieJar_new:',cookieJar,'\n')

data = {
    'source':'None',
    'redir':'https://accounts.douban.com/passport/login',
    'username':'',
    'password':''
}

#使用Session对象提交请求，相当于在浏览器中连续操作网页，而如果直接使用```request.post()```,则相当没提交一次请求，则打开一个浏览器，我们在实际使用浏览器的经验告诉我们，这样是不行的。
session = requests.Session()
res =session.post('https://www.douban.com/accounts/login',headers=headers,data=data)
print(res.status_code,'\n')

#此时，如果实在浏览器的话，我们应该可以看到已经登陆成功，并且跳转到了https://movie.douban.com/，页面，使用这个Session直接访问的我的账号，检查一下，是否是我的账号在登录状态。
res_a = session.get('https://www.douban.com/accounts')
print('account_html:',res_a.text,'\n')

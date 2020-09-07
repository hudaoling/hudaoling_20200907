import random
import requests
from pyquery import PyQuery as pq
from urllib.parse import urlencode,quote
import uuid
import time
from lxml import etree
import re



headers_str='''
Host: weixin.sogou.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
'''


def headers_to_dict(headers_str):
    '''
    将headers_str字符串形式转化成字典；；
    :param headers_str:
    :return:
    '''
    headers_str =headers_str.strip()
    headers_dict =dict((i.split(':',1)[0].strip(),i.split(':',1)[1].strip()) for i in headers_str.split('\n'))
    return headers_dict

a_str ='''
uigs_cl	first_click
uigs_refer	https://weixin.sogou.com/
uigs_productid	vs_web
terminal	web
vstype	weixin
pagetype	result
channel	result_article
s_from	input
sourceid	
type	weixin_search_pc
uigs_cookie	SUID,sct
query	亚马逊大火
weixintype	2
exp_status	-1
exp_id_list	0_0
wuid	00A1E9BBB49DFA675EA15F85C62A5538
rn	1
login	0
uphint	1
bottomhint	1
page	1
exp_id	null_0-null_1-null_2-null_3-null_4-null_5-null_6-null_7-null_8-null_9
'''

def str_to_dict(a_str):
    '''
    将a_str形式的字符串转化为字典形式；
    :param a_str:
    :return:
    '''
    str_a =list( i for i in a_str.split('\n') if i !='' )
    str_b ={}
    for a in str_a:
        a1 = a.split('\t')[0]
        a2 =a.split('\t')[1]
        str_b[a1] =a2

    return str_b

b_data =str_to_dict(a_str)
headers =headers_to_dict(headers_str)



def get_suva(SNUID):
    '''
    根据sunid来获取suv参数；并添加到cookie众
    :param a: sunid
    :return:'''

    b_data['snuid'] = SNUID.split('=')[-1]
    b_data['uuid'] = uuid.uuid1()
    b_data['uigs_t'] = str(int(round(time.time() * 1000)))

    print('b_data:', b_data, '\n')

    url_link = 'https://pb.sogou.com/pv.gif?' + urlencode(b_data)

    print('url_link:', url_link)

    res_temp = requests.get(url_link)

    cookie_s = res_temp.headers['Set-Cookie'].split(',')
    cookie_list_s = []
    for i in cookie_s:
        for j in i.split(','):
            if 'SUV' in j:
                cookie_list_s.append(j)
            else:
                continue

    print('cookie_list_s:', cookie_list_s)

    print(cookie_list_s[0].split(';')[0])

    headers['Cookie'] = cookie_list_s[0].split(';')[0]


def add_cookie(url):

    headers['Referer'] = url
    res =requests.get(url,headers=headers)
    cookies =res.headers['Set-Cookie'].split(';')
    print("res.headers['Set-Cookie']:",res.headers['Set-Cookie'],'\n')
    print('cookies:',cookies,'\n')

    cookie_list_long =[]
    cookie_list =[]
    for cookie in cookies:
        cookie_list_long.append(str(cookie).split(','))

    for i in cookie_list_long:
        for set in i:
            if 'SUID' in set or 'SNUID' in set:
                cookie_list.append(set)

    print('cookie_list:',cookie_list,'\n')
    SNUID = cookie_list[0].split(';')[0]
    print('SNUID:',SNUID,'\n')

    get_suva(SNUID) #调用get_suva获得cookie

    headers['Cookie'] = headers['Cookie'] + ';' + ';'.join(cookie_list)
    print("headers['Cookie'] 2:",headers['Cookie'] )

    return res


def get_articles(res):
    url_list = pq(res.text)('.news-list li').items()  # 获得首页得文章<li>标签

    article_list = []

    for i in url_list:
        # 提取href属性标签
        url_list12 = pq(i('.img-box a').attr('href'))
        url_list12 = str(url_list12).replace('<p>', '').replace('</p>', '').replace('amp;', '')

        print('url_list12:', url_list12, '\n')

        # 构造参数k与h,获得临时url;
        b = int(random.random() * 100) + 1
        a = url_list12.find("url=")
        result_link = url_list12 + "&k=" + str(b) + "&h=" + url_list12[a + 4 + 21 + b: a + 4 + 21 + b + 1]
        temp_url = "https://weixin.sogou.com" + result_link
        print('temp_url:', temp_url, '\n')

        # 根据临时链接发起网页请求，得到构造真实url所返回网页
        temp_response = requests.get(temp_url, headers=headers).content.decode()
        print('temp_response:', temp_response, '\n')

        # if 'antispider' in temp_response.url or '请输入验证码' in temp_response.text:
        # else:
        #     None

        #  通过正则解析，获取真实url
        url_text = re.findall("\'(\S+?)\';", temp_response, re.S)
        best_url = ''.join(url_text)
        true_url = best_url.replace("&from=inner", "").replace("@", "")
        print('true_url:', true_url, '\n')

        last_text = requests.get(true_url).text

        print('last_text:', last_text, '\n')

        article_dict = {}
        article_dict['key_word'] = key
        article_dict['title'] = pq(last_text)('#activity-name').text()
        # article_dict['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(tims_zone)))
        article_dict['sumary'] = pq(last_text)('#js_content > p').text()
        article_dict['from_gzh'] = pq(last_text)('#js_name').text()
        article_dict['true_url'] = true_url
        article_dict['content'] = pq(last_text)('#meta_content > span.rich_media_meta.rich_media_meta_text').text()

        # print(pq(last_text)('#activity-name').text())
        # print(pq(last_text)('#js_content > p').text())
        # print(pq(last_text)('#js_name').text())
        # print(pq(last_text)('#meta_content > span.rich_media_meta.rich_media_meta_text').text())

        article_list.append(article_dict)
    print(article_list)

    return  article_list

key ='亚马逊大火'
url = 'https://weixin.sogou.com/weixin?type=2&query={}'.format(quote(key))

res=add_cookie(key)
get_articles(res)


"""
igs_refer: https://weixin.sogou.com/weixin?type=2&query=%E4%BA%9A%E9%A9%AC%E9%80%8A%E5%A4%A7%E7%81%AB
uigs_t: 1589525009157
uigs_productid: vs_web
terminal: web
vstype: weixin
pagetype: result
channel: result_article
s_from: input
sourceid: 
type: weixin_search_pc
uigs_cookie: SUID,sct
uuid: 5a628e4c-2db7-4f98-9eb3-1dc04575aafa
query: 亚马逊大火
weixintype: 2
exp_status: -1
exp_id_list: 0_0
wuid: 00A1E9BBB49DFA675EA15F85C62A5538
snuid: 98678CA9DBDF7FABEDBCAB69DBAB594B
rn: 1
login: 1
uphint: 0
bottomhint: 1
page: 1
exp_id: null_0-null_1-null_2-null_3-null_4-null_5-null_6-null_7-null_8-null_9"""

"""
"""
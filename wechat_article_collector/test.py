import requests
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
import  numpy as np
import json,re,math,random
import time,datetime
import uuid
from urllib.parse import urlencode,quote


from pyquery import PyQuery as pq
import urllib3
urllib3.disable_warnings()
from API_Get_Ip import GetIp,Get_zhima
from API_Get_Ip import Get_zhima
from PIL import Image
import  pytesseract


#get_ip是自定义py文件，目前是爬取西刺免费代理，验证并返回可用的代理IP
from API_Get_Ip import GetIp,Get_zhima
from API_MongoDB import MongoAPI  #自定义模块


pd.set_option('display.width',5000)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',2000)



# def get_zhima_ip():
#     url='http://http.tiqu.alicdns.com/getip3?num=102&type=1&pro=&city=0&yys=0&port=11&pack=97654&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'
#     res=requests.get(url)
#     data=res.content.decode()
#     ips=list(i.strip() for i in data.split('\r\n') if i !='')
#
#     proxy_list = []
#     http="https"
#     for ip in ips:
#         ip_list = {}
#
#         ip_list["https"] = ip
#         proxy_list.append(ip_list)
#         return  proxy_list
#
# # proxy_list=get_zhima_ip()
# # print(proxy_list)
# for i in range(120,142):
#     print(i)
# #
# url_zhima = 'http://http.tiqu.alicdns.com/getip3?num=196&type=1&pro=&city=0&yys=0&port=1&pack=97654&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'
#
# zhima = Get_zhima(url_zhima)
# zhima.get_zhima_ip()
# proxy_list = zhima.proxy_list
# print(proxy_list)
# for i in range(10):
#     print(random.choice(proxy_list))
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# #
# gray_image = Image.open('D:/verify_code/edit_v2.jpg')
# gray_image.show()
# code = pytesseract.image_to_string(gray_image)
# print(code)





# sougou_webchat = MongoAPI("localhost", 27017, "webchat_spider", "sougou_t1")  # 其中有一个webchat_t1测试表
#
# dict={'title':'a5','age':19}
#
# sougou_webchat.insert_check([dict],{'title':dict['title']})  # 写入mongodb #,
# a_list=sougou_webchat.find({})
# for link in a_list:
#     title=link['title']
#     _id=link['_id']
#     print(title,_id)
#     link['test']="test"
#     link["yyy"]="yyy"
#
#     print(link)
#     print(type(link))
#     sougou_webchat.update({"_id": _id},link)
#     # print(link['test'])

# with open('html/tt.html','r',encoding='utf8') as f:
#     data=f.read()
# soup=BeautifulSoup(data, 'lxml')
# print(soup)
# img = soup.select_one('img[id="seccodeImage"]').get('src')
# print(img)

# cookies="""<Cookie bizuin=3548169269 for mp.weixin.qq.com/>, <Cookie cert=a_CRacQ68FAMt9r2lOXeELisziqNp46C for mp.weixin.qq.com/>, <Cookie data_bizuin=3548169269 for mp.weixin.qq.com/>, <Cookie data_ticket=nh0ejejFcZzw4nbveGrLVJbr0NYz5/woe8xfVB+YGAAvjZz9hqYKbo0Gq1n9S27W for mp.weixin.qq.com/>, <Cookie mm_lang=zh_CN for mp.weixin.qq.com/>, <Cookie openid2ticket_oNcR804hCFIm3veV1ovO5qMNl24g=+hYuao3lnLBoBkBDGIaeEPiiQ5/QQOF1LcDGo/YGHr4= for mp.weixin.qq.com/>, <Cookie rand_info=CAESIAhYVimJ1+WAzpW995y1NnYDDnpZU30FHSfxlnoSLHFw for mp.weixin.qq.com/>, <Cookie slave_bizuin=3548169269 for mp.weixin.qq.com/>, <Cookie slave_sid=aW5CUnE2NXpPX3JFdkJtMDhIMW5wMENoVUdxY1RvYThqN2doOGhUbFJua2Y2TnJoWFpZaEttVWwyQW5JV3FzSUhiVWJZQkY4dGJOSG55ZXlhYlFuc0oxcEFqa0VkWnFNNG8xVDJhU2Q3U3F0MWp6VG9pdGVZYU13Y0Z5dzlrdktNR1VtbFNwajlwOGtvMjFT for mp.weixin.qq.com/>, <Cookie slave_user=gh_4dbf3726657a for mp.weixin.qq.com/>, <Cookie ticket=18b75aece07e887a475a1eba5fe64731b7d3657a for mp.weixin.qq.com/>, <Cookie ticket_id=gh_4dbf3726657a for mp.weixin.qq.com/>, <Cookie ua_id=E943FKWoNFJmFv1OAAAAAIVPR71zdONKfveHd9WibMc= for mp.weixin.qq.com/>, <Cookie uuid=a52d25ff9a7053183079057eec2f1510 for mp.weixin.qq.com/>, <Cookie xid= for mp.weixin.qq.com/>"""
# #
# # cookie_list=[]
# #
# # for list in cookies.split(','): #.replace(" ", "")
# #     cookie=list.lstrip().replace('<',"").replace(">","").split(' ')
# #     # print(cookie)
# #     cookie_list.append(cookie[1])
# # print (cookie_list)
# # a=";".join(cookie_list)
# # print(a)

#
# dict={'bizuin': '3548169269', 'data_bizuin': '3548169269', 'data_ticket': 'twuAJByaxAYlLTl9DldKpKF346f+4XLVURniwgs1aRKpIqJTEgFcTy7E+V5Ublz8', 'mm_lang': 'zh_CN', 'openid2ticket_oNcR804hCFIm3veV1ovO5qMNl24g': 'guADauHJihY1XlalkEwEar9I24NsckWkQA6FyryXa2w=', 'rand_info': 'CAESIIhxwI96ghIqYb4brVzMSfkZE8w7QFikX5pfplBxyQ7X', 'slave_bizuin': '3548169269', 'slave_sid': 'Y1RfR2lGSE0zQnRxYlhJZTRUMWVnNUhHQVhIaE9YWkwyekVmVFpZSGl3SDBBRFVTeFV2bU1ZYW5manVrNmJlUktyMnV4TTcwbEpKbjBTWUc5ODBYR1B4c0lxYnVjUzdtdnZmakRoT1NjV1Q1ZXVqRHFBb0NocXFwRUUyNWk3Yk5UbHcxRDB4V29jUkdwY25v', 'slave_user': 'gh_4dbf3726657a', 'ua_id': 'V2HbCS2RrBGL0JYtAAAAAKqfk09JnxbHzhZBLpKtuTs=', 'xid': ''}
# # str=str(dict)
# # print(str)
# # b=str.replace("{","").replace("}","").split(',')
# # print (b)
#
# cookie = ''
# for key, value in dict.items():
#     cookie += key + '=' + value + ';'
# print (cookie)


#所有公众号抓取（手工过滤掉一部分）：
gzh_str_all="""
fakeid	            nickname		alias
MjM5NjU1OTYyMA==	爱数		AISHUchina
MzUxMDU5NjQ3Mg==	联想Filez		Lenovo-Filez
MzI4NDQ2NjM5Ng==	亿方云		hzfangcloud
MzA5MjM5MDgzOA==	英方云		i2soft
MjM5OTEzNTUzOA==	英方软件		info2soft
MzIwMDUxOTExMA==	鼎甲		SCUTECH-DJ
MzA4MjUyMTQ0NA==	VERITAS中文社区		VERITAS_CHINA
MjM5MDQxNjMxMA==	日志易		rizhiyi
MzI5MDQ5ODAxMQ==	Splunk大数据		Splunk-China
"""

#
# def str_to_dict(gzh_str):
#     '''
#     将a_str形式的字符串转化为字典形式；
#     :param a_str:
#     :return:
#     '''
#     str_a =list( i for i in gzh_str.split('\n') if i !='' )
#     str_b ={}
#     for a in str_a:
#         if 'fakeid' not in a:
#             a1 = a.split('\t')[0]
#             a2 =a.split('\t')[1]
#             # print ( a.split('\t'))
#             a3 = a.split('\t')[3]
#             str_b[a3] = a1
#     print(str_b)
#
#     return str_b
# strb=str_to_dict(gzh_str_all)
# # print (strb)


webchat_table = MongoAPI("localhost", 27017, "webchat_spider", "sougou_t1")  # 其中有一个webchat_t1测试表 "webchat_table"
#
# dict={  "id" : "MzI4NDQ2NjM5Ng==_0_21", "title" : "【转人民日报】转扩！给即将返岗人员的防护建议", "digest" : "共同努力打赢防疫阻击战", "date" : 1580547600, "create_time" : "2020-02-01 17:00:00", "from_gzh" : "hzfangcloud", "link" : "http://mp.weixin.qq.com/s?__biz=MzI4NDQ2NjM5Ng==&mid=2247485198&idx=2&sn=e84d908465864e9f92d5ed286711e7c3&chksm=ebfa4abddc8dc3ab604888365e1889e36c3f976d6b2afa4041f9440ab88958aa557079e8234e#rd", "content" : "共同努力\n打赢防疫阻击战" }
# print (dict['title'])
#
# key='title'
# webchat_table.insert_check(dict,key)
# # list=webchat_table.find()


#
# list=webchat_table.find()
# key='title'
# id=0
# for article in list:
#     webchat_table.insert_check(article, key) #按关键字内容搜索，存在就不写入，不存在则写入。
#     id +=1
# print (id)


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

headers=headers_to_dict(headers_str)

key ='亚马逊大火'
url = 'https://weixin.sogou.com/weixin?type=2&query={}'.format(quote(key))
print(url)


# headers['Referer'] = url
res =requests.get(url,headers=headers)
# print(res.text)

url_list= pq(res.text)('.news-list li').items()
print(url_list)


for i in url_list:
    #提取href属性标签
    url_list12 = pq(i('.img-box a').attr('href'))
    url_list12 =str(url_list12).replace('<p>','').replace('</p>','').replace('amp;','')

    print('url_list12:',url_list12,'\n')

    #构造参数k与h;
    b = int(random.random() * 100) + 1
    a = url_list12.find("url=")
    result_link = url_list12 + "&k=" + str(b) + "&h=" + url_list12[a + 4 + 21 + b: a + 4 + 21 + b + 1]
    a_url ="https://weixin.sogou.com" +result_link
    print('a_url:',a_url,'\n')

    second_url =requests.get(a_url,headers=headers).content.decode()

    print('second_url:',second_url), '\n'

    # url_text = re.findall("\'(\S+?)\';", second_url, re.S)
    # best_url = ''.join(url_text)



    # last_text = requests.get(url=str(best_url.replace("@", ""))).text
    #
    # print('last_url:', str(best_url.replace("@", "")), '\n')

    # print('last_text:', last_text, '\n')

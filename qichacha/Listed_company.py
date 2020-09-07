import requests
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
import  numpy as np
import json,re,math,random
import time,datetime

from pyquery import PyQuery as pq
import urllib3
urllib3.disable_warnings()
pd.set_option('display.width',3000)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',2000)

import urllib3
urllib3.disable_warnings()

from CommonTool.API_database import conn

# -----------创建爬虫代理-----------
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
]

headers = {"User-Agent": random.choice(user_agent_list),
           "Host": "www.qcc.com",
           "Connection": "keep-alive",
            'Cookie':'zg_did=%7B%22did%22%3A%20%221723b07f0d5bc-066d3fca9098cc-d373666-151800-1723b07f0d6bc4%22%7D; UM_distinctid=1723b07f11f818-0d37559f1c997-d373666-151800-1723b07f12081a; _uab_collina=159012827622387440712851; zg_aa480911ddef49788aa72aa12c90cea4=%7B%22sid%22%3A%201590128947238%2C%22updated%22%3A%201590128947245%2C%22info%22%3A%201590128947242%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E8%88%86%E6%83%85%E7%AE%A1%E5%AE%B6WEB%E7%AB%AF%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%7D; QCCSESSID=86ij9hlip277dhmbclt0731464; hasShow=1; Hm_lvt_78f134d5a9ac3f92524914d0247e70cb=1596424265,1597311824,1597375021,1597376381; acw_tc=df6ff44615973846253302406e4b1c7ed17bc9fd0e703298fd50f2bd34; CNZZDATA1254842228=1958501212-1590126024-https%253A%252F%252Fwww.google.com%252F%7C1597382693; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201597384625973%2C%22updated%22%3A%201597384635638%2C%22info%22%3A%201597311823976%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%22cc98fef9f368d8701de962b4d8f94aa0%22%7D; Hm_lpvt_78f134d5a9ac3f92524914d0247e70cb=1597384636'
           }

def list_company():
    '''获取企查查的上市公司名单'''

    for page in range(1,405):
        url='https://www.qcc.com/elib_ipo_p_{}.html'.format(page)

        res=requests.get(url,timeout=15,headers=headers)

        data_temp = res.content.decode('utf-8')  # 读取请求文件
        print(data_temp)
        # data_temp='abc'
        with open('html/{}.html'.format(page), 'w', encoding='utf8') as f:
            f.write(data_temp)

        time.sleep(random.randint(3,5) + random.random())


def xinsanban():
    '''获取企查查的新三板——上市公司名单'''

    for page in range(1,505):
        url='https://www.qcc.com/elib_sanban_p_{}.html'.format(page)

        res=requests.get(url,timeout=15,headers=headers)

        data_temp = res.content.decode('utf-8')  # 读取请求文件
        print(data_temp)
        # data_temp='abc'
        with open('html_xinsanban/{}.html'.format(page), 'w', encoding='utf8') as f:
            f.write(data_temp)

        time.sleep(random.randint(3,5) + random.random())


def get_juchao():
    '''获取巨潮网上的上市公司名单'''
    # url='http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#szseMain%2Fimportant'  #深市
    # url2='http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#szse%2Fimportant'     #深主板
    # url3='http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#szseSme%2Fimportant'  #中小板
    # url4='http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#szseGem%2Fimportant'  #创业板
    # url5='http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#sse%2F1' #沪市
    # url6='http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#sseMain%2F1' #沪主板
    # url7='http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#sseKcp%2F1' #科创办
    # url8='http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#third%2F1_newThree' #三板
    # url9='http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#hke%2F1_hkeMain'#港股

    # -----------创建爬虫代理-----------
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    ]

    headers = {"User-Agent": random.choice(user_agent_list),
               "Host": "www.cninfo.com.cn",
               "Connection": "keep-alive",
               'Cookie':'JSESSIONID=0DF3A68FB5CA6DA19E32183FB72A17DC; _sp_ses.2141=*; UC-JSESSIONID=B98180493105EBBB4C74A3D6A62B47CE; _sp_id.2141=cbbbb1e7-2349-4c6e-9be6-3ec8dde769b9.1597375386.3.1597628458.1597396420.435cdf0f-cd58-4d3a-a997-7e026b3ee676'
               }
    url='http://www.cninfo.com.cn/new/disclosure'

    dict={'szse_latest':12,'szse_main_latest':3,'szse_sme_latest':6,'szse_gem_latest':3,'sse_latest':32,'sse_main_latest':29,'sse_kcp_latest':9,'neeq_company_latest':82,'hke_main_latest':17}

    for m in dict.keys():
        if m=='szse_main_latest':
            for page in range(1,dict[m]+1):

                data = {
                    'column': m,
                    'pageNum': page,
                    'pageSize': 30,
                    'sortName': None,
                    'sortType': None,
                    # 'clusterFlag': 'True',
                }

                res=requests.post(url, params=data, timeout=15, headers=headers) #
                print(res.text)

            # data_temp = res.content.decode('utf-8')  # 读取请求文件
            # print(data_temp)
            # with open('html_juchao/{}_{}.html'.format(m,page), 'w', encoding='utf8') as f:
            #     f.write(data_temp)





def parse_detail():
    '''解析企查查爬去的上市公司名单'''
    df = pd.DataFrame()

    for page in range(1, 400):
        with open('html/{}.html'.format(page), 'r', encoding='utf8') as f:
            data = f.read()
            tree=etree.HTML(data)
            h=tree.xpath('/html/body/div[1]/div[2]/div/div[2]/table')[0]
            link = tree.xpath('//td[4]/a/@href')
            link= ['https://www.qcc.com/'+i for i in link]
            t2=pd.read_html(data)[0]
            t2['link']=pd.Series(link,index=t2.index)
            df=df.append(t2,ignore_index=True)


    for page in range(1, 501):
        with open('html_xinsanban/{}.html'.format(page), 'r', encoding='utf8') as f:
            data = f.read()
            tree=etree.HTML(data)
            h=tree.xpath('/html/body/div[1]/div[2]/div/div[2]/table')[0]
            link = tree.xpath('//td[4]/a/@href')
            link= ['https://www.qcc.com/'+i for i in link]
            # print (link)
            t2=pd.read_html(data)[0]
            t2['link']=pd.Series(link,index=t2.index)
            df=df.append(t2,ignore_index=True)



    df['股票代码'] = df['股票代码'].apply(lambda x:"%06d"%x)

    # print(len(df))
    df.to_excel('listed_company.xlsx')
    # df.to_sql('qcc_company_list',conn.mycom,if_exists='replace',index=False,dtype=None)


def juchao_parse():
    '''解析巨潮资讯网的信息'''
    dict = {'szse_latest': 12, 'szse_main_latest': 3, 'szse_sme_latest': 6, 'szse_gem_latest': 3, 'sse_latest': 32,
            'sse_main_latest': 29, 'sse_kcp_latest': 4, 'neeq_company_latest': 82, 'hke_main_latest': 2}

    df_all = pd.DataFrame()
    for m in dict.keys():
        print(m)
        # if m == 'szse_main_latest':
        for page in range(1, dict[m] + 1):
            with open('html_juchao/{}_{}.html'.format(m,page), 'r', encoding='utf8') as f:
                data=f.read()
                # print(data)
                # print(type(data))
                data=eval(data.replace("null",'None').replace("true",'True').replace("false",'False'))
                # print(type(data))
                print(data)
                if len(data["classifiedAnnouncements"])>=1:
                    data=data["classifiedAnnouncements"][0][0]
                    df=pd.DataFrame.from_dict(data, orient='index').T
                    df_all=df_all.append(df,ignore_index=True)

    print(len(df_all))
    print(df_all)




if __name__ == '__main__':
    pass
    # list_company()  #爬取页面
    # xinsanban()
    # parse_detail() #解析数据
    # get_juchao()
    # juchao_parse()

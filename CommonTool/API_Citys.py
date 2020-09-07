# -*- coding: utf-8 -*-
import requests
import datetime,time,random,re
import json
import  pandas as pd
from bs4 import BeautifulSoup
from queue import Queue       #线程
from threading import Thread  #线程
from pyquery import PyQuery as pq
from lxml import etree
import urllib.request
import urllib.parse
import string


pd.set_option('display.width',3000)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',2000)



user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
]

headers = {"User-Agent": random.choice(user_agent_list),
           }

p = ['省', '行政区', '自治区']
s = ['上海市', '北京市', '天津市', '重庆市']

class get_citys(object):

    def __init__(self,**args):

        self.p = ['省','行政区','自治区']
        self.s = ['上海市' , '北京市' ,'天津市' , '重庆市']
        self.data = None
        self.provinces_list = None
        self.area_list = None
        self.area_list_df = None
        self.area_df = None


    def get_map(self,datatype):
        '''datatype='url'时从网页爬取，='localfile'时从本地html读取'''

        if datatype=='url':
            url2='http://xzqh.mca.gov.cn/defaultQuery?shengji=-1&diji=-1&xianji=-1'
            response = requests.get(url2,timeout=3,headers=headers) #
            self.data = response.text

            with open('city.html', 'w') as f:  # 将返回结果写入文件，测试时避免重复发请求
                f.write(self.data)

        elif datatype=='localfile':
            with open('city.html','r') as f:
                self.data = f.read()




    #获得所有省\市\区的地理位置列表(没有层级关系)
    def get_detail(self,**args):

        # Index(['地 名', '驻地', '人口（万人）', '面积（平方千米）', '行政区划代码', '区号', '邮编'], dtype='object')
        # 读取html里面的所有地名表格,返回df
        self.area_df = pd.read_html(self.data)[2]
        print(self.area_df)

        xpath_address = etree.HTML(self.data)
        #获取省信息
        provinces = xpath_address.xpath("//script[last()]/text()")
        provinces_re = re.findall('json = ' + '(.+?);', str(provinces))[0]  # 正则解析出所有省列表,[0]取出后是字符串
        self.provinces_list = eval(provinces_re)
        print(type(self.provinces_list),self.provinces_list)


        #获取地区信息
        areas=xpath_address.xpath("//input[@type='hidden']/@value")
        self.area_list = eval(areas[3]) #将解析内容转换成列表
        self.area_list_df = pd.DataFrame(self.area_list)
        print(type(self.area_list),self.area_list)

    @staticmethod
    def get_city(area,*args):
        '''根据市信息读出市名及其级别'''
        # area=self.area_df['地 名'].strip().replace("+","")
        if any(k in area  for k in s):
            city=area
            type='Municipality'
        elif  '+' in area:
            city = area
            type='shiji'
        else:
            city=None
            type='quxianji'
        return city ,type

    @staticmethod
    def get_province(pron,*args):
        '''根据省份信息读出省及其级别'''
        if any(k in pron  for k in p):
            province=pron
            type='shengji'
        elif  any(k in pron  for k in s):
            province=pron
            type=""
        else:
            province=None
            type=""
        return province,type


    def run(self):
        '''主要执行程序'''
        self.get_map('url')  # 网页调用方式'url'

        self.get_detail()

        # 增加所属城市列，以及所属类型
        self.area_df['cityof'], self.area_df['type'] =zip(*self.area_df['地 名'].apply(self.get_city))
        # self.area_df['cityof'] =self.area_df.apply(self.get_city,axis=1)

        self.area_df['cityof'] = self.area_df['cityof'].fillna(method='ffill')
        self.area_df['地 名'] = self.area_df['地 名'].apply(lambda x: x.strip().replace("+", ""))
        print(self.area_df.head(50))

        # 增加所属['省','行政区','自治区']还有“直辖市”列，以及所属类型

        print('hhh:',self.area_list_df['cName'].apply(self.get_province))
        self.area_list_df['province'], self.area_list_df['type'] = zip(*self.area_list_df['cName'].apply(self.get_province))
        self.area_list_df['province'] = self.area_list_df['province'].fillna(method='ffill')
        # print(area_list_df.head(50))

        # 将省市两张表合并程最后信息
        self.area_all = pd.merge(self.area_list_df, self.area_df, how='left', left_on='cName', right_on='地 名')
        self.area_all['type_y'] = self.area_all['type_y'].fillna('shengji')

        print(self.area_all.head(1000))
        self.area_all.to_excel('area_all.xlsx', encoding='utf-8')

        return self.area_all



if __name__ == '__main__':
    citys=get_citys()
    area_all=citys.run()
























    # 备用，暂时用不上
    province = '''省、自治区、直辖市
    北京市(京)
    天津市(津)
    河北省(冀)
    山西省(晋)
    内蒙古自治区(内蒙古)
    辽宁省(辽)
    吉林省(吉)
    黑龙江省(黑)
    上海市(沪)
    江苏省(苏)
    浙江省(浙)
    安徽省(皖)
    福建省(闽)
    江西省(赣)
    山东省(鲁)
    河南省(豫)
    湖北省(鄂)
    湖南省(湘)
    广东省(粤)
    广西壮族自治区(桂)
    海南省(琼)
    重庆市(渝)
    四川省(川、蜀)
    贵州省(黔、贵)
    云南省(滇、云)
    西藏自治区(藏)
    陕西省(陕、秦)
    甘肃省(甘、陇)
    青海省(青)
    宁夏回族自治区(宁)
    新疆维吾尔自治区(新)
    香港特别行政区(港)
    澳门特别行政区(澳)
    台湾省(台)'''
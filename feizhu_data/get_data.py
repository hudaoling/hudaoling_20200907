import requests
import pandas as pd
import  numpy as np
import random
# from pymongo import MongoClient
pd.set_option('display.width',2000)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

class DataCrawler(object):
    def __init__(self):
        address=pd.read_csv('city_data.csv')
        # self.cities = address[address.province.isin(['浙江省','江苏省','上海市','广东省','北京市','安徽省','海南省','江西省','四川省','湖北省','湖南省','湖北省','福建省'])].city  #目前执行到了舟山
        self.cities = address[address.province.isin(['福建省'])].city  #目前执行到了舟山

        self.headers ={"User-Agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
        self.proxies = { "http": "http://114.223.208.165:8118", "https": "http://119.84.84.185:12345"
            , "https": "http://121.237.149.82:3000","https": "http://1111.222.141.127:8118"}

        col = ['trip_main_busness_type', 'src', 'fields', 'itemId', 'title', 'cityName', 'comment',
               'picUrl', 'soldRecent',
               'soldRecentNum', 'sold365', 'discountPrice', 'type', 'subTitle', 'shortInfo', 'scm', 'price',
               'itemTotalScore',
               'h5_url', 'native_url', 'pc_url', 'distance', 'longitude', 'latitude', 'p_score', 'fromName',
               'features',
               'featuresNew', 'tagList', 'titleTagInfos']
        self.data_ticket = pd.DataFrame(None, col).T  # 构建空的df,每个城市数据往里追加


    def create_df(self,data_list,city):
        df = pd.DataFrame(data_list)
        df_f = pd.DataFrame(list(df['fields']))
        data_city=(pd.concat([df, df_f], axis=1))
        data_city['cityName'] = city
        self.data_ticket = pd.concat([self.data_ticket, data_city])
        return self.data_ticket

    def get_city_trip(self):
        for city in self.cities :
            if city !='辛集' and city !='利川' and city !='建瓯' :
                print('正在爬取城市:{}的数据!'.format(city))
                # proxies = random.choice(self.proxies.keys())

                # 一、 创建请求response
                res = requests.get('https://travelsearch.fliggy.com/async/queryItemResult.do?searchType='
                                   'product&keyword={}&category=SCENIC&pagenum=1'.format(city),timeout=5,headers=self.headers)  #&category=SCENIC&pagenum=1是指page1(第一页)
                # print(response.text)  #可以打印出来

                # 二、返回请求,json格式
                data = res.json()
                # data=response.content.decode('utf-8')#content读取方法，读出来后是str（因为经过解码）
                # # 将data写入文件
                # with open('data.txt', 'w', encoding='utf-8') as f:
                #     f.write(str(data))

                # 三、取到字典data里的：itemPagenum项，继续向下取数
                itemPagenum = data['data']['data'].get('itemPagenum')  #.get等同于['keyname']
                # print(itemPagenum)
                if itemPagenum is not None:
                    data_list = data['data']['data']['itemProducts']['data']['list'][0]['auctions']

                    #数据读取成df，并追加到data_ticket
                    data_ticket=self.create_df(data_list,city)

                print('成功爬取城市:{}的第{}页数据!'.format(city, 1))

        #TypeError: 'NoneType'object is not subscriptable

                try:
                    page_count = itemPagenum['data']['count']
                except TypeError:
                    pass
                if page_count > 1:
                    for page in range(2, page_count+1): #
                        res = requests.get('https://travelsearch.fliggy.com/async/queryItemResult.do?searchType='
                                   'product&keyword={}&category=SCENIC&pagenum={}'.format(city, page),timeout=5,headers=self.headers)
                        data = res.json()
                        data_list = data['data']['data']['itemProducts']['data']['list'][0]['auctions']

                        # 数据读取成df，并追加到data_ticket
                        data_ticket = self.create_df(data_list, city)
                        print('成功爬取城市:{}的第{}页数据!'.format(city, page))

                self.data_ticket.to_excel('ticket_all_fujian.xlsx', encoding='utf-8', )




if __name__ == '__main__':
    data_crawler = DataCrawler()
    # print(data_crawler.cities)
    # print(data_crawler.col)
    data_crawler.get_city_trip()


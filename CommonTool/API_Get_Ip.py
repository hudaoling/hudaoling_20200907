# 用于发送 HTTP 请求的库
import requests
# 用于解析 HTML 并提取信息
from bs4 import BeautifulSoup
# time 这个库主要用来记录一下时间
import time
import  re
# 在验证 ip 有效性的时候我会开多线程
from queue import Queue
from threading import Thread
'''
队列用于线程间通信。需要注意的是，得从 queue 导入 Queue。
不能从 multiprocessing 导入 Queue，这是用于进程间通信的。
虽然两者用法基本一致，但底层实现不同。
'''




class GetIp(object):

    def __init__(self, verify_site):
        '''类初始化。
        :param str verify_site: 用于对代理ip进行测试的网站，可以填入要爬的网站链接。
        '''
        # proxy_list 保存从西刺爬下来的代理
        self.proxy_list = []
        # success_list 保存验证通过的代理
        self.success_list = []
        self.site = verify_site


    def get_proxies(self):
        '''从西刺首页获取 http 和 https 代理地址并存入实例变量 proxy_list。'''
        # u0='https://www.xicidaili.com/' #西刺
        # u1='https://ip.jiangxianli.com /?page = 1' #免费IP代理库
        # u2='https://www.kuaidaili.com/free /inha/2/' #快代理
        for n in ['nn']:
            for i in range(1,2):
                url='https://www.xicidaili.com/{}/{}'.format(n,i)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
                }

                start = time.time()# 记录开始时间
                print('start crawling ip...')
                try:
                    # 发送http请求，加一个 User-Agent 的请求头让服务器觉得我们不像爬虫脚本，
                    html = requests.get(url, headers=headers)
                except:
                    # 若请求失败则抛出异常，中断程序，因为获取不到网页内容，继续下去也没意义了。
                    raise

                # 以下的解析部分的注释省去，各位看一下 BeautifulSoup 的文档就知道了，不是本文的重点。
                soup = BeautifulSoup(html.text, 'lxml')
                trs = soup.find('table', id='ip_list').find_all('tr', class_=['', 'odd'])[2:]
                for tr in trs:
                    scheme = tr.findAll('td', class_="")[-3].get_text().lower()
                    valid_time = tr.findAll('td', class_="")[-2].get_text()
                    valid_time_unit = re.findall('\D', valid_time)[0]

                    if i==1 and scheme in ['http', 'https'] and valid_time_unit in ['天','小时'] :
                        ip = tr.findAll('td', class_="")[0].get_text()
                        port = tr.findAll('td', class_="")[1].get_text()
                        proxy = scheme + '://' + ip + ':' + port
                        self.proxy_list.append(proxy)

                    elif i>1 and scheme in ['http', 'https'] and valid_time_unit in ['天']:
                        ip = tr.findAll('td', class_="")[0].get_text()
                        port = tr.findAll('td', class_="")[1].get_text()
                        print('here', scheme, valid_time)
                        proxy = scheme + '://' + ip + ':' + port
                        self.proxy_list.append(proxy)

                # 打印运行时间
                print('[Get Proxies]total time: %.2f' % (time.time() - start))


    def run(self):
        ''' 负责获取代理，开启多线程任务对代理地址进行验证。'''
        self.get_proxies()
        start = time.time()
        # 实例化一个队列对象
        proxy_q = Queue()
        print('Verifying proxies...')
        # thread_list 列表保存线程
        thread_list = []
        # 把爬下来的代理地址逐个放进队列
        for p in self.proxy_list:
            proxy_q.put(p)
        # 开启15个线程并放入thread_list
        # 最后往队列放入数量与线程一样的数字0，作为每个线程结束的标记
        for _ in range(15):
            thread_list.append(Thread(target=self.verify_proxies, args=(proxy_q,))) #调用verify_proxies
            proxy_q.put(0)
        for w in thread_list:
            # 启动线程
            w.start()
        for w in thread_list:
            # 等待线程终止
            w.join()
        print('[verification] total time: %.2f s' % (time.time() - start))
        print('proxies verified !')



    def verify_proxies(self, proxy_q):
        '''顾名思义，验证代理的有效性。'''
        ''':param list proxy_q: 待验证的代理队列'''

        # 写一个死循环不断从传入队列中获取代理地址
        while 1:
            proxy = proxy_q.get()
            # 若获取到的值是 0，即退出循环，线程终止
            if proxy == 0:  break
            protocol = 'https' if 'https' in proxy else 'http'
            proxies = {
                protocol: proxy
            }
            # print('proxies',proxies)
            try:
                # 若返回状态码不等于200、或在HTTP连接过程中发生其他错误，则抛出异常
                # 设置连接超时时间为3秒
                # self.site为初始化时设置的测试链接
                assert requests.get(self.site, timeout=3, proxies=proxies).status_code == 200
            except:
                print('[fail] %s' % proxy)
            else:
                print('[success] %s' % proxy)
                # 保存验证通过的代理
                self.success_list.append(proxies)

#获取芝麻代理的IP列表
class Get_zhima:

    def __init__(self, url_zhima):
        self.url=url_zhima
        self.proxy_list = []

    def get_zhima_ip(self):
        res=requests.get(self.url)
        data=res.content.decode()
        ips=list(i.strip() for i in data.split('\r\n') if i !='')
        for ip in ips:
            ip_list = {}
            ip_list["https"] = ip

            self.proxy_list.append(ip_list)

        return  self.proxy_list



if __name__ == '__main__':
    print('Test Site: {}'.format('http://www.hiyd.com/dongzuo/'))
    g = GetIp('http://www.hiyd.com/dongzuo/')  #实例化
    g.run()  #调用run
    print(g.success_list)

    url_zhima = 'http://http.tiqu.alicdns.com/getip3?num=102&type=1&pro=&city=0&yys=0&port=11&pack=97654&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'
    url_zhima2 = 'http://http.tiqu.alicdns.com/getip3?num=198&type=1&pro=&city=0&yys=0&port=1&pack=97654&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'
    url_zhima3='http://http.tiqu.alicdns.com/getip3?num=400&type=1&pro=&city=0&yys=0&port=11&pack=97654&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'
    url_zhima4='http://http.tiqu.alicdns.com/getip3?num=196&type=1&pro=&city=0&yys=0&port=1&pack=97654&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'

    zhima=Get_zhima(url_zhima) #实例化
    zhima.get_zhima_ip()  #调用
    print(zhima.proxy_list)




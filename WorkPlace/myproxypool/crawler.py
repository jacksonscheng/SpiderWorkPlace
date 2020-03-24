import json
import re
from utils import get_page
from pyquery import PyQuery as pq


#创建一个元类，继承与type
#创建一类就是元类，其他都是定义一个类，继承与其他类
#元类和类关系，相当于于，类和对象的关系
class ProxyMetaclass(type):
    
    #定义类的基本属性，这样可以当做的__init__，在
    #类创建的时候创建如下属性
    def __new__(cls, name, bases, attrs):
        count = 0
        #创建一个方法列表的属性
        attrs['__CrawlFunc__'] = []
        #如果在类里面找到以crawl_开头的就把它加入列表，并做统计
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        #增加统计属性
        attrs['__CrawlFuncCount__'] = count
        #返回这个新的类对象
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies
      
    #过期 
    # def crawl_daxiang(self):
    #     url = 'http://vtp.daxiangdaili.com/ip/?tid=559363191592228&num=50&filter=on'
    #     html = get_page(url)
    #     if html:
    #         urls = html.split('\n')
    #         for url in urls:
    #             yield url
          
    def crawl_daili66(self, page_count=4):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    if not (ip==None and port==None):
                        # print(':'.join([ip, port]))
                        yield ':'.join([ip, port])
     
    # def crawl_ip3366(self):
    #     #page数量
    #     for page in range(1, 8):
    #         start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
    #         html = get_page(start_url)
    #         ip_adress = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
    #         # \s * 匹配空格，起到换行作用
    #         re_ip_adress = ip_adress.findall(html)
    #         for adress, port in re_ip_adress:
    #             result = adress+':'+ port
    #             #把空格替换为逗号
    #             yield result.replace(' ', '')   


    def crawl_xicidali(self, page_count=5):
        '''
        获取代理xiciadali的代理
        Parameters
        ----------
        page_count : TYPE, optional
            DESCRIPTION. The default is 4.
            爬取多少页
        Returns 代理
        '''
        urls = [' https://www.xicidaili.com/nn/{}'.format(x) for x in range(page_count+1)]
        
        for url in urls:
            print('Crawl',url)
            html = get_page(url)
            if html:
                doc = pq(html)
                #gt(0)0表示第一个，从第二个开始选择
                #多个结果用items
                trs = doc('.clearfix table tr:gt(0)').items()
                for tr in trs:
                    #选择一个td
                    ip = tr.find('td:nth-child(2)').text()
                    port = tr.find('td:nth-child(3)').text()
                    #建立以个proxes的集合，即一个代理的list
                    # print(':'.join([ip, port]))
                    yield ':'.join([ip, port])  

    def crawl_xsdali(self, page_count=40):
        '''
        获取代理xiciadali的代理
        Parameters
        ----------
        page_count : TYPE, optional
            DESCRIPTION. The default is 4.
            爬取多少页
        Returns 代理
        '''
  
        start_page = 2012
        urls = ['http://www.xsdaili.com/dayProxy/ip/{}.html'.format(x) for x in range(start_page,start_page+page_count+1)]
        
        for url in urls:
 
            print('Crawl',url)
            html = get_page(url)
            #这个br的标记是<br>...<br>            
            if html:
                exp = '<br>.*?(\d+.\d+.\d+.\d+:\d+)@'
                results = re.findall(exp, html, re.S)
                for result in results:
                    # print(result)
                    yield result
                    

    # def craw_iphai(self, page_count=0):
    #     '''
    #     获取代理海的代理
    #     Parameters
    #     ----------
    #     page_count : TYPE, optional
    #         DESCRIPTION. The default is 4.
    #         爬取多少页
    #     Returns 代理
    #     '''
    #     url = 'http://www.iphai.com/free/ng'

    #     print('Crawl',url)
    #     html = get_page(url)
    #     if html:
    #         doc = pq(html)
    #         #gt(0)0表示第一个，从第二个开始选择
    #         #多个结果用items
    #         trs = doc('.table-responsive table tr:gt(0)').items()
    #         for tr in trs:
    #             #选择一个td
    #             ip = tr.find('td:nth-child(1)').text()
    #             port = tr.find('td:nth-child(2)').text()
    #             #建立以个proxes的集合，即一个代理的list
    #             print(':'.join([ip, port]))
    #             # yield ':'.join([ip, port]) 
    # def crawl_goubanjia(self):
    #     """
    #     获取Goubanjia
    #     :return: 代理
    #     """
    #     start_url = 'http://www.goubanjia.com/free/gngn/index.shtml'
    #     html = get_page(start_url)
    #     if html:
    #         doc = pq(html)
    #         tds = doc('td.ip').items()
    #         for td in tds:
    #             td.find('p').remove()
    #             yield td.text().replace(' ', '')

   
    # def crawl_ip181(self):
    #     start_url = 'http://www.ip181.com/'
    #     html = get_page(start_url)
    #     ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
    #     # \s* 匹配空格，起到换行作用
    #     re_ip_adress = ip_adress.findall(html)
    #     for adress,port in re_ip_adress:
    #         result = adress + ':' + port
    #         yield result.replace(' ', '')


    # def crawl_data5u(self):
    #     for i in ['gngn', 'gnpt']:
    #         start_url = 'http://www.ip3366.net/free/?stype=1'.format(i)
    #         html = get_page(start_url)
    #         ip_adress = re.compile('<ul class="l2">\s*<span><li>(.*?)</li></span>\s*<span style="width: 100px;"><li class=".*">(.*?)</li></span>')
    #         # \s * 匹配空格，起到换行作用
    #         re_ip_adress = ip_adress.findall(html)
    #         for adress, port in re_ip_adress:
    #             result = adress+':'+port
    #             yield result.replace(' ','')

    # def crawl_kxdaili(self):
    #     for i in range(1, 4):
    #         start_url = 'http://www.kxdaili.com/ipList/{}.html#ip'.format(i)
    #         html = get_page(start_url)
    #         ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
    #         # \s* 匹配空格，起到换行作用
    #         re_ip_adress = ip_adress.findall(html)
    #         for adress, port in re_ip_adress:
    #             result = adress + ':' + port
    #             yield result.replace(' ', '')


    # def crawl_premproxy(self):
    #     for i in ['China-01','China-02','China-03','China-04','Taiwan-01']:
    #         start_url = 'https://premproxy.com/proxy-by-country/{}.htm'.format(i)
    #         html = get_page(start_url)
    #         if html:
    #             ip_adress = re.compile('<td data-label="IP:port ">(.*?)</td>') 
    #             re_ip_adress = ip_adress.findall(html)
    #             for adress_port in re_ip_adress:
    #                 yield adress_port.replace(' ','')

    # def crawl_xroxy(self):
    #     for i in ['CN','TW']:
    #         start_url = 'http://www.xroxy.com/proxylist.php?country={}'.format(i)
    #         html = get_page(start_url)
    #         if html:
    #             ip_adress1 = re.compile("title='View this Proxy details'>\s*(.*).*")
    #             re_ip_adress1 = ip_adress1.findall(html)
    #             ip_adress2 = re.compile("title='Select proxies with port number .*'>(.*)</a>") 
    #             re_ip_adress2 = ip_adress2.findall(html)
    #             for adress,port in zip(re_ip_adress1,re_ip_adress2):
    #                 adress_port = adress+':'+port
    #                 yield adress_port.replace(' ','')
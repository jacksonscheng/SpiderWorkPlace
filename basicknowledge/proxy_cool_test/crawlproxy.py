# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:19:22 2020

@author: Administrator
"""


import json
from utils import get_page
from pyquery import PyQuery as pq
import re

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)
    

class Crawler(object, metaclass=ProxyMetaclass):
    #callback是函数作为参数,应该一个验证proxy是否可用的函数
    def get_proxies(self, callback):
        proxies = []
        #eval返回一个字符串表达式的值
        for proxy in eval("self.{}()".format(callback)):
            print("get proxy!",proxy)
            proxies.append(proxy)
            return proxies
        
    def craw_daili66(self, page_count=30):
        '''
        获取代理66的代理
        Parameters
        ----------
        page_count : TYPE, optional
            DESCRIPTION. The default is 4.
            爬取多少页
        Returns 代理
        '''
        start_page = 3
        urls = ['http://www.66ip.cn/{}.html'.format(x) for x in range(start_page, page_count+1)]
        
        for url in urls:
            print('Crawl',url)
            html = get_page(url)
            if html:
                doc = pq(html)
                #gt(0)0表示第一个，从第二个开始选择
                #多个结果用items
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    #选择一个td
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    #建立以个proxes的集合，即一个代理的list
                    # print(':'.join([ip, port]))
                    yield ':'.join([ip, port])
                
    def craw_iphai(self, page_count=0):
        '''
        获取代理海的代理
        Parameters
        ----------
        page_count : TYPE, optional
            DESCRIPTION. The default is 4.
            爬取多少页
        Returns 代理
        '''
        url = 'http://www.iphai.com/free/ng'

        print('Crawl',url)
        html = get_page(url)
        if html:
            doc = pq(html)
            #gt(0)0表示第一个，从第二个开始选择
            #多个结果用items
            trs = doc('.table-responsive table tr:gt(0)').items()
            for tr in trs:
                #选择一个td
                ip = tr.find('td:nth-child(1)').text()
                port = tr.find('td:nth-child(2)').text()
                #建立以个proxes的集合，即一个代理的list
                # print(':'.join([ip, port]))
                yield ':'.join([ip, port])     
                  
                
    def craw_xicidali(self, page_count=30):
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
                    print(':'.join([ip, port]))
                    # yield ':'.join([ip, port])        
        
    
    def craw_xsdali(self, page_count=30):
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
                exp = '<br>.*?\d+.\d+.\d+.\d+:\d+@'
                results = re.findall(exp, html, re.S)
                for result in results:
                    print(result)
                    # yield result

       
        
            
            

                
        


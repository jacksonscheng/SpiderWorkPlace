'''
@模块说明：
01-调用RedisClient和Crawler类
02-爬取数据加入redis


'''


from db import RedisClient
from crawler import Crawler
from setting import *
import sys

class Getter():
    
   
    def __init__(self):
        '''
        初始化过程中实例化一个redis和一个crwal对象
        '''
        self.redis = RedisClient()
        self.crawler = Crawler()
    

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    
    def run(self):
        print('获取器开始执行')
        
        #如果代理数量太多，默认不执行获取工作
        if not self.is_over_threshold():
            
            #crawler.__CrawlFuncCount__获取有crawl开头方法的个数
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                
                #crawler.__CrawlFunc__获取crawl方法的列表
                callback = self.crawler.__CrawlFunc__[callback_label]
                
                # 调用方法获取代理,这里的callback指的是某个具体的爬取函数
                proxies = self.crawler.get_proxies(callback)
                
                '''
                在python中，执行结果都是经由sys.stdout()输出的，而stdout具有缓冲区，
                即不会每一次写入就输出内容，而是会在得到相应的指令后才将缓冲区的内容输出。
                sys.stdout.flush()的作用就是显示地让缓冲区的内容输出。
                '''
                sys.stdout.flush()
                
                #把proxy加入reids
                for proxy in proxies:
                    self.redis.add(proxy)




    



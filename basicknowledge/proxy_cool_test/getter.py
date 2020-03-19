# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:58:13 2020

@author: Administrator
"""


from proxy_cool_test.redispool import RedisClient
from proxy_cool_test.crawlproxy import Crawler

POOL_UPPER_THRESHOLD = 10000

class Getter():
    
    def __init__(self):
        self.redis = RedisClient()
        self.cralwer = Crawler()
        
    def is_over_threshold(self):
        if self.redis.count() > POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    def run(self):
        print("获取器开始执行")
        if not self.is_over_threshold():
            for callback_label in range(self.crawer.__CrawFunCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)
                    
    
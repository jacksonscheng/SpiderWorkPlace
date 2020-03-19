# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:50:58 2020

@author: Administrator
"""

import redis
from random import choice


MAX_SCORE = 100
MIN_SCORE = 0
INITAL_SCRE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯竭')

class RedisClient():
    
    #这种方式只创建了一个实例变量db
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, 
                                    port=port, password=password)
    
    def add(self, proxy, score=INITAL_SCRE):
        #Redis Zscore 命令返回有序集中，成员的分数值。 如果成员元素不是有序集 key 的成员，或 key 不存在，返回 nil
        
        #返回元素proxy的score
        if not self.db.zscore(REDIS_KEY, proxy):
            #如果没有score，则赋值为初始值score
            return self.db.zdd(REDIS_KEY, {proxy:score})
    
    def random(self):
        #通过score排序找到分数都是100的元素
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
    
        if len(result):
            return choice(result)
        #如果没有找排名0到100的这里的100是排名不是分数
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):  
                return result
            #如果没有rasieError
            else:
                raise PoolEmptyError
    
    def decrease(self, proxy):
        
        score = self.db.zscore(REDIS_KEY, proxy)
        if score > MIN_SCORE:
            print("代理：", proxy,"当前分数", score,"减1")
            return self.db.zincrby(REDIS_KEY, -1, proxy)
        
        else:
            print("代理：", proxy,"当前分数", score,"remove！")
            #删除
            return self.db.zrem(REDIS_KEY, proxy)
    
    def exists(self, proxy):
        
        return not self.db.zscore(REDIS_KEY, proxy)==None
    

    
    def set_max_score(self, proxy):
        print('代理',proxy,'可用，分数设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, {proxy:MAX_SCORE})
    
    def count(self):
        return self.db.zcard(REDIS_KEY)
    
    def all_proxies(self):
        #返回所有代理的代理的列表
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)        
        
    
    
    
 
            
        
    
    
    
    
    
    
    
    
                               
    
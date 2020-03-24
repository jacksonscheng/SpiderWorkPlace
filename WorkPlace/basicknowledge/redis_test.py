# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:45:52 2020

@author: Administrator
"""

from redis import StrictRedis as sr
from redis import ConnectionPool as cp

redis = sr(host='localhost', port=6379, db=0)

#设置和提取一个值
redis.set('name','bob')
redis.get('name')



#hash
dict={
    'name':'mike',
    'age': 12
      }
redis.hmset('user2', dict)
redis.hmget('user2','name')
redis.hmget('user2',['name', 'age'])


#列表
redis.rpush('names', 'jack', 'mike', 'time', 'job')
#列表头添加
redis.lpush('names', 'first')
#列表尾
redis.rpush('names', 'lastname')

#length of list
redis.llen('names')

redis.lrange('names', 0,4)

#集合set添加
redis.sadd('ages',1,2,3,4,5,4,2,7,8,1,'jack','sea','alen','cha')



#有序集合
dict2 = {
    'bobo': 100,
    'jaja': 95,
    'xx': 90,
    'jj':20,
    'thd':60,
    'dfer':10
      }
redis.zadd('grades', dict2)
redis.zadd('grades', {'jakcer':10})

#delete集合里面的元素'bobo'
redis.zrem('grades','bobo')

redis.zincrby('grades', )

#第一位索引是0
redis.zrank('grades','dfer')


redis.zrevrange('grades',0,0)

redis.zrevrangebyscore('grades', 100, 100)

#返回元素的个数
redis.zcard('grades')








# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:36:10 2020

@author: Administrator
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:28:13 2020

@author: Administrator
@content: 利用模拟ajax请求爬取魔兽世界微博的信息
"""


from urllib.parse import urlencode
import requests as reqs
from pyquery import PyQuery as pq
from pymongo import MongoClient
import time
import random


#这里是ajax请求的url
base_url = 'http://m.weibo.cn/api/container/getIndex?'

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"

headers = {
    'Host': 'm.weibo.cn',
    'Refers': 'https://m.weibo.cn/u/2318754072',#这里是html的网页
    'User-Agent': USER_AGENT,
    'X-Requested-With': 'XMLHttpRequest' 
    }


def get_page(since_id):
    # since_id = ''
    params = {
        'type': 'uid',
        'value': 2318754072,
        'containerid': '1076032318754072',
        'next_page': since_id
        }
    #urlencode构造get请求参数用来加在url中
    url = base_url + urlencode(params)
    try:
        response = reqs.get(url, headers=headers)
        if response.status_code ==200:
            return response.json()
    except reqs.ConnectionError as e:
        print('Error', e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')     
        for item in items:
            #针对有些item里面没有mblog的时候。例如wow第一条card就没有
            if item.get('mblog'):
                item = item.get('mblog')
                weibo = {}
                weibo['id'] = item.get('id')
                #这里因为get('text')得到内容再用pq初始化
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('commets_count')
                weibo['reposts'] = item.get('reposts_count')
                weibo['views'] = item.get('obj_ext')
                weibo['createtime'] = item.get('created_at')
                yield weibo


#这里刷新翻页没有了书中的pages参数
# 我们方向每次请求内容中的cardlistInfo中的since_id就是下一页的一个参数代码
# 因此把它加入到请求参数中
def get_next_page(json):
    next_page = json.get('data').get('cardlistInfo').get('since_id')
    return next_page
  


#打开Mongo把字典数据传入
def create_mongodb(dbname, tabname):
    client = MongoClient(host='localhost', port=27017)
    db = client[dbname] #如果没有则创建一个weibo db
    collection = db[tabname] #创建表 如果没有则创建一个collection表
    return collection



def main(pages):
    count = 0
    
    #当since_id内容为空可以把它看做一个首页
    since_id = ''
    table = create_mongodb('WOW','weibo')
    for i in range(pages):
        json = get_page(since_id)
        since_id  = get_next_page(json)
        result = parse_page(json)
        for info in result:
            if table.insert_one(info):
                count += 1
                print("savded to mongo"+str(count))
        time.sleep(2*random.random())

        

if __name__== '__main__':
    main(10)
    

    
            


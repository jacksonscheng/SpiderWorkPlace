# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 08:39:15 2020

@author: Administrator
@content:crawl the toutiao picures
@attention: 在header里面加入cookies，才能有效地获取response
"""

#
import os
import requests as reqs
from hashlib import md5
from pyquery import PyQuery as pq
from pymongo import MongoClient
from urllib.parse import urlencode
from urllib.robotparser import RobotFileParser
from multiprocessing.pool import Pool




#用来检验对象网址是否可以爬取，在实际操作中有问题
# 例如检查网址为false，但是实际上加入cookies以后是可以爬取的
def can_crawl(url):
    rp = RobotFileParser()
    rp.set_url('https://www.toutiao.com/robots.txt')
    rp.read()
    return (rp.can_fetch('*', url))


def get_page(offset):
      
    USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    COOKIES = 'tt_webid=6804222868491355656; s_v_web_id=verify_k7salhqm_FPENkc2r_zBW1_459g_AkcL_WVqsOMVsHn8d; \
    ttcid=62b3e0f2a0ce4e0f90719c0d41caa5fd15; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6804222868491355656; \
        SLARDAR_WEB_ID=189003bf-3c91-4579-85f7-f82ccc97808d; csrftoken=b0955571e056a26459afe8c655763703; \
            __tasessionId=pwbw7na1u1584235021658; tt_scid=3xrNBIN-xNkdXvRsvaJ.NGYQiv4E62utTrgI0Ug3IyasNjq1Oned3erT2ptK3.JWdac4'
    
    #在实际的爬取中headers的参数最好都加上，不加很有可能返回的response是None
    headers = {
        'Cookie': COOKIES,
        'Host': 'www.toutiao.com',
        'Refers': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',#这里是html的网页
        'User-Agent': USER_AGENT,
        'X-Requested-With': 'XMLHttpRequest' 
        }
    
   
    #构造url的get参数，实际的构造中不需要和原url一摸一样，应该选择关键部分
    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format':'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
        }
    

    url = 'https://www.toutiao.com/api/search/content/?'+urlencode(params)
        


    try:
        response = reqs.get(url, headers=headers)
        if response.status_code==200:
            return response.json()
    except reqs.ConnectionError:
        print("Connecion Error!")
        return None


#从返回的json中选取data部分
def get_img(json):
    if json.get('data'):
        for item in json.get('data'):
            #实际的data不是所有的item都是我们需要的图片信息块
            #只有item中包含abstract的item才有图片的链接
            if item.get('abstract'):        
                yield {
                    'img':item.get('large_image_url'),
                    'title': item.get('title')
                    }
                

#利用保存的图片的图片链接下载图片 
def save_img(item):
    files = 'pictures'
    if not os.path.exists(files):
        os.mkdir(files)

    try:
        response = reqs.get(item.get('img'))
        if response.status_code==200:
            #使用图片内容的md5值，来到达去重复的目的
            file_path = "{0}/{1}.{2}".format(files, md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open (file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print("Already Downloaded,", file_path)
        else:
            print("Failed to Save images!")
    except reqs.ConnectionError:
        print('Connection Error!')
        


def main(offset):
    json = get_page(offset)
    for item in get_img(json):
        print(item)
        save_img(item)
 

GROUP_START = 1
GROUP_END = 60


#这里应用了多进程池来运行多个main()
if __name__ == '__main__':
    pool = Pool()
    groups = ([x*20 for x in range(GROUP_START,GROUP_END+1)])
    #　Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到结果返回
    pool.map(main, groups)
    #　关闭进程池（pool），使其不在接受新的任务
    pool.close()
    #主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用
    pool.join()

    
    
















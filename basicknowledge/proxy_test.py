# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:57:26 2020

@author: Administrator
"""


import requests as reqs

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

proxy = '41.254.46.154:9999'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
    }

try:
    response = reqs.get('https://www.runoob.com', headers=base_headers, proxies=proxies, timeout=20)
    print(response.text)
except reqs.exceptions.ConnectionError as e:
    print('Error', e.args)
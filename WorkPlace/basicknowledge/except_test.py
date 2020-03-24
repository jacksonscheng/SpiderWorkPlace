# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 07:52:56 2020

@author: Administrator
"""


# =============================================================================
# 处理异常
# =============================================================================

# 01 URLEeeor

#  示例：打开一个不存在的url
from urllib import request, error

try:
    response = request.urlopen('https://www.dajiayiqilaixuepthon.com')

except error.URLError as e:
    print(e.reason)


#  02-HTTPError

from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.com')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')


# 因为URLError是HTTPEror的父类，因此可以选择先捕获子类错误，再捕获父类

try:
    response = request.urlopen('https:caichuichong.com/')
except error.HTTPError as e:
    print(e.code, e.reason, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')



#reason返回一个对象

import socket
from urllib import request, error

try:

    # 设置超时时间来强制抛出timeout错误
    response = request.urlopen('https://www.baidu.com', timeout=0.1)
except error.URLError as e:

    # e是socket.timeout类型
    print(e.reason)
    print(type(e))
    if isinstance(e.reason, socket.timeout):
        print('Time out!')








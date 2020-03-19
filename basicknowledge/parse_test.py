# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:56:27 2020

@author: Administrator
"""
# =============================================================================
# 解析链接
# =============================================================================

# 01 urlparse

from urllib.parse import urlparse


result1 = urlparse('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E7%BD%91%E6%98%93%E9%82%AE%E7%AE%B1%E7%99%BB%E5%BD%95&oq=%25E7%25BD%2591%25E6%2598%2593&rsv_pq=a08ca83300048302&rsv_t=2bd11d5Q1XXDm1DYkWc64q602xqLOMN8DLSoNmaPoZW7HKpJP%2BlgbVaQW2Y&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=8&rsv_sug1=8&rsv_sug7=101&rsv_sug2=0&inputT=9622&rsv_sug4=10683')
result = urlparse('https://www.baidu.com/index.html;user?id=5')
print(result1)

'''
urlparse(ulrstring, scheme='', allow_fragments=True)


'''

result = urlparse('www.baidu.com/index.html;user?id=5#comment',
                  allow_fragments=True
                  )

print(result)


# 02 urlunparse,
# 把字符串拼接为url

from urllib.parse import urlunparse

data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'commet']
result = urlunparse(data)
print(result)



# 03 urlsplit
# 解构url成5个部分

from urllib.parse import urlsplit

result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

# 04 urlunsplit
# 解构url成5个部分
from urllib.parse import urlunsplit

url_list = [x for x in result]

result = urlunsplit(url_list)

print(result)



#  unquote
# 把汉字的url编码转为汉字
from urllib.parse import unquote

url='%E7%BD%91%E6%98%93%E9%82%AE%E7%AE%B1%E7%99%BB%E5%BD%95'
print(unquote(url))






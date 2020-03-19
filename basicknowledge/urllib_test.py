# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:55:19 2020

@author: Administrator
"""


from urllib import request, parse

# =============================================================================
# urlopen()
# =============================================================================

#爬取百度首页的网页源代码

response = request.urlopen("https://www.python.org")
print(response.read().decode("utf-8"))
print(type(response))#这里得到了一个HTTPResponse对象
print(response.status)#得到状态码
print(response.getheaders())#响应头



#（1）open的data参数

data = bytes(parse.urlencode({'word':'hello'}),encoding='utf')
response = request.urlopen("https://httpbin.org/post",data=data)
print(response.read())


#（2）timeout
response2 = request.urlopen("http://httpbin.org/post",timeout=1)
print(response2.read())

#应用举例
#说明如果程序过了0.1秒后服务器还没有响应则打印信息

import socket
from urllib import request, error

try:
    response = request.urlopen("http://httpbin.org/post", timeout=0.1)

except error.URLError as e:

    #如果异常类型是timeout类型就打印信息
    if isinstance(e.reason, socket.timeout):
        print("timeout")


# =============================================================================
# #Request
# =============================================================================

from urllib import request

req = request.Request("https://www.baidu.com")
response = request.urlopen(req)
print(response.read().decode('utf-8'))


#利用Request构造多个参数
from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
    'Host': 'httpbin.org',
}

# 构造data参数的字典
dict= {
    'name': 'Germey'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req, timeout=3)
print(response.read().decode('utf-8'))

 # 此外还可以用add_header来加入header
# req = request.Request(url=url, data=data, method='POST')
# req.add_header(headers)


# =============================================================================
# 表单验证
# =============================================================================
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username  = 'username'
password = 'password'
url = 'http://localhost:5000'

p  = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)


# =============================================================================
# 爬虫代理
# =============================================================================


from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# 下面的内容为代理地址，可添加多个代理
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743',
})

#构造opener发送请求
opener = build_opener(proxy_handler)

try:
    response = opener.open('https://wwww.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)


# =============================================================================
# #Cookies
# =============================================================================


# 如何将网站上cookies获取下来

import http.cookiejar, urllib.request
from urllib import error

filename = 'cookies.txt'

# 声明一个cookiejar对象
# 把cookie保存为文件
cookie = http.cookiejar.MozillaCookieJar(filename);
cookie = http.cookiejar.LWPCookieJar(filename);
# 构建一个Handler
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True, ignore_expires=True)


# 读取利用生成的cookie

cookie = http.cookiejar.LWPCookieJar();
cookie.read('cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http//www.baid.com')
print(response.read().decode('utf-8'))
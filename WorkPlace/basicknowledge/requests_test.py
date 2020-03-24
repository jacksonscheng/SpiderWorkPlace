# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:34:40 2020

@author: Administrator
"""

# =============================================================================
# Requests库的使用
# =============================================================================


# =============================================================================
# get
# =============================================================================
import requests as reqs


r = reqs.get('http://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)


r1 = reqs.post('http://httpbin.org/post')
r2 = reqs.put('http://httpbin.org/put')
r3 = reqs.delete('http://httpbin.org/delete')
r4 = reqs.head('http://httpbin.org/get')
r5 = reqs.options('http://httpbin.org/get')


#  get请求
r = reqs.get('http://httpbin.org/get')
print(r.text)

url_test = 'http://httpbin.org'


# 对于请求中添加信息

data = {
    'name': 'jack',
    'age':22
}

r= reqs.get(url_test+'/get', params=data)
print(r.text)

# 转换为json格式
print(r.json())


#抓取网页

import requests as reqs
import re

#加入浏览器的标识
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
 AppleWebKit/537.36(KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

r = reqs.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern, r.text)
print(titles)


# 抓取图片，抓取的内容是二进制
r = reqs.get('https://github.com/favicon.ico')
print(r.text)# 二进制转换为Str打印，出来是乱码
print(r.content)# 二进制的内容

#将二进制文件进行保存
#第一个参数是文件名，第二个参数是以二进制形式打开
with open('favicon.ico', 'wb') as f:
    f.write(r.content)


# 添加header
r = reqs.get('http://www.zhihu.com/explore')
print(r.text)
#这样请求是得不到雷同的，要加入header里面的User-Agent信息

# =============================================================================
# Post
# =============================================================================

# 将参数提交到网页的Form中
data = {'name': 'jack', 'age': '22'}
r = reqs.post("http://httpbin.org/post", data=data)
print(r.text)


# get responser
r = reqs.get("https://www.jianshu.com")
print(type(r.status_code,), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)


# 通过比较返回码和内置成功返回码来保证请求得到了正常的响应

r = reqs.get("https://www.jianshu.com")

#如果请求码不等于成功码退出，否则打印请求成功
exit() if not r.status_code == reqs.codes.ok else print("Request Successfully!")


# =============================================================================
# Requests高级用法
# =============================================================================
# 文件上传

files = {'file': open('favicon.ico', 'rb')}
r = reqs.post("http://httpbin.org/post", files=files)
print(r.text)

# cookies

r = reqs.get("https://www.baidu.com")
print(r.cookies)

for key, value in r.cookies.items():
    print(key+'='+value)

# ####l利用cookie来维持登录
headers = {
    'Cookie':'csdn_tt_dd=v10_b1d1a0a0376183e2046e717fbfe5c72e2cb2106a8b9035850a9dc55aadfb1195; kd_user_id=6e1a0e22-0286-4aa2-aaf8-b10f07e6392f; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216002083edb11d-050d7410fc84db-6b1b1279-1296000-16002083edc5a9%22%2C%22%24device_id%22%3A%2216002083edb11d-050d7410fc84db-6b1b1279-1296000-16002083edc5a9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; gr_user_id=4a979d5e-6aa4-4b91-9bd4-9f78e3652cb4; smidV2=20180417175642282be30c5ebaed9ba57398f5978fc2d100648e6522badf670; dc_session_id=10_1531970711424.296899; uuid_tt_dd=10_30851393880-1564584839502-175798; UN=u011560780; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_30851393880-1564584839502-175798!1788*1*PC_VC!5744*1*u011560780; __gads=ID=f7fae8175b3e9e55:T=1581049556:S=ALNI_MasS-7-FblHWhf3_CSXgC51rnASiw; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblog.csdn.net%252Fblogdevteam%252Farticle%252Fdetails%252F103603408%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; TY_SESSION_ID=04c0281f-fc85-4266-b6c9-e73dac96977c; c_ref=https%3A//www.baidu.com/link%3Furl%3DfSKWBVni1CPNn5xQsIEzOnHtAN_sIJwBj1jA-iBpMV7%26wd%3D%26eqid%3De3d3520f0006921c000000065e684a27; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1583846572,1583847562,1583890593,1583893037; c-login-auto=1; SESSION=383d5013-f0b0-4197-a21f-0ed4a0d15ff5; dc_tos=q70buu; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1583893255; UserName=u011560780; UserInfo=6cb72b9d45ea4c9c98cbee823e804d88; UserToken=6cb72b9d45ea4c9c98cbee823e804d88; UserNick=viode; AU=872; BT=1583893281034; p_uid=U000000',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Host':'www.csdn.net'
    }

r = reqs.get("https://www.csdn.net/", headers=headers)
print(r.text)

# 利用Sesson维持同一个会话

s = reqs.Session()
s.get("http://httpbin.org/cookies/set/number/123456789")
r = s.get("http://httpbin.org/cookies")
print(r.text)

# =============================================================================
# SSL证书验证
# =============================================================================
response = reqs.get("https://www.12306.cn", verify=False)
print(response.status_code)

#


# =============================================================================
# 代理设置
# =============================================================================

proxy = {
    'http': 'http://10/10/1/10:3128',
    'httpS': 'http://10/10/1/10:3128'
}

r = reqs.get("https://taobao.com", proxy=proxies)



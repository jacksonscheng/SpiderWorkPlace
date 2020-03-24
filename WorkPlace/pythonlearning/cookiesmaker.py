# # -*- coding: utf-8 -*-
# """
# Created on Sun Mar 15 23:13:51 2020

# @author: Administrator
# """

# # -*- coding: utf-8 -*-

# import json
# import urllib
# import cookielib

# from pyquery import PyQuery as pq

# class YMT(object):

#     def __init__(self):
#         """
#         读取从 EditThisCookie 上获取的cookie
#         并将其绑定到 urllib2 上
#         以后每次爬虫访问网站时都会自动带上cookie，不再需要人工参与
#         """

#         cookie_jar = cookielib.MozillaCookieJar()
#         cookies = open('taobaologin.txt').read()
#         for cookie in json.loads(cookies):
#             cookie_jar.set_cookie(cookielib.Cookie(version=0, name=cookie['name'], value=cookie['value'], port=None, port_specified=False, domain=cookie['domain'], domain_specified=False, domain_initial_dot=False, path=cookie['path'], path_specified=True, secure=cookie['secure'], expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False))

#         opener = urllib.build_opener(urllib.HTTPCookieProcessor(cookie_jar),urllib.HTTPHandler)
#         urllib.install_opener(opener)

#     def _get(self, url):
#         """
#         :param url: 需要访问的url
#         :return:    返回该url的网页内容
#         """

#         request = urllib2.Request(url=url)
#         request.add_header('Referer', 'http://meddic.medlive.cn/search/search.do')
#         response = urllib2.urlopen(request)
#         data = response.read()
#         return data

#     def get_word_translate(self,word):
#         """
#         :param word: 需要翻译的英文单词
#         :return: 如果有对应英文的中文，则返回该中文翻译，否则返回None
#         """

#         url = 'http://meddic.medlive.cn/search/search.do?word=%s' % word.replace(' ','+')
#         html = self._get(url)

#         # 用 pyquery 定位翻译
#         q = pq(html)
#         paraphrase_list = q('.paraphrase_list')

#         for paraphrase in paraphrase_list:
#             p = pq(paraphrase)

#             if p('.dictionary').text() == '英汉医学短语词典':
#                 return p('.dictionary_message').text()

#         return None


# if __name__ == '__main__':
#     ymt = YMT()
#     word = 'Whipple disease'
#     print (ymt.get_word_translate(word))
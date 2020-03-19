# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:21:46 2020
@author: Administrator
@content: 抓取猫眼电影排行榜
"""


import requests as reqs
import re
import json
import time
import random

def get_one_page(url):

    USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    headers = {
        'User-Agent': USER_AGENT
        }
    response = reqs.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None



# 带有 yield 的函数在 Python 中被称之为 generator（生成器）
def parse_one_page(html):
    index = '<dd>.*?board-index.*?>(.*?)</i>'
    img = '.*?data-src="(.*?)"'
    #这里定位的时候尽量准确，有关键信息
    name = '.*?name.*?a.*?>(.*?)</a>'
    star = '.*?star.*?>(.*?)</p>'
    time = '.*?releasetime.*?>(.*?)</p>'
    score_int = '.*?integer.*?>(.*?)</i>'
    fraction = '.*?fraction.*?>(.*?)</i>'
    re_all = index + img + name +star +time + score_int + fraction
    pattern = re.compile(re_all, re.S)
    items = re.findall(pattern, html)

    #函数最后返回的是一个生成器
    # 因为items是多个电影的信息，item就是一部电影的信息，然后
    # 生成的是多不电影信息的生成器
    #利用for把每一部电影的信信息输出
    for item in items:

        # 01-生成了一个产生字典的生成器
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),#strip（[char]）去除字符串头尾的字符默认为空格和换行

            # 语法解释：if长度大于3则进行去空从第3位开始取，否则取空
            'actor': item[3].strip()[3:] if len(item[3])>3 else '',
            'time': item[4].strip()[5:] if len(item[4])>5 else '',
            'score': item[5].strip() + item[6].strip()
            }



def write_to_file(content):
    with open('maoyanresult.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(offset):
    url = "https://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
        #每次获得一个生成器
      # 当你调用函数的parse_one_page()时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象
    for item in parse_one_page(html):#当你使用for进行迭代的时候，函数中的代码才会执行，
        write_to_file(item)



if __name__ == '__main__':
    for i in range(3):
        main(offset=i * 10)
        time.sleep(3*random.random()+1)








# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 08:55:15 2020

@author: Administrator
@content: 把百度知道、回答者、回答保存下来
"""


from pyquery import PyQuery as pq
import random
import time



def get_one_page(url):

    doc = pq(url, encoding='gbk')#网页文件的编码方式
    if doc==None:
        print("抓取内容为空!")
    else:
        return doc
 
    
def parse_one_page(doc):

    # 提取所有节点并生成生成器
    items = doc('dl').items()
    
    #产生一个迭代器，在循环语句中被调用
    for item in items:
        yield [item('dt a').text(),
               item('.dd.answer').text(),
               item('span:first-child').text(),
               item("span:nth-child(2) ").text(),#选择第二个子类
               item("span:nth-child(3)").text(),
               item("span:nth-child(4)").text()
               ]
          
        
        #'a'以追加的方式打开一个文件
def write_to_file(doc, times):
    count = 0+10*times
    with open("housePreiceDiscuss.txt", 'a', encoding='utf-8') as f:
        for item in parse_one_page(doc): 
            #把\n应用于列表中的每个元素后面，即把列表里面的问题、回答换行
            f.write('\n'.join(item))
            count+=1
            f.write('\n'+'第'+str(count)+'个回答'+'='*50+'\n')
            

def main(offset, times):
    url = "https://zhidao.baidu.com/search?word=2020%C4%EA%D6%D8%C7%EC%B5%C4%B7%BF%BC%DB%BB%E1%B5%F8%C2%F0&ie=gbk&site=-1&sites=0&date=0&pn="+str(offset)      
    doc = get_one_page(url)
    write_to_file(doc, times)
    

if __name__ == "__main__":
    for i in range(10):
        main(offset=i*10, times=i)#
        time.sleep(3*random.random()+1)
    
    







# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:02:30 2020

@author: Administrator
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = "口罩"

def index_page(page):
    print("正在抓取第", page, "页")
    try:
        url = "http://s.taobao.com/search?q" + quote(KEYWORD)
        #这里出现需要登录淘宝思考如何利用cookies解决
        browser.get(url)
        if page > 1:
            inputer = wait.until(
                #选择id=mainsrp-pager内部id=form的<div>，选择父元素为 <div id=form> 元素的所有 <input> 元素
                #等待节点加载出来
                EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager div.form > input")))
            submit = wait.until(
                #等待节点可以点击
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager div.form > span.btn.J_Submit")))
            #清空input栏目
            inputer.clear()
            #发送页面
            inputer.send_keys(page)
            #点击确定
            submit.click()
            
        wait.until(
            #等待节点内文字出现  #li.item.active这里指的是class=item active, 因为选择器空格代表其他意思 没法打出clas名带空格的
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "mainsrp-pager li.item.active > span"),
                                             str(page)))
        wait.until(                                           #明显的层级关系
            EC.presence_of_element_located((By.CSS_SELECTOR, ".m-itemlist .items .item")))
      
        get_products()
    except TimeoutException:
        index_page(page)
        
        
def get_products():
    '''
    提取商品数据
    '''
    html = browser.page_source
    doc = pq(html)

    #  <class=m-itemlist>/<class=items>/<class=.item.J_MouserOnverReq>
    items= doc('.m-itemlist .items .item.J_MouserOnverReq').items()
    for item in items:
        product = {
            #<img class=J_ItemPic>的属性data-src的值
            'img': item.find('img.J_ItemPic').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
            }
        print(product)
        save_to_mongo(product)

   
    
MONGO_URL = "loaclhost"
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products' 
client =  pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
    
def save_to_mongo(product):
    try:
        if db[MONGO_COLLECTION].insert_one(product):
            print("Done!")
    #这里抛出异常以后程序应该停止如果是else则不会停止
    except Exception:
        print("Failed!")


MAX_PAGE = 100

def main(MAX_PAGE):
    for i in range(1, MAX_PAGE+1):
        index_page(i)

        
        

    
    
                                    
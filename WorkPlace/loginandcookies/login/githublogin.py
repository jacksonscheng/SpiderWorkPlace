# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:07:23 2020

@author: Administrator

@content:利用post方式模拟登陆github
"""

import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session' #post参数的发送的地址
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()
    
    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//input[@name="authenticity_token"]/@value')
        return token
    
    def login(self, email, password):
        
        #构造发往服务器的参数
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token()[0],
            'login': email,
            'password': password}
        
        try:
    
            response1 = self.session.post(self.post_url, data=post_data, headers=self.headers)
            response2 = self.session.get(self.logined_url, headers=self.headers)
            
            return response1.text, response2.text
        
        except Exception:
            print("连接错误！")
   
        
            
if __name__ == "__main__":
    login = Login()
    a, b = login.login(email='zhiweicheng_zc@163.com', password='*******')
        
        
        







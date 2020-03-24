# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:48:20 2020

@author: Administrator
"""


# =============================================================================
# 查看网站的Robots协议判断爬虫爬取的权限
# =============================================================================


from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
# robot协议一般在网站的根目录下
rp.set_url('https://blog.csdn.net/robots.txt')

# 这个方法执行了一个读取解析的方法如果不调用后面都会判断是false
rp.read()

# 判断user-agent为*,爬取的目标url 是否可以爬取
print(rp.can_fetch('*', 'https://blog.csdn.net/zhouzi_heng/article/details/95255017'))

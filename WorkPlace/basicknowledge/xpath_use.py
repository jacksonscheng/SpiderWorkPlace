# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:19:37 2020

@author: Administrator
"""

# =============================================================================
# 利用etree创建HTML对象
# =============================================================================
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

# 或者直接读取文件进行解析
html = etree.parse('test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))


result = html.xpath('//*')#选择所有节点
result = html.xpath('//li')#选择所有li节点
result = html.xpath('//li/a')#选择所有li节点下的a节点
result = html.xpath('//ul//a')#选择ul节点下所有的a
print( html.xpath('//li[@class="item-0"]'))

#选择href为link4的a节点，然后再选取父节点，再获取其class属性
result = html.xpath('//a[@herf="link4.html"]/../@class')

# 文本获取

result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)






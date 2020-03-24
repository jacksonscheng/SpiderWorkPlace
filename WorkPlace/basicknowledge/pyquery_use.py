# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:52:19 2020

@author: Administrator
"""



from pyquery import PyQuery as pq
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

doc = pq(html)
print(doc('li')) #选择了doc中所有的li节点


doc = pq("https://tieba.baidu.com/f?kw=dfef")
print(doc('a'))
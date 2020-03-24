# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:32:01 2020

@author: Administrator
"""

from bs4 import BeautifulSoup as bs

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = bs(html, 'lxml')
a = soup.p.contents
print(len(a))
print(a)


for i, child in enumerate(soup.p.descendants):
    print(i, child)


a = [1,2,3]

list(enumerate(a))







html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = bs(html, 'lxml')
print(soup.find_all(name='ul'))


for ul in soup.find_all(name='ul'):
    print(ul)
    for li in ul.find_all(name='li'):
        print(li.string)

#  通过属性值来查询
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'element'}))




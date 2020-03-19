# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 08:39:45 2020

@author: Administrator
"""

a = [(1,2,3), (4,5,6),(7,8,9)]

a1 = [(6,6,6), (7,7,7),(8,8,8)]

def test(a):
    for b in a:
        yield {
            'one': b[0],
            'two': b[1],
            'three': b[2]
            }


for c in test(a1):
    print(c)


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print(next(g))

.strip()[3:] if len(item[3])>3 else ''

a = ' 主演：111 \n'

b = a.strip()[3:] if len(a)>3 else ''







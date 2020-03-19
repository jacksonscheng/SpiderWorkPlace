# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:21:35 2020

@author: Administrator
"""


#通过type创建类

def hello_world_outside(self):
    print('helloworld')

HelloWorld = type('HelloWorld', (object,), dict(helloworld=hello_world_outside))

h = HelloWorld()
h.helloworld()


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L

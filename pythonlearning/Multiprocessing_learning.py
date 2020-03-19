# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:59:47 2020

@author: Administrator
"""


import multiprocessing
import time


def process_run(n):
    time.sleep(1)
    print(n)



p1 = multiprocessing.Process(target=process_run(1),  args=(1, ))
p1.start()
p2 = multiprocessing.Process(target=process_run(2),  args=(2, ))
p2.start()
p3 = multiprocessing.Process(target=process_run(3),  args=(3, ))
p3.start()
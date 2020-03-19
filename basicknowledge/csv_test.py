# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:37:59 2020

@author: Administrator
"""



import csv

with open("data.csv", 'w' ) as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'id'])
    writer.writerow(['jack', '11', '101'])
    writer.writerow(['mike', '12', '102'])
    
    
    
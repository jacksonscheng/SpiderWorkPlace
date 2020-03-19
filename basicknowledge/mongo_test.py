# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:19:34 2020

@author: Administrator
"""


import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test#创建数据库test
collection = db.students#声明一个collection对象类似于表

student = {
    'ids':20190055,
    'name': 'jordan',
    'age':20,
    'gender': 'male'
    }


student1 = {
    'ids':20190056,
    'name': 'jordan1',
    'age':20,
    'gender': 'male'
    }

student2 = {
    'ids':20190057,
    'name': 'jordan2',
    'age':20,
    'gender': 'male'
    }
student3 = {
    'ids':20190058,
    'name': 'jordan3',
    'age':20,
    'gender': 'male'
    }

student4 = {
    'ids':20190059,
    'name': 'jordan4',
    'age':20,
    'gender': 'male'
    }


result = collection.insert_many([student1,
                                 student2,
                                 student3,
                                 student4])
print(result)



# 查询

res = collection.find_one({'name':'jordan'})
res1 = collection.find({'age':20})#返回生成器
res2  = [x for x in  collection.find({'age':20})]
print(res2)
print(res1)
print(res)


res3 = collection.find({'age':{'$gt':10}})

print([x for x in res3 ])

#正则表示式
res4 = collection.find({'name':{'$regex':'^j.*'}})
if res4 is not None:
    print([x for x in res4])


count = collection.find().count()
print(count)





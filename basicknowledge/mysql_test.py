# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:14:10 2020

@author: Administrator
"""


import pymysql


db = pymysql.connect(host='localhost', user='root', 
                    password='12345678', port=3306,
                    db='spiders')


# =============================================================================
# 动态插入方法传入一个动态的字典，sql语句会根据字典改造
# =============================================================================

data = {
        'id': '002',
        'name': 'Jack',
        'age': 20
        }


#这样改造以后，如果以后多了字段，也不需要更改下面的sql语句
tables = 'students'
keys = ','.join(data.keys())#把keys用，逗号连接，l如a，b，c
values = ','.join(['%s']*len(data))
sql = 'INSERT INTO {0}({1}) VALUES ({2})'.format(tables, keys, values)

cursor = db.cursor()


try:
    if cursor.execute(sql, tuple(data.values())):#传元祖参数
        print('successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
    
db.close()

# =============================================================================
# 更新语句
# =============================================================================

sql = 'UPDATE students SET age=%s WHERE name=%s'

cursor = db.cursor()

try:
    cursor.execute(sql, (25, 'Bob'))
    db.commit()
except:
    print('Failed')
    db.rollback()
db.close()


# ================================



import pymysql


db = pymysql.connect(host='localhost', user='root', 
                    password='12345678', port=3306,
                    db='spiders')




datas = [{
        'id': '0001',
        'name': 'jacker',
        'age': 12
        },
    {
        'id': '0002',
        'name': 'Tim',
        'age': 13
        },
        {
        'id': '0003',
        'name': 'Mike',
        'age': 14
        }
    ]

for data in datas:

    tables = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s']*len(data))
    sql = 'INSERT INTO {tables}({keys}) VALUES ({values})\
     ON DUPLICATE KEY UPDATE'.format(tables=tables,keys=keys,values=values) 
    #ON DUPLICATE KEY UPDATE表示如果主键已经存在则更新数据
                                                                            
    #" {key}=%s"前边有个空格
    update = ','.join([" {key}=%s".format(key=key) for key in data])
    
    sql += update
    
    
    cursor = db.cursor()
    
    
    try:
        if cursor.execute(sql, tuple(data.values())*2):
            print('successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()   


db.close()



# =============================================================================
# 删除数据
# =============================================================================



import pymysql


db = pymysql.connect(host='localhost', user='root', 
                    password='12345678', port=3306,
                    db='spiders')


table = 'students'
condition = 'age>20'


#从表中删除年龄大于20岁的
sql ='DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)

cursor = db.cursor()

try:
    if cursor.execute(sql):
        print("successfull")
        db.commit()
except:
    print('Failed')
    db.rollback()
    
    
# =============================================================================
# 查询数据
# =============================================================================

table = 'students'
condn = 'age<20'

sql = 'SELECT * FROM {table} WHERE {condn}'.format(table=table, condn=condn)  




try:
    cursor = db.cursor()  
    cursor.execute(sql)
    print('Count',cursor.rowcount)
    one = cursor.fetchone() #取第一行
    print('one:', one)
    results = cursor.fetchall()#取所有行
    print(results)
    for row in results:
        print(row)
except:
    print('Error')
    










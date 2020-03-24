# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:33:37 2020

@author: Administrator
"""




# import asyncio
# from aiohttp import ClientSession
# import nest_asyncio



# async def hello(urls):
    
#     async with ClientSession() as session:
        
#         async with session.get(urls) as response:
            
#             response = await response.read()
            
#             print(response)
#             print('='*30)



# if __name__ =='__main__':
  
#     tasks = ['http://www.xsdaili.com/dayProxy/ip/{}.html'.format(x) for x in range(2012,2016)]
#     loop = asyncio.get_event_loop()
#     nest_asyncio.apply()
#     for i in range(len(tasks)):
#         loop.run_until_complete(hello(tasks[i]))
        
        
from flask import Flask
 
app = Flask(__name__)  
#生成app实例，传递 __name__参数，__name__ 就是当前模块名字。
 
@app.route("/")
def index():
    return "2017-08-21 天气不错， 风和日丽的"
 
if __name__ == '__main__':
    app.run(debug=False)

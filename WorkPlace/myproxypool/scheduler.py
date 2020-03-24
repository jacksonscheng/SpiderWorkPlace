import time
from multiprocessing import Process
from api import app
from getter import Getter
from tester import Tester
from db import RedisClient
from setting import *


class Scheduler():
    

    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(10)#如果返回None，等待一段时间
    
    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        getter = Getter()
        getter.run()
        # while True:
        #     print('开始抓取代理')
        #     getter.run()
        #     time.sleep(30)
    
    
    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)
    
    def run(self):
        print('proxypool is running......')
        
        api_process = Process(target=self.schedule_api())
        api_process.start()
        
        getter_process = Process(target=self.schedule_getter())
        getter_process.start()
        
        
        tester_process = Process(target=self.schedule_tester())
        tester_process.start()
        
        api_process = Process(target=self.schedule_api())
        api_process.start()
        
      
        # tester_process.join()
        # getter_process.join()
        # api_process.join()

  





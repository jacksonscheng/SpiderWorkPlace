import asyncio
import aiohttp
import nest_asyncio
import time
import sys
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from db import RedisClient
from setting import *


class Tester(object):
    def __init__(self):
        self.redis = RedisClient()
    
    #这是一个异步的方法
    async def test_single_proxy(self, proxy):
        
      
        """
        测试单个代理
        :param proxy:
        :return:
        """
        
        conn = aiohttp.TCPConnector(ssl=False)
        #建立一个session对象
        #session可以进行多项操作，比如post, get, put, head等
        async with aiohttp.ClientSession(connector=conn) as session:
            
            #检查如果是字节类型就解码
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试', proxy)
                
                #利用session对象去get
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
                    #如果状态码有效
                    if response.status in VALID_STATUS_CODES:
                        #状态码值设置为最大
                        self.redis.max(proxy)
                        print('代理可用', proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不合法 ', response.status, 'IP', proxy)
            except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                self.redis.decrease(proxy)
                print('代理请求失败', proxy)
    
    def run(self):
        """
        测试主函数
        :return:
        """
        print('测试器开始运行')
        try:
            count = self.redis.count()
            print('当前剩余', count, '个代理')
            
            #取出数量为BATCH_TEST_SIZE的proxy
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                #这样可以取到最后一个proxy
                stop = min(i + BATCH_TEST_SIZE, count)
                print('正在测试第', start + 1, '-', stop, '个代理')
                test_proxies = self.redis.batch(start, stop)
                
                #调用这个方法可以避免“进程已经运行”这个错误
                nest_asyncio.apply()
                
                #主线程调用asyncio.get_event_loop()时会创建事件循环
                loop = asyncio.get_event_loop()#
                
                #tasks为异步的任务,列表里面生成的为coroutine（协程）元素
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                #把异步的任务丢给这个循环的run_until_complete()方法
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误', e.args)


        



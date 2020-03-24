# from loguru import logger
# from proxypool.storages.redis import RedisClient
# from proxypool.setting import PROXY_NUMBER_MAX
# from proxypool.crawlers import __all__ as crawlers_cls#获取所有的类列表，这四个类是具体的爬取四个网站的类

from loguru import logger
from storages.redis import RedisClient
from setting import PROXY_NUMBER_MAX
from crawlers import __all__ as crawlers_cls#获取所有的类列表，这四个类是具体的爬取四个网站的类


class Getter(object):
    """
    getter of proxypool
    """
    
    def __init__(self):
        """
        init db and crawlers
        """
        self.redis = RedisClient()
        self.crawlers_cls = crawlers_cls 
       
        #获取类的实例对象列表，具体来说就是把四个类实例化以后组成列表
        self.crawlers = [crawler_cls() for crawler_cls in self.crawlers_cls]
    
    def is_full(self):
        """
        if proxypool if full
        return: bool
        """
        return self.redis.count() >= PROXY_NUMBER_MAX
    
    @logger.catch
    def run(self):
        """
        run crawlers to get proxy
        :return:
        """
        if self.is_full():
            return
        for crawler in self.crawlers:
            
            #这里子类对象在调用父类Crawl的方法craw()
            for proxy in crawler.crawl():
                self.redis.add(proxy)


if __name__ == '__main__':
    getter = Getter()
    getter.run()
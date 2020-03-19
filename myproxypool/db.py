import redis
from error import PoolEmptyError
from setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY
from setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from random import choice
import re


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis密码
        """
        #这种方式可以给类创建一个数据库实例变量db供类使用
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
    
    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """
        #如果不符合Ip的格式则直接返回
        #标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):#这里匹配点用到了转义 \.
            print('代理不符合规范', proxy, '丢弃')
            return
        
        #如果没有score，则赋值为初始值score
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, {proxy:score})
    
    def random(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果不存在，按照排名获取，否则异常
        :return: 随机代理
        """
        #通过score排序找到分数都是100的元素
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
       
        if len(result):
            return choice(result)
        else:
             #如果没有找排名0到100的这里的100是排名,z这里的0和100不是分数
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError
    
    def decrease(self, proxy):
        """
        代理值减一分，小于最小值则删除
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, -1,proxy,)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)
    
    def exists(self, proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        #proxy的score是否存在
        return not self.db.zscore(REDIS_KEY, proxy) == None
    
    def max(self, proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        print('代理', proxy, '可用，设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, {proxy:MAX_SCORE})
    
    def count(self):
        """
        获取数量
        :return: 数量
        """
        return self.db.zcard(REDIS_KEY)
    
    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
         #返回所有代理的代理的列表
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
    
    def batch(self, start, stop):
        """
        批量获取
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        #根据排名取proxy,在redis里面可以取到（start，end）中end的这个数，因此要-1
        return self.db.zrevrange(REDIS_KEY, start, stop - 1)


# if __name__ == '__main__':
#     conn = RedisClient()
#     result = conn.batch(680, 688)
#     print(result)

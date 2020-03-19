import requests
from requests.exceptions import ConnectionError

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}


def get_page(url, options={}):
    """
    抓取代理
    :param url:
    :param options:
    :return:
    """
    #构造headers
    headers = dict(base_headers, **options)
    print('正在连接', url)
    try:
        response = requests.get(url, headers=headers)
        print('连接成功', url, response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError as e:
        print('抓取失败', url, e.args)
        return None

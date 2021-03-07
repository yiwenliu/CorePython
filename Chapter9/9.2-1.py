# -*- coding:UTF-8 -*-

"""
以单线程的方式实现网站下载任务
"""

import requests
import time


sites = [
        'https://news.sina.com.cn/',
        'http://sports.sina.com.cn/',
        'https://finance.sina.com.cn/',
        'https://news.sina.com.cn/',
        'https://news.sina.com.cn/world/',
        'https://tech.sina.com.cn/discovery/',
        'https://finance.sina.com.cn/fund/',
        'https://news.sina.com.cn/china/',
        'https://mobile.sina.com.cn/',
        'https://finance.sina.com.cn/stock/',
        'https://mil.news.sina.com.cn/',
        'https://tech.sina.com.cn/',
        'http://travel.sina.com.cn/',
        'http://photo.sina.com.cn/',
        'http://edu.sina.com.cn/',
        'https://fashion.sina.com.cn/',
        'https://bj.leju.com/#source=pc_sina_tydh1&source_ext=pc_sina',
        'http://video.sina.com.cn/',
        'http://blog.sina.com.cn/',
        'https://auto.sina.com.cn/',
        'https://ent.sina.com.cn/'
    ]


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all():
    for site in sites:
        download_one(site)


def main():
    start_time = time.perf_counter()
    download_all()
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()

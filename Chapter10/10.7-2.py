# -*- coding:UTF-8 -*-
from concurrent.futures import ThreadPoolExecutor
import requests


def load_url(url):
    return requests.get(url)


if __name__ == "__main__":
    url = 'http://baidu.com'
    executor = ThreadPoolExecutor(max_workers=1)  # 定义一个执行器对象
    future = executor.submit(load_url, url)  # 将可调用对象load_url，以load_url(url)方式封装为异步执行的Future对象
    print(future.done())  # done()以非阻塞的方式，判断Future对象的任务是否完成
    print(future.result().status_code)  # result()阻塞主线程，返回调用返回的值

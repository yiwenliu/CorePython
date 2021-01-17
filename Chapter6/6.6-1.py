# -*- coding:UTF-8 -*-
import time


def my_decorator(func):
    """
    简单装饰器
    :param func: 被装饰的函数对象
    :return: 一个函数对象
    """

    def wrapper():
        # 新增功能——打印当前时间
        localtime = time.asctime(time.localtime(time.time()))
        print("当前时间：", localtime)
        func()

    return wrapper


@my_decorator
def greet():
    print('hello world')


if __name__ == "__main__":
    greet()

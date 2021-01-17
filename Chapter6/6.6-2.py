# -*- coding:UTF-8 -*-
import time


def my_decorator(func):
    """
    带参数的装饰器
    :param func: 被装饰的函数对象
    :return: 一个函数对象
    """

    def wrapper(*args, **kwargs):
        # 新增功能——打印当前时间
        localtime = time.asctime(time.localtime(time.time()))
        print("当前时间：", localtime)
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(name):
    print('hello ', name)


@my_decorator
def celebrate(name, message):
    print(message, name)


if __name__ == "__main__":
    greet("CorePython")
    celebrate(message="Go for it, ", name="everyone")

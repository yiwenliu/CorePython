# -*- coding:UTF-8 -*-
import time
import os


def my_decorator1(func):
    """
    简单装饰器，打印当前目录
    :param func: 被装饰的函数对象
    :return:
    """
    def wrapper():
        print("当前目录：", os.getcwd())
        func()

    return wrapper


def my_decorator2(func):
    """
    简单装饰器，打印当前时间
    :param func: 被装饰的函数对象
    :return: 一个函数对象
    """

    def wrapper():
        # 新增功能——打印当前时间
        localtime = time.asctime(time.localtime(time.time()))
        print("当前时间：", localtime)
        func()

    return wrapper


@my_decorator1
@my_decorator2
def greet():
    print('hello world')


if __name__ == "__main__":
    greet()

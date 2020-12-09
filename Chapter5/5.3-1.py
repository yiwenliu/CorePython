# -*- coding: utf-8 -*-
# @Time : 2020/12/9 9:16
# @Function :


import os
import psutil


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def test_iterator():
    """
    迭代器版本的求和
    :return:
    """
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')


def test_generator():
    """
    生成器版本的求和
    :return:
    """
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')


if __name__ == "__main__":
    test_iterator()
    test_generator()

# -*- coding:UTF-8 -*-
import time


def factorize(number):
    """
    计算密集型任务：一种非常原始的因数分解算法
    :param number:
    :return:
    """
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


if __name__ == "__main__":
    numbers = [2139079, 1214759, 1852285, 2135468, 2546813, 5421652, 2154632, 2154652,
               2139079, 1214759, 1852285, 2135468, 2546813, 5421652, 2154632, 2154652]
    start = time.time()
    for number in numbers:
        list(factorize(number))
    end = time.time()
    print('Took %.3f seconds.' % (end - start))
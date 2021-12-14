# -*- coding:UTF-8 -*-
import time
from threading import Thread
from multiprocessing import cpu_count


def factorize(number):
    """
    计算密集型任务：一种非常原始的因数分解算法
    :param number:
    :return:
    """
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


if __name__ == "__main__":
    print("CPU的核数为：{}".format(cpu_count()))
    numbers = [2139079, 1214759, 1852285, 2135468, 2546813, 5421652, 2154632, 2154652,
               2139079, 1214759, 1852285, 2135468, 2546813, 5421652, 2154632, 2154652]
    threads = []
    start = time.time()
    # 为numbers列表中的每个数字，都启动一个线程
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)
    # 等待全部线程执行完毕
    for thread in threads:
        thread.join()
    end = time.time()
    print('Took %.3f seconds.' % (end - start))
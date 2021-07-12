# -*- coding:UTF-8 -*-
import threading


class LockingCounter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


def worker(sensor_index, how_many, counter):
    """
    每个采集线程的工作
    :param sensor_index:
    :param how_many: 采集数据的次数
    :param counter: 共享的计数器对象
    :return:
    """
    for _ in range(how_many):
        # 读取传感器数据
        counter.increment(1)


def run_threads(func, how_many, counter):
    """
    为5个传感器各启动一个工作线程，然后等待它们完成各自的采样工作
    :param func: 线程函数
    :param how_many: 每个线程需要完成的采样的次数
    :param counter: 共享的计数器对象
    :return:
    """
    threads = []
    for i in range(5):
        args = (i, how_many, counter)
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    how_many = 10 ** 5
    counter = LockingCounter()
    run_threads(worker, how_many, counter)
    print('Counter 应该是 %d, 实际上是 %d' % (5*how_many, counter.count))
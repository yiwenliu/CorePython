# -*- coding:UTF-8 -*-
from queue import Queue
import threading


def download(num):
    """
    获取图片
    :param num:
    :return:
    """
    print('Download done, number: {}.\n'.format(num))
    return num


def resize(num):
    """
    缩放图片
    :param num:
    :return:
    """
    print('Resize done, number: {}.\n'.format(num))
    return num


def upload(num):
    """
    上载图片
    :param num:
    :return:
    """
    print('Upload done, number: {}.\n'.format(num))
    return num


class Worker(threading.Thread):
    """
    定义每个阶段的工作线程类
    """
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        while True:
            # 阻塞式获取任务
            item = self.in_queue.get()
            result = self.func(item)
            # 阻塞式上传任务
            self.out_queue.put(result)


if __name__ == "__main__":
    # 定义4个队列
    download_queue = Queue()
    resize_queue = Queue()
    upload_queue = Queue()
    done_queue = Queue()
    # 定义3个worker线程
    threads = [
        Worker(download, download_queue, resize_queue),
        Worker(resize, resize_queue, upload_queue),
        Worker(upload, upload_queue, done_queue)
    ]
    # 启动3个worker线程
    for thread in threads:
        thread.start()
    # 将任务添加到管线的第1个队列
    for task in range(3):
        download_queue.put(task)
    print('exit main thread!\n')
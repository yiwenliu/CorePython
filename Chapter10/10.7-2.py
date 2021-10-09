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
    def __init__(self, name, func, in_queue, out_queue):
        super().__init__()
        self.name = name
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        while True:
            # 阻塞式获取任务
            item = self.in_queue.get()
            # 接收到终止信号
            if item == -1:
                break
            result = self.func(item)
            # 由队列的消费者线程调用，通知队列完成了一个排队的任务
            self.in_queue.task_done()
            # 阻塞式上传任务
            self.out_queue.put(result)
        print('{} done.\n'.format(self.name))


if __name__ == "__main__":
    # 定义4个队列
    download_queue = Queue()
    resize_queue = Queue()
    upload_queue = Queue()
    done_queue = Queue()
    # 定义3个worker线程
    threads = [
        Worker('download thread', download, download_queue, resize_queue),
        Worker('resize thread', resize, resize_queue, upload_queue),
        Worker('upload thread', upload, upload_queue, done_queue)
    ]
    # 启动3个worker线程
    for thread in threads:
        thread.start()
    # 将任务添加到管线的第1个阶段
    for task in range(3):
        download_queue.put(task)
    # 阻塞主线程，直至”下载阶段“的任务处理完毕
    download_queue.join()
    # 给”下载队列“放入终止信号
    download_queue.put(-1)
    # 阻塞主线程，直至”缩放阶段“的任务处理完毕
    resize_queue.join()
    # 给”缩放队列“放入终止信号
    resize_queue.put(-1)
    # 阻塞主线程，直至”上传阶段“的任务处理完毕
    upload_queue.join()
    # 给”下载队列“放入终止信号
    upload_queue.put(-1)

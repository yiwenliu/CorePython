# -*- coding:UTF-8 -*-
import threading
import time

if __name__ == "__main__":
    print('thread %s is running...' % threading.current_thread().name)
    time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
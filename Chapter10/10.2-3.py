# -*- coding:UTF-8 -*-
import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        time.sleep(2)
        print("function called by thread %i\n" % self.threadID)
        return


if __name__ == "__main__":
    for i in range(5):
        t = myThread(i)
        t.start()

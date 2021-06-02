# -*- coding:UTF-8 -*-
import threading
import time


def function(i):
    time.sleep(2)
    print("function called by thread %i\n" % i)
    return


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=function, args=(i,))
        t.start()

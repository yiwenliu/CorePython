# -*- coding:UTF-8 -*-
import time
from datetime import datetime


def log(message, when=datetime.now()):
    print("%s:%s" %(when, message))


if __name__ == "__main__":
    log('Hi there!')
    time.sleep(1)
    log('Hi again')

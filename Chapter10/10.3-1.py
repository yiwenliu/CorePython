# -*- coding:UTF-8 -*-

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


def n():
    logging.debug('Starting')
    logging.debug('Exiting')


def d():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')


if __name__ == '__main__':
    t = threading.Thread(name='non-daemon', target=n)

    d = threading.Thread(name='daemon', target=d)
    d.daemon = True

    d.start()
    t.start()

    logging.debug('Exiting')

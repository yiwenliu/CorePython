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
    t = threading.Thread(target=n)

    d = threading.Thread(target=d)

    d.start()
    t.start()

    t.join()
    d.join()
    # d.join(3.0)
    # logging.debug('d.isAlive():{}'.format(d.is_alive()))

    logging.debug('Exiting')
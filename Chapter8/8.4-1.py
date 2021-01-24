# -*- coding:UTF-8 -*-
import logging
from contextlib import contextmanager


def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


if __name__ == "__main__":
    my_function()
    logging.warning('****************')  # 程序的默认日志等级是WARNING
    with debug_logging(logging.DEBUG):
        my_function()
    logging.warning('****************')
    my_function()

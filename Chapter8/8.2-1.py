# -*- coding:UTF-8 -*-
import logging


def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


class DebugLogging(object):
    def __init__(self, level):
        """
        :param level: 指定的程序日志等级
        """
        self.level = level
        self.old_level = None
        return

    def __enter__(self):
        """
        保留原来日志等级；
        设置新的日志等级
        :return:
        """
        logger = logging.getLogger()
        self.old_level = logger.getEffectiveLevel()
        logger.setLevel(self.level)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        恢复原来的日志等级
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        logger = logging.getLogger()
        logger.setLevel(self.old_level)


if __name__ == "__main__":
    my_function()
    logging.warning('****************')  # 程序的默认日志等级是WARNING
    with DebugLogging(logging.DEBUG):
        my_function()
    logging.warning('****************')
    my_function()

# -*- coding:UTF-8 -*-
import logging


class Error(Exception):
    """这个模块抛出的所有异常的基类"""


class InvalidDensityError(Error):
    """当提供的密度值有问题时抛出的异常"""


def determine_weight(volume, density):
    if density <= 0:
        raise InvalidDensityError('密度必须是正值')
    # ...


if __name__ == "__main__":
    try:
        weight = determine_weight(1, -1)
    except InvalidDensityError:  # 无效密度异常
        weight = 0
    except Error as e:  # API抛出但是未捕获的其他异常
        logging.error("调用代码错误：%s", e)
    except Exception as e:  # 捕获API实现代码里面尚未修复的bug
        logging.error("API代码错误：%s", e)
        raise

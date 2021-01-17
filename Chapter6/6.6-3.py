# -*- coding:UTF-8 -*-


def repeat(num):
    """
    带有自定义参数的装饰器
    :param num: 重复执行的次数
    :return:
    """
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(i, 'wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat(4)
def greet(message):
    print(message)


if __name__ == "__main__":
    greet('hello world')

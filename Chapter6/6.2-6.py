# -*- coding:UTF-8 -*-

# A simple generator function
def my_gen():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n


class MyGen:
    """
    依据迭代器协议，定义了一个iterable，容器类。
    """
    def __iter__(self):
        n = 1
        yield n
        n += 1
        yield n
        n += 1
        yield n


def handle_numbers(numbers):
    if iter(numbers) is numbers:  # 依据迭代器协议约定，如果参数是迭代器，抛出异常
        raise TypeError('Must supply a container')
    print(list(numbers))
    print("Sum is {}.".format(sum(a)))


if __name__ == "__main__":
    # a = my_gen()
    a = MyGen()
    handle_numbers(a)

# -*- coding: utf-8 -*-
# @Time : 2020/12/8 9:27
# @Function : 自定义可迭代对象和迭代器


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max_power=0):
        self.max = max_power

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        # 自定义class一定要有这条件语句，用来终止next()
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            # 表示next()要终止
            raise StopIteration


if __name__ == "__main__":
    for i in PowTwo(5):
        print(i)

# -*- coding:UTF-8 -*-

from collections.abc import Iterable
from collections.abc import Iterator


# A simple generator function
def my_gen():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n


if __name__ == "__main__":
    a = my_gen()
    print(isinstance(a, Iterable))
    print(isinstance(a, Iterator))

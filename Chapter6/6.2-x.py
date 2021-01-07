# -*- coding:UTF-8 -*-

from collections.abc import Iterable
from collections.abc import Iterator


if __name__ == "__main__":
    rr = range(5)
    print(list(rr))
    print(list(rr))
    print(type(range))
    print(isinstance(rr, Iterable))
    print(isinstance(rr, Iterator))
    print(next(iter(rr)))

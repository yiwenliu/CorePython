# -*- coding:UTF-8 -*-
from concurrent.futures import ThreadPoolExecutor


def divide(x):
    return 5 / x


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        e = executor.map(divide, [1, 0, 2])
        try:
            for i in e:
                print(i)
        except Exception as exc:
            print('Exception: {}'.format(exc))

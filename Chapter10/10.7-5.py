# -*- coding:UTF-8 -*-
from concurrent.futures import ThreadPoolExecutor


def divide(x):
    return 5 / x


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_list = [executor.submit(divide, num) for num in [1, 0, 2]]
        for future in future_list:
            try:
                print(future.result())
            except Exception as exc:
                print('Exception: {}'.format(exc))
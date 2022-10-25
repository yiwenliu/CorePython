# -*- coding:UTF-8 -*-
import json


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


if __name__ == "__main__":
    f1 = decode('bad data')
    f1['stuff'] = 5  # 修改了函数的返回值
    print(f1)
    f2 = decode('also bad')
    f2['meep'] = 1  # 修改了函数的返回值
    print('Foo:', f1)  # 并非{'stuff': 5}
    print('Bar:', f2)  # 并非{'meep': 1}
    print(f1 is f2)

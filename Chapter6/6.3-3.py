# -*- coding:UTF-8 -*-
import json


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


if __name__ == "__main__":
    f1 = decode('bad data')
    f1['stuff'] = 5
    f2 = decode('also bad')
    f2['meep'] = 1
    print('Foo:', f1)  # 并非{'stuff': 5}
    print('Bar:', f2)  # 并非{'meep': 1}
    # print(fo is ba)
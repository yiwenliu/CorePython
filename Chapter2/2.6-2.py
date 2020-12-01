# -*- coding: utf-8 -*-
# @Time : 2020/12/1 14:48


# 返回第2个元素作为sorting key
def takeSecond(elem):
    return elem[1]


if __name__ == "__main__":
    random = [(2, 2), (3, 4), (4, 1), (1, 3)]
    print('Before sort: ', random)
    random.sort()
    print('Default sort: ', random)
    random.sort(key=takeSecond)
    print('Custom sort: ', random)

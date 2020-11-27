# coding=utf-8
import copy
if __name__ == "__main__":
    a = [0, [1, 2], 3]
    b = copy.deepcopy(a)
    a[0] = 8
    a[1][1] = 9
    print('a ', a)
    print('b ', b)

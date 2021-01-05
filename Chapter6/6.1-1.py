# -*- coding:UTF-8 -*-


def my_func(l2):
    l2.append(4)


if __name__ == "__main__":
    l1 = [1, 2, 3]
    my_func(l1)
    print(l1)

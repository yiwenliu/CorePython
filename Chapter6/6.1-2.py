# -*- coding:UTF-8 -*-


def my_func(l2):
    l2 = l2 + [4]
    print("In my func, l2 is {}.".format(l2))


if __name__ == "__main__":
    l1 = [1, 2, 3]
    my_func(l1)
    print("In main, l1 is {}.".format(l1))

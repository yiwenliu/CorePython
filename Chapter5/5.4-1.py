# -*- coding:UTF-8 -*-

# A simple generator function
def my_gen():
    print('Start running the generator function......')
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n


if __name__ == "__main__":
    a = my_gen()
    print("1st next, return value is {}".format(next(a)))
    print("2nd next, return value is {}".format(next(a)))
    print("3rd next, return value is {}".format(next(a)))
    next(a)

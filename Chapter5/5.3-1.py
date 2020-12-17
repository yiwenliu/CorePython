# -*- coding:UTF-8 -*-

# A simple generator function
def my_gen():
    print('Start running the generator function......')
    n = 1
    print('n =', n)
    yield n

    n += 1
    print('n =', n)
    yield n

    n += 1
    print('n =', n)
    yield n


if __name__ == "__main__":
    a = my_gen()
    next(a)
    next(a)
    next(a)
    next(a)
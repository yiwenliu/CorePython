# -*- coding:UTF-8 -*-

# A simple generator function
def my_gen():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n


if __name__ == "__main__":
    a = my_gen()
    for item in a:
        print("n={}".format(item))

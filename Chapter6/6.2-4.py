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
    # 求序列的和
    print("Sum is {}.".format(sum(a)))
    # 打印序列
    print(list(my_gen()))

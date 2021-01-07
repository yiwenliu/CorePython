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
    # 打印数据类型
    print(type(a))
    # 求序列的和
    print("Sum is {}.".format(sum(a)))
    # 打印序列
    print(list(a))


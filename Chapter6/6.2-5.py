# -*- coding:UTF-8 -*-
class MyGen:
    def __iter__(self):
        n = 1
        yield n
        n += 1
        yield n
        n += 1
        yield n


if __name__ == "__main__":
    a = MyGen()
    # 求序列的和
    print("Sum is {}.".format(sum(a)))
    # 打印序列
    print(list(a))

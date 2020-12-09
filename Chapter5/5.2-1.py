# -*- coding: utf-8 -*-
# @Time : 2020/12/9 10:38
# @Function : 内建数据结构的迭代器

if __name__ == "__main__":
    x = [42, 23, 24]
    it = iter(x)
    print("列表迭代器的数据类型是： ", type(it))
    print("列表x的下一个元素是：", next(it))
    print("列表x的下一个元素是：", it.__next__())


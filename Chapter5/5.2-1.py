# -*- coding: utf-8 -*-
# @Time : 2020/12/9 10:38
# @Function : 内建数据结构的迭代器

if __name__ == "__main__":
    x = [42, 23, 24]
    it = iter(x)
    print(it == iter(it))
    print("列表x的下一个元素是：", next(it))
    print("列表x的下一个元素是：", it.__next__())
    print("列表x的下一个元素是：", next(it))
    print("列表x的下一个元素是：", next(it))


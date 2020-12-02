# -*- coding: utf-8 -*-
# @Time : 2020/12/2 9:16
# @Function : in运算符在字典中的应用

if __name__ == "__main__":
    d = {'name': 'jason', 'age': '20'}
    print("--遍历字典的keys--")
    for key in d:
        print(key)
    print("--遍历字典的keys--")
    for key in d.keys():
        print(key)
    print("--遍历字典的values--")
    for value in d.values():
        print(value)

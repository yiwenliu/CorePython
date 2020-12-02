# -*- coding: utf-8 -*-
# @Time : 2020/12/2 9:16
# @Function : 字典的遍历

if __name__ == "__main__":
    d = {'name': 'jason', 'age': '20'}
    print("--遍历字典对象所有的键--")
    for key in d:
        print(key)
    print("--遍历字典对象所有的键--")
    for key in d.keys():
        print(key)
    print("--遍历字典对象所有的values--")
    for value in d.values():
        print(value)
    print("--遍历字典对象每个元素的key和value--")
    for key, value in d.items():
        print('%s is %s.' % (key, value))

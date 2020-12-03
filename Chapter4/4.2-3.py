# -*- coding: utf-8 -*-
# @Time : 2020/12/2 17:24
# @Function : 解析url

if __name__ == "__main__":
    path = 'https://www.udemy.com/'
    print(path.split('//'))
    print(path.split('//')[1].split('.'))


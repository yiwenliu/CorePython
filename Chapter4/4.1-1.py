# -*- coding: utf-8 -*-
# @Time : 2020/12/3 16:30
# @Function :

if __name__ == "__main__":
    title = "python核心编程"
    print("--unicode字符--")
    print('title是：', title)
    print('title的类型：', type(title))
    print('title的长度：', len(title))
    print("--原始字节--")
    title = title.encode('utf-8')
    print('title是：', title)
    print('title的类型：', type(title))
    print('title的长度：', len(title))

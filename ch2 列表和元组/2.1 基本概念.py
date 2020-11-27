# coding=utf-8

if __name__ == "__main__":
    # section 1
    lt = [1, 2, 'hello', 'world']  # "列表"中同时含有int和string类型的元素
    tup = ('jason', 22)  # "元组"中同时含有int和string类型的元素
    # section 2
    lt = [1, 2, 3, 4]
    print('Before lt: ', lt)
    lt[3] = 40
    print('After lt: ', lt)
    tup = (1, 2, 3, 4)
    tup[3] = 40
    # section 3
    lt = [[1, 2, 3], [4, 5]]  # 列表的每一个元素也是一个列表
    tup = ((1, 2, 3), (4, 5, 6))  # 元组的每一个元素也是一个元组
    # section 4
    print(list((1, 2, 3)))
    print(tuple([1, 2, 3]))





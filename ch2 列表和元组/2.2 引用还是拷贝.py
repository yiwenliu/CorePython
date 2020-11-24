# coding=utf-8

if __name__ == "__main__":
    # section 1
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(a is b)
    print(a == b)
    # section 2
    values = [0, 1, 2]
    print('Before ', values)
    values[1] = values
    print('After ', values)
    # section 3
    values = [0, 1, 2]
    print('Before ', values)
    values[1] = values[:]
    print('After ', values)
    # section 4
    a = [0, [1, 2], 3]
    b = a[:]
    a[0] = 8
    a[1][1] = 9
    print('a ', a)
    print('b ', b)
    # section 5
    import copy
    a = [0, [1, 2], 3]
    b = copy.deepcopy(a)
    a[0] = 8
    a[1][1] = 9
    print('a ', a)
    print('b ', b)

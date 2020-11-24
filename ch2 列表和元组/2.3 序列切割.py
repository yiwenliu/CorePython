# coding=utf-8

if __name__ == "__main__":
    # section 1
    a = [1, 2, 3, 4]
    print('The last one: ', a[-1])
    # section 2
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print('First four:', a[:4])
    print('Last four: ', a[-4:])
    print('Middle two: ', a[3:-3])
    # section 3
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    b = a[4:]
    print("Before:", b)
    b[1] = 99
    print("After:", b)
    print("Original:", a)
    # section 4
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print("Before:", a)
    a[2:7] = [99, 22, 14]
    print("After:", a)
    # section 5
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    b = a
    print("Before:", a)
    a[:] = [101, 102, 103]
    print("After:", a)
    print('Whether a is b: ', a is b)



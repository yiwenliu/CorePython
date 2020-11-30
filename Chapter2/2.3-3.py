# coding=utf-8

if __name__ == "__main__":
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    b = a
    print("Before:", a)
    a[:] = [101, 102, 103]
    print("After:", a)
    print('Whether a is b: ', a is b)

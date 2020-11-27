# coding=utf-8

if __name__ == "__main__":
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    b = a[4:]
    print("Before:", b)
    b[1] = 99
    print("After:", b)
    print("Original:", a)

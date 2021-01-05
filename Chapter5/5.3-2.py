# -*- coding:UTF-8 -*-

if __name__ == "__main__":
    a = [1, 2, 3]
    gene = (x ** 2 for x in a)
    for item in gene:
        print(item)

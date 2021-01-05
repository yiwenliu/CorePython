# -*- coding:UTF-8 -*-

if __name__ == "__main__":
    a = [1, 2, 3]
    comp = [x ** 2 for x in a]
    gene = (x ** 2 for x in a)
    print(comp)
    print(gene)

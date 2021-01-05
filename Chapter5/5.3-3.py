# -*- coding:UTF-8 -*-


if __name__ == "__main__":
    a = [1, 2, 3]
    gene = (x ** 2 for x in a)
    print("the 1st item in the generator is {}.".format(next(gene)))
    print("the 2nd item in the generator is {}.".format(next(gene)))
    print("the 3rd item in the generator is {}.".format(next(gene)))
    print(next(gene))

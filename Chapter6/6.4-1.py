# -*- coding:UTF-8 -*-

a = 1


def g():
    print("in function g: ", a)


def f():
    print("in function a, before: ", a)
    a = 2
    print("in function a, after: ", a)


if __name__ == "__main__":
    # g()
    # f()
    import dis
    dis.dis(g)
    dis.dis(f)


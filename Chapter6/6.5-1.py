# -*- coding:UTF-8 -*-


def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    printer()


if __name__ == "__main__":
    print_msg("Hello")

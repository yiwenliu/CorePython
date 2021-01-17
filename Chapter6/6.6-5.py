# -*- coding:UTF-8 -*-


class Count:
    def __init__(self, func):
        """
        :param func: 被装饰函数名
        """
        print("Initializing a Count object...")
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        self.func(*args, **kwargs)
        return


if __name__ == "__main__":
    @Count
    def example():
        print("hello world")

    print(type(example))
    # example()
    # example()

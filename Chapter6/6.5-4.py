# -*- coding:UTF-8 -*-


class Sorter(object):
    def __init__(self, group):
        self.group = group

    def run(self, values):
        self.found = False

        def helper(x):
            if x in self.group:
                self.found = True
                return 0, x
            return 1, x

        values.sort(key=helper)


if __name__ == "__main__":
    sorter = Sorter([7, 9])
    values = [1, 5, 3, 9, 7, 4, 2, 8, 6]
    sorter.run(values)
    print(values)
    print(sorter.found)


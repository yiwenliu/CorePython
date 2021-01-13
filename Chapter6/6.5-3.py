# -*- coding:UTF-8 -*-


def sort_priority(values, group):
    """
    给列表按优先级排序
    :param values: 需要排序的列表
    :param group: 高优先级群组列表
    :return:
    """
    found = False  # 是否存在高优先级元素的标志位

    def helper(x):
        if x in group:
            found = True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found


if __name__ == "__main__":
    values = [1, 5, 3, 9, 7, 4, 2, 8, 6]
    group = [7, 9]
    found = sort_priority(values, group)
    print(values)
    print("Found:", found)

# -*- coding:UTF-8 -*-


def log(message, *values):
    if not values:
        print(message)
    else:
        print(type(values))
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s ' % (message, values_str))


if __name__ == "__main__":
    log('Hi there')
    print('**********')
    log('My numbers are', 1, 2, 3)


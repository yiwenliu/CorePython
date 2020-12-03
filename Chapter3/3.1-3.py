# -*- coding: utf-8 -*-
# @Time : 2020/12/2 9:49
# @Function :

if __name__ == "__main__":
    d = {'name': 'jason', 'age': '20'}
    items = d.items()
    print('---Before---')
    for key, value in items:
        print('%s is %s.' % (key, value))
    d['name'] = 'ben'
    print('---After---')
    for key, value in items:
        print('%s is %s.' % (key, value))

# coding=utf-8
# @Function :找出字母数目最多的名字

if __name__ == "__main__":
    longest_name = None
    max_letters = 0
    names = ['Cecilia', 'Lise', 'Marie']
    letters = [len(n) for n in names]
    for name, count in zip(names, letters):
        if count > max_letters:
            longest_name = name
            max_letters = count
    print('The longest name is %s of %d letters' % (longest_name, max_letters))

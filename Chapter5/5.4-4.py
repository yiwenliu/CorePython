# -*- coding:UTF-8 -*-


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


if __name__ == "__main__":
    address = "Four score ad sever years ago..."
    result = index_words_iter(address)
    print(result)
    print(list(result))

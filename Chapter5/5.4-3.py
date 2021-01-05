# -*- coding:UTF-8 -*-


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


if __name__ == "__main__":
    address = "Four score ad sever years ago..."
    result = index_words(address)
    print(result)
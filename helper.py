# Created by 碎心咒 at 2018/10/21


def is_key_or_isbn(word):
    """
    判断ISBN或者是关键词
    :param word:
    :return:
    """
    is_key = 'key'
    if len(word) == 13 and word.isdigit():
        is_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        is_key = 'isbn'
    return is_key

# Created by 碎心咒 at 2018/10/21
from httper import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def seach_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def seach_by_key(cls, key, count=15, start=0):
        url = cls.key_url.format(key, count, start)
        result = HTTP.get(url)
        return result

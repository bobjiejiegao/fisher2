# Created by 碎心咒 at 2018/10/22
from flask import jsonify

from helper import is_key_or_isbn
from yushu_book import YuShuBook


@app.route('/book/seach/<q>/<page>')
def seach(q, page):
    key_or_isbn = is_key_or_isbn(q)
    if key_or_isbn == 'isbn':
        result = YuShuBook.seach_by_isbn(q)
    else:
        result = YuShuBook.seach_by_key(q)
    return jsonify(result)

# 文件创建时间 ：2018/10/21 10:22

from flask import Flask
from helper import is_key_or_isbn

__author__ = "碎心咒"

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/seach/<q>/<page>')
def seach(q, page):
    is_key_or_isbn(q)
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=80)

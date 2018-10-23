# Created by 碎心咒 at 2018/10/21


from flask import Flask


app = Flask('__name__')
app.config.from_object('config')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=80)

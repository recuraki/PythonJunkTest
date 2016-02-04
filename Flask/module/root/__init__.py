#!env python
# coding:utf-8

from flask import Flask
from hoge.main import hoge

app = Flask(__name__)
app.debug = True

app.config.from_envvar('FLASK_APP_SETTINGS', silent=True)
app.register_module(hoge, url_prefix="/moge")

@app.route("/")
def index():
    return("index")

if __name__ == '__main__':
    app.run()

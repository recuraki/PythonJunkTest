#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return('index', 200)

@app.route('/hello', methods=['GET'])
def hello():
    print(request.args)
    name = request.args.get("name", "")
    print("<br>\n")
    c = ""
    c += "<hr>"
    c += "hello" + name
    c += "<hr>"
    return(c, 200)

@app.route('/hello/<name>', methods=['GET'])
def hello_withname(name):
    return("hi! {0}".format(name), 200)

@app.route('/set/<name>/<value>', methods=['GET'])
def set_func(name, value):
    return("hi!hi! {0} to {1}".format(name, value), 200)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

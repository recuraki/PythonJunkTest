#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from urllib import urlencode
import json

"""
テストは以下のように実施します。
正常な例:
curl -H "Content-Type:application/json" -X POST -d '{"val1": 1, "val2": 2}' http://localhost:5000/add
失敗する例
curl -H "Content-Type:application/json" -X POST -d '{"val1": 1, "val2": "2"}' http://localhost:5000/add

"""

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return('index')


@app.route('/add', methods=['POST'])
def hello():
    res = proc_add(request.data)
    c = ""
    c += str(res)
    return(c)

@app.route('/hello/<name>', methods=['GET'])
def hello_withname(name):
    return("hi! {0}".format(name))

def proc_add(stJson):
    diInput = json.loads(stJson)
    if not "val1" in diInput:
        raise Excetion("noval1")
    if not "val2" in diInput:
        raise Excetion("noval2")

    inRes = diInput["val1"] + diInput["val2"]
    diRet = {}
    diRet['res'] = inRes
    return(json.dumps(diRet, indent = 2))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

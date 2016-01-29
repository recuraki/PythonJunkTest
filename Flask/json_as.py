#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from urllib import urlencode
import json
import telnetlib

"""
"""

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    # slackからの入力をおけとります
    stText = request.form["text"]

    # 入力をそのまま関数に渡します
    res = proc_add(stText)

    # 結果を返します
    c = ""
    c += str(res)
    print c
    return(c)

def proc_add(stText):
    # " "でセパレート
    liText = stText.split(" ")

    # 引数の数が違ったらエラーを返します
    if len(liText) != 2:
        diRet = {}
        diRet['text'] = "usage: asnum <ASNUM>"
        diRet['username'] = "asbot"
        return(json.dumps(diRet, indent = 2))


    # 引数が整数かを確認します
    try:
        asnum = int(liText[1])
    except ValueError:
        # 整数じゃなかったら怒ります
        diRet = {}
        diRet['text'] = "plz input int :p"
        diRet['username'] = "asbot"
        return(json.dumps(diRet, indent = 2))

    # 返信を作ります
    diRet = {}
    # ここでaslookupする
    diRet['text'] = aslook(liText[1])
    diRet['username'] = "asbot"
    return(json.dumps(diRet, indent = 2))

def aslook(stNum):
    # telnetしてほげほげ
    tn = telnetlib.Telnet(host = "asn.cymru.com", port = 43)
    # unicodeになっているんでstrにして連結
    stQue = "AS" + str(stNum) + "\n"
    # "AS290"とかを送信
    tn.write(stQue)
    # 返信を全部格納
    ret = tn.read_all()
    tn.close()
    return(ret)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

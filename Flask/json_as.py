#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from urllib import urlencode
import json
import telnetlib

"""
テストは以下のように実施します。
正常な例:
curl -H "Content-Type:application/json" -X POST -d '{"val1": 1, "val2": 2}' http://localhost:5000/add
"""

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    stText = request.form["text"]
    res = proc_add(stText)
    c = ""
    c += str(res)
    print c
    return(c)

def proc_add(stText):
    liText = stText.split(" ")
    
    if len(liText) != 2:
        diRet = {}
        diRet['text'] = "oops"
        diRet['username'] = "asbot"
        return(json.dumps(diRet, indent = 2))


    try:
        asnum = int(liText[1])
    except ValueError:
        diRet = {}
        diRet['text'] = "plz input int :p"
        diRet['username'] = "asbot"
        return(json.dumps(diRet, indent = 2))

    print "try" + liText[1]
    print "hoge"
    diRet = {}
    print "st"
    diRet['text'] = aslook(liText[1])
    print "end"
    diRet['username'] = "asbot"
    return(json.dumps(diRet, indent = 2))

def aslook(stNum):
    tn = telnetlib.Telnet(host = "asn.cymru.com", port = 43)
    stQue = "AS" + str(stNum) + "\n"
    tn.write(stQue)
    ret = tn.read_all()
    tn.close()
    return(ret)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

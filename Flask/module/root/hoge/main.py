#!/usr/bin/env python
# coding:utf-8

from flask import Module, render_template
from flask import Flask

hoge = Module(__name__)
app = Flask(__name__)

@hoge.route('/')
def index():
    return(render_template("hoge/hello.html", name= "hoge"))



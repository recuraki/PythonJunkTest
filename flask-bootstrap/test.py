#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask import render_template
from flask_bootstrap import Bootstrap

from flask_bootstrap import Bootstrap
#from flask_appconfig import AppConfig

from flask_wtf import Form, RecaptchaField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = \
						'6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
Bootstrap(app)


class ExampleForm(Form):
    field1 = TextField('First Field', description='This is field one.')
    submit_button = SubmitField('Submit Form')

@app.route('/', methods=['GET'])
def index():
    form = ExampleForm()
    return render_template('index.html', form = form)

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


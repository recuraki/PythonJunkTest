#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template, FileSystemLoader
from jinja2 import Environment, PackageLoader
import math

env = Environment(loader=FileSystemLoader("./"))
def is_prime(n):
    if n == 2:
        return True
    for i in xrange(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

env.tests['prime'] = is_prime



template = env.get_template('templ1.html')
# print(template.render())
# print(template.render(name=u"hoge"))
print(template.render({"name": u"hoge"}))

t2 = env.get_template('templ2.html')
print(t2.render({"title": "hoge", "users": [
{"url": "a", "username": "namea"},
{"url": "b", "username": "nameb"},
] }))

stream = template.stream(name='John Doe')

print stream.next()

m = Template(u"{% set a, b = 'foo', 'föö' %}").module
print m.a
print m.b

t = Template('{% macro foo() %}42{% endmacro %}23')
print unicode(t.module)
print t.module.foo()



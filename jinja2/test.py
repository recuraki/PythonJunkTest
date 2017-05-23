#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template

templ="""
{% if flag == None %}
True
{% else %}
False
{% endif %}
{{ name }}
"""
template = Template(templ)
print template.render(flag=1, name="kanai")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install pygments
# git clone https://github.com/dart-lang/py-gfm.git
# cd py-gfm
# python setup.py install

import markdown

templ = u"""
hogehoge

```
import sys

def hoge(fuga):
  fugafuga = 123
  print fugafuga
  return 'ok'
```

`ほげ`です

> 引用
>> もっと引用
"""

if '__main__' == __name__:
    codehilite = 'codehilite(force_linenos=True, guess_lang=False, css_class=syntax)'
    html = markdown.markdown(templ, extentions = ['extra', codehilite, 'gfm'])
    print(html.encode('utf-8'))


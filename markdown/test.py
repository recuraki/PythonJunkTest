#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install pygments

# git clone https://github.com/dart-lang/py-gfm.git
# cd py-gfm
# sudo python setup.py install

# sudo pip install mdx_linkify  bleach  html5lib
# sudo pip install mdx_del_ins

import markdown


templ = u"""
hogehoge

[google](http://www.google.com)

```ruby
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
    html = markdown.markdown(templ, ['extra', codehilite, 'gfm' ])
    print(html.encode('utf-8'))

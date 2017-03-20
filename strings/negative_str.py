#!/usr/bin/python
# -*- coding: utf-8 -*-

# 結果として想定される文字列をstrに代入
str="""
neighbor as100 192.168.100.1
neighbor as200 192.168.100.2
neighbor as200 192.168.100.3
neighbor as300 192.168.100.4
"""

import re

print("Original:")
print("[" + str + "]")

for l in str.split("\n"):
  res = re.search("neighbor (?!as200)", l)
  if res is not None:
    print(l)


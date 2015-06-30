#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# 結果として想定される文字列をstrに代入
str="""Result
eth 1/1
 incount = 100
 outcount = 200
eth 1/2
 incount = 0
 outcount = 10
eth 1/3
 incount = 0
 outcount = 100
"""

# incountにeth 1/1の結果を代入
incount=re.search("eth 1/1\n incount = (\d+)", str).group(1)
print("eth1/1 INCOUNTER = " + incount)
# incountにeth 1/2の結果を代入
incount=re.search("eth 1/2\n incount = (\d+)", str).group(1)
print("eth1/2 INCOUNTER = " + incount)

# 大変なので、関数にする
def get_incount(str, port):
  incount=re.search("eth " + port + "\n incount = (\d+)", str).group(1)
  return incount
print("eth1/1 INCOUNTER = " + get_incount(str, "1/1"))
print("eth1/2 INCOUNTER = " + get_incount(str, "1/2"))
print("eth1/3 INCOUNTER = " + get_incount(str, "1/3"))

# printを繰り返すのはかっこわるい
for port in ["1/1", "1/2", "1/3"]:
  print("eth" + port + " INCOUNTER = " + get_incount(str, port))

# もうちょっとかっこ良く書くなら、format使う
for port in ["1/1", "1/2", "1/3"]:
  print("eth{0} INCOUNTER = {1}").format(port, get_incount(str, port))


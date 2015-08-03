#!/usr/bin/python
# -*- coding: utf-8 -*-

# 結果として想定される文字列をstrに代入
str="""
interface port 1/1
 description hogehoge
 switchport trunk add 201-700
interface port 1/2
 description hogehoge2
 switchport trunk add 201-700,801,900
interface port 1/3
 description hogehoge
 switchport access 2
"""

# まず、元の文字列を表示
print("Original:")
print("[" + str + "]")

import re

# で区切って、extractvlanに渡す
# 100-101,201などを100-101と201に分割し、渡す
def parsevlan(vlanstr):
    vlanlist = []
    for i in vlanstr.split(","):
        vlanlist = vlanlist + extractvlan(i)
    print vlanlist
    
# 100-101などを100,101に展開する
# - が含まれていないならそのまま
def extractvlan(vlanstr):
  res = re.search("(\d+)-(\d+)", vlanstr)
  if res != None:
      bnum = int(res.group(1))
      enum = int(res.group(2)) + 1
      return(range(bnum, enum))
  else:
      return([int(vlanstr)])

# 以下のような文字列を検索し、イテレータ(for可能)にする
# interface port <num>/<num>
# (空白)ほにゃらら
# (空白)ほにゃらら
# switchport trunk add <num>(改行)
r = re.finditer("interface port (\d+/\d+)(\n\s+.*)+\n\s+switchport (trunk add|access) (.*)\n", str)
for res in r:
    eth = res.group(1)
    vlanstr =  res.group(4)
    print eth
    parsevlan(vlanstr)

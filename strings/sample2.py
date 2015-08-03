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

print("Original:")
print("[" + str + "]")

import re

def parsevlan(vlanstr):
    vlanlist = []
    for i in vlanstr.split(","):
        vlanlist = vlanlist + extractvlan(i)
    print vlanlist
    

def extractvlan(vlanstr):
  res = re.search("(\d+)-(\d+)", vlanstr)
  if res != None:
      bnum = int(res.group(1))
      enum = int(res.group(2)) + 1
      return(range(bnum, enum))
  else:
      return([int(vlanstr)])

r = re.finditer("interface port (\d+/\d+)(\n\s+.*)+\n\s+switchport (trunk add|access) (.*)\n", str)
for res in r:
  eth = res.group(1)
  vlanstr =  res.group(4)
  print eth
  parsevlan(vlanstr)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

str="""
interface port 1/1
 description hogehoge
 switchport trunk add 201-700
interface port 1/2
 description hogehoge2
 switchport trunk add 201-700,801,900
interface port 1/3
 description hogehoge
 switchport aceess 2
"""

if __name__ == "__main__":
  res = re.search("interface port 1/1\n[^\n]*\n switchport trunk add ([^\n]*)\n", str, re.DOTALL)
  if res != None:
    vlanstr =  res.group(0)
    print vlanstr

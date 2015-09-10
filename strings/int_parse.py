#!/usr/bin/python
# -*- coding: utf-8 -*-

# 結果として想定される文字列をstrに代入
str="""
interface port 1/1
 description hogehoge
 switchport trunk add  10-12
interface port 1/2
 description hogehoge2
 switchport trunk add 10-20,30,40
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
    # ","でくぎる
    for i in vlanstr.split(","):
        # くぎった文字列を展開する
        vlanlist = vlanlist + extractvlan(i)
    print vlanlist
    
# 100-101などを100,101に展開する
# - が含まれていないならそのまま
def extractvlan(vlanstr):
    # 数値-数値をパース
    res = re.search("(\d+)-(\d+)", vlanstr)
    # これにマッチするなら
    if res != None:
        bnum = int(res.group(1))
        enum = int(res.group(2)) + 1
        # range(数値, 数値 + 1)を実行
        return(range(bnum, enum))
    # マッチしない = 1とか2だけなら
    else:
        # そのまま返す
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

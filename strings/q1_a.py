#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# Try1: "pen"が含まれているか確認し、含まれていたらokと表示しましょう
query = "pen"
if re.search(query, "this is a pen.") != None:
    print("ok")
if re.search(query, "this is a hoge.") != None:
    print("ok")

# Try2: "axcx"という文字列が含まれているか確認しましょう
# そして、その文字列を表示しましょう。
# ただし、ここではxは「なにかの文字」です
query = r"a.c."
print(re.search(query, "abcABC").group())

# Try3: "a"からはじまって"d"で終わる文字列を探してください
# 対象は"a12b23c34d45e56f"です
query = "a.*d"
print(re.search(query, "a12b23c34d45e56f").group())
print(re.search(query, "ad1234").group())

# Try4: "ab"のあとに"c"が一個以上あり、"d"で終わる文字列を探してください
query = "abc+d"
print(re.search(query, "abcccdef").group())
# 以下はcがないのでNoneが帰ってokと表示されるべきです
if re.search(query, "abd") == None:
    print("ok")

# Try5: "hoge12345foo"から12345を探すように「数字の列」を探してください
query = "[0-9]+"
print(re.search(query, "hoge12345foo").group())
print(re.search(query, "this is 34567").group())

# try6: fooかbarが含まれているか確認してください
query = "(foo|bar)"
print(re.search(query, "hoge12345foo").group())
if re.search(query, "this is 34567") is None:
    print("ok")

# try7: "Incounter: 数字"という文字列かどうか確認してください
query = "Incounter: \d+"
print(re.search(query, "Incounter: 100").group())
if re.search(query, "incounter: 100") is None:
    print("ok")

# try7-2: 上記の例で、「Incounter」でも「incounter」でもいいようにしてください 
query = "[Ii]ncounter: \d+"
print(re.search(query, "Incounter: 100").group())
print(re.search(query, "incounter: 100").group())

# try8: "incounter: 数字"から数字の部分を抜き出してください
query = "incounter: (\d+)"
print(re.match(query, "incounter: 100").group(1))

# try8-2: "incounter: 数字, outcounter: 数字"から数字を抜き出してください
query = "incounter: (\d+), outcounter: (\d+)"
print(re.match(query, "incounter: 100, outcounter: 200").group(1))
print(re.match(query, "incounter: 100, outcounter: 200").group(2))
print(re.match(query, "incounter: 100, outcounter: 200").groups())

# try9: "foo"を"bar"に置換してください
query = "foo"
replaceas = "bar"
print(re.sub(query, replaceas, "I'm foo."))

# try10: "incounter: 数字"を"in = 数字"に変換してください
query = "incounter: (\d+)"
replaceas = "in = \\1"
print(re.sub(query, replaceas, "incounter: 100"))

# try10-2: "incounter: 数字, outcounter: 数字"を"in,out = 数字,数字"に変換してください
query = "incounter: (\d+), outcounter: (\d+)"
replaceas = "in,out = \\1,\\2"
print(re.sub(query, replaceas, "incounter: 100, outcounter: 200"))


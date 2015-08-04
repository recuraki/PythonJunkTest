#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

def check_result(res):
    if res is None:
        print("NOT FOUND")
    else:
        print("FOUND:[" + res.group() + "]") 

# Try1: "pen"が含まれているか確認し、含まれていたらokと表示しましょう
print("Try1")
query = ""
res = re.search(query, "this is a pen.")
check_result(res)

res = re.search(query, "this is a hoge.")
check_result(res)

# Try2: "axcx"という文字列が含まれているか確認しましょう
# そして、その文字列を表示しましょう。
# ただし、ここではxは「なにかの文字」です
print("Try2")
query = ""
res = re.search(query, "abcABC")
check_result(res)

# Try3: "a"からはじまって"d"で終わる文字列を探してください
# 対象は"a12b23c34d45e56f"です
print("Try3")
query = ""
res = re.search(query, "a12b23c34d45e56f")
check_result(res)
res = re.search(query, "ad1234")
check_result(res)

# Try4: "ab"のあとに"c"が一個以上あり、"d"で終わる文字列を探してください
print("Try4")
query = ""
res = re.search(query, "abcccdef")
check_result(res)
res = re.search(query, "abd")
check_result(res)

# Try5: "hoge12345foo"から12345を探すように「数字の列」を探してください
print("Try5")
query = ""
res = re.search(query, "hoge12345foo")
check_result(res)
res = re.search(query, "this is 34567")
check_result(res)

# try6: fooかbarが含まれているか確認してください
print("Try6")
query = ""
res = re.search(query, "hoge12345foo")
check_result(res)
res = re.search(query, "this is 34567")
check_result(res)

# try7: "Incounter: 数字"という文字列かどうか確認してください
print("Try7")
query = ""
res = re.search(query, "Incounter: 100")
check_result(res)
res = re.search(query, "incounter: 100")
check_result(res)

# try7-2: 上記の例で、「Incounter」でも「incounter」でもいいようにしてください 
print("Try7-2")
query = r""
re.search(query, "Incounter: 100")
check_result(res)
re.search(query, "incounter: 100")
check_result(res)

# try8: "incounter: 数字"から数字の部分を抜き出してください
print("Try8")
query = ""

res = re.match(query, "incounter: 100")
# 以下の
print(res.group())
# 以下のプリント分をかんがえてみてください
print(res.group(1))


# try8-2: "incounter: 数字, outcounter: 数字"から数字を抜き出してください
print("")
query = "incounter: (\d+), outcounter: (\d+)"
res = re.match(query, "incounter: 100, outcounter: 200")
if res is not None:
    print(res.group(1))
    print(res.group(2))
    print(res.groups())

# try9: "foo"を"bar"に置換してください
print("Try9")
query = ""
replaceas = ""
print(re.sub(query, replaceas, "I'm foo."))

# try10: "incounter: 数字"を"in = 数字"に変換してください
print("Try10")
query = ""
replaceas = ""
print(re.sub(query, replaceas, "incounter: 100"))

# try10-2: "incounter: 数字, outcounter: 数字"を"in,out = 数字,数字"に変換してください
print("Try10-2")
query = ""
replaceas = ""
print(re.sub(query, replaceas, "incounter: 100, outcounter: 200"))


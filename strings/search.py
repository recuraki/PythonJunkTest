#!/usr/bin/python
# -*- coding: utf-8 -*-

# 結果として想定される文字列をstrに代入
str="""Result
eth 1/1
 InOctet = 100
 OutOctet = 200
"""

print("Original:")
print(str)

print("----")
print("Parse:")

pos = str.find("InOctet")
print(str[pos:pos+7])


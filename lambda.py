#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
lambda式関係を色々書きためる
"""

# 基本
add_lambda = lambda x,y: x + y
sqr_lambda = lambda x: x ** 2

# 実行時に評価
print apply(add_lambda, [2,2])
# 4

# リストに2項ずつ適応
print reduce(add_lambda, [1,2,3])
# 6

# 全てのリストに適応
print map(sqr_lambda, [1,2,3])
# [1,4,9]


"""
>>> compare = lambda a,b:1 if a > b else 0 if a == b else -1
>>> compare(1,2)
-1
>>> compare(2,1)
1
>>> compare(1,1)
0
"""
compare = lambda a,b:1 if a > b else 0 if a == b else -1
print compare(1,2)

"""
>>> GetReverseString = lambda x: ''.join(list(reversed(x)))
>>> GetReverseString("hoge")
'egoh'
>>> "hoge"[::-1]
'egoh'
"""
GetReverseString = lambda x: ''.join(list(reversed(x)))
print GetReverseString("hoge")
print "hoge"[::-1]


"""
>>> str2indexlist = lambda stInput: map(lambda x,y: [x,y], stInput, range(len(stInput)))
>>> str2indexlist("hoge")
[['h', 0], ['o', 1], ['g', 2], ['e', 3]]
"""
str2indexlist = lambda stInput: map(lambda x,y: [x,y], stInput, range(len(stInput)))
print str2indexlist("hoge")

"""
>>> str2indexlist = lambda stInput: [[y, x] for x, y in enumerate(stInput)]
>>> str2indexlist("hoge")
[['h', 0], ['o', 1], ['g', 2], ['e', 3]]
"""
str2indexlist = lambda stInput: [[y, x] for x, y in enumerate(stInput)]
print str2indexlist("hoge") 

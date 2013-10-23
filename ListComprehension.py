#!/usr/bin/python
# -*- coding: utf-8 -*-

# 内包リスト表記
print [x ** 2 for x in [1,2,3]]
# [1, 4, 9]

# 内包リストのif
print [x ** 2 for x in [1,2,3,4,5] if x == 3]
# [9]

# 内包リストの２変数
print [[x,y] for x in [1,2] for y in [3,4,5] if y < 5]
# [[1, 3], [1, 4], [2, 3], [2, 4]]

print [[x,y] for x in [1,2,3] for y in [4,5,6] if y < 5]
# [[1, 4], [2, 4], [3, 4]]

# 条件分岐はどっちでもいい
print [[x,y] for x in [1,2,3] if x < 3 for y in [4,5,6] if y < 5]
# [[1, 4], [2, 4]]

print [[x,y] for x in [1,2,3] for y in [4,5,6] if y < 5 and x < 3]
# [[1, 4], [2, 4]]

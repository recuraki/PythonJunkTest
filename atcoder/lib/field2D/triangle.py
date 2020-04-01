
# heron の公式
# a,b,cは三角形の各辺の長さ
def triangleAreaByHeron(a, b, c):
    from decimal import Decimal
    a,b,c = Decimal(a), Decimal(b), Decimal(c)
    s = (a + b + c) / Decimal(2)
    return Decimal(s * (s - a) * (s - b) * (s - c)).sqrt()
"""
print(triangleAreaByHeron(3,4,5))
>>> 6
"""

# sarrus の公式 / サラス の公式
# https://mathtrain.jp/sarrus_formula
# (0, 0), (a, b), (c, d)で囲まれた面積
# 0, 0がない場合、うまくシフトすること
def triangleAreaBySarrus(a, b, c, d):
    return abs( (a*d) - (b*c) ) / 2
"""
print(triangleAreaBySarrus(1, 4, -1, -2))
>>> 1
"""

#https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266
def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

# 高速にpopcountする。1の数を数える。
# https://atcoder.jp/contests/abc157/submissions/10434154
#def popcount(i):
#    assert 0 <= i < 0x100000000
#    i = i - ((i >> 1) & 0x55555555)
#    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
#    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

"""
>>> popcount(2)
1
>>> popcount(3)
2
"""

# list(int)をbinaryに変換する
bin_a="".join(["{:020b}\n".format(a) for a in map(int, "2 3 4".split())])
"""
print(bin_a)
00000000000000000010
00000000000000000011
00000000000000000100
"""

# 1からnをbinaryに変換する
bin_a="".join(["{:07b}\n".format(a) for a in range(1,7)])
"""
0000001
0000010
0000011
0000100
0000101
0000110
"""

# ビット全探索用の基本コード
def bit_all_find():
    for pat in range(2 ** n):
        tmp = [0] * m
        for i in range(n):
            if (pat >> i & 1) == 1:
                tmp[i] = True

# 1からnをbinaryのリストにする
bin_a = ["{:03b}".format(a) for a in range(1,7+1)]
bin_a = list(map(lambda x: [int(y) for y in list(x)], bin_a))
print(bin_a)

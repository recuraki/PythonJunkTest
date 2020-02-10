# sec 15.4
from pprint import pprint
dna1="ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
dna2="GTCGTTCGGAATGCCGTTGCTCTGTAAA"
dna3="GTCGTCGGAAGCCGGCCGAA"

# >>> [chr(i) for i in range(0x61,0x61+26)]
list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

str_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_lower = 'abcdefghijklmnopqrstuvwxyz'
str_digit = "0123456789"

# アルゴリズムイントロダクション 15.4 LCS
# Longest Common Subsequenceをとり、以下を返す
# b: 結果
# c: そこまでのlongestのcount(内部用)
def lcs_length(x, y):
    m, n  = len(x), len(y)
    b = [[0 for _ in range(n+1)] for _ in range(m+1)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '↖'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "←"
    return c, b

# アルゴリズムイントロダクション 15.4 LCS
# bを基にもともとのinput xから共通部分を抜き出す。
def lcs_decode(b, X, i, j):
    import collections
    res = collections.deque([])
    while True:
        #print("i={0}, j={1} b={2}".format(i,j,b[i][j]))
        if i == 0 or j == 0:
            break
        if b[i][j] == '↖':
            res.appendleft(X[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == "↑":
            i -= 1
            continue
        else:
            j -= 1
            continue
    return res

# 適当に実装したけどあってるはず
# lcsした結果から「一致しなかった部分」を取得する
def lcs_decode_negative(b, X, i, j):
    import collections
    res = collections.deque([])
    while True:
        #print("i={0}, j={1} b={2}".format(i,j,b[i][j]))
        if i == 0 or j == 0:
            break
        if b[i][j] == '↖':
            i -= 1
            j -= 1
        elif b[i][j] == "↑":
            res.appendleft(X[i-1])
            i -= 1
            continue
        else:
            j -= 1
            continue
    if i != 0:
        for i in range(1,i+1):
            res.appendleft(X[i-1])
    return res


def lcs_print_recurcive(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == '↖':
        lcs_decode(b, X, i - 1, j - 1)
        print(X[i-1])
    elif b[i][j] == "↑":
        lcs_decode(b, X, i - 1, j)
    else:
        lcs_decode(b, X, i, j - 1)


import itertools
def countstrs(s):
    return [(k, len(list(g))) for k, g in itertools.groupby(s)]

"""
>>> countstrs("1110000111")->    [('1', 3), ('0', 4), ('1', 3)]
>>> countstrs("") ->    []
>>> countstrs("aaa") ->    [('a', 3)]
"""


"""
deque(['B', 'C', 'B', 'A'])
deque(['A', 'D', 'B'])
"""
from pprint import pprint
str1 = "ABCBDAB"
str2 = "BDCABA"
c, b = lcs_length(str1, str2)
#pprint(c)
#pprint(b)
print(lcs_decode(b, str1, len(str1), len(str2)))
print(lcs_decode_negative(b, str1, len(str1), len(str2)))

"""
deque(['B', 'C', 'B', 'A'])
deque(['D', 'B'])
"""
str1 = "BCBDAB"
str2 = "BDCABA"
c, b = lcs_length(str1, str2)
#pprint(c)
#pprint(b)
print(lcs_decode(b, str1, len(str1), len(str2)))
print(lcs_decode_negative(b, str1, len(str1), len(str2)))

"""
deque(['a', 'b', 'c', 'd', 'f'])
deque(['g', 'e'])
"""
str1 = "agbcdfe"
str2 = "abcdefg"
c, b = lcs_length(str1, str2)
print(lcs_decode(b, str1, len(str1), len(str2)))
print(lcs_decode_negative(b, str1, len(str1), len(str2)))


"""
deque(['a', 'b', 'c', 'd'])
deque([])
"""
str1 = "abcd"
str2 = "abcd"
c, b = lcs_length(str1, str2)
#pprint(c)
#pprint(b)
print(lcs_decode(b, str1, len(str1), len(str2)))
print(lcs_decode_negative(b, str1, len(str1), len(str2)))



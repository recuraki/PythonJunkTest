from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict



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


###################################
# Paste the template of question
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        str1 = s
        str2 = t
        c, b = lcs_length(s,t )
        print(lcs_decode(b, s, len(s), len(t)))



###################################


st = Solution()

print(st.minimumScore(s = "abacaba", t = "bzaa")==1)
print(st.minimumScore(s = "cde", t = "xyz")==3)


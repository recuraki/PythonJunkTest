
from typing import List, Tuple
from pprint import pprint



"""
>>> countstrs("1110000111")->    [('1', 3), ('0', 4), ('1', 3)]
>>> countstrs("") ->    []
>>> countstrs("aaa") ->    [('a', 3)]
>>> countstrs_withIndex("1110000111")-> [('1', 3, 0), ('0', 4, 3), ('1', 3, 7)]
"""
import itertools

def countstrs(s):
    return [(k, len(list(g))) for k, g in itertools.groupby(s)]

def countstrs_withIndex(s):
    d = countstrs(s)
    r = []
    ind = 0
    for i in range(len(d)):
        r.append((d[i][0], d[i][1], ind))
        ind += d[i][1]
    return r


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        C = countstrs(s)
        max0 = max1 = 0
        for ch, cnt in C:
            if ch == "1":
                max1 = max(max1, cnt)
            else:
                max0 = max(max0, cnt)
        if max1 > max0:
            return True
        else:
            return False

st = Solution()

print(st.checkZeroOnes( s = "1101"))
print(st.checkZeroOnes(s = "111000"))
print(st.checkZeroOnes(s = "110100010"))


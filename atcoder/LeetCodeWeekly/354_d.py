from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

"""
文字列の長さはn
禁則の数はn
それぞれ10まで
なので、長さ1 - 10でろりはをとる。


"""

import itertools
class rollingHash61():
    MOD = (1<<61) - 1
    BASE = 20200213
    MASK30 = (1 << 30) - 1
    MASK31 = (1 << 31) - 1
    hashTable = []
    pow = []
    slen = -1
    sdat = []

    def __init__(self, s: str):
        self.sdat = list(map(lambda x: ord(x), s))
        self.slen = len(s)
        self.hashTable = [0] * (self.slen + 1)
        self.pow = [1] * (self.slen + 1)
        for i in range(self.slen):
            self.hashTable[i + 1] = self.multi(self.hashTable[i], self.BASE)
            self.hashTable[i + 1] += self.xorshift(self.sdat[i] + 1)
            self.pow[i+1] = self.multi(self.pow[i], self.BASE)
            self.hashTable[i + 1] = (self.hashTable[i + 1] - self.MOD) if (self.hashTable[i + 1] >= self.MOD) else self.hashTable[i + 1]

    def hash(self, l, r):
        # calc hash [l, r)  r = OPEN
        res = self.MOD + self.hashTable[r] - self.multi(self.hashTable[l], self.pow[r - l])
        return res if (res < self.MOD) else (res - self.MOD)

    def mod(self, x):
        res = (x >> 61) + (x & self.MOD)
        return res - self.MOD if res >= self.MOD else res

    def multi(self, x, y):
        xu, xd = x >> 31, x & self.MASK31
        yu, yd = y >> 31, y & self.MASK31
        m = xd * yu + xu * yd
        mu = m >> 30
        md = m & self.MASK30
        return self.mod(xu * yu * 2 + mu + (md << 31) + xd * yd)

    def xorshift(self, x):
        return x ^ (x << 13) ^ (x >> 17) ^ (x << 5)

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
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        rh = rollingHash61(word)
        n = len(word)
        forb = set()
        for s in forbidden:
            rs = rollingHash61(s)
            forb.add(rs.hash(0, len(s)))
        #print(rh.hash(0, n))
        #print(forb)
        l = 0
        r = -1
        ans = 0
        rok = True # rを伸ばしていいですか？
        cand= []
        while r < (n-1): # [l, r] とする(close, close)
            # 基本的には伸ばしていきたい
            if rok:
                r += 1
                #print(l, r)
                can = True # いけるかな？
                goodl = r
                for le in range(1, 11):
                    x = r - le  # l 相当
                    if x < l: break # これ以上見られないならOK
                    if rh.hash(x, r+1) in forb:
                        #print("-", l, r, word[x: r+1])
                        can = False
                        break
                for le in range(1, 11):
                    rr = l + le - 1
                    if r < rr: break # これ以上見られないならOK
                    if rh.hash(l, rr+1) in forb:
                        #print("-2", l, rr, word[l:rr+1])
                        can = False
                        break
                if can:
                    #print("!1", l, r)
                    ans = max(ans, r-l + 1)
                    continue
                rok = False
            # rok = Falseの時しか来ない
            #print("?")
            while l <= r:
                l += 1
                can = True # いけるかな？
                for le in range(1, 11):
                    x = l + le - 1
                    if r < x: break # これ以上見られないならOK
                    if rh.hash(l, x + 1) in forb:
                        can = False
                        break

                if can:
                    rok = True
                    break
                if l == r:
                    l += 1
                    rok = True
                    break
        print(ans)
        return ans
st = Solution()

print(st.longestValidSubstring(word = "cbaaaabc", forbidden = ["aaa","cb"])==4)
print(st.longestValidSubstring( word = "leetcode", forbidden = ["de","le","e"])==4)
print(st.longestValidSubstring( word = "eee", forbidden = ["e"])==0)
print(st.longestValidSubstring( word = "lelele", forbidden = ["le", "el"])==1)
print(st.longestValidSubstring( word = "leeel", forbidden = ["leee", "eeel"])==3)
print(st.longestValidSubstring( word = "a", forbidden = ["n"])==1)
print(st.longestValidSubstring("bcac", ["bcac","caca","bcac","bca"])==3)
print(st.longestValidSubstring("babbb", ["bbb","aacb","babbb","bcab"]) == 4)

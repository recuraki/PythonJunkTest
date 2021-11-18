from typing import List, Tuple
from pprint import pprint

class rollingHash61():
    MOD = (1<<61) - 1
    BASE = 20200213
    MASK30 = (1<<30) - 1
    MASK31 = (1<<31) - 1
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
        return x ^ (x<<13) ^ (x>>17) ^ (x<<5)



###################################
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        return 0


###################################


st = Solution()

print(st.countSubstrings(s = "aba", t = "baba"))
print(st.countSubstrings(s = "ab", t = "bb"))
print(st.countSubstrings(s = "a", t = "a"))
print(st.countSubstrings(s = "abe", t = "bbc"))

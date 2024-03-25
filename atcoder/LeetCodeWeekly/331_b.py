from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class BinaryIndexTreeSum:
    #
    # BE
    #
    def __init__(self, n): # [1-n]を作る
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i): # [1-i]のsumを取る(閉区間なことに注意)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def addCloseClose(self, i, x):
        assert i > 0 # bitなので1-indexed
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def rangesumCloseOpen(self, i, j): # [i, j) の和 Close-Open
        assert i > 0 # bitなので1-indexed
        assert i <= j
        return self.sum(j-1) - self.sum(i-1)

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        bit = BinaryIndexTreeSum(n)
        v = set()
        v.add("a")
        v.add("e")
        v.add("i")
        v.add("o")
        v.add("u")
        for i in range(n):
            if words[i][0] in v and words[i][-1] in v: bit.addCloseClose(i+1, 1)
        ans = []
        for l, r in queries:
            l += 1
            r += 1
            ans.append(bit.rangesumCloseOpen(l, r+1))
        return ans




st = Solution()

print(st.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])== [2,3,0])
print(st.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])==[3,2,1])


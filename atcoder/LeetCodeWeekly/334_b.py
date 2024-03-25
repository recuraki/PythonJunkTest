from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        dat = []
        n = len(word)
        for i in range(n): dat.append(int(word[i]))
        cur = 0
        ans = []
        for i in range(n):
            cur += dat[i]
            cur %= m
            if cur == 0:ans.append(1)
            else: ans.append(0)
            cur *= 10
        return ans


st = Solution()

print(st.divisibilityArray( word = "998244353", m = 3)== [1,1,0,0,0,1,1,0,0])
print(st.divisibilityArray(word = "1010", m = 10)== [0,1,0,1])


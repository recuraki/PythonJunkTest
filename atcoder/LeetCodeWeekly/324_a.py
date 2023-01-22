from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

###################################
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        buf = list()
        ans = 0
        for s in words:
            se = set(list(s))
            for p in buf:
                if se == p: ans += 1
            buf.append(se)
        return ans




st = Solution()

print(st.similarPairs(words = ["aba","aabb","abcd","bac","aabc"])==2)
print(st.similarPairs(words = ["aabb","ab","ba"])==3)
print(st.similarPairs(words = ["nba","cba","dba"])==0)



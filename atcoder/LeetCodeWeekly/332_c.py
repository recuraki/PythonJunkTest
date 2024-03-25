from typing import List, Tuple, Optional
from collections import deque, defaultdict


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        buf = defaultdict(lambda : [-1, -1])
        for i in range(1, 32):
            for l in range(len(s) - i+1):
                if s[l:l+i] not in buf: buf[s[l:l+i]] = [l, l+i-1]
        ans = []
        for a, b in queries: ans.append(buf[bin(a^b)[2:]])
        return ans


st = Solution()

print(st.substringXorQueries( s = "101101", queries = [[0,5],[1,2]])==[[0,2],[2,3]])
print(st.substringXorQueries( s = "0101", queries = [[12,8]])== [[-1,-1]])
print(st.substringXorQueries(  s = "1", queries = [[4,5]])== [[0,0]])



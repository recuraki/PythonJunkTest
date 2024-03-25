from typing import List, Tuple
from pprint import pprint


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        point = [0] * n
        for i in range(n):
            nxt = edges[i]
            point[nxt] += i
        m = max(point)
        for i in range(n):
            if point[i] == m:
                return i
        assert False


st = Solution()

print(st.edgeScore(edges = [1,0,0,0,0,7,7,5])==7)
print(st.edgeScore(edges = [2,0,0,2])==0)


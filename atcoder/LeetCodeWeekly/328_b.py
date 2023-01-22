from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        addtable = [[0] * n for _ in range(n)]
        for h1, w1, h2, w2 in queries:
            for h in range(h1, h2+1):
                addtable[h][w1] += 1
                if w2 < (n-1):
                    addtable[h][w2+1] -= 1
        print(addtable)
        for h in range(n):
            cur = 0
            for w in range(n):
                cur += addtable[h][w]
                ans[h][w] = cur
        print(ans)
        print(addtable)
        return (ans)



st = Solution()

print(st.rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]])==[[1,1,0],[1,2,1],[0,1,1]])
print(st.rangeAddQueries( n = 2, queries = [[0,0,1,1]])== [[1,1],[1,1]])


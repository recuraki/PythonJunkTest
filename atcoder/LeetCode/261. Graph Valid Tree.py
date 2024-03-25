from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        from collections import deque
        q = deque([])
        visited = [False] * n
        q.append( (0, -1) )
        while(len(q) > 0):
            cur, parent = q.popleft()
            visited[cur] = True
            for nxt in g[cur]:
                if nxt == parent: continue
                if visited[nxt] == True: return False
                q.append( (nxt, cur) )
        for x in visited:
            if x is False: return False
        return True


st = Solution()

print(st.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]])==True)
print(st.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]])==False)


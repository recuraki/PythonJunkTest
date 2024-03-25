from typing import List, Tuple
from pprint import pprint


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = [[] for _ in range(n)]
        rest = set(restricted)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n
        from collections import deque
        q = deque([0])
        visited[0] = True
        while len(q) > 0:
            cur = q.popleft()
            for nxt in g[cur]:
                if nxt in rest: continue
                if visited[nxt]: continue
                visited[nxt] = True
                q.append(nxt)
        ans = 0
        for x in visited:
            if x: ans += 1
        return ans


st = Solution()

print(st.reachableNodes(n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5])==4)
print(st.reachableNodes(n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1])==3)


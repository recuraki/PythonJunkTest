class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n
        ans = 0
        for st in range(n):
            if visited[st]: continue
            q = [st]
            ans += 1
            while (len(q) > 0):
                cur = q.pop()
                for nxt in g[cur]:
                    if visited[nxt]: continue
                    visited[nxt] = True
                    q.append(nxt)

        return ans



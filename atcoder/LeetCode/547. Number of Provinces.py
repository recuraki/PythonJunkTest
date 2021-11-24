
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        from collections import deque
        q = deque([])
        ans = 0
        for i in range(n):
            if visited[i]: continue
            visited[i] = True
            ans += 1
            q.append(i)
            while len(q) > 0:
                cur = q.pop()
                for nnode in range(n):
                    if visited[nnode]: continue
                    if isConnected[cur][nnode] == 0: continue
                    q.appendleft(nnode)
                    visited[nnode] = True
        return ans
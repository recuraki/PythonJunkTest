

from collections import deque
class topologicalSort():
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.edgeNum = [0] * n
    def makeEdge(self, u, v):
        assert u != v
        self.g[u].append(v)
        self.edgeNum[v] += 1 # 入次++
    def solve(self):
        q = deque([])
        ans = []
        for i in range(self.n):
            if(self.edgeNum[i] != 0): continue
            q.appendleft(i)
            ans.append(i)
        while(len(q) > 0):
            cur = q.popleft()
            for nxt in self.g[cur]:
                self.edgeNum[nxt] -= 1
                if self.edgeNum[nxt] == 0:
                    ans.append(nxt)
                    q.append(nxt)
        return ans


def GRL_4_B():
    n, m = map(int, input().split())
    ts = topologicalSort(n)
    for _ in range(m):
        u, v = map(int, input().split())
        ts.makeEdge(u, v)
    ans = ts.solve()
    for x in ans: print(x)

GRL_4_B()
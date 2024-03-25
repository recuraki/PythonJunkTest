

from collections import deque
class StronglyConnectedComponent():
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.gr = [[] for _ in range(n)] # graph rev
    def addEdge(self, u, v):
        self.g[u].append(v)
        self.gr[v].append(u)

    def dfs(self, v):
        # 正方向のDFS
        self.visited[v] = True
        for nxt in self.g[v]:
            if self.visited[nxt]: continue
            self.dfs(nxt)
        self.vs.append(v)

    def solve(self):
        self.vs = [] # かえりがけ
        self.visited = [False] * self.n
        k = 0
        self.cmp = [None] * self.n
        # DFS1

        for i in range(self.n):
            if self.visited[i] is True: continue
            self.dfs(i)

        q = deque([])
        self.visited = [False] * self.n
        for i in self.vs[::-1]:
            if self.visited[i] is True: continue
            q.append(i)
            while len(q) > 0:
                cur = q.popleft()
                self.visited[cur] = True
                self.cmp[cur] = k
                for nxt in self.gr[cur]:
                    if self.visited[nxt]: continue
                    q.append(nxt)
            k += 1

        return k


vCount = 13 # 超点数
sc = StronglyConnectedComponent(13)
sc.addEdge( 0,12)
sc.addEdge( 12, 11)
sc.addEdge( 11, 8)
sc.addEdge( 11, 10)
sc.addEdge( 10, 9)
sc.addEdge( 9, 8)
sc.addEdge( 9, 7)
sc.addEdge( 8,10)
sc.addEdge( 7,6)
sc.addEdge( 6,5)
sc.addEdge( 5,7)
sc.addEdge( 6,3)
sc.addEdge( 6,4)
sc.addEdge( 4,3)
sc.addEdge( 3,2)
sc.addEdge( 2,3)
sc.addEdge( 4,1)

# vs:  [5, 2, 3, 1, 4, 6, 7, 9, 10, 8, 11, 12, 0]
# cmp: [0, 6, 7, 7, 5, 4, 4, 4, 3, 3, 3, 2, 1]
sc.solve()
print(sc.cmp)
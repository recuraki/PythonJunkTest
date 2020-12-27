
from collections import deque
class Dinic(object):
    INF = 2**60
    def __init__(self, n):
        """
        n: num of vertex
        """
        self.e = [[] for _ in range(n)]
        self.dist = [-1] * n
        self.iter = [-1] * n
        self.n = n

    def makeEdge(self, s, t, cap):
        l = [t, cap, None] # edge
        lrev = [s, 0, l] # reverse edge
        l[2] = lrev
        self.e[s].append(l)
        self.e[t].append(lrev)

    def bfs(self, s):
        self.dist[s] = 0 # init start point
        q = deque([])
        q.appendleft(s)
        while len(q) > 0:
            curNode = q.popleft()
            #print("curNode", curNode)
            for nextNode, edgeCap, revEdge in self.e[curNode]:
                #print("edgeCap", nextNode, edgeCap)
                if edgeCap > 0 and self.dist[nextNode] == -1:
                    self.dist[nextNode] = self.dist[curNode] + 1
                    q.appendleft(nextNode)


    def dfs(self, curNode, g, flow):
        if curNode == g:
            return flow

        for i in range(self.iter[curNode], len(self.e[curNode])):

            self.iter[curNode] += 1

            l = self.e[curNode][i] # node, cap, revpath

            # go only forward, don't back to parent
            if l[1] > 0 and self.dist[curNode] < self.dist[l[0]]:
                f = self.dfs(l[0], g, min(flow, l[1]))
                if f > 0:
                    l[1] -= f
                    l[2][1] += f
                    return f
        return 0

    def solve(self, s, g):
        """Max-Flow! """
        flow = 0
        while True:
            self.dist = [-1] * self.n
            self.bfs(s)
            if self.dist[g] == -1:
                return flow
            self.iter = [-1] * self.n
            while True:
                res = self.dfs(s, g, self.INF)
                #print("res", res)
                if res <= 0: # cannot more flow Then End
                    break
                flow += res


#mf = Dinic(4)
#mf.makeEdge(0,1,2)
#mf.makeEdge(0,2,1)
#mf.makeEdge(1,2,1)
#mf.makeEdge(1,3,1)
#mf.makeEdge(2,3,2)
#print(mf.e)
#print(mf.solve(0, 4-1))
n, m = map(int, input().split())
mf = Dinic(n)
for _ in range(m):
    a,b,c = map(int,input().split())
    mf.makeEdge(a,b,c)
print(mf.solve(0, n-1))

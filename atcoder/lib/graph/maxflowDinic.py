from collections import deque


class DinicRecurcive(object):
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

def arc111_b():
    nmax = 2 * 10 ** 5
    colormax = 4 * 10 ** 5
    import sys
    input = sys.stdin.readline

    n = int(input())
    node = nmax + colormax + 10
    snode = node - 3
    tnode = node - 2
    mf = DinicRecurcive(node)
    for i in range(n):
        a, b = map(int, input().split())
        a += nmax
        b += nmax
        mf.makeEdge(snode, i, 1)
        mf.makeEdge(i, a, 1)
        mf.makeEdge(i, b, 1)

    for i in range(nmax, nmax + colormax + 2):
        mf.makeEdge(i, tnode, 1)

    print(mf.solve(snode, tnode))

def test():
    mf = DinicRecurcive(4)
    mf.makeEdge(0,1,2)
    mf.makeEdge(0,2,1)
    mf.makeEdge(1,2,1)
    mf.makeEdge(1,3,1)
    mf.makeEdge(2,3,2)
    print(mf.solve(0, 4-1))


def aoj():
    n, m = map(int, input().split())
    mf = DinicRecurcive(n)
    for _ in range(m):
        a,b,c = map(int,input().split())
        mf.makeEdge(a,b,c)
    print(mf.solve(0, n-1))

def GRL_7_A():
    x,y,e = map(int, input().split())
    mf = DinicRecurcive(x+y+2)
    for _ in range(e):
        a,b = map(int,input().split())
        mf.makeEdge(a+1, x+1+b,1)
    for i in range(x):
        mf.makeEdge(0, i+1,1)
    for i in range(y):
        mf.makeEdge(x+i+1,x+y+1,1)
    print(mf.solve(0, x+y+1))


#test()
GRL_7_A()
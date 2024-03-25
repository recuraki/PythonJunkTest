import heapq
from collections import deque
class dijkstra():
    INF = 2 ** 62 + 10000
    INF = float("inf")
    def __init__(self, numV):
        self.numV = numV
        self.e = [[] for _ in range(numV)]

    def makeEdge1way(self, s, t, cost):
        self.e[s].append((t, cost))

    def makeEdge2way(self, s, t, cost):
        self.e[s].append((t, cost))
        self.e[t].append((s, cost))

    def solve(self, nodeS, nodeT):
        self.cost = [self.INF] * self.numV # cost
        self.parent = [-1] * self.numV # parent node
        q = [(0, nodeS)]  # 初期ノード(cost 0)
        self.cost[nodeS] = 0
        heapq.heapify(q)
        while len(q) > 0:
            curcost, curnode = heapq.heappop(q)
            #print("Curcost:{0}, Curnode{1}".format(curcost, curnode))
            # 打ち切り。ゴールが明確ならここに入れる。
            #if curnode == nodeT: return
            if curcost > self.cost[curnode]:
                continue
            for nextnode, edgecost in self.e[curnode]:
                nextcost = curcost + edgecost
                if self.cost[nextnode] > nextcost:
                    self.cost[nextnode] = nextcost
                    self.parent[nextnode] = curnode
                    heapq.heappush(q, (nextcost, nextnode))

    def findRoute(self, s, t):
        # THIS FUNCTION should be called after solve()
        route = deque([])
        nextnode = t
        while nextnode != -1:
            route.appendleft(str(nextnode))
            nextnode = self.parent[nextnode]
        return route

def test():
    dj = dijkstra(4)
    dj.makeEdge(0,1,10)
    dj.makeEdge(0,2,4)
    dj.makeEdge(1,2,2)
    dj.makeEdge(2,3,1)
    dj.makeEdge(1,3,5)
    dj.solve(0, 0)
    print(dj.cost)
    print(dj.findRoute(0,2))

def aoj_1_a():
    v, e, r = map(int, input().split())
    dj = dijkstra(v)
    for _ in range(e):
        # 0 origin
        p,q,w = map(int,input().split())
        dj.makeEdge(p, q, w)

    res = dj.solve(r,r)

    for i in range(v):
        if dj.cost[i] == dj.INF:
            print("INF")
            continue
        print(dj.cost[i])
#test()
aoj_1_a()

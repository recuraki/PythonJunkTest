from typing import List, Tuple
from pprint import pprint

import heapq
from collections import deque


class dijkstra():
    INF = 2 ** 62 + 10000
    INF = float("inf")
    useedge = None

    def __init__(self, numV, numE):
        self.numV = numV
        self.e = [[] for _ in range(numV)]
        self.useedge = [False] * numE
        self.edgeinfo = dict()

    def makeEdge(self, s, t, cost, i):
        self.e[s].append( [t, cost, i] )
        self.edgeinfo[i] = [s,t,cost]

    def changeCost(self, s,t,cost):
        for i in range(len(self.e[s])):
            tt,_,info = self.e[s][i]
            if tt == t:
                self.e[s][i][1] = cost
                self.edgeinfo[info][2] = cost

    def solve(self, nodeS, ):
        self.cost = [self.INF] * self.numV  # cost
        self.parent = [[] for _ in range( self.numV)]
        self.donoPath = [[] for _ in range( self.numV)]
        q = [(0, nodeS, -1)]  # 初期ノード(cost 0)
        self.cost[nodeS] = 0
        heapq.heapify(q)
        while len(q) > 0:
            curcost, curnode, usepath = heapq.heappop(q)
            # print("Curcost:{0}, Curnode{1}".format(curcost, curnode))
            # 打ち切り。ゴールが明確ならここに入れる。
            # if curnode == nodeT: return
            if curcost > self.cost[curnode]:
                continue
            for nextnode, edgecost, edgeID in self.e[curnode]:
                nextcost = curcost + edgecost
                if self.cost[nextnode] > nextcost:
                    self.cost[nextnode] = nextcost
                    self.parent[nextnode].clear()
                    self.parent[nextnode].append(curnode)
                    heapq.heappush(q, (nextcost, nextnode, edgeID))
                    self.useedge[edgeID] = True
                    self.donoPath[nextnode].clear()
                    self.donoPath[nextnode].append(edgeID)
                if self.cost[nextnode] == nextcost:
                    self.donoPath[nextnode].append(edgeID)
                    self.parent[nextnode].append(curnode)
                    heapq.heappush(q, (nextcost, nextnode, edgeID))

    edgeroute = []
    def findRoute(self, s, t):
        # THIS FUNCTION should be called after solve()
        edgeroute = deque([])
        q = deque([t])
        visited = [False] * self.numV
        visited[t] = True
        while len(q) > 0:
            curnode = q.popleft()
            if self.donoPath[curnode] != -1:
                edgeroute.appendleft(self.donoPath[curnode])
            for nn in self.parent[curnode]:
                if visited[nn]: continue
                q.append(nn)
        return edgeroute

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        a = self.minimumWeightCo(n,edges,src1, src2, dest)
        b = self.minimumWeightCo(n, edges, src2, src1, dest)
        return min(a,b)

    def minimumWeightCo(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        m = len(edges)
        dj = dijkstra(n, m)
        for i in range(m):
            u, v, w = edges[i]
            dj.makeEdge(u, v, w, i)
        for i in range(n):
            dj.e[i].sort()

        ans = 0

        #print("--gogo1")
        #print(dj.e)
        dj.solve(src2)
        ans += dj.cost[dest]
        p = dj.findRoute(src2, dest)
        for ens in p:
            for en in set(ens):
                s,t,w = dj.edgeinfo[en]
                #print(en, s,t,w)
                dj.changeCost(s,t,0)
        #print(dj.e)
        if dj.cost[dest] == dj.INF: return -1
        #print("--gogo2")
        dj.solve(src1)
        ans += dj.cost[dest]
        if dj.cost[dest] == dj.INF: return -1
        return ans


st = Solution()

print(st.minimumWeight(n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5)==9)
print(st.minimumWeight(n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2)==-1)
print(st.minimumWeight(10,
[[5,8,28],[5,4,25],[5,1,42],[0,6,22],[5,9,26],[0,2,35],[5,3,10],[0,7,41],[9,7,24],[6,7,19],[2,7,23]],
0,
5,
7,)==91)
import heapq
from collections import deque


class bellmanFord():
    INF = float("inf")
    def __init__(self, v):
        self.numv = v
        self.distance = [self.INF] * v
        self.e = [[] for _ in range(v)]

    def makeEdge(self, s, t, cost):
        self.e[s].append([t, cost])

    def solve(self, s):
        self.distance[s] = 0
        negativeCycle = False
        for i in range(self.numv):
            for curNode in range(self.numv):
                isUpdate = False
                for nextNode, cost in self.e[curNode]:
                    if self.distance[curNode] == self.INF:
                        continue
                    if self.distance[nextNode] > self.distance[curNode] + cost:
                        isUpdate = True
                        self.distance[nextNode] = self.distance[curNode] + cost
                        if i == self.numv - 1:
                            negativeCycle = True
                            break
        if negativeCycle:
            return -1
        return self.distance

def test():
    bf = bellmanFord(7)
    bf.makeEdge(0,1,10)
    bf.makeEdge(1,2,1)
    bf.makeEdge(1,3,5)
    bf.makeEdge(2,1,1)
    bf.makeEdge(2,3,1)
    bf.makeEdge(3,4,2)
    bf.makeEdge(3,6,4)
    bf.makeEdge(4,5,5)
    bf.makeEdge(4,6,1)
    bf.makeEdge(5,2,2)
    bf.makeEdge(6,5,2)
    res = bf.solve(0) # solve from s
    print(res[6])

def test_inf():
    bf = bellmanFord(4)
    bf.makeEdge(0, 1, 1)
    bf.makeEdge(0, 2, 1)
    bf.makeEdge(1,3, 1)
    bf.makeEdge(2,3, 1)
    bf.makeEdge(1,2, -10)
    res = bf.solve(0)
    print(res)

def aoj_1_a():
    v,e,r = map(int, input().split())
    bf = bellmanFord(v)
    for _ in range(e):
        # 0 origin
        p,q,w = map(int,input().split())
        bf.makeEdge(p, q, w)
    res = bf.solve(r)
    if res == -1:
        print("NEGATIVE CYCLE")
        return

    for i in range(v):
        if bf.distance[i] == bf.INF:
            print("INF")
            continue
        print(bf.distance[i])
aoj_1_a()
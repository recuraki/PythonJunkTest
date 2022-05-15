import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


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

        def makeEdge(self, s, t, cost, i):
            self.e[s].append((t, cost, i))

        def solve(self, nodeS, nodeT):
            self.cost = [self.INF] * self.numV  # cost
            self.parent = [-1] * self.numV  # parent node
            self.donoPath = [-1] * self.numV
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
                        self.parent[nextnode] = curnode
                        heapq.heappush(q, (nextcost, nextnode, edgeID))
                        self.useedge[edgeID] = True
                        self.donoPath[nextnode] = edgeID
                    if self.cost[nextnode] == nextcost:
                        self.donoPath[nextnode] = min(edgeID,  self.donoPath[nextnode])

        def findRoute(self, s, t):
            # THIS FUNCTION should be called after solve()
            edgeroute = deque([])
            nextnode = t
            while nextnode != -1:
                if self.donoPath[nextnode] != -1:
                    edgeroute.appendleft(self.donoPath[nextnode])
                nextnode = self.parent[nextnode]
            return edgeroute

    import sys
    input = sys.stdin.readline
    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))

    def do():
        n, m = map(int, input().split())
        dj = dijkstra(n, 2 * m)
        for i in range(m):
            u, v, w = map(int, input().split())
            v -= 1
            u -= 1
            dj.makeEdge(u, v, w, 2 * i + 0)
            dj.makeEdge(v, u, w, 2 * i + 1)
        for i in range(n):
            dj.e[i].sort()
        useflag = [False] * (2 * m)
        for i in range(n):
            dj.solve(i, i)
            for j in range(n):
                p = dj.findRoute(i, j)
                for x in p:
                    if x == -1: continue
                    useflag[x] = True
        ans = 0
        for i in range(m):
            if useflag[2 * i + 0] is True: continue
            if useflag[2 * i + 1] is True: continue
            ans += 1
        print(ans)

    # 1 time
    do()


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """3 3
1 2 2
2 3 3
1 3 6"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 4
1 3 3
2 3 9
3 5 3
4 5 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 10
1 2 71
1 3 9
1 4 82
1 5 64
2 3 22
2 4 99
2 5 1
3 4 24
3 5 18
4 5 10"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        import heapq
        from collections import deque

        n, m = map(int, input().split())
        dat = list(map(int, input().split()))

class dijkstra():
    INF = 2 ** 62 + 10000
    INF = float("inf")

    def __init__(self, numV):
        self.numV = numV
        self.e = [[] for _ in range(numV)]

    def makeEdge(self, s, t, cost):
        self.e[s].append((t, cost))

    def solve(self, nodeS, nodeT):
        self.cost = [self.INF] * self.numV  # cost
        self.parent = [-1] * self.numV  # parent node
        q = [(0, nodeS)]  # 初期ノード(cost 0)
        self.cost[nodeS] = 0
        heapq.heapify(q)
        while len(q) > 0:
            curcost, curnode = heapq.heappop(q)
            # print("Curcost:{0}, Curnode{1}".format(curcost, curnode))
            # 打ち切り。ゴールが明確ならここに入れる。
            # if curnode == nodeT: return
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

        dj = dijkstra(n)
        for _ in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            dj.makeEdge(u, v, 0)







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
        input = """4 4
10 8 12 5
1 2
1 3
2 3
3 4"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1
0 10
1 2"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
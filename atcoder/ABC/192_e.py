import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import heapq
    from collections import deque
    import math

    class dijkstra():
        INF = 2 ** 60 + 10000
        def __init__(self, numV):
            self.numV = numV
            self.e = [[] for _ in range(numV)]
        def makeEdge(self, s, t, keep, cost):
            self.e[s].append((t, cost, keep)) # dist, cost, 間隔

        def solve(self, nodeS, nodeT):
            self.distance = [self.INF] * self.numV
            self.cost = [self.INF] * self.numV  # cost
            self.parent = [-1] * self.numV  # parent node
            q = [(0, nodeS)]  # cost, node
            self.cost[nodeS] = 0
            heapq.heapify(q)
            while len(q) > 0:
                curcost, curnode = heapq.heappop(q)
                for nextnode, pathcost, k in self.e[curnode]:
                    nextcost = (math.ceil(curcost / k) * k) + pathcost
                    if self.cost[nextnode] > nextcost:
                        self.cost[nextnode] = nextcost
                        self.parent[nextnode] = curnode
                        heapq.heappush(q, (nextcost, nextnode))

    from pprint import pprint
    import sys
    input = sys.stdin.readline
    n, m, x, y = map(int, input().split())
    dj = dijkstra(n + 10)
    for i in range(m):
        a,b,t,k = map(int,input().split())
        dj.makeEdge(a, b, k, t) # 順番合ってる
        dj.makeEdge(b, a, k, t) # 順番合ってる

    dj.solve(x, x)
    if dj.cost[y] == dj.INF:
        print(-1)
    else:
        print(dj.cost[y])


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
        input = """3 2 1 3
1 2 2 3
2 3 3 4"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2 3 1
1 2 2 3
2 3 3 4"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 0 3 1"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """9 14 6 7
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3
2 3 8 4
6 2 6 4
3 8 3 2
7 9 5 2
8 4 1 9
7 1 6 9
3 9 9 3
7 5 1 5
8 2 9 7
4 9 4 4"""
        output = """26"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
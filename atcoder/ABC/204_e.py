import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    def getmintime(d):
        def f(d, i):
            return int( (d // (i + 1)) + i)
        l = 0
        h = math.sqrt(d)
        targetval = f(d, h)
        while l <= h:
            mid = (l + h) // 2
            curval = f(d, mid)
            if targetval == curval:
                h = mid - 1  # 買えないのでそれ以下の数をトライ
            else:  # 買えないなら
                l = mid + 1  # 買えるのでそれ以上の数
        if f(d, l) == targetval:
            return int(l)
        else:
            return int(h)

    import heapq
    from collections import deque
    class dijkstra():
        INF = 2 ** 62 + 10000
        INF = float("inf")

        def __init__(self, numV):
            self.numV = numV
            self.e = [[] for _ in range(numV)]

        def makeEdge(self, s, t, cost, deltahour):
            self.e[s].append((t, cost, deltahour))

        def solve(self, nodeS, nodeT):
            self.distance = [self.INF] * self.numV
            self.cost = [self.INF] * self.numV  # cost
            self.parent = [-1] * self.numV  # parent node
            q = [(0, nodeS)]  # 初期ノード(cost 0)
            self.cost[nodeS] = 0
            heapq.heapify(q)
            while len(q) > 0:
                curcost, curnode = heapq.heappop(q)
                # 打ち切り。ゴールが明確ならここに入れる。
                if curnode == nodeT: return
                if curcost > self.cost[curnode]:
                    continue
                for nextnode, edgecost ,deltahour in self.e[curnode]:
                    otokuhour = getmintime(deltahour)
                    if otokuhour >= curcost:
                        nextcost = otokuhour + edgecost + math.floor(deltahour / (otokuhour + 1))
                    else:
                        nextcost = curcost + edgecost + math.floor(deltahour / (curcost + 1))
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
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        n, m = map(int, input().split())
        dk = dijkstra(n)
        for _ in range(m):
            a,b,c,d = map(int, input().split())
            a -= 1
            b -= 1
            dk.makeEdge(a,b,c,d)
            dk.makeEdge(b,a,c,d)
        dk.solve(0, n-1)
        if dk.cost[n-1] == dk.INF:
            print(-1)
        else:
            print(dk.cost[-1])


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
        input = """2 1
1 2 2 3"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 3
1 2 2 3
1 2 2 1
1 1 1 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 2
1 2 3 4
3 4 5 6"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """6 9
1 1 0 0
1 3 1 2
1 5 2 3
5 2 16 5
2 6 1 10
3 4 3 4
3 5 3 10
5 6 1 100
4 2 0 110"""
        output = """20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    # import pypyjit
    # pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))

    def do():

        import heapq
        from collections import deque
        class dijkstra():
            INF = 2 ** 62 + 10000
            INF = float("inf")

            def __init__(self, numV):
                self.numV = numV
                self.e = [[] for _ in range(numV)]

            def makeEdge(self, s, t, cost, ind):
                self.e[s].append((t, cost, ind))

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
                    for nextnode, edgecost, ind in self.e[curnode]:
                        nextcost = curcost + edgecost
                        if self.cost[nextnode] > nextcost:
                            self.cost[nextnode] = nextcost
                            self.parent[nextnode] = ind
                            heapq.heappush(q, (nextcost, nextnode))

            def findRoute(self, s, t):
                # THIS FUNCTION should be called after solve()
                route = deque([])
                nextnode = t
                while nextnode != -1:
                    route.appendleft(str(nextnode))
                    nextnode = self.parent[nextnode]
                return route

        n, m = map(int, input().split())
        dj = dijkstra(n)
        roadnum = [dict() for _ in range(n)]
        for i in range(m):
            u, v, c = map(int, input().split())
            u -= 1
            v -= 1
            dj.makeEdge(u, v, c, i + 1)
            dj.makeEdge(v, u, c, i + 1)
        dj.solve(0, 0)
        ans = set()
        for t in range(0, n):
            if dj.parent[t] == -1: continue
            ans.add(dj.parent[t])
        res = []
        for k in ans: res.append(k)
        res.sort()
        print(*res)

    # 1 time
    do()
    # n questions
    # q = int(input())
    # for _ in range(q):
    #    do()


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
1 2 1
2 3 2
1 3 10"""
        output = """1 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 6
1 2 1
1 3 1
1 4 1
2 3 1
2 4 1
3 4 1"""
        output = """3 1 2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
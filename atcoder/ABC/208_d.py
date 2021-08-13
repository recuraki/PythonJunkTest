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

        def __init__(self, numV):
            self.numV = numV
            self.e = [[] for _ in range(numV)]

        def makeEdge(self, s, t, cost):
            self.e[s].append((t, cost))

        def solve(self, nodeS, k):
            self.distance = [self.INF] * self.numV
            self.cost = [self.INF] * self.numV  # cost
            self.parent = [-1] * self.numV  # parent node
            q = [(0, nodeS)]  # 初期ノード(cost 0)
            self.cost[nodeS] = 0
            heapq.heapify(q)

            while len(q) > 0:
                curcost, curnode = heapq.heappop(q)
                #print("cur", curnode, curcost)
                if curcost > self.cost[curnode]:
                    continue
                for nextnode, edgecost in self.e[curnode]:
                    #print("try", nextnode)
                    if curnode != nodeS and curnode > k:
                        if nextnode > k:
                            continue
                    #print(" > yes", curnode, nextnode)
                    nextcost = curcost + edgecost
                    if self.cost[nextnode] > nextcost:
                        self.cost[nextnode] = nextcost
                        self.parent[nextnode] = curnode
                        heapq.heappush(q, (nextcost, nextnode))


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        n, m = map(int, input().split())
        dj = dijkstra(n)

        timeData = [[] for _ in range(n)]
        for i in range(m):
            a,b,c = map(int, input().split())
            a -= 1
            b -= 1
            dj.makeEdge(a, b, c)
            #print("add path", a,b, c)
        #print("---")
        #k = 1
        #i = 0
        #dj.solve(i, k)
        #print(i, k, dj.cost)
        #return
        res = 0
        for k in range(n):
            for i in range(n):
                dj.solve(i, k)
                #print(i, k, dj.cost)
                for x in dj.cost:
                    if x != dj.INF and x != 0:
                        res += x
        print(res)

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
        input = """3 2
1 2 3
2 3 2"""
        output = """25"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 0"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 20
1 2 6
1 3 10
1 4 4
1 5 1
2 1 5
2 3 9
2 4 8
2 5 6
3 1 5
3 2 1
3 4 7
3 5 9
4 1 4
4 2 6
4 3 4
4 5 8
5 1 2
5 2 5
5 3 6
5 4 5"""
        output = """517"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
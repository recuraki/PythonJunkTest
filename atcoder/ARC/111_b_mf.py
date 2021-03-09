import sys
from io import StringIO
import unittest
import logging

logging.basicConfig(level=logging.DEBUG)

def resolve():
    from collections import deque
    from functools import lru_cache
    class DinicRecurcive(object):
        INF = 2 ** 60

        def __init__(self, n):
            """
            n: num of vertex
            """
            self.e = [[] for _ in range(n)]
            self.dist = [-1] * n
            self.iter = [-1] * n
            self.n = n

        def makeEdge(self, s, t, cap):
            l = [t, cap, None]  # edge
            lrev = [s, 0, l]  # reverse edge
            l[2] = lrev
            self.e[s].append(l)
            self.e[t].append(lrev)

        def bfs(self, s):
            self.dist[s] = 0  # init start point
            q = deque([])
            q.appendleft(s)
            while len(q) > 0:
                curNode = q.popleft()
                # print("curNode", curNode)
                for nextNode, edgeCap, revEdge in self.e[curNode]:
                    # print("edgeCap", nextNode, edgeCap)
                    if edgeCap > 0 and self.dist[nextNode] == -1:
                        self.dist[nextNode] = self.dist[curNode] + 1
                        q.appendleft(nextNode)

        def dfs(self, curNode, g, flow):
            if curNode == g:
                return flow

            for i in range(self.iter[curNode], len(self.e[curNode])):

                self.iter[curNode] += 1

                l = self.e[curNode][i]  # node, cap, revpath

                # go only forward, don't back to parent
                if l[1] > 0 and self.dist[curNode] < self.dist[l[0]]:
                    f = self.dfs(l[0], g, min(flow, l[1]))
                    if f > 0:
                        l[1] -= f
                        l[2][1] += f
                        return f
            return 0

        @lru_cache(maxsize=None)
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
                    # print("res", res)
                    if res <= 0:  # cannot more flow Then End
                        break
                    flow += res

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
        input = """4
1 2
1 3
4 2
2 3"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
111 111
111 111"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """12
5 2
5 6
1 2
9 7
2 7
5 5
4 2
6 7
2 2
7 8
9 7
1 8"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
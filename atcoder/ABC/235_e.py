import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint


    import math
    INF = 1 << 63
    def do():
        from heapq import heappush, heappop, heapify
        class mstPrim():
            INF = float("inf")
            res = []
            used = set()

            def __init__(self, numv):
                self.numv = numv
                self.e = [[] for _ in range(numv)]

            def makeEdge(self, a, b, w=1, flag= True):
                self.e[a].append((b, w, flag) )
                self.e[b].append((a, w, flag) )

            def solve(self, root=0):
                q = []
                res = 0
                visited = [False] * self.numv
                visited[root] = True
                for t, w, f in self.e[root]:
                    heappush(q, (w, t, root, f))

                while len(q) > 0:
                    cost, nextNode, cur, flag = heappop(q)
                    if visited[nextNode]:
                        continue
                    if flag:

                        visited[nextNode] = True

                        res += cost
                        for t, w, f in self.e[nextNode]:
                            if visited[t]: continue
                            heappush(q, (w, t, nextNode, f))
                    else:
                        self.used.add((cur, nextNode, cost))

                return res


        """
        n: 頂点
        m: 辺の数
        q: クエリ
        """
        n, m, q = map(int, input().split())
        mst = mstPrim(n)
        for _ in range(m):
            # a<->b weight = c
            # 全てのコストは排他
            a, b, c = map(int, input().split())
            a -= 1
            b -= 1
            mst.makeEdge(a, b, c, True)

        querys = []
        for _ in range(q):
            u, v, w = map(int, input().split())
            u -= 1
            v -= 1
            querys.append((u, v, w))
            mst.makeEdge(u, v, w, False)

        mst.solve(0)
        for u, v, w in querys:
            if (u, v, w) in mst.used or (v, u, w) in mst.used:
                print("Yes")
            else:
                print("No")
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
        input = """5 6 3
1 2 2
2 3 3
1 3 6
2 4 5
4 5 9
3 5 8
1 3 1
3 4 7
3 5 7"""
        output = """Yes
No
Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 3 2
1 2 100
1 2 1000000000
1 1 1
1 2 2
1 1 5"""
        output = """Yes
No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
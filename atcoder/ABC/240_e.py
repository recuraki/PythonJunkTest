import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
cnt = 1


def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    cnt = 1
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    visited = [False] * n
    from collections import deque
    q = deque([0])
    visited[0] = True
    mi = [10**9] * n
    ma = [-1] * n
    route = []
    cnt = 1
    parent = [-1] * n
    def dfs1(cur):
        route.append(cur)
        did = False # 探索をしたか？
        for nn in g[cur]:
            if visited[nn]: continue #訪問済みなら行かない
            parent[nn] = cur
            visited[nn] = True
            did = True
            dfs1(nn)
        if did is False:
            mi[cur] = cnt
            ma[cur] = cnt
            cnt += 1
    dfs1(0)
    for cur in route[::-1]:
        if mi[cur] != 10**9: continue # 計算済み
        for nn in g[cur]:
            if nn == parent[cur]: continue # 親は計算しない
            mi[cur] = min(mi[cur], mi[nn])
            ma[cur] = max(ma[cur], ma[nn])
    for i in range(n):
        print(mi[i], ma[i])




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
        input = """3
2 1
3 1"""
        output = """1 2
2 2
1 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
3 4
5 4
1 2
1 4"""
        output = """1 3
3 3
2 2
1 2
1 1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
4 5
3 2
5 2
3 1"""
        output = """1 1
1 1
1 1
1 1
1 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
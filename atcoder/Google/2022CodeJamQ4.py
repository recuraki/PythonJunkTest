import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():




    import sys
    input = sys.stdin.readline
    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    from collections import deque
    class topologicalSort():
        def __init__(self, n):
            self.n = n
            self.g = [[] for _ in range(n)]
            self.edgeNum = [0] * n

        def makeEdge(self, u, v):
            assert u != v
            self.g[u].append(v)
            self.edgeNum[v] += 1  # 入次++

        def solve(self):
            q = deque([])
            ans = []
            for i in range(self.n):
                if (self.edgeNum[i] != 0): continue
                q.appendleft(i)
                ans.append(i)
            while (len(q) > 0):
                cur = q.popleft()
                for nxt in self.g[cur]:
                    self.edgeNum[nxt] -= 1
                    if self.edgeNum[nxt] == 0:
                        ans.append(nxt)
                        q.append(nxt)
            return ans


    def do(qnum):

        # node 0 = abyssとしてn+1のノードを読み込む。(abyssの親は-1
        n = int(input()) + 1
        cost = [0] + list(map(int, input().split()))
        parents = [-1] + list(map(int, input().split()))
        # 親から見たときの子の情報
        g = [[] for _ in range(n)]

        # トポロジカルソート
        ts = topologicalSort(n)
        for v in range(n):
            if parents[v] == -1: continue
            u = parents[v]
            ts.makeEdge(u, v)
            g[u].append(v)
        path = ts.solve()
        ans = 0
        #　トポロジカルソートを後ろから見る=葉からたどる
        for cur in path[::-1]:
            if len(g[cur]) == 0: continue # 葉なら次へ
            childCosts = []
            for child in g[cur]:
                childCosts.append(cost[child])
            childCosts.sort()
            ans += sum(childCosts[1:])
            cost[cur] = max(cost[cur], childCosts[0])
            if cur == 0: ans += cost[cur]
        print("Case #{}:".format(qnum), ans)
    q = int(input())
    for i in range(q):
        do(i+1)






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
4
60 20 40 50
0 1 1 2
5
3 2 1 4 5
0 1 1 1 0
8
100 100 100 90 80 100 90 100
0 1 2 1 2 3 1 3"""
        output = """Case #1: 110
Case #2: 14
Case #3: 490"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
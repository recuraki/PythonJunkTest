
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    sys.setrecursionlimit(200000)
    from collections import deque
    # a-zに正方向と逆辺を張る
    def addEdge(g, a, z):
        g[0][a].append(z)
        g[1][z].append(a)

    # グラフの初期化
    def initGraph(g, edgenum):
        g.append([])  # [0] 正方向のグラフ
        g.append([])  # [1] 逆方向のグラフ
        for _ in range(edgenum):
            g[0].append(deque(list()))
        for _ in range(edgenum):
            g[1].append(deque(list()))

    def dfs(g, v, visited, vs):
        # 正方向のDFS
        visited[v] = True
        for i in range(len(g[0][v])):
            if visited[g[0][v][i]] is False:
                dfs(g, g[0][v][i], visited, vs)
        vs.append(v)

    def rdfs(g, v, visited, cmp, k):
        # 逆方向のDFS
        # kがcall元に指定される連結成分の通し番号
        visited[v] = True
        cmp[v] = k
        # 指定したノードの逆辺をたどる
        for i in range(len(g[1][v])):
            # print("go? {0}".format(g[1][v][i]))
            # 逆辺の先がrDFSで到達できないときのみ
            if visited[g[1][v][i]] is False:
                # print("yes")
                rdfs(g, g[1][v][i], visited, cmp, k)

    def scc(g, cmp):
        vs = []  # 帰りがけのリスト
        visited = [False] * len(g[0])
        cmp.extend([None] * len(g[0]))
        for i in range(len(g[0])):
            if visited[i] is False:
                dfs(g, i, visited, vs)

        visited = [False] * len(g[1])
        k = 0
        # pprint(vs)
        for i in range(len(vs) - 1, -1, -1):
            # print("vited: i={0} vs[i] = {1}".format(i, vs[i]))
            # print(parent)
            if visited[vs[i]] is False:
                # print("rdfs [{0}]".format(i))
                rdfs(g, vs[i], visited, cmp, k)
                k += 1
        # pprint(vs)
        return k

    vCount, e = map(int, input().split())

    g = []  # グラフ。[0] = 正方向のグラフ。 [1] = 逆方向のグラフ
    v = []  # 辺
    cmp = []

    from pprint import pprint
    initGraph(g, edgenum=vCount)
    for _ in range(e):
        x, y = map(int, input().split())
        addEdge(g, x, y)

    scc(g, cmp)

    for _ in range(int(input())):
        x, y = map(int, input().split())
        print(1 if cmp[x] == cmp[y] else 0)


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
        input = """5 6
0 1
1 0
1 2
2 4
4 3
3 2
4
0 1
0 3
2 3
3 4"""
        output = """1
0
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
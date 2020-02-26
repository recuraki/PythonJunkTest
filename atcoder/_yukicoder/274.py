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
        g[0][z].append(a)
        g[1][a].append(z)

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
            # print(visited)
            if visited[vs[i]] is False:
                # print("rdfs [{0}]".format(i))
                rdfs(g, vs[i], visited, cmp, k)
                k += 1
        # pprint(vs)
        return k


    n, m = map(int, input().split())
    dat = []
    for _ in range(n):
        a,b = map(int, input().split())
        dat.append((a,b))

    f = True

    vCount = n * 2  # 各xとnot x分で2倍
    # 0-n-1が各要素のx, n - n*2-1がnot x の 領域

    g = []  # グラフ。[0] = 正方向のグラフ。 [1] = 逆方向のグラフ
    cmp = []

    from pprint import pprint
    initGraph(g, edgenum=vCount)

    def isSafe(a, b, c, d):
        a,b,c,d = min(a,b), max(a,b), min(c,d), max(c,d)
        #print("{0} {1} {2} {3}".format(a,b,c,d))
        if a < c and b < c:
            #print("T")
            return True
        if a > d and b > d:
            #print("T2")
            return True
        #print("{0} {1} {2} {3}".format(a,b,c,d))
        #print("F")
        return False

    for i in range(n):
        if f is False:
            break
        # あくまで縦のほかとの一致なので
        for j in range(i+1, n):

            if isSafe(dat[i][0], dat[i][1], dat[j][0], dat[j][1]) is False:
                # もし、そのままで通らない場合、
                if isSafe((m-1) - dat[i][0], (m-1) - dat[i][1], dat[j][0], dat[j][1]):
                    # 自分を反転して通るのであれば not x → y, あるいはx → not yなのだから
                    addEdge(g, n + i, j)
                    addEdge(g, i, n + j)
                else:
                    # 何をしても通らないので通らないダミーパスを作る
                    f = False
                    break

            else: # そのままで通る場合で
                if isSafe((m-1) - dat[i][0], (m-1) - dat[i][1], dat[j][0], dat[j][1]) is False:
                    # 反転させてしまうと通らないのであれば、 x → y あるいは not x → not yなのだから
                    addEdge(g, i, j)
                    addEdge(g, n + i, n + j)
                else:
                    pass # 回転させても通るならなにをしても通るので制約は要らない


                """
                if isSafe(dat[i][0], dat[i][1], dat[pi][0], dat[pi][1]) is False:
                    addEdge(g, n + i, n + pi)
                if isSafe(m - dat[i][0], m - dat[i][1], dat[pi][0], dat[pi][1]) is False:
                    addEdge(g, i, n + pi)
                if isSafe(dat[i][0], dat[i][1], m - dat[pi][0], m - dat[pi][1]) is False:
                    addEdge(g, n + i, pi)
                if isSafe(m - dat[i][0], m - dat[i][1], m - dat[pi][0], m - dat[pi][1]) is False:
                    addEdge(g, i, pi)
                """

    if f is False:
        print("NO")
    else:
        k = scc(g, cmp)
        #pprint(g)
        f = True
        for i in range(n):
            if cmp[i] == cmp[n+i]:
                #print("hit{0} {1}, by {2} {3}".format(cmp[i], cmp[n+i], i, n+i))
                f = False
                break
        #print(cmp)
        print("YES" if f else "NO")


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
        input = """4 6
5 5
2 3
4 4
1 1"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        self.maxDiff=10000
        print("test_input_2")
        input = """4 6
3 5
3 4
4 4
1 2"""
        output = """NO"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """12 1009
632 683
895 962
841 884
22 23
900 1007
973 984
325 441
358 700
919 1006
510 555
975 990
574 600"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        self.maxDiff=40000

        input = """5 10
8 8
0 0
2 4
2 3
8 8"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
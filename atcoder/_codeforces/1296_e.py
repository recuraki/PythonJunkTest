import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from collections import deque
    # a-zに正方向と逆辺を張る
    def addEdge(g, a, z):
        print("addgraph {0} {1}".format(a,z))
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
            # print(parent)
            if visited[vs[i]] is False:
                # print("rdfs [{0}]".format(i))
                rdfs(g, vs[i], visited, cmp, k)
                k += 1
        # pprint(vs)
        return k

    n = int(input())
    s = input()
    dat = []
    for i in range(len(s)):
        dat.append(ord(s[i]) - ord("a"))
    vCount = 26 * 2  # 超点数
    g = []  # グラフ。[0] = 正方向のグラフ。 [1] = 逆方向のグラフ
    v = []  # 辺
    cmp = []
    initGraph(g, edgenum=vCount)
    from pprint import pprint
    for i in range(len(s)):
        for j in range(i+1, len(s)):

            # もし、iのほうがjより大きいならこれはまたがないといけないので
            if dat[i] > dat[j]:
                #print("{0} > {1} ({2}, {3})".format(dat[i], dat[j],i, j))
                # i は not j だし、
                addEdge(g, dat[i], 26+dat[j])
                # j は not i
                #addEdge(g, 26+dat[i], dat[j])
    #pprint(g)
    scc(g, cmp)
    print(cmp)
    print("is?")
    for i in range(26):
        if cmp[i] == cmp[26+i]:
            print("NO")

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
        input = """9
abacbecfd"""
        output = """YES
001010101"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """8
aaabbcbb"""
        output = """YES
01011011"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
abcdedc"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """5
abcde"""
        output = """YES
00000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        n = int(input())
        g = [[] for _ in range(n)]

        for _ in range(n-1):
            u, v, w = map(int, input().split())
            u -= 1
            v -= 1
            g[u].append( (v, w) )
            g[v].append( (u, w) )


        # PreOrder(先行順巡回) 0 -> 1と追うやつ。典型。
        from collections import deque
        q = []
        path = []
        pathdepth = []

        rootnode = 0
        depth = [-1] * n
        nodein = [-1] * n
        nodeout = [-1] * n
        q.append([rootnode, 0])
        curtime = -1
        parent = [None] * n
        nodeCount = [1] * n
        # q: nodenum, depth, vcost
        while len(q) != 0:
            curtime += 1
            curnode, curdepth = q.pop()
            print("curnode", curnode)
            if curnode >= 0:  # 行き掛け
                print("gogo")
                if nodein[curnode] == -1:
                    nodein[curnode] = curtime
                depth[curnode] = curdepth
                pathdepth.append(curdepth)
                path.append(curnode)
                proc = 0
                if len(g[curnode]) == 0:  # 子がいないときの処理
                    nodeout[curnode] = curtime + 1
                for nextnode, nextvcost in g[curnode][::-1]:
                    if depth[nextnode] != -1:
                        continue
                    q.append([~curnode, curdepth])
                    q.append([nextnode, curdepth + 1])
                    parent[nextnode] = curnode
                    proc += 1
                if proc == 0:
                    print("rev!1")
                    nodeCount[parent[curnode]] += nodeCount[curnode]

            else:  # もどりがけ
                curnode = ~curnode
                if nodein[curnode] == -1:
                    nodein[curnode] = curtime
                path.append(curnode)
                pathdepth.append(curdepth)
                nodeout[curnode] = curtime + 1
                if parent[curnode] is not None:
                    nodeCount[parent[curnode]] += nodeCount[curnode]
        print(path)
        print(nodeCount)
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
        input = """3
1 2 10
2 3 20"""
        output = """50"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
1 2 1
2 3 2
4 2 5
3 5 14"""
        output = """76"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
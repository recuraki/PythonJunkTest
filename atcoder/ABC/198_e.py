import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        dat = [0] * (10 ** 5 + 10)
        color = list(map(int, input().split()))
        G = [[] for _ in range(n)]
        for i in range(n - 1):
            a, b = map(int, input().split())
            a,b = a-1, b-1
            dat.append([a, b])
            G[a].append(b)
            G[b].append(a)
        q = []
        depth = [-1] * n
        q.append([0, 0, 0])
        curtime = -1
        parent = [None] * n
        res = []
        while len(q) != 0:
            curtime += 1
            curnode, curdepth, vcost = q.pop()
            if curnode >= 0:  # 行き掛け
                if dat[color[curnode]] == 0:
                    res.append(curnode + 1)
                dat[color[curnode]] += 1
                depth[curnode] = curdepth
                q.append([~curnode, curdepth, 0])
                for nextnode in G[curnode][::-1]:
                    if depth[nextnode] != -1:
                        continue
                    q.append([nextnode, curdepth + 1, 0])
                    parent[nextnode] = curnode
            else: # 帰りがけ
                curnode = ~curnode
                dat[color[curnode]] -= 1
        res.sort()
        for x in res:
            print(x)
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
        input = """6
2 7 1 8 2 8
1 2
3 6
3 2
4 3
2 5"""
        output = """1
2
3
4
6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10"""
        output = """1
2
3
5
6
7
8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
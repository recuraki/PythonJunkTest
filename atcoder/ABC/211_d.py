import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    INF = 1 << 63
    def do():
        mod = 10**9 + 7
        n, m = map(int, input().split())
        g = [set() for _ in range(n)]
        for _ in range(m):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            g[a].add(b)
            g[b].add(a)
        from collections import deque
        depth = [-1] * n
        count = [0] * n
        startnode = 0
        q = deque([startnode])
        depth[startnode] = 0
        count[startnode] = 1
        proc = [False] * n
        while len(q) > 0:
            curnode = q.popleft()
            if proc[curnode] is True: continue
            #print("cur", curnode)
            proc[curnode] = True
            DepthCurrent = depth[curnode]
            DepthNext = DepthCurrent + 1
            for nextnode in g[curnode]:
                #print("next", nextnode)
                if depth[nextnode] == -1 or depth[nextnode] > DepthNext: # はじめて か 遠い距離を記憶しているなら
                    depth[nextnode] = DepthNext
                    count[nextnode] = count[curnode]
                    count[nextnode] %= mod
                    q.append(nextnode)
                    continue
                if depth[nextnode] == DepthNext:
                    count[nextnode] += count[curnode]
                    count[nextnode] %= mod

        #print(count)
        #print(depth)
        print(count[n-1])

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
        input = """4 5
2 4
1 2
2 3
1 3
3 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
1 3
2 3
2 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 0"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """7 8
1 3
1 4
2 3
2 4
2 5
2 6
5 7
6 7"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
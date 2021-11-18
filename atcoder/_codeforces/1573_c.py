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

    """
    neededg 必要とされている本
    """

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        from collections import deque
        n = int(input())
        g = [list() for _ in range(n)]
        q = deque([])
        needg = [list() for _ in range(n)]
        needcnt = [None] * n
        visited = [False] * n
        for i in range(n):
            dat = list(map(int, input().split()))
            for j in range(len(dat)):
                if j == 0:
                    needcnt[i] = dat[j]
                    if dat[j] == 0:
                        q.appendleft(i)
                    continue
                x = dat[j] -1
                g[i].append(x)
                needg[x].append(i)
        #print(n, g, q)
        res = 0
        while len(q) > 0:
            q = list(q)
            q.sort()
            q = deque(q)
            res += 1 # Count Up
            nextq = deque([])
            while len(q) > 0:
                q = list(q)
                q.sort()
                q = deque(q)
                curnode = q.popleft()

                visited[curnode] = True
                for nextnode in needg[curnode]:
                    if visited[nextnode]: continue
                    needcnt[nextnode] -= 1
                    if needcnt[nextnode] == 0: # ok! next read
                        if nextnode > curnode:
                            q.appendleft(nextnode)
                        else:
                            nextq.append(nextnode)
            q = nextq

        if all(visited):
            print(res)
        else:
            print(-1)

    q = int(input())
    for _ in range(q):
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
        input = """5
4
1 2
0
2 1 4
1 2
5
1 5
1 1
1 2
1 3
1 4
5
0
0
2 1 2
1 2
2 2 1
4
2 2 3
0
0
2 3 2
5
1 2
1 3
1 4
1 5
0"""
        output = """2
-1
1
2
5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
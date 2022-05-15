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
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        from collections import deque
        dat = list(map(int, input().split()))
        ans = []
        for i in range(n):
            dat[i] -= 1
        dat = deque(dat)
        #print(dat)
        for i in range(n-1, -1, -1): # from back
            x = dat.index(i)
            #print(i, "x", x, dat)
            if x == i:
                dat.pop()
                ans.append(0)
                continue
            t = (x+1)
            #print("beforerot",dat, t)
            dat.rotate(-t)
            #print("afrot",dat, t)
            ans.append(t)
            dat.pop()
        #print(ans)
        ans.reverse()
        print(*ans)


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
        input = """3
6
3 2 5 6 1 4
3
3 1 2
8
5 8 1 3 2 6 4 7"""
        output = """0 1 1 2 0 4
0 0 1
0 1 2 0 2 5 6 2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
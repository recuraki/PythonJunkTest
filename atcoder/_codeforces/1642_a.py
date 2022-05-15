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

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        ans = 0
        dat = []
        for _ in range(3):
            x, y = map(int, input().split())
            dat.append( (x, y) )
        for i in range(3):
            for j in range(3):
                if i == j: continue
                a, b = dat[i]
                c, d = dat[j]
                x = set([0,1,2])
                x.remove(i)
                x.remove(j)
                x = list(x)
                e, f = dat[x[0]]
                if b != d: continue
                if b > f:
                    print(abs(a-c))
                    return
        print(0)


    # n questions
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
8 10
10 4
6 2
4 6
0 1
4 2
14 1
11 2
13 2
0 0
4 0
2 4
0 1
1 1
0 0"""
        output = """0.0000000
0
2.0000
0.00
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
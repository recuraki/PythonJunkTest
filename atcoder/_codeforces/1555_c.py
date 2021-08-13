import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        import itertools
        class CumSum1D():
            def __init__(self):
                pass

            def load(self, a):
                self.sdat = list(itertools.accumulate(itertools.chain([0], a)))

            def query(self, l, r):
                return self.sdat[r] - self.sdat[l]


        n = int(input())
        dat1 = list(map(int, input().split()))
        dat2 = list(map(int, input().split()))
        s1 = CumSum1D()
        s2 = CumSum1D()
        s1.load(dat1)
        s2.load(dat2)
        res = INF
        for i in range(n):
            score = max( s1.query(i+1, n), s2.query(0,i) )
            res = min(res, score)
        print(res)


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
3
1 3 7
3 5 1
3
1 3 9
3 5 1
1
4
7"""
        output = """7
8
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
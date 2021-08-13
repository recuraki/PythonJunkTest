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

    INF = 1 << 63

    class cumSum1D(object):
        sdat = []

        def init(self):
            pass
        def load(self, l):
            import itertools
            self.sdat = list(itertools.accumulate(itertools.chain([0], l)))

        def query(self, l, r):
            """
            query [l, r)
            """
            # assert l < r
            return self.sdat[r] - self.sdat[l]
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        total = sum(dat)
        res = - (10**18)
        dat.sort()
        ss = cumSum1D()
        ss.load(dat)
        for i in range(n-1):
            a = ss.query(0, i + 1) / (i+1)
            b = ss.query(i + 1, n) / (n-1-i)
            res = max(res, a+b)
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
        input = """4
3
3 1 2
3
-7 -6 -6
3
2 2 2
4
17 3 5 -3"""
        output = """4.500000000
-12.500000000
4.000000000
18.666666667"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
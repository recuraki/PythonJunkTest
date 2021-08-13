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
    def do():

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

        import collections
        n = int(input())
        l = list(map(int, input().split()))
        l.sort()

        cs = cumSum1D()
        cs.load(l)
        res = 0
        for i in range(2, len(l)):
            x = l[i]
            cnt = i - 1
            subtotal = x * cnt
            tmp = cs.query(0, i - 1)
            res += tmp - subtotal

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
0 2 3
2
0 1000000000
1
0"""
        output = """-3
0
0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
5
0 5 3 2 3
"""
        output = """-14"""
        self.assertIO(input, output)
    def test_input_23(self):
        print("test_input_23")
        input = """1
5
0 2 2 5 3
"""
        output = """-14"""
        self.assertIO(input, output)

    def test_input_231(self):
        print("test_input_231")
        input = """1
4
0 2 4 8
"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
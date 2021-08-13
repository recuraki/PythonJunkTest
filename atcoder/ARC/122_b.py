import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
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

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        from fractions import Fraction
        from bisect import bisect_left, bisect_right
        n = int(input())
        dat = list(map(int, input().split()))
        dat.sort()
        cs = cumSum1D()
        cs.load(dat)
        #print()
        finalres = 10**18
        for i in range(n):
            res = 0
            hoken = Fraction(dat[i], 2)
            res += hoken * n # 保険で賄う
            #print(i,"hokenkaunt", hoken * (n))
            res += cs.query(i+1, n) - (dat[i] * (n-1-i))
            #print(i, float(Fraction(res, n)))
            finalres = min(Fraction(res, n), finalres)
        print(float(finalres))

    do()
    # do()


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
3 1 4"""
        output = """1.83333333333333333333"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
866111664 178537096 844917655 218662351 383133839 231371336 353498483 865935868 472381277 579910117"""
        output = """362925658.10000000000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
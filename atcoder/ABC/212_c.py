import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    from bisect import bisect_left, bisect_right

    INF = 1 << 63
    def do():
        n, m = map(int, input().split())
        dat1 = list(map(int, input().split()))
        dat2 = list(map(int, input().split()))
        dat1.sort()
        dat2 = list(set(dat2))
        dat2.sort()

        res = 10**18
        for x in dat1:
            ind = bisect_left(dat2, x)
            #print(ind)
            for d in range(-1, 2):
                ii = ind + d
                if ii < 0: continue
                if ii > (len(dat2) - 1): continue
                res = min(res, abs(dat2[ii] - x))
        print(res)

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
        input = """2 2
1 6
4 9"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1
10
10"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6 8
82 76 82 82 71 70
17 39 67 2 45 35 22 24"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import bisect
    n = int(input())
    dat = list(map(int, input().split()))
    dat.sort(reverse=True)
    dat = list(map(lambda x: -x, dat))
    print(dat)
    res = 0
    for a in range(n):
        print("a={0}".format(dat[a]))
        for b in range(a+1, n):
            print(" b={0}, {1}".format(dat[b],b))
            le = dat[a] - dat[b]
            print(" le={0}".format(le))
            y = bisect.bisect_left(dat, dat[a] - dat[b], b+1)
            z = bisect.bisect_right(dat, dat[a] + dat[b], y)
            print(" xxx = {0},{1}".format(y,  z ))
            res +=  y - (b+1)

    print(res)


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
3 4 2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
1 1000 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """7
218 786 704 233 645 728 389"""
        output = """23"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
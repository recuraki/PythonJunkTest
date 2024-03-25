import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

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
        n, x, y = map(int, input().split())
        r = [0] * 12
        b = [0] * 12
        r[n] = 1
        for ind in range(10, 1, -1):
            #print("ind", ind, r[ind], b[ind])
            r[ind-1] += r[ind]
            b[ind]   += r[ind] * x
            #print(" ind", ind, r[ind], b[ind])
            if ind > 1:
                r[ind - 1] += b[ind]
                b[ind - 1] += b[ind] * y
        print(b[1])

    # 1 time
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
        input = """2 3 4"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 5 5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 5 5"""
        output = """3942349900"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
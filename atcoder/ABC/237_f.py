import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        mod = 998244353
        n, m = map(int, input().split())
        # dp[i][j][k]
        # i個めの jまで決まって 最後かk
        dp = [ [0] * m   ]

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
        input = """4 5"""
        output = """135"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 4"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """111 3"""
        output = """144980434"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

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
        a, b = map(int, input().split())
        r = math.sqrt(a*a+b*b)
        print(a/r, b/r)


    # 1 time
    do()
    # n questions
    #q = int(input())
    #for _ in range(q):
    #    do()


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
        input = """3 4"""
        output = """0.600000000000 0.800000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 0"""
        output = """1.000000000000 0.000000000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """246 402"""
        output = """0.521964870245 0.852966983083"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
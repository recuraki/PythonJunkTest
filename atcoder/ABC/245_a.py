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
        a,b,c,d = map(int, input().split())
        x = a*60 + b
        y = c*60 + d + 1
        if x < y:
            print("Takahashi")
        else:
            print("Aoki")


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
        input = """7 0 6 30"""
        output = """Aoki"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 30 7 30"""
        output = """Takahashi"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 0 23 59"""
        output = """Takahashi"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
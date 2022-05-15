
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

    memo = dict()
    def do():
        n = int(input())
        memo[1] = [1]
        for i in range(2, 18): memo[i] = memo[i-1] + [i] + memo[i-1]
        print(*memo[n])

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
        input = """2"""
        output = """1 2 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4"""
        output = """1 2 1 3 1 2 1 4 1 2 1 3 1 2 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
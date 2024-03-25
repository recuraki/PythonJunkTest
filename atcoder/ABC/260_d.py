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
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))

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
        input = """5 2
3 5 2 1 4"""
        output = """4
3
3
-1
4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 1
1 2 3 4 5"""
        output = """1
2
3
4
5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """15 3
3 14 15 9 2 6 5 13 1 7 10 11 8 12 4"""
        output = """9
9
9
15
15
6
-1
-1
6
-1
-1
-1
-1
6
15"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
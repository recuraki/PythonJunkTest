
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
        dx = [0,  1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 1

        n = int(input())
        t = input()
        x = 0
        y = 0
        for op in t:
            if op == "S":
                x += dx[d]
                y += dy[d]
            else:
                d += 1
                d = d % 4
        print(x, y)


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
        input = """4
SSRS"""
        output = """2 -1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20
SRSRSSRSSSRSRRRRRSRR"""
        output = """0 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
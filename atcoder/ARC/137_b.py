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
        def max_subarray(numbers):
            """Find the largest sum of any contiguous subarray."""
            best_sum = 0
            current_sum = 0
            for x in numbers:
                current_sum = max(0, current_sum + x)
                best_sum = max(best_sum, current_sum)
            return best_sum
        """
        方針: 最小の数と、最大の数が分かればいい
        """
        n = int(input())
        dat = list(map(int, input().split()))
        orig = dat.count(1)
        from copy import deepcopy

        buf = deepcopy(dat)
        for i in range(n):
            if buf[i] == 1: pass
            if buf[i] == 0: buf[i] = -1
        a = max_subarray(buf)
        mi = orig - a

        buf = deepcopy(dat)
        for i in range(n):
            if buf[i] == 1: buf[i] = -1
            if buf[i] == 0: buf[i] = 1
        b = max_subarray(buf)
        ma = orig + b

        print(ma - mi + 1)
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
0 1 1 0"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
0 0 0 0 0"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
0 1 0 1 0 1"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
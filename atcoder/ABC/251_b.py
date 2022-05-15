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
        n, w = map(int, input().split())
        dat = list(map(int, input().split()))
        from itertools import combinations
        l = list(range(n))
        ans = set()
        for cnt in (1,2,3):
            for x in combinations(l, cnt):
                t = 0
                for i in x:
                    t += dat[i]
                if t <= w:
                    ans.add(t)
        print(len(ans))


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
        input = """2 10
1 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1
2 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 12
3 3 3 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """7 251
202 20 5 1 4 2 100"""
        output = """48"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
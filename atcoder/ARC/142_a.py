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
        se = set()
        for i in range(20):
            se.add(k * 10**i)
        a = int(str(k)[::-1])
        for i in range(20):
            se.add(a * 10**i)
        ans = []
        #print(se)
        def f(x):
            mi = 1 << 60
            for _ in range(60):
                x = int(str(x)[::-1])
                mi = min(mi, x)
            return mi == k


        for item in se:
            if item <= n:
                if f(item):
                    ans.append(item)

        finalans = []
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
        input = """1420 142"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1419 142"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6 19"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
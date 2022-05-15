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
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        mod = 998244353
        dat = []
        g = [[] for _ in range(n)]
        for i in range(n):
            a, b = data[i], datb[i]
            a -= 1
            b -= 1
            a, b = min(a, b), max(a,b)
            dat.append( (a,b) )
            g[a].append(i)
            g[b].append(i)
        dp = [0] * n
        bias = [0] * n
        for i in range(n):
            a, b =




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
        input = """3
1 2 3
2 1 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
2 3 5 4 1
4 2 1 3 5"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
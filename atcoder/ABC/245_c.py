
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
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        dp = [[None] * 2 for _ in range(n)]
        dp[0][0] = data[0]
        dp[0][1] = datb[0]
        for ind in range(1, n):
            if dp[ind-1][0] is not None:
                if abs(data[ind] - dp[ind-1][0]) <= k:
                    dp[ind][0] = data[ind]
                if abs(datb[ind] - dp[ind-1][0]) <= k:
                    dp[ind][1] = datb[ind]

            if dp[ind - 1][1] is not None:
                if abs(data[ind] - dp[ind-1][1]) <= k:
                    dp[ind][0] = data[ind]
                if abs(datb[ind] - dp[ind-1][1]) <= k:
                    dp[ind][1] = datb[ind]

        if dp[n-1][0] is not None:
            print("Yes")
            return
        if dp[n - 1][1] is not None:
            print("Yes")
            return
        print("No")

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
        input = """5 4
9 8 3 7 2
1 6 2 9 5"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 90
1 1 1 100
1 2 3 100"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 1000000000
1 1 1000000000 1000000000
1 1000000000 1 1000000000"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
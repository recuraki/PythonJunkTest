
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, m, k = map(int, input().split())
        mod = 998244353
        dp = [[0] * (k+1) for _ in range(n)]
        # 0
        for i in range(1, m+1):
            dp[0][i] = 1
        for ind in range(1, n):
            for addNum in range(1, m+1):
                for prev in range(k+1):
                    curnum = prev + addNum
                    if curnum > k: break
                    dp[ind][curnum] += dp[ind-1][prev]
                    dp[ind][curnum] %= mod
        ans = sum(dp[n-1]) % mod
        print(ans)

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
        input = """2 3 4"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """31 41 592"""
        output = """798416518"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
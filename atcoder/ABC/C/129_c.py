import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 1000000007
    n, m = map(int, input().split())
    dat_m = []
    dp = []
    for i in range(n + 1):
        dp.append([0] * (n + 1))
    for i in range(m):
        dat_m.append(int(input()))

    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][i-1] = dp[i - 1][i - 1]
        dp[i][i] = dp[i - 1][i - 1]

        if i > 1:
            dp[i][i] += dp[i - 1][i - 2]
            dp[i][i-2] = dp[i - 1][i - 2]

        if i in dat_m:
            dp[i][i] = 0

        dp[i][i] = dp[i][i] % mod

    import pprint
    print(dp[n][n])
    #pprint.pprint(dp)

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
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    base = 2500
    n,a = map(int, input().split())
    dat_x = list(map(int, input().split()))
    dat_x = list(map(lambda x: x - a, dat_x))

    #print(dat_x)
    dp = []
    for i in range(50 + 12):
        dp.append([0] * 5002)

    dp[0][base] = 1
    #print(dp[0][2500 - 10: 2500 + 10])
    for i in range(1, n + 1):
        for j in range(5001):
            dp[i][j] += dp[i - 1][j]

            #print(j + dat_x[i-1])
            if dp[i - 1][j] != 0:
                dp[i][j + dat_x[i-1]] += dp[i - 1][j]
        #print(dp[i][2500 - 10: 2500+10])
    print(dp[n][base] - 1)


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
        input = """4 1
0 2 1 2"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 8
6 6 9"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8 5
3 6 2 8 7 6 5 9"""
        output = """19"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """33 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3"""
        output = """8589934591"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_n = list(map(int, input().split()))
    dp = [0] * n
    dp [0]
    for i in range(1, n):
        if i > 1:
            dp[i] = min(dp[i - 1] + abs(dat_n[i] - dat_n[i-1]),dp[i - 2] + abs(dat_n[i] - dat_n[i-2]) )
        else:
            dp[i] = dp[i - 1] + abs(dat_n[i] - dat_n[i-1])
    print(dp[n-1])


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
10 30 40 20"""
        output = """30"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
10 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
30 10 60 10 60 50"""
        output = """40"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
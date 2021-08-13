import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        mod = 10**9 + 7
        s, k = input().split()
        k = int(k)
        l = []
        n = len(s)
        for i in range(n):
            l.append(int(s[i], 16))
        print(l)

        dp = [[0] * 17 for _ in range(n)]
        dp[0][1] = l[0]
        for i in range(1, n):
            print(i)
            print(dp[i])
            for j in range(16):
                dp[i][j] += dp[i-1][j] * min(j, l[i] + 1)
                if j != 16:
                    dp[i][j + 1] += dp[i-1][j] * (16 * l[i-1] + l[i])
                dp[i][j] %= mod
        print(dp[n-1])






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
        input = """10 1"""
        output = """15"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """FF 2"""
        output = """225"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100 2"""
        output = """226"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1A8FD02 4"""
        output = """3784674"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """DEADBEEFDEADBEEEEEEEEF 16"""
        output = """153954073"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
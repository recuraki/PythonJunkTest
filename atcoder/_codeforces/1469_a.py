import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        s = input()
        if len(s) % 2 == 1:
            print("NO")
            return
        l = s.find("(")
        r = s.find(")")
        if r == 0 or l == len(s)-1:
            print("NO")
            return
        print("YES")
    def do_dp():
        s = input()
        n = len(s)
        dp = [[0] * (100 + 10) for _ in range(100 + 10)]
        dp[0][0] = 1
        for i in range(n):
            ch = s[i]
            if ch == "(":
                for k in range(105):
                    dp[i+1][k+1] += dp[i][k]
            elif ch == ")":
                for k in range(105):
                    if k != 0:
                        dp[i + 1][k - 1] += dp[i][k]
            else:
                for k in range(105):
                    dp[i+1][k+1] += dp[i][k]
                    if k != 0:
                        dp[i + 1][k - 1] += dp[i][k]
        print("YES" if dp[n][0] != 0 else "NO")

    q = int(input())
    for _ in range(q):
        do_dp()



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        self.maxDiff = 10000000
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """8
()
(???)
(??)
??()
)?(?
()??
(??)??
?(?)??"""
        output = """YES
NO
YES
YES
NO
YES
YES
YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_11")
        input = """1
?)(?
"""
        output = """YES"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
import array
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    def do():
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        total = 0
        for i in range(n): total += data[i] * datb[i]
        res = total
        dp = list([Decimal(0)] * n)
        newdp = list([Decimal(0)] * n)
        for step in range(1, n):
            for i in range(n): newdp[i] = 0
            l = n - step - 1
            newdp[l] = total
            newdp[l + 1] = total + data[l] * (datb[l+1] - datb[l]) + data[l+1] * (datb[l] - datb[l+1])
            for r in range(n - step + 1, n):
                newdp[r] = dp[r - 1] + data[l] * (datb[r] - datb[l]) + data[r] * (datb[l] - datb[r])
            dp, newdp = newdp, dp
            res = max(max(dp), res)
        print(res)
    do()

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        self.maxDiff = 1000000
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_1(self):
        print("test_input_1")
        input = """5
2 3 2 1 3
1 3 2 4 2"""
        output = """29"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
13 37
2 4"""
        output = """174"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
1 8 7 6 3 6
5 9 6 8 8 6"""
        output = """235"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
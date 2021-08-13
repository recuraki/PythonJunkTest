import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():

    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        dat0, dat1 = [], []
        for i in range(n):
            if dat[i] == 0: dat0.append(i)
            else: dat1.append(i)
        if len(dat1) == 0:
            print(0)
            return
        dp = [None] * len(dat1)
        dp[0] = 10**18
        for ind0 in range(len(dat0)):
            for ind1 in range(len(dat1)-1, 0, -1):
                curcost = abs(dat0[ind0] - dat1[ind1])
                if dp[ind1 - 1] is None: continue
                if dp[ind1] is None: dp[ind1] = 10**18
                dp[ind1] = min(dp[ind1], dp[ind1 - 1] + curcost)
            curcost = abs(dat0[ind0] - dat1[0])
            dp[0] = min(curcost, dp[0])
        print(dp[-1])
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
        input = """7
1 0 0 1 0 0 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
1 1 1 0 0 0"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10
0 1 1 1 1 0 0 1 0 0"""
        output = """13"""
        self.assertIO(input, output)

    def test_input_41(self):
        print("test_input_41")
        input = """10
0 0 1 0 0 1 1 1 1 0"""
        output = """13"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
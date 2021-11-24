import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint

    INF = 1 << 63

    def do():
        import math
        mod = 998244353
        n = int(input())
        datlow = list(map(int, input().split()))
        dathigh = list(map(int, input().split()))
        dp = [0] * (3000 + 10)
        newdp = [0] * (3000 + 10)

        # init
        for i in range(datlow[0], dathigh[0] + 1):
            dp[i] += 1
        #print()
        for ind in range(1, n):
            #print(i, dp[0:20])
            for i in range(3010):
                newdp[i] = 0
            basenum = 0 # a[n] の直前までの数

            for i in range(0, datlow[ind]):
                basenum += dp[i]
                basenum %= mod
            #print("base", basenum)
            # a-bをなめる
            for i in range(datlow[ind], dathigh[ind] + 1):
                basenum += dp[i]
                basenum %= mod
                dp[i] = basenum
                dp[i] %= mod
            for i in range(datlow[ind]):
                dp[i] = 0

            #dp, newdp = newdp, dp

        #print(dp[0:20])
        finalres = 0
        for x in dp:
            finalres += x
            finalres %= mod

        print(finalres % mod)

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

    def test_input_11(self):
        print("test_input_11")
        input = """1
1
2"""
        output = """"""
        self.assertIO(input, output)


    def test_input_1(self):
        print("test_input_1")
        input = """2
1 1
2 3"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
2 2 2
2 2 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
1 2 3 4 5 6 7 8 9 10
1 4 9 16 25 36 49 64 81 100"""
        output = """978222082"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
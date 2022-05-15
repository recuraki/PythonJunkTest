import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():




    from pprint import pprint
    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        s = input()
        dat = [0]
        for x in s:
            dat.append(-1 if x=="-" else 1)
        print(dat)
        center = 3010
        si = (3000 * 2 + 20)
        dp = [[0] * 2 for _ in range(si)]
        dp[center] = 1
        for i in range(n):
            newdp = [[0] * 2 for _ in range(si)]
            canpoly = False
            if dat[i] == -1: # --?
                if i != 0 and dat[i-1] == -1: canpoly = True
                if i != n-1 and dat[i+1] == -1: canpoly = True
            if not canpoly: # normal
                if dat[i] == -1:
                    for j in range(1, si - 1):
                        newdp[j][0] += dp[j+1][0]
                        newdp[j][0] += dp[j+1][1]
                else: # +
                    for j in range(1, si - 1):
                        newdp[j][1] += dp[j-1][0]
                        newdp[j][1] += dp[j-1][1]
            else: # --
                for j in range(1, si - 1):
                    newdp[j][0] += dp[j + 1][0] + dp[j + 1][0]
                    newdp[j][0] += dp[j + 1][1] + dp[j + 1][1]
                    newdp[j][1] += dp[j - 1][0]
                    newdp[j][1] += dp[j - 1][1]
            #dp = newdp
        print(dp[center])



    # n questions
    q = int(input())
    for _ in range(q):
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
        input = """5
3
+-+
5
-+---
4
----
7
--+---+
6
+++---"""
        output = """2
4
2
7
4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
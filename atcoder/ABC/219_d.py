import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    import math
    INF = 1 << 31
    def do():
        from copy import deepcopy
        n = int(input())
        xx, yy = map(int, input().split())
        totala = 0
        totalb = 0
        dat = []
        for _ in range(n):
            a, b = map(int, input().split())
            totala += a
            totalb += b
            dat.append( (a, b) )
        dp = [[INF] * 301 for _ in range(301)]
        dp[0][0] = 0
        for a, b in dat:
            for x in range(300, -1, -1):
                for y in range(300, -1, -1):
                    if dp[x][y] == INF: continue
                    newx = x + a
                    newy = y + b
                    if newx > 300: newx = 300
                    if newy > 300: newy = 300
                    dp[newx][newy] = min(dp[newx][newy], dp[x][y] + 1)
        res = INF
        for x in range(xx, 301):
            for y in range(yy, 301):
                res = min(res, dp[x][y])
        if res == INF:
            print(-1)
        else:
            print(res)
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
        input = """3
5 6
2 1
3 4
2 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
8 8
3 4
2 3
2 1"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
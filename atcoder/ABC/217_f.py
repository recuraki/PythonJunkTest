import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    mod = 998244353
    INF = 1 << 63
    def do():
        nn, m = map(int, input().split())
        n = 2 * nn
        dp = [[0] * n for _ in range(n)]
        #pprint(dp)
        for _ in range(m):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            if a+1 == b: # 隣り合うペア
                dp[a][b] = 1
        for c in range(1,nn):
            b = 2 * c
            for a in range(n-1 - 2 * c):
                cnt = 0
                b += 1
                #print(c,a,b)
                for i in range(b - a - 2):
                    cura = a + i
                    curb = b - 2 + i
                    mergea = curb + 1
                    mergeb = curb + 2
                    if mergea > b: mergea -= 2*(c+1)
                    if mergeb > b: mergeb -= 2*(c+1)
                    cnt += dp[cura][curb]
                    cnt += dp[mergea][mergeb]
                    cnt %= mod
                    mergea += 1
                    mergeb += 1
                dp[a][b] = cnt
        print(dp[0][n-1] % mod)
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
        input = """3 3
1 2
1 4
2 3"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2
1 2
3 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 2
1 3
2 4"""
        output = """0"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
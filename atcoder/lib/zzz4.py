import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        mod = 998244353

        total = sum(dat)
        if total %2 == 1:
            print(0)
            return

        def myfrac(n):
            x = 1
            for i in range(1, n + 1):
                x *= i % mod
            return x

        dp = [[[0] * 110 for _ in range(5200)] for _ in range(110)]
        dp[0][0][0] = 1
        for i in range(n):
            for value in range(5010):
                for cnt in range(i+1):
                    dp[i + 1][value][cnt] += dp[i][value][cnt]
                    if value+dat[i] > 5010:
                        continue
                    dp[i + 1][value + dat[i]][cnt + 1] += dp[i][value][cnt]
        dat = []
        a = 0
        for i in range(1, n):
            if dp[n][total // 2][i] != 0:
                a += myfrac(i) * myfrac(n-i) * dp[n][total // 2][min(i, n-i)]
                a %= mod

        print(a%mod)
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
1 1 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 2 3 8"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20
2 8 4 7 5 3 1 2 4 1 2 5 4 3 3 8 1 7 8 2"""
        output = """373835282"""
        self.assertIO(input, output)

    def test_input_31(self):
        print("test_input_31")
        input = """100
100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100"""
        output = """"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """7
1 1 2 2 3 5 4"""
        output = """"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """10
1 1 2 2 3 5 4 2 2 2
"""
        output = """1471680"""
        self.assertIO(input, output)

    def test_input_311(self):
        print("test_input_311")
        input = """10
2 2 2 2 2 2 2 2 2 2
"""
        output = """3628800"""
        self.assertIO(input, output)
    def test_input_3121(self):
        print("test_input_3121")
        input = """10
1 2 3 4 5 6 7 8 9 11
"""
        output = """630720"""
        self.assertIO(input, output)
    def test_input_31211(self):
        print("test_input_31211")
        input = """99
57 69 17 68 66 98 31 80 77 32 29 92 62 39 62 100 2 50 60 81 26 82 16 1 94 93 67 25 60 30 99 24 90 25 7 97 100 11 46 61 8 16 75 94 36 11 12 55 5 96 45 24 15 81 81 56 49 62 25 43 84 71 40 56 10 60 42 81 23 27 66 64 14 31 65 79 76 3 34 16 21 11 84 80 53 93 11 67 68 89 72 58 66 92 64 11 80 43 11
"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
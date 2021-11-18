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


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():

        MOD = 998244353
        N = 1000

        fact = [1] * (N + 1)
        rfact = [1] * (N + 1)
        r = 1
        for i in range(1, N + 1):
            fact[i] = r = r * i % MOD
        rfact[N] = r = pow(fact[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            rfact[i - 1] = r = r * i % MOD

        # nPk (mod MOD) を求める
        def perm(n, k):
            return fact[n] * rfact[n - k] % MOD

        # nCk (mod MOD) を求める
        def comb(n, k):
            return fact[n] * rfact[k] * rfact[n - k] % MOD



        ans = 0
        mod = 998244353
        print()
        n, k = map(int, input().split())
        for high in range(1, k+ 1): # 最も高い人のHP
            for ninzu in range(2, n+1): # 何人高い人はいる？
                nokoninzu = n - ninzu
                pat = comb(n, ninzu) # この人たちのHPは決まりました
                nokoripat = pow(high - 1, nokoninzu, MOD)
                print("high", high, "ninzu", ninzu, "nokori", nokoninzu, "pat", pat, "nokori", nokoripat)
                print(">", pat * nokoripat)
                ans += (pat * nokoripat) % MOD
        print(ans % MOD)


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
        input = """2 5"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3"""
        output = """15"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 4"""
        output = """1024"""
        self.assertIO(input
                      , output)
    def test_input_4(self):
        print("test_input_4")
        input = """13 37"""
        output = """976890680"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
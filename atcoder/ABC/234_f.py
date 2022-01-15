import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    import math
    INF = 1 << 63
    def do():
        mod = 998244353

        def egcd(a, b):
            if a == 0:
                return b, 0, 1
            else:
                g, y, x = egcd(b % a, a)
                return g, x - (b // a) * y, y

        # mを法とするaの乗法的逆元
        def modinv(a, m):
            g, x, y = egcd(a, m)
            if g != 1:
                raise Exception('modular inverse does not exist')
            else:
                return x % m

        # nCr mod m
        # modinvが必要
        # rがn/2に近いと非常に重くなる
        def combination(n, r, mod=998244353):
            r = min(r, n - r)
            res = 1
            for i in range(r):
                res = res * (n - i) * modinv(i + 1, mod) % mod
            return res

        def nHrMod(n, r, mod=10 ** 9 + 7):
            return combination((n + r - 1), r, mod=mod)
        s = input()
        cnt = [0] * 26
        for x in s:
            cnt[ord(x) - ord('a')] += 1

        ans = 0
        for i in range(26):
            for j in range(cnt[i] + 1):
                ans *= combination(cnt[i], j)
                ans %= mod




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
        input = """aab"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """aaa"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """abcdefghijklmnopqrstuvwxyz"""
        output = """149621752"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
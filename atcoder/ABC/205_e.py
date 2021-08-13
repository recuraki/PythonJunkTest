import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        mod = 10**9 + 7
        p = mod
        N = 2000000 + 10
        # 適当に計算しておく
        fact = [1, 1]
        factinv = [1, 1]
        inv = [0, 1]
        for i in range(2, N + 1):
            fact.append((fact[-1] * i) % p)
            inv.append((-inv[p % i] * (p // i)) % p)
            factinv.append((factinv[-1] * inv[-1]) % p)
        n, m, k = map(int, input().split())
        # total = (n+m)! / (n! * m!)を計算したい
        x = factinv[n] * factinv[m]
        total = fact[n+m]* x % mod
        res = total
        cnt = 0
        prevcount = 0
        # 取ってはいけない頭の組み合わせ。k=1なら2,0 や 3,1など
        for w in range(k+1, n + 1):
            cnt += 1
            b = w - k - 1
            nokoriw = n - w
            nokorib = m - b
            # subtotal1 このw, bで頭で並ぶ組み合わせの数
            subtotal1 = fact[w + b] * factinv[w] * factinv[b]
            subtotal1 -= prevcount * 2
            subtotal1 %= mod
            # 残りの組み合わせの数
            subtotal2 = fact[nokoriw + nokorib] * factinv[nokoriw] * factinv[nokorib]
            subtotal2 %= mod
            subtotal = (subtotal1 * subtotal2)
            subtotal %= mod
            res -= subtotal
            res %= mod
            prevcount += subtotal1 + prevcount * 2

            # 前の重複を避ける
        print(res % mod)
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
        input = """2 3 1"""
        output = """9"""
        #self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 0 0"""
        output = """0"""
        #self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000000 1000000 1000000"""
        output = """192151600"""
        #self.assertIO(input, output)

    def test_input_122(self):
        print("test_input_122")
        input = """2 3 0"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
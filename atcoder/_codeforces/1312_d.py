import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 998244353

    def cmb(n, r, p):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return fact[n] * factinv[r] * factinv[n - r] % p

    p = mod
    N = 5 * 10 ** 5  # N は必要分だけ用意する
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]

    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)


    n, m = map(int, input().split())
    res = 0
    import math
    if n == 2:
        print(0)
    else:
        for i in range(n-1, m+1):
            res += (i - 1) * cmb(i - 2, n - 3, mod) * pow(2, n-3, mod)
            res %= mod
        print(res)



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
        input = """3 4"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100000 200000"""
        output = """707899035"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
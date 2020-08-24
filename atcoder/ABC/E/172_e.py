import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
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
    def combination(n, r, mod=10 ** 9 + 7):
        r = min(r, n - r)
        res = 1
        for i in range(r):
            res = res * (n - i) * modinv(i + 1, mod) % mod
        return res

    def div(a, b):
        return (a * pow(b, mod - 2, mod) ) % mod

    mod = 10**9 + 7
    n, m = map(int, input().split())
    res = 1
    for i in range(n):
        res *= m - i
        res %= mod

    print(res)

    x = 1
    for i in range(n-1):
        x *= m - 1 - i
        x %= mod
    print(x)
    x *= m-1
    x %= mod

    #x -= (m-1) * (m-1)

    #res = div(res, n-1)

    res *= x
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
        input = """2 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 3"""
        output = """18"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """141421 356237"""
        output = """881613484"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
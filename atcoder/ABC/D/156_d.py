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


    n, a, b = map(int, input().split())
    res = 0
    mod = 1000000000 + 7
    #res = (2** (n) -1 )% mod
    res = (pow(2, n, mod) -1 )% mod
    res -= combination(n, a)
    res %= mod
    res -= combination(n, b)
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
        input = """4 1 3"""
        output = """7"""
        self.assertIO(input, output)


    def test_input_23(self):
        print("test_input_2")
        input = """1000000000 141421 173205"""
        output = """34076506"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
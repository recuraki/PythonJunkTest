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

    n, k = map(int, input().split())
    res = 1
    p = 1
    for i in range(k, -1, -1):
        print(i)
        c = combination(n - (k-i), i, 10000000007)
        res += p * c
        print("{0}C{1}".format(n-(k-i), i))
        print("c={0}, add {1}, p = {2}".format(c, p*c, p))
        p = c
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
        input = """3 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """15 6"""
        output = """22583772"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

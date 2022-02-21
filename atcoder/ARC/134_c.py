import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():





    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():

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

        def nHrMod(n, r, mod=998244353):
            return combination((n + r - 1), r, mod=mod)

        mod = 998244353
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        ball1 = dat[0]
        dat = dat[1:]
        ball1 -= k # まずball1をいれる
        ball1 -= sum(dat) # すべてのやつと組み合わせる
        if ball1 < 0:
            print(0)
            return
        ans = 1
        for x in dat:
            # x がボールの数
            x += 0
            k += 0
            a = x + (k-1)
            b = (k-1)
            #print(a, b)
            #print(combination(a , b, mod))
            ans *= combination(a , b, mod)

        # さいごにball1を適当にk個にいれていい
        ans *= combination(ball1 + (k-1), k-1, mod)

        # ただしいかな
        print( (ans ) % mod)
    print(" ".join(list(map(str, dat))))


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
        input = """2 2
3 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1
1 100"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20 100
1073813 90585 41323 52293 62633 28788 1925 56222 54989 2772 36456 64841 26551 92115 63191 3603 82120 94450 71667 9325"""
        output = """313918676"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
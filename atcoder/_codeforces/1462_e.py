import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import itertools
    def countstrs(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]

    def nCr(n, r):
        import math
        if r > n:
            return 0
        return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))

    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def combination(n, r, mod=10**9 + 7 ):
        if r > n:
            return 0
        r = min(r, n - r)
        res = 1
        for i in range(r):
            res = res * (n - i) * modinv(i + 1, mod) % mod
        return res

    def do():
        n = int(input())
        n, m, k = map(int, input().split())

        dat = list(map(int, input().split()))
        dat.sort()
        C = countstrs(dat)
        res = 0
        for ii in range(1, m+1): # iiこ取る
            # get ii
            for i in range(len(C)- (ii - 1) ):
                cur = 1
                minind = dat[i][0]
                if dat[i + (ii - 1)][0] - dat[i][0] > k:
                    continue

                for j in range(ii):
                    res *= dat[j][1]
                    res %= 10**9+7
        print(res)


    q = int(input())
    for _ in range(q):
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
        input = """4
4 3 2
1 2 4 3
4 3 2
1 1 1 1
1 3 2
1
10 3 2
5 6 1 3 2 9 8 1 2 4"""
        output = """2
4
0
15"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
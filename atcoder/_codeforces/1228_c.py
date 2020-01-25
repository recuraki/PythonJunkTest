import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = map(int, input().split())
    mod = 1000000007
    def g(a, b):
        if b == 1:
            return 1
        k = 0
        res = 1
        while True:
            if (b ** k) > a:
                k -= 1
                break
            if a % (b ** k):
                res = k
            k += 1
        return b ** k

    import math

    def isPrime(n):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        m = math.floor(math.sqrt(n)) + 1
        for p in range(3, m, 2):
            if n % p == 0:
                return False
        return True

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors

    def make_divisors_without_own(n):
        r = make_divisors(n)
        r.remove(n)
        r.remove(1)
        re = []
        for i in range(len(r)):
            if isPrime(r[i]):
                re.append(r[i])
        return re

    def f(a, b):
        res = 1
        dat = make_divisors_without_own(a)
        for i in range(len(dat)):
            res *= g(b, dat[i])
            res %= mod
        return res

    res = 1
    for i in range(1, b+1):
        res *= f(a, i)
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
        input = """20190929 100"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20190929 1605"""
        output = """363165664"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """947 987654321987654321"""
        output = """593574252"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
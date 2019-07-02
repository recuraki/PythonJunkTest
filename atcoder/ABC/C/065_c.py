import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    MOD1 = 1000000000 + 7
    def factorial_mod(n, mod):
        import math
        return math.factorial(n) % mod
    n,m = map(int, input().split())
    if abs(n-m) > 1:
        print(0)
    elif n == m:
        res = factorial_mod(m, MOD1) * factorial_mod(n, MOD1)
        res *= 2
        res %= MOD1
        print(res)
    else:
        res = factorial_mod(m, MOD1) * factorial_mod(n, MOD1)
        res %= MOD1
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
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 8"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """100000 100000"""
        output = """530123477"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
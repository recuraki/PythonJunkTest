import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    MOD = 1000000007
    def nCr(n, r):
        import math
        return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))
    n, k = map(int, input().split())
    b, r = k, n-k
    for i in range(0, k):
        x = nCr(b - 1,  i) # 青いブロックの分け方
        if r - i < 0:
            print(0)
        else:
            y = nCr(r + 1, r - i)
            print(x * y % MOD)


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
        input = """5 3"""
        output = """3
6
1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2000 3"""
        output = """1998
3990006
327341989"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
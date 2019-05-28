import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    n = int(input())
    dat_a = list(map(int, input().split()))
    dat_a = list(dat_a)
    m = []
    l = [0] * n
    r = [0] * (n + 1)
    l[0] = 0
    r[n - 1] = 0
    for i in range(n):
        l[i + 1] = math.gcd(l[i], dat_a[i])
        r[n - i-1] = math.gcd(r[n-i], dat_a[i])




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
        logging.info("test_input_1")
        input = """3
7 6 8"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """3
12 15 18"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """2
1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
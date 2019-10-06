import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = map(int, input().split())
    dat_a = list(dat_a)
    l = [0] * n
    r = [0] * n
    res = [0] * n
    import fractions

    l[0] = 0
    r[n-1] = 0
    for i in range(1, n):
        l[i] = fractions.gcd(l[i-1], dat_a[i-1])

    for i in range(n-2, -1, -1):
        r[i] = fractions.gcd(r[i+1], dat_a[i+1])
    for i in range(n):
        res[i] = fractions.gcd(l[i], r[i])

    print(max(res))





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
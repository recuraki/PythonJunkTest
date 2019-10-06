import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import fractions
    n = int(input())
    dat_a = list(map(int, input().split()))
    res = dat_a[0]
    for i in range(n - 1):
        res = fractions.gcd(res, dat_a[1+i])
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
        input = """4
2 10 8 40"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
5 13 8 1000000000"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
1000000000 1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
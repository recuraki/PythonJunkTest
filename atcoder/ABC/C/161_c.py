import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    if n == 0 or n == k:
        print(0)
    else:
        a = abs(n % k)
        b = abs(a - k)
        print(min(a, b))


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
        input = """7 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 6"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000000000000000000 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_3")
        input = """0 1"""
        output = """0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
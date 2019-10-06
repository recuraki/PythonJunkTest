import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    n,m = min(n,m), max(n,m)
    if n == 1 and m == 1:
        print(1)
    elif n == 1:
        print(m-2)
    else:
        print(n * m - 2*n - 2*m + 4)

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
        output = """0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 7"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """314 1592"""
        output = """496080"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
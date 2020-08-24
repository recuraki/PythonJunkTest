import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    import math
    x = math.ceil(n / 1000) * 1000
    print(x - n)

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
        input = """1900"""
        output = """100"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3000"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
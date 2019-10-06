import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    if n == 1:
        print(2)
    elif n % 2 == 0:
        print(n-1)
    else:
        print(n+1)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """100"""
        output = """99"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """123456789"""
        output = """123456790"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
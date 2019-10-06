import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    if n == 12:
        print("1")
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
    def test_入力例1(self):
        input = """1"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """12"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
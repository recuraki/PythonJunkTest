import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    print(n-1)

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
        input = """4"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """100"""
        output = """99"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
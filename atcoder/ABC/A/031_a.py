import sys
from io import StringIO
import unittest

def resolve():
    a,d = map(int, input().split())
    if (a * (d+1)) < ((a+1) * d):
        print(((a+1) * d))
    else:
        print(((a) * (d + 1)))


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
        input = """31 87"""
        output = """2784"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """101 65"""
        output = """6666"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """3 3"""
        output = """12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
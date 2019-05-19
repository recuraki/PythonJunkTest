import sys
from io import StringIO
import unittest

def resolve():
    a,b,c = map(int, input().split())
    r = 0
    r+= 2 * a*b
    r+= 2 * c*b
    r+= 2 * a*c
    print(r)

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
        input = """2 3 4"""
        output = """52"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """3 4 2"""
        output = """52"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """100 100 100"""
        output = """60000"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """1 1 1"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
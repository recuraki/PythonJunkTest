import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3
4"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """19
100"""
        output = """261"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """10
0"""
        output = """100"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    n = int(input())
    a = int(input())
    print( n*n - a)
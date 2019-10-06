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
        input = """0 5"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 11"""
        output = """1100"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2 85"""
        output = """850000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():

    d,n = map(int, input().split())
    r = 0
    if n == 100:
        if d == 0:
            print( 1 * 101)
        elif d == 1:
            print( 100 * 101)
        elif d == 2:
            print( 100*100 * 101)
    else:
        if d == 0:
            print(n * 1)
        elif d == 1:
            print(n * 100)
        elif d == 2:
            print(n * 100*100)

:
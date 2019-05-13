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
        input = """8 3"""
        output = """2.6666666667"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """99 1"""
        output = """99.0000000000"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 100"""
        output = """0.0100000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    import math
    t, x = map(float, input().split())
    count = float( float(t)/ float(x))
    print("{0:6f}".format(float(round(count, 10))))
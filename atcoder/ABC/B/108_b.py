import sys
from io import StringIO
import unittest

def resolve():
    x1,y1,x2,y2 = map(int, input(). split())
    dx = (x2 - x1)
    dy = (y2 - y1)


    x3, y3 = x2 - dy, y2 + dx
    x4, y4 = x1 - dy, y1 + dx
    x3, y3, x4, y4 = int(x3), int(y3), int(x4), int(y4)
    print("{0} {1} {2} {3}".format( x3, y3, x4, y4))

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
        input = """0 0 0 1"""
        output = """-1 1 -1 0"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 3 6 6"""
        output = """3 10 -1 7"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """31 -41 -59 26"""
        output = """-126 -64 -36 -131"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
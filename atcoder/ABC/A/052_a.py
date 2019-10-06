import sys
from io import StringIO
import unittest

def resolve():
    a,b,c,d = map(int, input().split())
    if a*b > c*d:
        print(a*b)
    else:
        print(c*d)

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
        input = """3 5 2 7"""
        output = """15"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """100 600 200 300"""
        output = """60000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
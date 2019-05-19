import sys
from io import StringIO
import unittest

def resolve():
    a,b,c = map(int, input().split())
    if (b-a ) == (c-b):
        print("YES")
    else:
        print("NO")

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
        input = """2 4 6"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 5 6"""
        output = """NO"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3 2 1"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
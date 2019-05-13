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
        input = """5"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
def resolve():
    x = int(input())
    if x == 3 or x == 5 or x == 7:
        print("YES")
    else:
        print("NO")
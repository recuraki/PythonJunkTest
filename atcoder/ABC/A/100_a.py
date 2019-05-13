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
        input = """5 4"""
        output = """Yay!"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """8 8"""
        output = """Yay!"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """11 4"""
        output = """:("""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
def resolve():
    a, b = map(int, input().split())
    if a > 8 or b > 8:
        print(":(")
    else:
        print("Yay!")
import sys
from io import StringIO
import unittest

def resolve():
    a,b = map(int, input().split())
    if a==b:
        print("Draw")
    elif a == 1:
        print("Alice")
    elif b == 1:
        print("Bob")
    elif a> b :
        print("Alice")
    else:
        print("Bob")


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
        input = """8 6"""
        output = """Alice"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 1"""
        output = """Draw"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """13 1"""
        output = """Bob"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
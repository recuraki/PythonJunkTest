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
        input = """575"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """123"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """812"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    n = input()
    if n[0] == n[2]:
        print("Yes")
    else:
        print("No")
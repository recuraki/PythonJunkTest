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
        input = """999"""
        output = """ABC"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1000"""
        output = """ABD"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1481"""
        output = """ABD"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    n = int(input())
    if n < 1000:
        print("ABC")
    else:
        print("ABD")
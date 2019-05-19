import sys
from io import StringIO
import unittest

def resolve():
    x,y = map(int, input().split())
    if x > y:
        print("Worse")
    else:
        print("Better")

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例1(self):
        input = """12 34"""
        output = """Better"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """98 56"""
        output = """Worse"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
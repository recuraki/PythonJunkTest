import sys
from io import StringIO
import unittest

def resolve():
    a,o,b = input().split()
    a = int(a)
    b = int(b)
    if o == "+":
        print(a+b)
    else:
        print(a-b)

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
        input = """1 + 2"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 - 7"""
        output = """-2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
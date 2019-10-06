import sys
from io import StringIO
import unittest

def resolve():
    a = "ABCDE"
    x = input()
    num = a.find(x)
    print(num + 1)

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
        input = """A"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """B"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """C"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """D"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
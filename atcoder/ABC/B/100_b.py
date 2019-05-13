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
        input = """0 5"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 11"""
        output = """1100"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2 85"""
        output = """850000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():

    d,n = map(int, input().split())
    r = 0
    r = n * (pow(100 ,d))
    print(r)
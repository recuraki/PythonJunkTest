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
        input = """1 5 2"""
        output = """53"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """9 9 9"""
        output = """108"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 6 7"""
        output = """82"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    a,b,c = map(int, input().split())
    if a == max(a,b,c):
        res = a*10 + b + c
    if b == max(a,b,c):
        res = b*10 + a + c
    if c == max(a,b,c):
        res = c*10 + a + b
    print(res)

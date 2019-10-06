import sys
from io import StringIO
import unittest

def resolve():
    a,b,c = input().split()
    if a[-1] == b[0] and b[-1] == c[0]:
        print("YES")
    else:
        print("NO")

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
        input = """rng gorilla apple"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """yakiniku unagi sushi"""
        output = """NO"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """a a a"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """aaaaaaaaab aaaaaaaaaa aaaaaaaaab"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

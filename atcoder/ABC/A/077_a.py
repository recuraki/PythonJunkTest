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
        input = """pot
top"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """tab
bet"""
        output = """NO"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """eye
eel"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    a,b,c = list(input())
    d,e,f = list(input())
    if a==f and b == e and c == d:
        print("YES")
    else:
        print("NO")
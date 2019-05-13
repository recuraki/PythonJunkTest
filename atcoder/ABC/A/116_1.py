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
        input = """3 4 5"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 12 13"""
        output = """30"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """45 28 53"""
        output = """630"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    a,b,c = map(int, input().split())
    if a == max(a,b,c):
        print(int(b*c / 2))
    elif b == max(a,b,c):
        print(int(a*c / 2))
    elif c == max(a,b,c):
        print(int(a*b / 2))

import sys
from io import StringIO
import unittest

def resolve():
    s = input()
    x = s[0] + s[1]
    y = s[2] + s[3]
    x = int(x)
    y = int(y)
    if x > 0 and x < 13:
        if y > 0 and y < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    elif y > 0 and y < 13:
        print("YYMM")
    else:
        print("NA")


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
        input = """1905"""
        output = """YYMM"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """0112"""
        output = """AMBIGUOUS"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1700"""
        output = """NA"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
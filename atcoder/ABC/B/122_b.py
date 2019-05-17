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
        input = """ATCODER"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """ATAGAYA"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """A"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    s = input()
    sub = ["A", "C", "G", "T"]
    ml = 0
    nowml = 0
    for i in range(len(s)):
        if s[i] in sub:
            nowml += 1
        else:
            nowml = 0
        ml = max(nowml, ml)
    print(ml)

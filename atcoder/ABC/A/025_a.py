import sys
from io import StringIO
import unittest

def resolve():
s = input()
n = int(input()) - 1
print(s[int(n/5)] + s[int(n%5)])

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
        input = """abcde
1"""
        output = """ab"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """aeiou
22"""
        output = """ue"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """vwxyz
25"""
        output = """zz"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
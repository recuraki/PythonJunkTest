import sys
from io import StringIO
import unittest

def resolve():
    s = input()
    i = int(input())

    print(s[i-1])

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
        input = """atcoder
3"""
        output = """c"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """beginner
1"""
        output = """b"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """contest
7"""
        output = """t"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """z
1"""
        output = """z"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
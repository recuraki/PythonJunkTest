import sys
from io import StringIO
import unittest

def resolve():
    n,m = map(int, input().split())
    res = [0] * n
    num = 1
    for i in range(m):
        a,b,c = map(int, input())




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
        input = """3 1
1 2 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 5
1 2 1
2 3 2
1 3 3
4 5 4
5 6 5"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """100000 1
1 100000 100"""
        output = """99999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
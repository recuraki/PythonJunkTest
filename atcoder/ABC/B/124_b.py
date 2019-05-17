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
        input = """4
6 5 6 8"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
4 5 3 5 4"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
9 5 6 8 4"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    n = int(input())
    h = map(int, input().split())
    h = list(h)
    mh = 0
    count = 0
    for i in range(n):
        if mh <= h[i]:
            mh = h[i]
            count += 1
    print(count)
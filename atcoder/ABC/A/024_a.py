import sys
from io import StringIO
import unittest

def resolve():
    a,b,c,k = map(int, input().split())
    s,t = map(int, input().split())

    res = a * s + b * t
    if k <= (s+t):
        res -= c * (s+t)
    print(res)

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
        input = """100 200 50 20
40 10"""
        output = """3500"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """400 1000 400 21
10 10"""
        output = """14000"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """400 1000 400 20
10 10"""
        output = """6000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
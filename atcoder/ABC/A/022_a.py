import sys
from io import StringIO
import unittest

def resolve():
    n,s,t = map(int, input().split())
    w = int(input())
    count = 0
    if w <= t and w >= s:
        count += 1
    for i in range(n-1):
        a = int(input())
        w += a
        if w <= t and w >= s:
            count += 1
    print(count)

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
        input = """5 60 70
50
10
10
10
10"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """5 50 100
120
-10
-20
-30
70"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
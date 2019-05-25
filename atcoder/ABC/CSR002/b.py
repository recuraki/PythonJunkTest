import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(a%b)

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
        input = """3
10 3
1000000000 1
11 92"""
        output = """1
0
11"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
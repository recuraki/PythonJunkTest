import sys
from io import StringIO
import unittest


def resolve():
    dat_a = []
    dat_b = []
    n = int(input())
    m = 0
    for i in range(n):
        a, b = map(int, input().split())
        m = max(a+b, m)
    print(m)


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
4 4
3 7
8 1"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
12345678 111111111
103050709 20406080"""
        output = """123456789"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
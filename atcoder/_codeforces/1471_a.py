import sys
from io import StringIO
import unittest
import logging

logging.basicConfig(level=logging.DEBUG)


def resolve():
    from pprint import pprint

    def do():
        import math
        n, x = map(int, input().split())
        dat = list(map(int, input().split()))
        a = math.ceil(sum(dat) / x)
        b = 0
        for i in range(n):
            b += math.ceil(dat[i] / x)
        print(a, b)

    q = int(input())
    for _ in range(q):
        do()


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_1(self):
        print("test_input_1")
        input = """2
3 3
3 6 9
3 3
6 4 11"""
        output = """6 6
7 8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
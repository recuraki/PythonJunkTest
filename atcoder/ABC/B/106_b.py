import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue
        c = 0
        for j in range(1, i + 1):

            if i % j == 0:
                c += 1
        if c == 8:
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
    def test_入力例_1(self):
        input = """105"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    res = 0
    d = dict()
    for i in range(2, 100000 + 10):
        k = 2
        while i ** k <= n:
            x = i ** k
            if x not in d:
                res += 1
            d[x] = True
            k += 1
    print(n - res)


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
        input = """8"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """100000"""
        output = """99634"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
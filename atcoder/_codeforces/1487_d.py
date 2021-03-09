import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline

    def solv_quadratic_equation(a, b, c):
        D = (b ** 2 - 4 * a * c) ** (1 / 2)
        x_1 = (-b + D) / (2 * a)
        x_2 = (-b - D) / (2 * a)
        return max(x_1, x_2)

    def do():
        n = int(input())
        n -= 1
        n //= 4
        import math


        print(math.floor(solv_quadratic_equation(1, 1, -2 * n)))

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
        input = """3
3
6
9"""
        output = """0
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
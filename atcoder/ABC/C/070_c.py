import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import fractions
    def lcm(x, y):
        return (x * y) // fractions.gcd(x, y)
    n = int(input())
    res = -1
    for i in range(n):
        t = int(input())
        if res == -1:
            res = t
        else:
            res = lcm(res, t)
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
    def test_input_1(self):
        print("test_input_1")
        input = """2
2
3"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
2
5
10
1000000000000000000
1000000000000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
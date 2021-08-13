import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import math
    def do():

        n = int(input())
        if n == 1 or n == 2:
            raise
            assert False
        r = (math.cos(math.pi / n) ** 2)
        print(1 / (1 - r))
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
3
4"""
        output = """1.33333333
2.00000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
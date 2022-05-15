import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        s = input()
        s = list(s)
        s.sort()
        print("".join(s))

    # 1 time
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
        input = """aba"""
        output = """aab"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """zzzz"""
        output = """zzzz"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
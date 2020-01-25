import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import math
    def dp(s):
        if True:
            print(s)

    def dpp(s):
        if True:
            pprint(s)

    n = int(input())
    if n != 1:
        ab = 0
        for i in range(2, n+1):
            ab += 1 / i
        print(1+ ab)
    else:
        print("1.0000000000")



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
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2"""
        output = """1.500000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
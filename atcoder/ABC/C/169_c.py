import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from decimal import Decimal
    import math
    a,b= map(Decimal, input().split())
    print(math.floor(a*b))


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
        input = """198 1.10"""
        output = """217"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 0.01"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000000000000000 9.99"""
        output = """9990000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
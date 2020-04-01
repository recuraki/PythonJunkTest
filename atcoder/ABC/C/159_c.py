import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    l = int(input())
    from decimal import Decimal
    d = Decimal(l) / Decimal(3)
    print(d*d*d)

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
        input = """3"""
        output = """1.000000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """999"""
        output = """36926037.000000000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100"""
        output = """36926037.000000000000"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
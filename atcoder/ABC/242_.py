import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    pass

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
        input = """30 500 20 103"""
        output = """0.042553191489"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """50 500 100 1"""
        output = """1.000000000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 2 1 1000"""
        output = """0.000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
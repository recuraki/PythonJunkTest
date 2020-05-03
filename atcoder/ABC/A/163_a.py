import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    print(2*n*3.14159265)

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
        output = """6.28318530717958623200"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """73"""
        output = """458.67252742410977361942"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
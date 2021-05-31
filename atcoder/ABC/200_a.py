import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    print((n-1)//100 + 1)

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
        input = """2021"""
        output = """21"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """200"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
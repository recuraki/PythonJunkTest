import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    a, b = map(int, input().split())
    print(32 ** (a-b))

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
        input = """6 4"""
        output = """1024"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 5"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
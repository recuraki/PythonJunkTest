
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    s = input()
    print(s[1] + s[2])

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
        input = """254"""
        output = """54"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """101"""
        output = """01"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
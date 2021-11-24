import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    s = input()
    print(s.zfill(4))

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
        input = """321"""
        output = """0321"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7777"""
        output = """7777"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1"""
        output = """0001"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
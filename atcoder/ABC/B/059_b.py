import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a = int(input())
    b = int(input())
    if a > b:
        print("GREATER")
    elif a < b:
        print("LESS")
    else:
        print("EQUAL")


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
        input = """36
24"""
        output = """GREATER"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """850
3777"""
        output = """LESS"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """9720246
22516266"""
        output = """LESS"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """123456789012345678901234567890
234567890123456789012345678901"""
        output = """LESS"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
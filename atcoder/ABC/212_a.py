import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    a, b = map(int, input().split())
    if 0 < a and  b == 0: print("Gold")
    elif a == 0 and 0 < b: print("Silver")
    else: print("Alloy")


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
        input = """50 50"""
        output = """Alloy"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """100 0"""
        output = """Gold"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 100"""
        output = """Silver"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """100 2"""
        output = """Alloy"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
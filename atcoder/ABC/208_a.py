import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = map(int, input().split())
    if a<= b <= (6*a):
        print("Yes")
    else:
        print("No")

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
        input = """2 11"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 13"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100 600"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x = int(input())
    if 400 <= x <= 599:
        print(8)
    elif 600 <= x <= 799:
        print(7)
    elif 800 <= x <= 999:
        print(6)
    elif 1000 <= x <= 1199:
        print(5)
    elif 1200 <= x <= 1399:
        print(4)
    elif 1400 <= x <= 1599:
        print(3)
    elif 1600 <= x <= 1799:
        print(2)
    elif 1800 <= x <= 1999:
        print(1)

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
        input = """725"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1600"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
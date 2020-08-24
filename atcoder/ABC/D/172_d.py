import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n,x = int(input()),0
    x = (1+n) * n - 1
    for i in range(2, (n // 2) + 1):
        x += i * ( (1 + n // i) * (n // i) // 2 - 1)
    print(x)


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
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """100"""
        output = """26879"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10000000"""
        output = """838627288460105"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
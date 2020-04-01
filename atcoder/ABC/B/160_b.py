import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x = int(input())
    a = x // 500
    x -= 500 * a
    b = x // 5
    print(a * 1000 + b * 5)


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
        input = """1024"""
        output = """2020"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000000000"""
        output = """2000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
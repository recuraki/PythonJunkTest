import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

    def resolve():
    n = int(input())
    import math
    x = math.floor(1.08 * n)
    if x < 206:
        print("Yay!")
    elif x== 206:
        print("so-so")
    else:
        print(":(")

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
        input = """180"""
        output = """Yay!"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """200"""
        output = """:("""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """191"""
        output = """so-so"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
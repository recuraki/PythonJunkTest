
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = map(int, input().split())
    xx = a + b
    x = xx // 2
    y = a - x
    print(x,y)

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
        input = """2 -2"""
        output = """0 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 1"""
        output = """2 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
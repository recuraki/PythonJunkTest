import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, a, x, y = map(int, input().split())
    res = n * x - (x-y) * max(0, n - a)
    print(res)

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
        input = """5 3 20 15"""
        output = """90"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 10 100 1"""
        output = """1000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
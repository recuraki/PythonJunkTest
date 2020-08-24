import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    if n < 30000:
        print(0)
    elif 30000<=n<100000:
        print(1)
    elif 100000<=n<200000:
        print(2)
    else:
        print(3)

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
        input = """1000"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2262943"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
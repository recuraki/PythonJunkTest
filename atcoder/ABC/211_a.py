import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = map(int, input().split())
    print((a-b)/ 3 + b)

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
        input = """130 100"""
        output = """110"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """300 50"""
        output = """133.3333333"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """123 123"""
        output = """123"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x,y,z = map(int, input().split())
    print(z, x, y)

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
        input = """1 2 3"""
        output = """3 1 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """100 100 100"""
        output = """100 100 100"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """41 59 31"""
        output = """31 41 59"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
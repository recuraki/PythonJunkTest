import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    r,g,b = map(int, input().split())
    if (r*100 + g * 10 + b) % 4 == 0:
        print("YES")
    else:
        print("NO")

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
        logging.info("test_input_1")
        input = """4 3 2"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """2 3 4"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
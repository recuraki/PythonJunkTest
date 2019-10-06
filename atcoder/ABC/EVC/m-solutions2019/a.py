import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    print(180 * (n-2))

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
        input = """3"""
        output = """180"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """100"""
        output = """17640"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
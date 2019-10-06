import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,x = map(int, input().split())
    na = (a - 1)// x + 1
    nb = b // x + 1
    print(nb - na)

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
        input = """4 8 2"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """0 5 1"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """9 9 2"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        logging.info("test_input_4")
        input = """1 1000000000000000000 3"""
        output = """333333333333333333"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_x = list(map(int, input().split()))
    print(max(dat_x) - min(dat_x))

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
        input = """4
2 3 7 9"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """8
3 1 4 1 5 9 2 6"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    n = int(input())
    curnum = 1
    curmax = 0
    for i in range(1, n + 1):
        c = int(math.log2(i))
        if c > curmax:
            curmax = c
            curnum = i
    print(curnum)


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
        input = """7"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """32"""
        output = """32"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_4(self):
        logging.info("test_input_4")
        input = """100"""
        output = """64"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
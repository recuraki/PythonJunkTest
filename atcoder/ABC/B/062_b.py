import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h, w = map(int, input().split())
    print("#" * (w + 2))
    for i in range(h):
        print("#" + input() + "#")
    print("#" * (w + 2))


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
        input = """2 3
abc
arc"""
        output = """#####
#abc#
#arc#
#####"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """1 1
z"""
        output = """###
#z#
###"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
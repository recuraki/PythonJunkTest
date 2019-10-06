import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    for i in range(0, len(s), 2):
        print(s[i], end="")
    print("")


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
        input = """atcoder"""
        output = """acdr"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """aaaa"""
        output = """aa"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """z"""
        output = """z"""
        self.assertIO(input, output)
    def test_input_4(self):
        logging.info("test_input_4")
        input = """fukuokayamaguchi"""
        output = """fkoaaauh"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
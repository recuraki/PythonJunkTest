import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c = map(int, input().split())
    print("Yes" if min(a, b) < c and c < max(a, b) else "No")


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
        input = """3 8 5"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """7 3 1"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """10 2 4"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_4(self):
        logging.info("test_input_4")
        input = """31 41 59"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
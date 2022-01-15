import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    n = int(input())
    if n < 42:
        print("AGC" + str(n).zfill(3))
    else:
        print("AGC" + str(n+1).zfill(3))


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
        input = """42"""
        output = """AGC043"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """19"""
        output = """AGC019"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1"""
        output = """AGC001"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """50"""
        output = """AGC051"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
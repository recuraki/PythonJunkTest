import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    s = input()
    for i in range(6):
        print(s[i % len(s)], end="")
    print()


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
        input = """abc"""
        output = """abcabc"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """zz"""
        output = """zzzzzz"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
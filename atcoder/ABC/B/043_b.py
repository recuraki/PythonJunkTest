import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    res = ""
    for i in range(len(s)):
        if s[i] == "0":
            res = res + "0"
        if s[i] == "1":
            res = res + "1"
        if s[i] == "B":
            res = res[:-1]
    print(res)

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
        input = """01B0"""
        output = """00"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0BB1"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
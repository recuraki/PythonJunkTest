import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    c0 = 0
    c1 = 0
    for i in range(len(s)):
        if s[i] == "1":
            c1 += 1
        else:
            c0 += 1

    if len(s) == 1:
        print(0)
    else:
        print(min(c0, c1) * 2)


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
        input = """0011"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """11011010001011"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
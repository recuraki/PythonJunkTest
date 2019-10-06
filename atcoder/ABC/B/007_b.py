import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    if s != "a":
        print("a")
    else:
        print("-1")

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """xyz"""
        output = """xy"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """c"""
        output = """b"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """a"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """aaaaa"""
        output = """aaaa"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
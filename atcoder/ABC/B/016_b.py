import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c = map(int, input().split())
    if c == a+b and c == a-b:
        print("?")
    elif c == a + b:
        print("+")
    elif c == a - b:
        print("-")
    else:
        print("!")

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
        input = """1 0 1"""
        output = """?"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """1 1 2"""
        output = """+"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """1 1 0"""
        output = """-"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """1 1 1"""
        output = """!"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = input().split()
    print(int(a+b) * 2)

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
        input = """1 23"""
        output = """246"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """999 999"""
        output = """1999998"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
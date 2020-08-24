import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x = int(input())
    print(x+x*x+x*x*x)

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
        input = """2"""
        output = """14"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10"""
        output = """1110"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
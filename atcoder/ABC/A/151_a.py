import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    c = input()
    print(chr(ord(c[0]) + 1))

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
        input = """a"""
        output = """b"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """y"""
        output = """z"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
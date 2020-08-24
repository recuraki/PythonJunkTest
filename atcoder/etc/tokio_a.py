import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    print(s[:3])

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
        input = """takahashi"""
        output = """tak"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """naohiro"""
        output = """nao"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
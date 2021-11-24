import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    d = set()
    d.add("ABC")
    d.add("ARC")
    d.add("AGC")
    d.add("AHC")
    d.discard(input())
    d.discard(input())
    d.discard(input())
    for k in d:
        print(k)

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
        input = """ARC
AGC
AHC"""
        output = """ABC"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """AGC
ABC
ARC"""
        output = """AHC"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
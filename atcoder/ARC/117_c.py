import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        n =
    do()

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
        input = """3
BWR"""
        output = """W"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
RRBB"""
        output = """W"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
BWWRBW"""
        output = """B"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """8
WWBRBBWB"""
        output = """R"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """21
BWBRRBBRWBRBBBRRBWWWR"""
        output = """B"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
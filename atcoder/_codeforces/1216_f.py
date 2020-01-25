import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


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
        input = """5 2
00100"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 1
000000"""
        output = """21"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 1
0011"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """12 6
000010000100"""
        output = """15"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
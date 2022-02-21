import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    pass

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
        input = """6 2
1 2 1 2 2 2
2 3
1 4"""
        output = """6 2
5 6
4 5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 1
1 1 1 1 4
2 3"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 0
3 3 3 3"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
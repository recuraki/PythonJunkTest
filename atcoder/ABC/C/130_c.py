import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    w,h,x,y = map(int, input().split())
    out1 = w * h / 2
    out2 = 1 if x == w/2 and y == h/2 else 0
    print("{0} {1}".format(str(out1), str(out2)))


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
        input = """2 3 1 2"""
        output = """3.000000 0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2 1 1"""
        output = """2.000000 1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_2")
        input = """3 3 1 1"""
        output = """3.500000 1"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_2")
        input = """3 4 1 2"""
        output = """3.500000 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
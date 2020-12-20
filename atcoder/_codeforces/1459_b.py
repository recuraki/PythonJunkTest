import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    n = int(input())
    if n & 1 == 0:
        x = n // 2
        x += 1
        print(x*x)
    else:
        x = n // 2 + 1
        print((x + x + 1) * x + x)





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
        input = """1"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """4"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_4")
        input = """5"""
        output = """24"""
        self.assertIO(input, output)

    def test_input_6(self):
        print("test_input_6")
        input = """6"""
        output = """16"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
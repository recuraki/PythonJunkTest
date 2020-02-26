import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n,a,b = map(int, input().split())
    if a > b:
        print(0)
    elif a==b:
        print(1)
    elif n == 1 and a!=b:
        print(0)
    elif n == 1:
        print(1)
    elif n == 2:
        print(1)
    else:
        c1 = a * n + (b-a)
        c2 = b * n - (b-a)
        print(c2-c1 + 1)

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
        input = """4 4 6"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 4 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 7 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1 3 3"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
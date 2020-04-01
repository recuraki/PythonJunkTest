import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h, w = map(int,input().split())
    if h == 1 or w == 1:
        print(1)
    elif h%2 == 1 and w % 2 ==1:
        print(h*w // 2 + 1)
    else:
        print(h*w // 2 )

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
        input = """4 5"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 3"""
        output = """11"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000000000 1000000000"""
        output = """500000000000000000"""
        self.assertIO(input, output)
    def test_input_13(self):
        print("test_input_3")
        input = """1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_311(self):
        print("test_input_3")
        input = """1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_3111(self):
        print("test_input_3")
        input = """2 2"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
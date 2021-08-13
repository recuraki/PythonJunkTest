import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        a,b = map(int, input().split())
        c = a + b
        if c >= 15 and b >= 8:
            print(1)
            return
        if c >= 10 and b >= 3:
            print(2)
            return
        if c >= 3:
            print(3)
            return
        print(4)
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
        input = """10 8"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 2"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 0"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
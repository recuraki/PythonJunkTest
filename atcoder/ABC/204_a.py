import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        x,y = map(int, input().split())
        if x == y:
            print(x)
            return
        dat = [x,y]
        if 0 not in dat:
            print(0)
            return
        if 1 not in dat:
            print(1)
            return
        if 2 not in dat:
            print(2)
            return
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
        input = """0 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
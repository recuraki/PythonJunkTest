import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        for x in range(1, 100 + 1):
            if (n + x) % 100 == 0:
                print(x)
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
        input = """140"""
        output = """60"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1000"""
        output = """100"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """99"""
        output = """1"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
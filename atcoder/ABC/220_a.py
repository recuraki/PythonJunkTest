import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    INF = 1 << 63
    def do():
        a, b, c = map(int, input().split())
        if (a%c==0): print(a)
        elif (b//c-a//c>2) print()
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
        input = """123 456 100"""
        output = """200"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """630 940 314"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
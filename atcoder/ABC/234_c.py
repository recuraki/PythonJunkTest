import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n = int(input())
        s = bin(n)[2:].replace("1", "2")
        print(s)

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
        input = """3"""
        output = """22"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """11"""
        output = """2022"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """923423423420220108"""
        output = """220022020000202020002022022000002020002222002200002022002200"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
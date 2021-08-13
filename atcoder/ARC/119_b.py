import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        import collections
        n = int(input())
        s = list(map(int, list(input())))
        t = list(map(int, list(input())))
        same = 0
        for i in range(n):
            if s[i] == t[i]:
                same += 1
        print(n-same)

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
        input = """7
1110110
1010111"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20
11111000000000011111
11111000000000011111"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
111100
111000"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """119
10101111011101001011111000111111101011110011010111111111111111010111111111111110111111110111110111101111111111110111011
11111111111111111111111111011111101011111011110111110010100101001110111011110111111111110010011111101111111101110111011"""
        output = """22"""
        self.assertIO(input, output)
    def test_input_13(self):
        print("test_input_13")
        input = """3
001
100"""
        output = """2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
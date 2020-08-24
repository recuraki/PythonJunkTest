import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
    else:
        dat = list(map(int, input().split()))

        for i in range(200):
            a = x - i
            if a not in dat:
                print(a)
                break
            a = x + i
            if a not in dat:
                print(a)
                break

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
        input = """6 5
4 7 10 6 5"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 5
4 7 10 6 5"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100 0"""
        output = """100"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
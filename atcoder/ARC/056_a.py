import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, k, l = map(int, input().split())
    sval = min(b, a*l)
    res = 0
    # まず、l個以内まで買う
    lnum = k // l
    res += sval * lnum
    res += min(b, a* (k % l))
    print(res)

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """3 7 10 3"""
        output = """24"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """4 5 11 3"""
        output = """20"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """3 8 3 3"""
        output = """8"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """3 8 2 3"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
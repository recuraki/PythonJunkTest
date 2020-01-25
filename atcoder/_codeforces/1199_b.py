import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h, l = map(int, input().split())
    res = l*l
    res -= h*h
    res /= 2*h
    print(res)





class TestClass(unittest.TestCase):
    maxDiff = 100000
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
        input = """1 2"""
        output = """1.5000000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5"""
        output = """2.6666666666667"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
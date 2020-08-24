import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x, k, d = map(int, input().split())
    x = abs(x)
    a = x // d
    a = min(k, a)
    k -= a
    x -= (d*a)
    if k == 0:
        print(x)
    else:
        y = abs(x - d)
        if k &1 == 0:
            print(x)
        else:
            print(y)




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
        input = """6 2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 4 3"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 1 2"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1000000000000000 1000000000000000 1000000000000000"""
        output = """1000000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
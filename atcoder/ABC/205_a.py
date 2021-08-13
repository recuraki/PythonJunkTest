import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        from fractions import Fraction
        a, b = map(int, input().split())
        tani = Fraction(a, 100)
        print(float(tani * b))


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
        input = """45 200"""
        output = """90"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """37 450"""
        output = """166.5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 1000"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """50 0"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
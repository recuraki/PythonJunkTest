import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    a, b, w = map(int, input().split())
    w *= 1000
    valma = w / a
    valmi = w / b
    x = math.ceil(valmi)
    y = math.floor(valma)
    print(valmi, valma, x, y)
    if x > y:
        print("UNSATISFIABLE")
    else:
        print(x,y)

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
        input = """100 200 2"""
        output = """10 20"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """120 150 2"""
        output = """14 16"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """300 333 1"""
        output = """UNSATISFIABLE"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
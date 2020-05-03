
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    a,b,c,d = map(int, input().split())
    x = math.ceil(c / b)
    y = math.ceil(a / d)
    if x > y:
        print("No")
    else:
        print("Yes")

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
        input = """10 9 10 10"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """46 4 40 5"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
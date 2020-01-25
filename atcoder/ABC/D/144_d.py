import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, x = map(int, input().split())
    import math
    s = x / a
    ss = s / a
    print(math.degrees(math.atan()))


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
        input = """2 2 4"""
        output = """45.0000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """12 21 10"""
        output = """89.7834636934"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 1 8"""
        output = """4.2363947991"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
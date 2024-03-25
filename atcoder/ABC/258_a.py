import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    n = int(input())
    a = 21 + n // 60
    b = str(n % 60)
    b = b.zfill(2)
    print("{0}:{1}".format(a,b))

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
        input = """63"""
        output = """22:03"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """45"""
        output = """21:45"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100"""
        output = """22:40"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_3")
        input = """60"""
        output = """22:00"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
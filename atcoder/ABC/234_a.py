import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    t = int(input())
    print(1371+t*(40+t*(29+2*t*(5+t)))*(74+t*(40+t*(29+2*t*(5+t)))))





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
        input = """0"""
        output = """1371"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3"""
        output = """722502"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10"""
        output = """1111355571"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
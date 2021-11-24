import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    n = int(input())
    if n >= 90: print("expert")
    elif 70 <= n < 90: print(90-n)
    elif 40 <= n < 70: print(70-n)
    else: print(40-n)



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
        input = """56"""
        output = """14"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """32"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0"""
        output = """40"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """100"""
        output = """expert"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    print((pow(10, n, m*m) // m) % m)

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
        input = """1 2"""
        output = """1"""
        #self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 7"""
        output = """0"""
        #self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000000000000000000 9997"""
        output = """9015"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
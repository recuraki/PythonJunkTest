import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b = map(int,input().split())
    b *= 100
    a*=100
    x = b/a
    print( (1-x)*100 )

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
        input = """100 80"""
        output = """20.0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 6"""
        output = """14.285714285714285714"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """99999 99998"""
        output = """0.00100001000010000100"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
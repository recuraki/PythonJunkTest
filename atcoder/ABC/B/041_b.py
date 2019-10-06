import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c = map(int, input().split())
    print(a%1000000007 * b%1000000007*c%1000000007)

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """2 3 4"""
        output = """24"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """10000 1000 100"""
        output = """1000000000"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """100000 1 100000"""
        output = """999999937"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """1000000000 1000000000 1000000000"""
        output = """999999664"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 1000000007
    n = int(input())
    res = 1
    for i in range(1,n+1):
        res *= i
        res %= mod
    print(res)


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
        input = """3"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10"""
        output = """3628800"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100000"""
        output = """457992974"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
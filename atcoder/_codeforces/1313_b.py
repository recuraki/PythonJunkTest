import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def dp(s):
        if True:
            print(s)
    def dpp(s):
        if True:
            pprint(s)
    q = int(input())
    s = input()
    dat = list(map(int, input().split()))
    pass



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
        input = """1
5 1 3"""
        output = """1 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
6 3 4"""
        output = """2 6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
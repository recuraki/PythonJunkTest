import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    l = [[dat[i], i+1] for i in range(2**n)]
    print(min(max(l[:2**(n-1)]),max(l[2**(n-1):]))[1])



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
1 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
3 1 5 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
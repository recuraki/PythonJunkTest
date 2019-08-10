
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = input()
    import collections
    c = collections.Counter(s)
    num_balance = n // 3
    c0, c1, c2 = 0,0,0
    c0 = c["0"] - num_balance
    c1 = c["1"] - num_balance
    c2 = c["2"] - num_balance

    print("{0} {1} {2}: {3}".format(c0,c1,c2,s))


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
        input = """3
121"""
        output = """YES
021"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
000000"""
        output = """001122"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
211200"""
        output = """211200"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """6
120110"""
        output = """120120"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
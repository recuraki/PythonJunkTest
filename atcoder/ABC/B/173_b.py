import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = dict()
    dat["AC"] = 0
    dat["WA"] = 0
    dat["RE"] = 0
    dat["TLE"] = 0
    for i in range(n):
        s = input()
        dat[s] += 1
    print("AC x", dat["AC"])
    print("WA x", dat["WA"])
    print("TLE x", dat["TLE"])
    print("RE x", dat["RE"])



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
        input = """6
AC
TLE
AC
AC
WA
TLE"""
        output = """AC x 3
WA x 1
TLE x 2
RE x 0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
AC
AC
AC
AC
AC
AC
AC
AC
AC
AC"""
        output = """AC x 10
WA x 0
TLE x 0
RE x 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
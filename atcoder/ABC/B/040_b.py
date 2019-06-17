import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    res = 9999999999
    for i in range(1, n):
        amari = n % i
        sa = abs( (n // i) - i)
        sa = int(sa)
        #print("{3} {0} {1} {2} ".format(str(i), str(amari), str(sa), str(n)))
        res = min(res, amari+sa)
    if n == 1:
        res = 0
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
    def test_input1(self):
        print("test_input1")
        input = """1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """41"""
        output = """4"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """100000"""
        output = """37"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
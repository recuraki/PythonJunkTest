import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    import math
    res = 10 ** 18
    for b in range(1000):
        sumb = 2 ** b
        if sumb > n:
            break
        a = n // sumb
        c = n - (a*sumb)
        if a >= 0 and b >= 0 and c >= 0:
            res = min(res, a+b+c)
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
        input = """998244353"""
        output = """143"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1000000007"""
        output = """49483"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """998984374864432412"""
        output = """2003450165"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
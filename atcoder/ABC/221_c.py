import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    INF = 1 << 63
    def do():
        import math
        s = input()
        l = len(s)
        res = -1
        for pat in range(1, 2**l-1):
            a = ""
            b = ""
            for i in range(l):
                if (pat >> i & 1) == 1: b += s[i]
                else: a += s[i]
            a = list(a)
            b = list(b)
            a.sort(reverse=True)
            b.sort(reverse=True)
            a = "".join(a)
            b = "".join(b)
            #print(pat,a, b)
            res = max(res, int(a) * int(b))
        print(res)

    do()


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
        input = """123"""
        output = """63"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1010"""
        output = """100"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """998244353"""
        output = """939337176"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_3")
        input = """99"""
        output = """81"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
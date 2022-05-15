
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        s = input()
        if s == s.upper():
            print("No")
            return
        if s == s.lower():
            print("No")
            return
        from collections import defaultdict
        se = set()
        for x in s:
            se.add(x)
        if len(se) != len(s):
            print("No")
            return
        print("Yes")
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
        input = """AtCoder"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """Aa"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """atcoder"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """Perfect"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
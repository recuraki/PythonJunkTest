import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        dat = list(map(int, input().split()))
        i = 0
        for _ in range(3):
            i = dat[i]
        print(i)


    # 1 time
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
        input = """9 0 1 2 3 4 5 6 7 8"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 8 8 8 0 8 8 8 8 8"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 0 0 0 0 0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
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
    from collections import defaultdict

    def do():
        d = defaultdict(int)
        n = int(input())
        for _ in range(n):
            s = input()
            if s not in d:
                d[s] += 1
                print(s)
                continue
            print(s + "(" + str(d[s]) +")")
            d[s] += 1



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
        input = """5
newfile
newfile
newfolder
newfile
newfolder"""
        output = """newfile
newfile(1)
newfolder
newfile(2)
newfolder(1)"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """11
a
a
a
a
a
a
a
a
a
a
a"""
        output = """a
a(1)
a(2)
a(3)
a(4)
a(5)
a(6)
a(7)
a(8)
a(9)
a(10)"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
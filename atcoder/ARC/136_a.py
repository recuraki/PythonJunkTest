import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    import sys
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        s = input()
        l = list(s)
        newl = []
        for x in l:
            if x == "A":
                newl.append("B")
                newl.append("B")
            else:
                newl.append(x)
        l = newl
        i = 0
        ans = []
        n = len(l)
        while i < len(newl):
            if l[i] != "B":
                ans.append(l[i])
                i += 1
                continue
            # A!
            if i == n-1:
                ans.append(l[i])
                i+= 1
                continue
            if l[i+1] == "B":
                ans.append("A")
                i += 1
                i += 1
                continue
            ans.append(l[i])
            i+= 1

        print("".join(ans))

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
        input = """4
CBAA"""
        output = """CAAB"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
A"""
        output = """A"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
BBBCBB"""
        output = """ABCA"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
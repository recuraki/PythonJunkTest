import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    n = int(input())
    dat = []
    for _ in range(n):
        a, b = map(int, input().split())
        dat.append( (a**2 + b**2, a, b) )
    dat.sort()
    print(dat)
    _, x1, y1 = dat[0]
    _, x2, y2 = dat[-1]
    print(min(abs(x1-x2), abs(y1-y2)))




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
0 3
3 1
4 10"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
0 1
0 4
0 10
0 6"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
897 729
802 969
765 184
992 887
1 104
521 641
220 909
380 378"""
        output = """801"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
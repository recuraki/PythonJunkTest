import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    d = [0] * 5
    for i in range(n):
        s = input()
        if s[0] == "M":
            d[0] += 1
        if s[0] == "A":
            d[1] += 1
        if s[0] == "R":
            d[2] += 1
        if s[0] == "C":
            d[3] += 1
        if s[0] == "H":
            d[4] += 1
    import itertools
    res = 0
    for x  in list(itertools.combinations([0,1,2,3,4], 3)):
        res += d[x[0]] * d[x[1]] * d[x[2]]
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
        input = """5
MASHIKE
RUMOI
OBIRA
HABORO
HOROKANAI"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
ZZ
ZZZ
Z
ZZZZZZZZZZ"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
CHOKUDAI
RNG
MAKOTO
AOKI
RINGO"""
        output = """7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
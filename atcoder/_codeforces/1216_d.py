import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    n = int(input())
    dat = list(map(int, input().split()))
    dat_loss = []
    m = max(dat)
    nn = 0
    for i in range(n):
        if dat[i] != m:
            dat_loss.append(m - dat[i])
            nn += 1
    res = 0
    for i in range(nn):
        res = math.gcd(res, dat_loss[i])
    res2 = 0
    for i in range(nn):
        res2 += dat_loss[i] // res
    print("{0} {1}".format(res2, res))






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
3 12 6"""
        output = """5 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
2 9"""
        output = """1 7"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
2 1000000000 4 6 8 4 2"""
        output = """2999999987 2"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """6
13 52 0 13 26 52"""
        output = """12 13"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, x,y = map(int,input().split())
    dat = list(map(int, input().split()))
    rmin = 10000000000000000000
    lmax = 10000000000000000000
    def init():
        rmin = 10000000000000000000
        lmax = 10000000000000000000
    index = -1
    indexnum = -1
    mode = 0
    countr = 0
    countl = 0
    for i in range(n):
        if mode == 0 and countr == x:
            mode = 1
        elif mode == 1:
            pass
        else mode == 1 and
        if mode = 0:
            if dat[i] < rmin:
                count










class TestClass(unittest.TestCase):
    maxDiff = 100000
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
        input = """aa"""
        output = """aa"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """aa0"""
        output = """aa"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
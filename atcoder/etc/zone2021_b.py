import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, dd, hh = map(int, input().split())
    dat = []
    for i in range(n):
        d, h = map(int, input().split())
        dat.append( (d, h) )

    res = 0
    val = 0
    for d, h in dat:
        katamuki = (hh - h)  / (dd - d)
        #print(katamuki)
        #print(h, d, katamuki)
        val = h - (d * katamuki)
        #print(val)
        res = max(res, val)
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
        input = """1 10 10
3 5"""
        output = """2.857142857142857"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 10 10
3 2"""
        output = """0.0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 896 483
228 59
529 310
339 60
78 266
659 391"""
        output = """245.3080684596577"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
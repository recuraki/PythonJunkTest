import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    dat_d = []

    total = 0
    for i in range( n):
        total += (dat[i] - (i+1))
        dat_d.append(dat[i] - (i+1))

    #print(dat)
    #print(dat_d)
    #print(total)
    #f = (total // n)
    #print(f)

    dat_d.sort()
    #print(dat_d)
    f = dat_d[n//2]

    total = 0
    for i in range( n):
        total += abs(dat_d[i] - f)

    print(total)

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
2 2 3 5 5"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """9
1 2 3 4 5 6 7 8 9"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
6 5 4 3 2 1"""
        output = """18"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """7
1 1 1 1 2 3 4"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
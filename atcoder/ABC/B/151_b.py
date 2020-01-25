import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k, m = map(int, input().split())
    dat = list(map(int, input().split()))
    s = sum(dat)
    t = (m * n) - s
    #print("t={0}".format(t))
    if t < 0:
        print(0)
    elif k >= t:
        print(t)
    else:
        print(-1)


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
        input = """5 10 7
8 10 3 6"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 100 60
100 100 100"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 100 60
0 0 0"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
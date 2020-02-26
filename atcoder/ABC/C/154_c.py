import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    f = True
    d = dict()
    for i in range(len(dat)):
        if dat[i] in d:
            f = False
        d[dat[i]] = True
    print("YES" if f else "NO")

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
2 6 1 4 5"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
4 1 3 88 6 1"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
10000000 10000000"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
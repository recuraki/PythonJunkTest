import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        h, w = map(int, input().split())
        dat = []
        for _ in range(h):
            l = list(map(int, input().split()))
            dat.append(l)

        for i1 in range(h):
            for i2 in range(i1+1, h):
                for j1 in range(w):
                    for j2 in range(j1 + 1, w):
                        if dat[i1][j1] + dat[i2][j2] > dat[i2][j1] + dat[i1][j2]:
                            print("No")
                            return
        print("Yes")

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
        input = """3 3
2 1 4
3 1 3
6 4 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 4
4 3 2 1
5 6 7 8"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
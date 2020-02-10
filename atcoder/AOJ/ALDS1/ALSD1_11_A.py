import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    dat = []
    n = int(input())
    for i in range(n):
        dat.append([0] * n)
    for i in range(n):
        s = list(map(int, input().split()))
        for j in range(len(s) - 2):

            dat[i][s[j + 2] - 1] = 1
    for i in range(n):
        l = list(map(str, dat[i]))
        print(" ".join(l))

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
1 2 2 4
2 1 4
3 0
4 1 3"""
        output = """0 1 0 1
0 0 0 1
0 0 0 0
0 0 1 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
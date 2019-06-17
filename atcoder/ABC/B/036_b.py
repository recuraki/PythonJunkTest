import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_n = []

    for i in range(n):
        dat_n.append(input())

    for i in range(n):
        for j in range(n):
            print(dat_n[n-j-1 ][i], end="")
        print("")




class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """4
ooxx
xoox
xxxx
xxxx"""
        output = """xxxo
xxoo
xxox
xxxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
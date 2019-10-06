import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    dat_h = []
    for i in range(n):
        dat_h.append(int(input()))
    dat_h.sort(reverse=True)
    res = 100000000000
    for i in range(n-k+1):
        res = min(res, dat_h[i] - dat_h[i+k-1])
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
        input = """5 3
10
15
11
14
12"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 3
5
7
5
7
7"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    n, q, k = map(int, input().split())
    dat = list(map(int, input().split()))
    for i in range(q):
        l, r = map(lambda x: int(x) - 1, input().split())
        print( (dat[l] - 1) + (k - dat[r]) + (dat[r] - dat[l] - (r-l) ) * 2 )



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
        input = """4 2 5
1 2 4 5
2 3
3 4"""
        output = """4
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 5 10
2 4 6 7 8 9
1 4
1 2
3 5
1 6
5 5"""
        output = """8
9
7
6
9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_t = list(map(int, input().split()))
    m = int(input())
    dat_d = []
    s = sum(dat_t)
    for i in range(m):
        p,x = map(int, input().split())
        print(s - dat_t[p - 1] + x)


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
        input = """3
2 1 4
2
1 1
2 3"""
        output = """6
9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
7 2 3 8 5
3
4 2
1 7
4 13"""
        output = """19
25
30"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
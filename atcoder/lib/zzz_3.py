import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    datn = list(map(int, input().split()))
    m = int(input())
    datm = list(map(int, input().split()))
    import collections
    d = collections.defaultdict(int)
    for i in range(n):
        d[datn[i]] += 1
    f = True
    for j in range(m):
        c = d[datm[j]]
        if c == 0:
            f = False
        d[datm[j]] -= 1
    print("YES" if f  else "NO")



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
3 1 4 1 5
3
5 4 3"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
100 200 500 700 1200 1600 2000
6
100 200 500 700 1600 1600"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1
800
5
100 100 100 100 100"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """15
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
9
5 4 3 2 1 2 3 4 5"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
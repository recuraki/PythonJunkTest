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
        n, q = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort()
        from bisect import bisect_left
        for _ in range(q):
            x = int(input())
            ind = bisect_left(dat, x)
            print(n - ind)


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
        input = """3 1
100 160 130
120"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 5
1 2 3 4 5
6
5
4
3
2"""
        output = """0
1
2
3
4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 5
804289384 846930887 681692778 714636916 957747794
424238336
719885387
649760493
596516650
189641422"""
        output = """5
3
5
5
5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
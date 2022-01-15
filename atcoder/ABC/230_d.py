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
        n, d = map(int, input().split())
        dat = []
        for _ in range(n):
            l, r = map(int, input().split())
            dat.append( (l, r) )
        dat.sort(key=lambda x: x[1])
        ans = 0
        reach = -1
        for l, r in dat:
            #print(l, r, "r", reach)
            if l <= reach: continue
            ans += 1
            reach = r + d - 1
        print(ans)
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
1 2
4 7
5 9"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3
1 2
4 7
4 9"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 2
1 100
1 1000000000
101 1000
9982 44353
1000000000 1000000000"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """5 1
1 1
2 2
3 3
4 4
5 5"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
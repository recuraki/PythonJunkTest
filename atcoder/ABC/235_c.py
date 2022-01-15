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
        querys = []
        for _ in range (q):
            x, k = map(int, input().split())
            querys.append( (x, k) )
        from collections import defaultdict
        buf = defaultdict(list)
        for i in range(n):
            x = dat[i]
            buf[x].append(i+1)
        for x, k in querys:
            if x not in buf:
                print(-1)
                continue
            if k > len(buf[x]):
                print(-1)
                continue
            print(buf[x][k-1])


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
        input = """6 8
1 1 2 3 1 2
1 1
1 2
1 3
1 4
2 1
2 2
2 3
4 1"""
        output = """1
2
5
-1
3
6
-1
-1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2
0 1000000000 999999999
1000000000 1
123456789 1"""
        output = """2
-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
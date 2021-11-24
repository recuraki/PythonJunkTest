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
    from decimal import Decimal
    def do():
        n = int(input())
        dat = []
        for _ in range(n):
            x, y = map(int, input().split())
            dat.append( (x, y) )
        res = 0
        for i in range(n):
            x1, y1 = dat[i]
            for j in range(i+1, n):
                x2, y2 = dat[j]
                for k in range(j+1, n):

                    x3, y3 = dat[k]
                    x1 -= x3
                    x2 -= x3
                    y1 -= y3
                    y2 -= y3
                    if x1 * y2 == x2 * y1:
                        continue
                    res += 1

        print(res)


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
        input = """4
0 1
1 3
1 1
-1 -1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20
224 433
987654321 987654321
2 0
6 4
314159265 358979323
0 0
-123456789 123456789
-1000000000 1000000000
124 233
9 -6
-4 0
9 5
-7 3
333333333 -333333333
-9 -1
7 -10
-1 5
324 633
1000000000 -1000000000
20 0"""
        output = """1124"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
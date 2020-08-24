import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys

    import itertools
    def countstrs(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]
    import math

    q = int(input())
    for _ in range(q):
        n,k = map(int, input().split())
        s = input()

        res = 0

        dat = countstrs(s)
        #print(dat)
        l = len(dat)
        for i in range(l):
            ignoreLeft = False
            ignoreRight = False
            if i == 0:
                ignoreLeft = True
            if i == (l-1):
                ignoreRight = True

            if dat[i][0] == "1":
                continue

            cnt = dat[i][1]
            if ignoreRight is False:
                cnt -= (k)
            if ignoreLeft is False:
                cnt -= (k)

            #print("space", cnt)
            if cnt <= 0:
                continue

            res += math.ceil(cnt / (k+1))

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
        input = """6
6 1
100010
6 2
000000
5 1
10101
3 1
001
2 2
00
1 100
0"""
        output = """1
2
0
1
1
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
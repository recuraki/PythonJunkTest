import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():




    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        _ = input()
        n, d = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.append(0)
        n += 1
        dat.sort()
        mi = INF
        ma = -INF

        for i in range(n-1):
            mi = min(mi, dat[i+1] - dat[i] - 1)
            ma = max(ma, dat[i + 1] - dat[i] - 1)
            #print("!!!", i, dat[i+1] - dat[i] - 1)
        ans = mi
        cnt = 0
        miind = -1
        maind = -1
        mican = []
        for i in range(n-1):
            if mi == (dat[i+1] - dat[i] - 1):
                cnt += 1
                miind = i # track
                mican.append(i)
            if ma == (dat[i+1] - dat[i] - 1):
                maind = i # track

        if cnt > 1:
            miind = mican[-1]

        from copy import deepcopy
        odat = deepcopy(dat)


        #print("!0 ", mi)

        # if move to other pos
        if miind != 0:
            dat[miind] = (dat[maind+1] + dat[maind]) // 2
            dat.sort()
            mi = INF
            for i in range(n-1):
                mi = min(mi, dat[i+1] - dat[i] - 1)
            ans = max(ans, mi)
            dat = deepcopy(odat)

        dat[miind+1] = (dat[maind+1] + dat[maind]) // 2
        dat.sort()
        #print(dat)
        mi = INF
        for i in range(n-1):
            mi = min(mi, dat[i+1] - dat[i] - 1)
        ans = max(ans, mi)
        dat = deepcopy(odat)


        #print("!1", mi)

        # if move to neightbor # _ N _ _ _ Y Y _ _ _ _ N _
        if miind != 0: # can move aida
            dat[miind] = (dat[miind-1] + dat[miind+1]) // 2
            dat.sort()
            mi = INF
            for i in range(n-1):
                mi = min(mi, dat[i+1] - dat[i] - 1)
            ans = max(ans, mi)
            dat = deepcopy(odat)
        #print("!2", mi)

        if (miind+1) != n-1: # can move aida
            dat[miind+1] = (dat[miind] + dat[miind+2]) // 2
            dat.sort()
            mi = INF
            for i in range(n-1):
                mi = min(mi, dat[i+1] - dat[i] - 1)
            ans = max(ans, mi)
            dat = deepcopy(odat)
        #print("!3", mi)


        if dat[-1] != d:
            dat[miind+1] = d
            dat.sort()
            mi = INF
            for i in range(n-1):
                mi = min(mi, dat[i+1] - dat[i] - 1)
            ans = max(ans, mi)
            dat = deepcopy(odat)

        if dat[-1] != d and miind != 0:
            dat[miind] = d
            dat.sort()
            mi = INF
            for i in range(n-1):
                mi = min(mi, dat[i+1] - dat[i] - 1)
            ans = max(ans, mi)
            dat = deepcopy(odat)

        print(ans)





    # n questions
    q = int(input())
    for _ in range(q):
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
        input = """9

3 12
3 5 9

2 5
1 5

2 100
1 2

5 15
3 6 9 12 15

3 1000000000
1 400000000 500000000

2 10
3 4

2 2
1 2

4 15
6 11 12 13

2 20
17 20"""
        output = """2
1
1
2
99999999
3
0
1
9"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_1")
        input = """1

2 100
1 2
"""
        output = """3"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import math

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    from bisect import bisect_left, bisect_right
    def do():
        import itertools
        squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)
        def createSDAT(l):
            return list(itertools.accumulate(itertools.chain([0], l)))

        n, qs = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort()
        sdat = createSDAT(dat)
        can = dict()
        from collections import deque
        q = deque([])
        total = squery(0, n)
        q.append([0, n, total])
        #print(q)

        #print(dat)
        while len(q) > 0:
            l, r, total = q.popleft()
            #print(l, r, total)
            can[total] = True
            lval, rval = dat[l], dat[r - 1]
            if lval == rval:
                continue
            mid = math.floor( (rval + lval) / 2)
            midind = bisect_right(dat, mid, lo=l, hi=r)
            rtotal = total - squery(l, midind)
            ltotal = total - squery(midind, r)
            q.append([l, midind, ltotal])
            q.append([midind, r, rtotal])
        #print(can)

        for qq in range(qs):
            ss = int(input())
            if ss in can:
                print("Yes")
            else:
                print("No")


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
        input = """2
5 5
1 2 3 4 5
1
8
9
12
6
5 5
3 1 3 1 3
1
2
3
9
11"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
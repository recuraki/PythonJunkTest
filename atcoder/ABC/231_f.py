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
        class BinaryIndexTreeSum:
            #
            # BE
            #
            def __init__(self, n):
                self.size = n
                self.tree = [0] * (n + 1)

            def sum(self, i):
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & -i
                return s

            def add(self, i, x):
                while i <= self.size:
                    self.tree[i] += x
                    i += i & -i

        n = int(input())
        dddata = list(map(int, input().split()))
        dddatb = list(map(int, input().split()))
        dat = []
        for i in range(n):
            dat.append( (dddata[i], dddatb[i]) )
        import collections
        c = collections.Counter(dat)
        dat = []
        for k in c.keys():
            dat.append( (k[0], k[1], c[k]) )
        dat.sort(key=lambda x: (x[0], -x[1]))
        #print(dat)
        datb = []

        for a, b, cnt in dat:
            datb.append(b)
        #print(datb)

        zatsu = sorted(set(datb))
        zatsuTable = dict()
        zatsuTableRev = dict()
        for ind, value in enumerate(zatsu):
            zatsuTable[value] = ind
            zatsuTableRev[ind] = value
        newl = []
        for x in datb:
            newl.append(zatsuTable[x])
        #print(datb)
        #print(newl)
        bit = BinaryIndexTreeSum(n+1)
        ans = 0
        for i in range(len(dat)): # sortしたdatに従って処理
            a, b, cnt = dat[i]
            b = zatsuTable[b] + 1# 座標圧縮後に変換
            bit.add(b, cnt)
            #print("add", b, 1)
            can = bit.sum(n) - bit.sum(b-1)
            #print(i, can,)
            ans += can * cnt
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
        input = """3
50 100 150
1 3 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
123456789 123456 123
987 987654 987654321"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
3 1 4 1 5 9 2 6 5 3
2 7 1 8 2 8 1 8 2 8"""
        output = """37"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
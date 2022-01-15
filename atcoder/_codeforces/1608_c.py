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
    class sparseTable(object):
        func = None
        depthTreeList: int = 0
        table = []

        def __init__(self):
            self.table = []
            self.depthTreeList = 0

        def load(self, l):
            self.n = len(l)
            self.depthTreeList = (self.n - 1).bit_length()  # Level
            self.table.append(l)
            for curLevel in range(1, self.depthTreeList):
                l = []
                for i in range(self.n - (2 ** curLevel - 1)):
                    l.append(
                        self.func(self.table[curLevel - 1][i], self.table[curLevel - 1][i + (2 ** (curLevel - 1))]))
                self.table.append(l)

        def query(self, l, r):  # [l, r)
            diff = r - l
            if diff <= 0:
                raise
            if diff == 1:
                return self.table[0][l]
            level = (diff - 1).bit_length() - 1
            return self.func(self.table[level][l], self.table[level][r - (2 ** level)])

    class sparseTableMax(sparseTable):
        func = max

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        dat = []
        for i in range(n):
            dat.append( (data[i], datb[i], i) )
        dat.sort()
        #print(dat)
        buf = []
        for a, b, i in dat:
            buf.append(b)
        st = sparseTableMax()
        st.load(buf)
        ans = [None] * n
        print(dat)
        ans[dat[-1][2]] = "1"
        print(ans)
        for i in range(n - 1):
            a, b, ind = dat[i]
            teki = st.query(ind + 1, n)
            print(a,b, ind, teki)
            if b > teki:
                ans[ind] = "1"
            else:
                ans[ind] = "0"
        print("".join(ans))


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
        input = """3
4
1 2 3 4
1 2 3 4
4
11 12 20 21
44 22 11 30
1
1000000000
1000000000"""
        output = """0001
1111
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
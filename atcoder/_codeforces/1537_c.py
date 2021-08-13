import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        n = int(input())
        l = list(map(int, input().split()))
        class cumSum1D(object):
            sdat = []

            def init(self):
                pass

            def load(self, l):
                import itertools
                self.sdat = list(itertools.accumulate(itertools.chain([0], l)))

            def query(self, l, r):
                """
                query [l, r)
                """
                # assert l < r
                return self.sdat[r] - self.sdat[l]

        l.sort()
        dan = []
        for i in range(n - 1):
            if l[i + 1] > l[i]:
                dan.append(1)
            else:
                dan.append(0)
        st = cumSum1D()
        st.load(dan)
        #print(st.sdat)
        mindiff = 10**18
        minmax = -1
        for i in range(n - 1):
            x = st.query(0, i)
            y = st.query(i + 1, n - 1)
            #print(x, y, x + y)
            diff = l[i+1] - l[i]
            if mindiff < diff:
                continue
            if mindiff > diff:
                mindiff = diff
                minmax = x+y
                res = (i, i+1)
                continue
            if minmax < (x+y):
                minmax = x + y
                res = (i, i+1)
        #print(mindiff, minmax, res)
        finalres = [l[res[0]]]  + l[res[1]+1:] + l[:res[0]]+  [l[res[1]]]
        print(" ".join(list(map(str, finalres))))

    q = int(input())
    for _ in range(q):
        do()
    # do()





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
4
4 2 1 2
2
3 1"""
        output = """2 4 1 2
1 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
5
3 3 4 5 6
"""
        output = """
"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
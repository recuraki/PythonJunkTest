
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

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


    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        s = dat[:k]
        init = dat[:k]
        nokori = dat[k:]
        nokorimax = max(nokori)
        ans = 1 << 61
        st = sparseTableMax()
        st.load(nokori)

        for i in range(k-1, -1, -1):
            a = dat[i]
            # この時成功しえない

            if nokorimax <= a: continue
            # [ok, ng) for max value
            # (ng, ok] for min value
            # CATION: ok is result  (NOT mid)
            ng = -1
            ok = len(nokori) - 1
            while (abs(ok - ng) > 1):
                mid = (ok + ng) // 2
                state = st.query(0, mid + 1) > a
                if state: ok = mid;
                else: ng = mid;
            if nokori[ok] <= ok:
                print("error")
                assert False
            bind = k + ok
            b = dat[bind]
            #print("a,b, aind, bind", a, nokori[ok], i, bind)
            dist = bind - i
            can = dist + dist - 1
            ans = min(ans, dist)
        if ans == 1<<61:
            print(-1)
            return
        else:
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
        input = """4 2
2 1 1 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 1
3 2 1"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20 13
90699850 344821203 373822335 437633059 534203117 523743511 568996900 694866636 683864672 836230375 751240939 942020833 865334948 142779837 22252499 197049878 303376519 366683358 545670804 580980054"""
        output = """13"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
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
        N = int(input())

        INF = 2 ** 31 - 1

        LV = (N - 1).bit_length()
        N0 = 2 ** LV
        data = [0] * (2 * N0)
        lazy = [0] * (2 * N0)

        def gindex(l, r):
            L = (l + N0) >> 1;
            R = (r + N0) >> 1
            lc = 0 if l & 1 else (L & -L).bit_length()
            rc = 0 if r & 1 else (R & -R).bit_length()
            for i in range(LV):
                if rc <= i:
                    yield R
                if L < R and lc <= i:
                    yield L
                L >>= 1;
                R >>= 1

        # 遅延伝搬処理
        def propagates(*ids):
            for i in reversed(ids):
                v = lazy[i - 1]
                if not v:
                    continue
                lazy[2 * i - 1] += v;
                lazy[2 * i] += v
                data[2 * i - 1] += v;
                data[2 * i] += v
                lazy[i - 1] = 0

        # 区間[l, r)にxを加算
        def update(l, r, x):
            *ids, = gindex(l, r)
            propagates(*ids)

            L = N0 + l;
            R = N0 + r
            while L < R:
                if R & 1:
                    R -= 1
                    lazy[R - 1] += x;
                    data[R - 1] += x
                if L & 1:
                    lazy[L - 1] += x;
                    data[L - 1] += x
                    L += 1
                L >>= 1;
                R >>= 1
            for i in ids:
                data[i - 1] = min(data[2 * i - 1], data[2 * i])

        # 区間[l, r)内の最小値を求める
        def query(l, r):
            propagates(*gindex(l, r))
            L = N0 + l;
            R = N0 + r

            s = INF
            while L < R:
                if R & 1:
                    R -= 1
                    s = min(s, data[R - 1])
                if L & 1:
                    s = min(s, data[L - 1])
                    L += 1
                L >>= 1;
                R >>= 1
            return s

        dat = list(map(int, input().split()))
        from heapq import heappop, heappush, heapify
        q = []
        cnt = 0
        for i in range(N):
            x = dat[i]
            if x >= 0:
                update(i, N, x)
                cnt += 1
            else:
                q.append( (-x, -i) )
        #print(q)
        heapify(q)

        while len(q) > 0:
            cost, ind = heappop(q)
            ind = -ind
            #print(cost, ind)
            aftermin = query(ind, N)
            if aftermin >= cost: # can fetch
                cnt += 1
                update(ind, N, -cost)
        print(cnt)



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
        input = """6
4 -4 1 -3 1 -3"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
9 -10 1 -1 1 -1"""
        output = """"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
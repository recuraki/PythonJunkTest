import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    INF = 1 << 63
    def do():


        dat = []
        n, m = map(int, input().split())

        INF = 2 ** 31 - 1
        LV = (n - 1+1).bit_length()
        N0 = 2 ** LV
        data = [0] * (2 * N0)
        lazy = [0] * (2 * N0)
        def gindex(l, r):
            L = (l + N0) >> 1;
            R = (r + N0) >> 1
            lc = 0 if l & 1 else (L & -L).bit_length()
            rc = 0 if r & 1 else (R & -R).bit_length()
            v = 2
            for i in range(LV):
                if rc <= i:
                    yield R
                if L < R and lc <= i:
                    yield L
                L >>= 1;
                R >>= 1;
                v <<= 1
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

        g = [[] for _ in range(n + 10)]
        for _ in range(m):
            a, b = map(int, input().split())
            g[a].append(b)

        for a in range(n+1):
            updatedata = []
            for b in g[a]:
                x = query(0, b) # bの一個手前までの最大 (minなので最小)
                updatedata.append((b, x - 1))
            for b, cannewb in updatedata:
                curb = query(b, b+1) # bの値
                newb = min(curb, cannewb)
                update(b, b+1, -curb + newb)
        finalres = - query(0, n+1)

        print(finalres)


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
        input = """3 3
1 2
2 3
3 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5
1 1
2 1
2 2
3 2
3 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7 5
1 7
7 1
3 4
2 6
5 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """7 5
1 4
2 5
3 6
4 7
4 1"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_312(self):
        print("test_input_321")
        input = """7 6
1 1
2 2
3 3
4 4
1 5
5 1
"""
        output = """4"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
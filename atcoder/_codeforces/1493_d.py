import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        mod = 10 ** 9 + 7
        import math
        def segfunc(x, y):
            return math.gcd(x, y)
        class SegTree:
            def __init__(self, init_val, segfunc, ide_ele):
                n = len(init_val)
                self.segfunc = segfunc
                self.ide_ele = 0
                self.num = 1 << (n - 1).bit_length()
                self.tree = [0] * 2 * self.num
                for i in range(n):
                    self.tree[self.num + i] = init_val[i]
                for i in range(self.num - 1, 0, -1):
                    self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
            def update(self, k, x):
                k += self.num
                self.tree[k] = x
                while k > 1:
                    self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
                    k >>= 1
            def query(self, l, r):
                res = self.ide_ele
                l += self.num
                r += self.num
                while l < r:
                    if l & 1:
                        res = self.segfunc(res, self.tree[l])
                        l += 1
                    if r & 1:
                        res = self.segfunc(res, self.tree[r - 1])
                    l >>= 1
                    r >>= 1
                return res
        n, qq = map(int, input().split())
        dat = list(map(int, input().split()))
        st = SegTree(dat, segfunc, 0)
        for q in range(qq):
            a, b = map(int, input().split())
            a -= 1
            dat[a] *= b
            dat[a] %= mod
            st.update(a, dat[a])
            print(st.query(0, n) % mod)
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
        input = """4 3
1 6 8 12
1 12
2 3
3 3"""
        output = """2
2
6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
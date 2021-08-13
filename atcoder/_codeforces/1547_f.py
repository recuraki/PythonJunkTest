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
        import math

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

        class sparseTableGcd(sparseTable):
            func = math.gcd


        def factorization(n):
            arr = []
            temp = n
            for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
                if temp % i == 0:
                    cnt = 0
                    while temp % i == 0:
                        cnt += 1
                        temp //= i
                    arr.append([i, cnt])
            if temp != 1:
                arr.append([temp, 1])
            if arr == []:
                arr.append([n, 1])
            return arr

        # [2, 5, 5]
        def factorization_expand(n):
            l = factorization(n)
            dat = []
            for a, b in l:
                dat += [a] * b
            return dat

        import math
        def lcm(x, y):
            return (x * y) // math.gcd(x, y)

        def lcmList(l):
            x = 1
            for i in range(len(l)):
                x = lcm(x, l[i])
            return x

        def gcdList(l):
            x = 0
            for i in range(len(l)):
                x = math.gcd(x, l[i])
            return x

        n = int(input())
        dat = list(map(int, input().split()))

        import math
        gcdall = gcdList(dat)
        # print("gcd", gcdall, factorization_expand(gcdall))
        newdat = []
        for x in dat:
            newdat.append(x)
        newdat.append(dat[0])

        st = sparseTableGcd()
        st.load(newdat)
        # print(newdat)
        # print(st, st.query(0, 1))
        res = 0
        l = 0

        def ff(k):
            if k > len(newdat) + 1:
                assert False
            for i in range(n - k + 1 + 1):
                x = st.query(i, i + k)
                # print("ff",i, k,x)
                if x > gcdall: return False
            return True

        l = 1
        h = n
        while l <= h:
            mid = (l + h) // 2
            # print("2bu-tan", l, h, mid, ff(mid))
            if ff(mid) is False:
                l = mid + 1
            else:
                h = mid - 1
        res = None
        if ff(l):
            res = l
        else:
            res = h
        print(res - 1)

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
        input = """6
4
16 24 10 5
4
42 42 42 42
3
4 6 4
5
1 2 3 4 5
6
9 9 27 9 9 63
6
12 4 12 6 24 12
"""
        output = """3
0
2
1
1
5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
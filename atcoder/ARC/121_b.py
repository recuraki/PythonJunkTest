import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        cntr, cntg, cntb = 0, 0, 0
        datr, datg, datb = [], [], []
        for i in range(2 * n):
            a, b = input().split()
            a = int(a)
            if b == "R":
                datr.append(a)
                cntr += 1
            elif b == "G":
                datg.append(a)
                cntg += 1
            elif b == "B":
                datb.append(a)
                cntb += 1
            else:
                assert False

        if cntr % 2 == 0 and cntg % 2 == 0 and cntb % 2 == 0:
            print(0)
            return

        # どれかがodd
        if cntr % 2 == 0:
            pass
        elif cntb % 2 == 0:
            cntr, cntb = cntb, cntr
            datr, datb = datb, datr
        elif cntg % 2 == 0:
            cntr, cntg = cntg, cntr
            datr, datg = datg, datr
        else:
            assert False

        datr.sort()
        datg.sort()
        datb.sort()
        from bisect import bisect_left, bisect_right

        def mindiffsearch(x, l):
            candidate = []
            ll = len(l)
            indl = bisect_left(l, x)
            if indl == 0:
                return abs(x - l[0])
            if indl == ll:
                return abs(x - l[-1])
            else:
                return min(abs(x - l[indl]), abs(x - l[indl - 1]))

        res = 10 ** 18
        # GとBでの比較を行う これは候補1
        for i in range(cntg):
            val = mindiffsearch(datg[i], datb)
            res = min(res, val)

        res2 = 10 ** 18
        if cntr > 0:
            # Rを中心に G と B
            cang = []
            canb = []

            for i in range(cntr):
                val = mindiffsearch(datr[i], datg)
                cang.append((val, i))
            for i in range(cntr):
                val = mindiffsearch(datr[i], datb)
                canb.append((val, i))
            cang.sort()
            canb.sort()
            res2 = cang[0][0] + canb[0][0]
            if cang[0][1] == canb[0][1]:
                res2 = min(cang[1][0] + canb[0][0], cang[0][0] + canb[1][0])

        print(min(res, res2))

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

    def test_input_11(self):
        print("test_input_11")
        input = """4
1 R
2 G
5 G
5 B
5 B
5 B
10 B
20 B
"""
        output = """3"""
        self.assertIO(input, output)


    def test_input_1(self):
        print("test_input_1")
        input = """1
1 R
2 G"""
        output = """1"""
        #self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
1 B
2 B"""
        output = """0"""
        #self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
585 B
293 B
788 B
222 B
772 G
841 B
115 R
603 G
450 B
325 R
851 B
205 G
134 G
651 R
565 R
548 B
391 G
19 G
808 B
475 B"""
        output = """0"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
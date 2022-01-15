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


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        from copy import deepcopy
        n = int(input())
        odat = list(map(int, input().split()))

        # [ok, ng) for max value
        # (ng, ok] for min value
        # CATION: ok is result  (NOT mid)
        ok = 0
        ng = 10 ** 9 + 100
        ng = 100
        def func(target):
            dat = deepcopy(odat)

            for i in range(n-2):
                #print("?", target, dat, sum(dat), "i=", i)
                if dat[i] < 0: return False
                if dat[i] >= target: continue
                #print("gogo")

                need = target - dat[i]
                d = min(math.ceil(need / 2), dat[i + 2] // 3)
                #print("?", target, dat, sum(dat), "i=", i)
                dat[i+0] += 2 * d
                dat[i+1] += 1 * d
                dat[i+2] -= 3 * d

                need = target - dat[i]
                d = math.ceil(need / 2)
                if (dat[i+2] < (3 * d)) and i >= 1:
                   cand = dat[i+2] // 3
                   tarinai = d - cand
                   dat[i-1] += 2*tarinai
                   dat[i+0] += tarinai
                   dat[i+1] -= 3*tarinai

                if dat[i] < target: return False

                if dat[i+1] < 0: return False
                if dat[i+2] < 0: return False
            if dat[-2] < target:
                d = target - dat[-2]
                dat[-3] += 2*d
                dat[-2] += 1*d
                dat[-1] -= 3*d
            if dat[-1] < target: return False
            #print(target, dat, sum(dat))
            return True

        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            if (func(mid)):
                ok = mid;
            else:
                ng = mid;
        print(ok)


    # n questions
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
        input = """4
4
1 2 10 100
4
100 100 100 1
5
5 1 1 1 8
6
1 2 3 4 5 6"""
        output = """7
1
1
3"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
6
1 2 3 4 5 6"""
        output = """3"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()
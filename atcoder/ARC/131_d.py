import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    from bisect import bisect_left, bisect_right

    import math
    from copy import deepcopy
    INF = 1 << 63
    def do():
        n, m, d = map(int, input().split())
        datr = list(map(int, input().split()))
        dats = list(map(int, input().split()))
        datr[0] = -INF
        dats += [0]
        datr.append(INF)
        def createYa(center):
            # 2 -> 0本で左右
            # 3 -> 1本ずつ
            # 4 -> 1本日で左右にどっちか
            # 5 -> 2本ずつ
            # 6 -> 2本日で左右にどっちか
            res = [center]
            bothnum = (n - 1) // 2
            for i in range(bothnum):
                res.append(center + d *(i+1))
                res.append(center - d *(i+1))
            res.sort()
            if n % 2 == 0:
                return (res + [res[-1] + d], [res[0] - d] + res)
            return tuple( [res] )
        def attack(yaind):
            score = 0
            for x in yaind:
                x = abs(x)
                ind = bisect_left(datr, x)
                score += dats[ind-1]
            return score
        ans = -1

        # [ok, ng) for max value
        # (ng, ok] for min value
        # CATION: ok is result  (NOT mid)
        def func(mid):
            ans = -1
            for ya in createYa(mid):
                ans = max(ans , attack(ya))
            return ans != 0
        ok = 0
        ng = 10 ** 18 + 1
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            if (func(mid)):
                ok = mid;
            else:
                ng = mid;
        ma = ok
        ok = 0
        ng = -(10 ** 18 + 1)
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            if (func(mid)):
                ok = mid;
            else:
                ng = mid;
        mi = ok
        print(ma, mi)

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
        input = """3 3 3
0 2 7 9
100 70 30"""
        output = """270"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 8
0 2 7 9
100 70 30"""
        output = """200"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7 5 47
0 10 40 100 160 220
50 25 9 6 3"""
        output = """111"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """100 1 5
0 7
100000000000"""
        output = """300000000000"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """15 10 85
0 122 244 366 488 610 732 854 976 1098 1220
10 9 8 7 6 5 4 3 2 1"""
        output = """119"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
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
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        from copy import deepcopy
        from copy import deepcopy
        def f(dat):
            dat = deepcopy(dat)
            ans = 0
            n = len(dat)
            minval = min(dat)
            if minval > 0:
                ans = minval
                for i in range(n):
                    dat[i] -= minval
            if minval < 0:
                ans = abs(minval)
                for i in range(n):
                    dat[i] += abs(minval)
            rnum = 0  # 引いた数の合計
            alladd = 0  # 足した数
            haveleftzero = False
            for i in range(n):
                x = dat[i] - rnum + alladd
                if x == 0:
                    pass
                elif x > 0:  # 大きい場合
                    if i != 0:
                        rnum += x
                    ans += x
                elif x < 0:  # 小さい場合
                    alladd += abs(x)
                    ans += -x  # 0..iをx足して
                    if haveleftzero:
                        ans += -x  # 0..i-1のxを引く
                haveleftzero = True

            return ans

        n = int(input())
        dat = list(map(int, input().split()))
        print(min(f(dat), f(list(reversed(dat)))))

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
3
-2 -2 -2
3
10 4 7
4
4 -4 4 -4
5
1 -2 3 -4 5"""
        output = """2
13
36
33"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
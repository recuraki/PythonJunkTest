
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
        n, target = map(int, input().split())
        l = list(map(int, input().split()))
        def func(x):
            hikutotal = 0
            # print(l)
            for i in range(len(l)):
                if i == x: continue
                val = l[i] - hikutotal
                # print(i, "li", l[i], "curval", val, "ikutotal", hikutotal)
                hikutotal += val
                # print(i, "li", l[i], "curval", val, "ikutotal", hikutotal)
            return (l[x] - hikutotal)

        ok = 0
        ng = len(l)
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            if (func(mid) < -target):
                ok = mid;
            else:
                ng = mid;
        for i in range(-2, 3):
            j = ok + i
            if not (0 <= j < n): continue
            if func(j) == -target:
                print("YES")
                return
        print("NO")

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
4 5
4 2 2 7
5 4
1 9 1 3 4
2 17
17 0
2 17
18 18"""
        output = """YES
NO
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
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

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        dp = [-1] * 5010
        dp[0] = 0
        n, m = map(int, input().split())
        dat = list(map(int, input().split()))
        from collections import defaultdict
        d = defaultdict(int)
        for i in range(m):
            c, y = map(int, input().split())
            d[c] = y

        for turn in range(n):
            newdp = [-1] * 5010
            for cur in range(5002):
                if dp[cur] == -1: break # これより上はない
                # 表の処理
                newdp[cur+1] = max(newdp[cur+1], dp[cur] + dat[turn] + d[cur+1])
                # 裏の処理: 0にもどり、今の値
                newdp[0] = max(newdp[0], dp[cur])
            #print(turn, dp[:10])
            #print(turn, newdp[:10])
            dp = newdp
        print(max(dp))
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
        input = """6 3
2 7 1 8 2 8
2 10
3 1
5 5"""
        output = """48"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2
1000000000 1000000000 1000000000
1 1000000000
3 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
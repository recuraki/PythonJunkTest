
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

    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        s = input()
        n = len(s)
        dat = list(map(lambda x: ord(x) - ord("a"), s))
        dp = [[None] * 2 for _ in range(n)]
        pos = [[] for _ in range(26)]
        for i in range(n):
            pos[dat[i]].append(i)
        # init
        from bisect import bisect_left
        dp[dat[0]][0] = 0




        print(dat)

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
        input = """6
aabbdabdccc
zyx
aaababbb
aabbcc
oaoaaaoo
bmefbmuyw"""
        output = """3
3
2
0
2
7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
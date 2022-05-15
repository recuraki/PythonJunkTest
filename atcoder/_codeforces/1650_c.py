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
        _ = input()
        n, m = map(int, input().split())
        dat = []
        for i in range(m):
            x, w = map(int, input().split())
            dat.append( (w, x, i+1) )
        dat.sort()
        dat = dat[:n*2]
        buf = []
        answ = 0
        for w,x,ind in dat:
            answ += w
            buf.append( (x, ind) )
        buf.sort()
        ans = []
        for i in range(n):
            ans.append( (buf[i][1], buf[2*n-1-i][1]) )
        print(answ)
        for a, b in ans: print(a, b)
        print()



        # 出力は1originでnコメ


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
        input = """3

3 8
0 10
-2 1
4 10
11 20
7 -1
9 1
2 3
5 -2

3 6
-1 2
1 3
3 -1
2 4
4 0
8 2

2 5
5 -1
3 -2
1 0
-2 0
-5 -3"""
        output = """12
2 6
5 1
7 8

10
1 6
5 2
3 4

-6
5 1
4 2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
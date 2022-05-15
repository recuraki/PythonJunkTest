
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

    # 2以上しかないとき-> 絶対YES -> 上からやれば絶対0
    # 0と1があるとき -> 絶対NO
    # 0があるとき -> (1はないので) 絶対OK
    # 1がある時 -> 隣接がなければOK

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        if dat.count(0) == 0 and dat.count(1) == 0:
            print("YES")
            return
        if dat.count(0) > 0:
            if dat.count(1) > 0:
                print("NO")
                return
            else:
                print("YES")
                return
        dat.sort()
        for i in range(n-1):
            if dat[i+1] - dat[i] == 1:
                print("NO")
                return
        print("YES")

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
2 5 6 8
3
1 1 1
5
4 1 7 0 8
4
5 9 17 5"""
        output = """YES
YES
NO
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
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
        n = int(input())
        dat = [0] + list(map(int, input().split())) + [0]
        n += 2
        a = b = 0
        l = 0
        r = n-1
        ans = 0
        #print(dat,n)
        while l < r:
            #print(l, r)
            if a == b: # ok!
                ans = (l + 1) + (n- r)
                l += 1
                a += dat[l]
                continue
            elif a < b:
                l += 1
                a += dat[l]
                continue
            elif a > b:
                r -= 1
                b += dat[r]
                continue
            else:
                assert False
        print(ans - 2)

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
10 20 10
6
2 1 4 2 4 1
5
1 2 4 8 16
9
7 3 20 5 15 1 11 8 10"""
        output = """2
6
0
7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
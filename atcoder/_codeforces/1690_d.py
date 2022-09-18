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
        n, k = map(int, input().split())
        s = input()
        dat = []
        for x in s:
            if x == "B": dat.append(1)
            else: dat.append(0)
        cur = 0
        for i in range(k):
            x = dat[i]
            if x == 0: cur += 1
        ans = cur
        l = 0
        r = k - 1
        #print("---------------------")
        #print(ans)
        for _ in range(n - k):
            #print(r, l)
            r += 1
            if dat[r] == 0: cur += 1
            if dat[l] == 0: cur -= 1
            l += 1
            ans = min(ans, cur)
        print(ans)


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
5 3
BBWBW
5 5
BBWBW
5 1
BBWBW
1 1
W"""
        output = """1
2
0
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
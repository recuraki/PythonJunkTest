
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
        dat = list(map(int, input().split()))
        dat = dat + [0]
        #print("----------")
        #print(dat)
        elems = []
        buf = []
        for i in range(n+1):
            x = dat[i]
            if x == 0:
                if len(buf) == 0: continue
                st = i - len(buf)
                elems.append( (st, i-1, buf) )
                buf = []
                continue
            # x != 1
            buf.append(x)
        #print(elems)
        cadidate = []
        for st, la, buf in elems:
            v = 1
            smin = lmin = None
            for i in range(len(buf)):
                if buf[i] == 1:
                    pass
                elif buf[i] == -1:
                    v *= -1
                elif buf[i] == 2:
                    if v < 0: v -= 1
                    else: v += 1
                elif buf[i] == -2:
                    if v < 0: v -= 1
                    else: v += 1
                    v *= -1

                if buf[i] < 0 and smin is None: smin = i
                if buf[i] < 0: lmin = i
            if v > 0: # ok
                cadidate.append( (st, la, None, v) )
                continue

            v = 1
            for i in range(smin+1, len(buf)):
                if buf[i] == 1:
                    pass
                elif buf[i] == -1:
                    v *= -1
                elif buf[i] == 2:
                    if v < 0: v -= 1
                    else: v += 1
                elif buf[i] == -2:
                    if v < 0: v -= 1
                    else: v += 1
                    v *= -1
            cadidate.append( (st + smin+1, la, None, v) )

            v = 1
            for i in range(lmin):
                if buf[i] == 1:
                    pass
                elif buf[i] == -1:
                    v *= -1
                elif buf[i] == 2:
                    if v < 0: v -= 1
                    else: v += 1
                elif buf[i] == -2:
                    if v < 0: v -= 1
                    else: v += 1
                    v *= -1
            cadidate.append( (st, st + lmin-1, None, v) )

        if len(cadidate) == 0:
            print(n, 0)
            return
        cadidate.sort(key=lambda x: -x[3])
        #print("can", cadidate)
        s, t, _, _ = cadidate[0]
        print(s, n-1-t)







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
        input = """5
4
1 2 -1 2
3
1 1 -2
5
2 0 -2 2 -1
3
-2 -1 -1
3
-1 -2 -2"""
        output = """0 2
3 0
2 0
0 1
1 0"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
7
-2 1 1 -1 1 1 -2
"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()